import requests
import pandas as pd
import numpy as np
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import json

class DataSFAPIClient:
    """API client for DataSF APIs with mock fallbacks."""
    
    def __init__(self):
        self.base_url = "https://data.sfgov.org/resource"
        self.api_key = None  # Would be set from environment in production
        self.session = requests.Session()
        
    def get_311_data(self, location: str = "San Francisco", limit: int = 100) -> List[Dict[str, Any]]:
        """Fetch 311 service request data."""
        try:
            # Real DataSF API endpoint for 311 data
            url = f"{self.base_url}/vw6y-z8j6.json"
            params = {
                '$limit': limit,
                '$where': f"service_request_type LIKE '%{location}%'"
            }
            
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            return self._process_311_data(data)
            
        except Exception as e:
            print(f"Error fetching 311 data: {e}")
            return self._get_mock_311_data(location, limit)
    
    def get_eviction_data(self, location: str = "San Francisco", limit: int = 100) -> List[Dict[str, Any]]:
        """Fetch eviction data."""
        try:
            # Real DataSF API endpoint for eviction data
            url = f"{self.base_url}/5cei-gny5.json"
            params = {
                '$limit': limit,
                '$where': f"neighborhood LIKE '%{location}%'"
            }
            
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            return self._process_eviction_data(data)
            
        except Exception as e:
            print(f"Error fetching eviction data: {e}")
            return self._get_mock_eviction_data(location, limit)
    
    def get_building_permits(self, location: str = "San Francisco", limit: int = 100) -> List[Dict[str, Any]]:
        """Fetch building permit data."""
        try:
            # Real DataSF API endpoint for building permits
            url = f"{self.base_url}/ipu4-2q9a.json"
            params = {
                '$limit': limit,
                '$where': f"neighborhood LIKE '%{location}%'"
            }
            
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            return self._process_permit_data(data)
            
        except Exception as e:
            print(f"Error fetching permit data: {e}")
            return self._get_mock_permit_data(location, limit)
    
    def get_budget_data(self, fiscal_year: int = 2024) -> List[Dict[str, Any]]:
        """Fetch budget allocation data."""
        try:
            # Real DataSF API endpoint for budget data
            url = f"{self.base_url}/6j9d-3q6k.json"
            params = {
                '$limit': 1000,
                '$where': f"fiscal_year = {fiscal_year}"
            }
            
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            return self._process_budget_data(data)
            
        except Exception as e:
            print(f"Error fetching budget data: {e}")
            return self._get_mock_budget_data(fiscal_year)
    
    def _process_311_data(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Process 311 data into standardized format."""
        processed_data = []
        
        for item in data:
            processed_item = {
                'id': item.get('service_request_id'),
                'type': item.get('service_request_type', 'unknown'),
                'location': item.get('street_address', 'Unknown'),
                'severity': self._calculate_severity(item),
                'description': item.get('service_request_details', ''),
                'status': item.get('status', 'open'),
                'created_date': item.get('requested_datetime', ''),
                'category': self._categorize_311_request(item.get('service_request_type', ''))
            }
            processed_data.append(processed_item)
        
        return processed_data
    
    def _process_eviction_data(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Process eviction data into standardized format."""
        processed_data = []
        
        for item in data:
            processed_item = {
                'id': item.get('eviction_id'),
                'address': item.get('address', 'Unknown'),
                'risk_score': self._calculate_eviction_risk(item),
                'type': item.get('eviction_type', 'unknown'),
                'neighborhood': item.get('neighborhood', 'Unknown'),
                'date': item.get('file_date', ''),
                'reason': item.get('eviction_reason', '')
            }
            processed_data.append(processed_item)
        
        return processed_data
    
    def _process_permit_data(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Process building permit data into standardized format."""
        processed_data = []
        
        for item in data:
            processed_item = {
                'id': item.get('permit_number'),
                'address': item.get('street_address', 'Unknown'),
                'type': item.get('permit_type', 'unknown'),
                'value': float(item.get('estimated_cost', 0)),
                'status': item.get('status', 'unknown'),
                'issued_date': item.get('issued_date', ''),
                'description': item.get('description', '')
            }
            processed_data.append(processed_item)
        
        return processed_data
    
    def _process_budget_data(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Process budget data into standardized format."""
        processed_data = []
        
        for item in data:
            processed_item = {
                'category': item.get('department', 'Unknown'),
                'amount': float(item.get('amount', 0)),
                'year': int(item.get('fiscal_year', 2024)),
                'source': item.get('fund_source', 'general_fund'),
                'description': item.get('description', '')
            }
            processed_data.append(processed_item)
        
        return processed_data
    
    def _calculate_severity(self, item: Dict[str, Any]) -> float:
        """Calculate severity score for 311 requests."""
        # Simple severity calculation based on request type
        severity_map = {
            'graffiti': 0.8,
            'street_light': 0.6,
            'pothole': 0.7,
            'trash': 0.5,
            'noise': 0.4
        }
        
        request_type = item.get('service_request_type', '').lower()
        for key, value in severity_map.items():
            if key in request_type:
                return value
        
        return 0.5  # Default severity
    
    def _calculate_eviction_risk(self, item: Dict[str, Any]) -> float:
        """Calculate eviction risk score."""
        # Simple risk calculation based on eviction type
        risk_map = {
            'non_payment': 0.8,
            'lease_violation': 0.6,
            'owner_move_in': 0.9,
            'demolition': 0.7
        }
        
        eviction_type = item.get('eviction_type', '').lower()
        for key, value in risk_map.items():
            if key in eviction_type:
                return value
        
        return 0.5  # Default risk
    
    def _categorize_311_request(self, request_type: str) -> str:
        """Categorize 311 requests."""
        request_type_lower = request_type.lower()
        
        if any(word in request_type_lower for word in ['graffiti', 'trash', 'litter']):
            return 'gross'
        elif any(word in request_type_lower for word in ['light', 'pothole', 'glass']):
            return 'safety'
        elif any(word in request_type_lower for word in ['sidewalk', 'ramp']):
            return 'accessibility'
        else:
            return 'other'
    
    def _get_mock_311_data(self, location: str, limit: int) -> List[Dict[str, Any]]:
        """Generate mock 311 data."""
        mock_data = [
            {'id': 1, 'type': 'graffiti', 'location': 'Market St', 'severity': 0.8, 'description': 'Graffiti on building'},
            {'id': 2, 'type': 'street_light', 'location': 'Mission St', 'severity': 0.6, 'description': 'Broken street light'},
            {'id': 3, 'type': 'pothole', 'location': 'Castro St', 'severity': 0.7, 'description': 'Large pothole'},
            {'id': 4, 'type': 'trash', 'location': 'Haight St', 'severity': 0.5, 'description': 'Trash accumulation'},
            {'id': 5, 'type': 'noise', 'location': 'Tenderloin', 'severity': 0.4, 'description': 'Excessive noise'}
        ]
        return mock_data[:limit]
    
    def _get_mock_eviction_data(self, location: str, limit: int) -> List[Dict[str, Any]]:
        """Generate mock eviction data."""
        mock_data = [
            {'id': 1, 'address': '123 Market St', 'risk_score': 0.8, 'type': 'non_payment'},
            {'id': 2, 'address': '456 Mission St', 'risk_score': 0.6, 'type': 'lease_violation'},
            {'id': 3, 'address': '789 Castro St', 'risk_score': 0.9, 'type': 'owner_move_in'},
            {'id': 4, 'address': '321 Haight St', 'risk_score': 0.7, 'type': 'demolition'}
        ]
        return mock_data[:limit]
    
    def _get_mock_permit_data(self, location: str, limit: int) -> List[Dict[str, Any]]:
        """Generate mock building permit data."""
        mock_data = [
            {'id': 1, 'address': '123 Market St', 'type': 'renovation', 'value': 50000},
            {'id': 2, 'address': '456 Mission St', 'type': 'new_construction', 'value': 200000},
            {'id': 3, 'address': '789 Castro St', 'type': 'demolition', 'value': 100000},
            {'id': 4, 'address': '321 Haight St', 'type': 'renovation', 'value': 75000}
        ]
        return mock_data[:limit]
    
    def _get_mock_budget_data(self, fiscal_year: int) -> List[Dict[str, Any]]:
        """Generate mock budget data."""
        mock_data = [
            {'category': 'housing', 'amount': 50000000, 'year': fiscal_year, 'source': 'general_fund'},
            {'category': 'infrastructure', 'amount': 75000000, 'year': fiscal_year, 'source': 'general_fund'},
            {'category': 'social_services', 'amount': 30000000, 'year': fiscal_year, 'source': 'general_fund'},
            {'category': 'homeless_services', 'amount': 25000000, 'year': fiscal_year, 'source': 'federal'},
            {'category': 'public_transport', 'amount': 40000000, 'year': fiscal_year, 'source': 'federal'}
        ]
        return mock_data 