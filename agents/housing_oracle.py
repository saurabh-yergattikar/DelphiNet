from typing import Dict, List, Any
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import requests
from .base_agent import BaseAgent, AgentMode

class HousingOracle(BaseAgent):
    """Housing Oracle Agent: Predicts housing risks with parcel/zoning overlays and SNAP guidance."""
    
    def __init__(self):
        super().__init__("Housing Oracle", threshold=0.8)
        self.parcel_data = {}
        self.zoning_classifier = DecisionTreeClassifier(random_state=42)
        self.snap_guidance_templates = {
            'eligibility_check': self._check_snap_eligibility,
            'benefits_calculation': self._calculate_snap_benefits,
            'application_guide': self._generate_application_guide
        }
        
    def detect(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Detect housing issues using eviction and permit data."""
        # Simulate eviction and permit data
        evictions = self._fetch_eviction_data(data.get('location', 'San Francisco'))
        permits = self._fetch_permit_data(data.get('location', 'San Francisco'))
        
        # Level-up: Parcel data integration
        parcel_issues = self._detect_parcel_issues(evictions, permits)
        
        confidence = min(0.9, len(evictions) * 0.1 + len(permits) * 0.05 + len(parcel_issues) * 0.15)
        self.update_confidence(confidence)
        
        self.add_level_up_feature('parcel_analysis', parcel_issues)
        
        return {
            'evictions': evictions,
            'permits': permits,
            'parcel_issues': parcel_issues,
            'confidence': confidence,
            'mode': 'detect',
            'level_up_message': f"Parcel analysis: {len(parcel_issues)} zoning compliance issues detected"
        }
    
    def predict(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Predict housing risks with parcel/zoning overlays."""
        evictions = data.get('evictions', [])
        permits = data.get('permits', [])
        parcel_issues = data.get('parcel_issues', [])
        
        # Level-up: Zoning ruleset simulation
        zoning_predictions = self._predict_zoning_risks(evictions, permits)
        
        # Risk prediction with parcel overlays
        risk_predictions = self._predict_housing_risks(evictions, permits, parcel_issues)
        
        confidence = min(0.85, len(zoning_predictions) * 0.1 + len(risk_predictions) * 0.15)
        self.update_confidence(confidence)
        
        self.add_level_up_feature('zoning_predictions', zoning_predictions)
        
        return {
            'zoning_predictions': zoning_predictions,
            'risk_predictions': risk_predictions,
            'confidence': confidence,
            'mode': 'predict',
            'level_up_message': f"Zoning ruleset sim in predict - {len(zoning_predictions)} compliance risks"
        }
    
    def prevent(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate prevention strategies with SNAP guidance integration."""
        predictions = data.get('risk_predictions', [])
        zoning_predictions = data.get('zoning_predictions', [])
        
        prevention_strategies = []
        
        # Generate aid strategies
        for prediction in predictions:
            if prediction.get('risk_level', 0) > 0.7:
                strategy = {
                    'type': 'aid',
                    'target': prediction.get('location'),
                    'action': 'Emergency housing assistance',
                    'priority': 'high'
                }
                prevention_strategies.append(strategy)
        
        # Level-up: SNAP guidance integration
        snap_guidance = self._generate_snap_guidance(predictions)
        
        confidence = min(0.8, len(prevention_strategies) * 0.15 + len(snap_guidance) * 0.1)
        self.update_confidence(confidence)
        
        self.add_level_up_feature('snap_guidance', snap_guidance)
        
        return {
            'strategies': prevention_strategies,
            'snap_guidance': snap_guidance,
            'confidence': confidence,
            'mode': 'prevent',
            'level_up_message': f"SNAP tool integration - {len(snap_guidance)} guidance items generated"
        }
    
    def broadcast(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Broadcast housing findings to other agents."""
        evictions = data.get('evictions', [])
        predictions = data.get('risk_predictions', [])
        strategies = data.get('strategies', [])
        snap_guidance = data.get('snap_guidance', [])
        
        broadcast_data = {
            'housing_issues': evictions,
            'predictions': predictions,
            'prevention_strategies': strategies,
            'snap_guidance': snap_guidance,
            'zoning_predictions': data.get('zoning_predictions', [])
        }
        
        confidence = min(0.9, len(broadcast_data) * 0.1)
        self.update_confidence(confidence)
        
        return {
            'broadcast_data': broadcast_data,
            'confidence': confidence,
            'mode': 'broadcast',
            'level_up_message': f"Broadcasting housing data with SNAP guidance"
        }
    
    def _fetch_eviction_data(self, location: str) -> List[Dict[str, Any]]:
        """Simulate eviction data API call."""
        mock_evictions = [
            {'id': 1, 'address': '123 Market St', 'risk_score': 0.8, 'type': 'non_payment'},
            {'id': 2, 'address': '456 Mission St', 'risk_score': 0.6, 'type': 'lease_violation'},
            {'id': 3, 'address': '789 Castro St', 'risk_score': 0.9, 'type': 'owner_move_in'}
        ]
        return mock_evictions
    
    def _fetch_permit_data(self, location: str) -> List[Dict[str, Any]]:
        """Simulate building permit data API call."""
        mock_permits = [
            {'id': 1, 'address': '123 Market St', 'type': 'renovation', 'value': 50000},
            {'id': 2, 'address': '456 Mission St', 'type': 'new_construction', 'value': 200000},
            {'id': 3, 'address': '789 Castro St', 'type': 'demolition', 'value': 100000}
        ]
        return mock_permits
    
    def _detect_parcel_issues(self, evictions: List[Dict[str, Any]], permits: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Detect parcel and zoning compliance issues."""
        parcel_issues = []
        
        # Simulate parcel analysis
        for eviction in evictions:
            address = eviction['address']
            # Check if address has zoning compliance issues
            if 'Market St' in address:
                parcel_issues.append({
                    'address': address,
                    'issue_type': 'zoning_violation',
                    'severity': 0.7,
                    'description': 'Residential use in commercial zone'
                })
        
        return parcel_issues
    
    def _predict_zoning_risks(self, evictions: List[Dict[str, Any]], permits: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Predict zoning compliance risks using ML classifier."""
        predictions = []
        
        # Simulate zoning risk prediction
        for eviction in evictions:
            address = eviction['address']
            risk_score = eviction['risk_score']
            
            # Level-up: Zoning ruleset simulation
            if risk_score > 0.7:
                predictions.append({
                    'address': address,
                    'risk_type': 'zoning_compliance',
                    'risk_level': risk_score,
                    'prediction': 'High risk of zoning violation',
                    'confidence': 0.8
                })
        
        return predictions
    
    def _predict_housing_risks(self, evictions: List[Dict[str, Any]], permits: List[Dict[str, Any]], parcel_issues: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Predict housing risks with parcel overlays."""
        risk_predictions = []
        
        for eviction in evictions:
            address = eviction['address']
            risk_score = eviction['risk_score']
            
            # Check for parcel overlay issues
            parcel_issue = next((p for p in parcel_issues if p['address'] == address), None)
            
            if parcel_issue:
                risk_score += 0.2  # Increase risk due to parcel issues
            
            risk_predictions.append({
                'address': address,
                'risk_level': min(1.0, risk_score),
                'risk_type': 'eviction',
                'parcel_issues': parcel_issue is not None,
                'prediction': f"Eviction risk: {risk_score:.2f}"
            })
        
        return risk_predictions
    
    def _generate_snap_guidance(self, predictions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate SNAP guidance for high-risk households."""
        snap_guidance = []
        
        for prediction in predictions:
            if prediction.get('risk_level', 0) > 0.7:
                address = prediction['address']
                
                # Level-up: SNAP guidance templates
                guidance = {
                    'address': address,
                    'type': 'snap_guidance',
                    'eligibility': self._check_snap_eligibility(address),
                    'benefits': self._calculate_snap_benefits(address),
                    'application': self._generate_application_guide(address),
                    'priority': 'high'
                }
                snap_guidance.append(guidance)
        
        return snap_guidance
    
    def _check_snap_eligibility(self, address: str) -> Dict[str, Any]:
        """Check SNAP eligibility for address."""
        # Mock SNAP eligibility check
        return {
            'eligible': True,
            'income_threshold': 2500,
            'household_size': 2,
            'estimated_benefits': 400
        }
    
    def _calculate_snap_benefits(self, address: str) -> Dict[str, Any]:
        """Calculate estimated SNAP benefits."""
        return {
            'monthly_benefit': 400,
            'calculation_method': 'standard_formula',
            'deductions_applied': ['housing', 'utilities']
        }
    
    def _generate_application_guide(self, address: str) -> Dict[str, Any]:
        """Generate SNAP application guide."""
        return {
            'application_url': 'https://www.cdss.ca.gov/snap',
            'required_documents': ['ID', 'Income proof', 'Rent receipt'],
            'processing_time': '30 days',
            'contact_info': '1-800-952-5253'
        } 