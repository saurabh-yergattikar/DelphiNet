from typing import Dict, List, Any
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import requests
from .base_agent import BaseAgent, AgentMode

class StreetPrecog(BaseAgent):
    """Street Precog Agent: Detects and predicts street issues with 311 integration and QR-inspired patterns."""
    
    def __init__(self):
        super().__init__("Street Precog", threshold=0.75)
        self.issue_patterns = {
            'gross': ['trash', 'litter', 'graffiti', 'vandalism'],
            'safety': ['broken_glass', 'potholes', 'streetlights'],
            'accessibility': ['sidewalk_obstruction', 'ramp_issues']
        }
        self.qr_inspired_patterns = {
            'location_clusters': [],
            'time_patterns': {},
            'severity_scores': {}
        }
        
    def detect(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Detect street issues using 311 API and QR-inspired patterns."""
        # Simulate 311 API call for street issues
        issues = self._fetch_311_data(data.get('location', 'San Francisco'))
        
        # QR-inspired pattern detection
        qr_patterns = self._detect_qr_patterns(issues)
        
        # Calculate confidence based on pattern strength
        confidence = min(0.95, len(issues) * 0.1 + len(qr_patterns) * 0.2)
        self.update_confidence(confidence)
        
        # Level-up: Add QR-inspired detection status
        self.add_level_up_feature('qr_patterns_detected', qr_patterns)
        self.add_level_up_feature('311_integration', f"Processed {len(issues)} 311 reports")
        
        return {
            'issues_detected': issues,
            'qr_patterns': qr_patterns,
            'confidence': confidence,
            'mode': 'detect',
            'level_up_message': f"Gross prevent via 311 forecast - {len(qr_patterns)} patterns detected"
        }
    
    def predict(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Predict future street issues using weather and historical patterns."""
        current_issues = data.get('issues_detected', [])
        weather_data = data.get('weather', {})
        
        # Predict based on weather conditions and historical patterns
        predictions = self._predict_weather_impact(current_issues, weather_data)
        
        # Level-up: Rain/SSI + gross patterns prediction
        rain_predictions = self._predict_rain_impact(weather_data)
        
        confidence = min(0.9, len(predictions) * 0.15 + len(rain_predictions) * 0.1)
        self.update_confidence(confidence)
        
        self.add_level_up_feature('weather_predictions', rain_predictions)
        
        return {
            'predictions': predictions,
            'rain_impact': rain_predictions,
            'confidence': confidence,
            'mode': 'predict',
            'level_up_message': f"Rain/SSI + gross patterns predicted"
        }
    
    def prevent(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate prevention strategies for street issues."""
        predictions = data.get('predictions', [])
        current_issues = data.get('issues_detected', [])
        
        prevention_strategies = []
        
        # Generate outreach strategies
        for issue in current_issues + predictions:
            if issue.get('type') == 'gross':
                strategy = {
                    'type': 'outreach',
                    'target': issue.get('location'),
                    'action': 'Schedule cleanup crew',
                    'priority': 'high' if issue.get('severity', 0) > 0.7 else 'medium'
                }
                prevention_strategies.append(strategy)
        
        confidence = min(0.85, len(prevention_strategies) * 0.2)
        self.update_confidence(confidence)
        
        return {
            'strategies': prevention_strategies,
            'confidence': confidence,
            'mode': 'prevent',
            'level_up_message': f"Outreach strategies generated for {len(prevention_strategies)} issues"
        }
    
    def broadcast(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Broadcast findings to other agents."""
        issues = data.get('issues_detected', [])
        predictions = data.get('predictions', [])
        strategies = data.get('strategies', [])
        
        broadcast_data = {
            'street_issues': issues,
            'predictions': predictions,
            'prevention_strategies': strategies,
            'qr_patterns': data.get('qr_patterns', []),
            'weather_impact': data.get('rain_impact', [])
        }
        
        confidence = min(0.9, len(broadcast_data) * 0.1)
        self.update_confidence(confidence)
        
        return {
            'broadcast_data': broadcast_data,
            'confidence': confidence,
            'mode': 'broadcast',
            'level_up_message': f"Broadcasting {len(issues)} issues with QR patterns"
        }
    
    def _fetch_311_data(self, location: str) -> List[Dict[str, Any]]:
        """Simulate 311 API call for street issues."""
        # Mock 311 data - in real implementation, this would call the actual API
        mock_issues = [
            {'id': 1, 'type': 'gross', 'location': 'Market St', 'severity': 0.8, 'description': 'Trash accumulation'},
            {'id': 2, 'type': 'safety', 'location': 'Mission St', 'severity': 0.6, 'description': 'Broken glass'},
            {'id': 3, 'type': 'gross', 'location': 'Castro St', 'severity': 0.9, 'description': 'Graffiti'},
            {'id': 4, 'type': 'accessibility', 'location': 'Haight St', 'severity': 0.5, 'description': 'Sidewalk obstruction'}
        ]
        return mock_issues
    
    def _detect_qr_patterns(self, issues: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Detect QR-inspired patterns in issue data."""
        patterns = []
        
        # Location clustering
        locations = [issue['location'] for issue in issues]
        location_counts = pd.Series(locations).value_counts()
        
        for location, count in location_counts.items():
            if count > 1:
                patterns.append({
                    'type': 'location_cluster',
                    'location': location,
                    'count': count,
                    'severity': np.mean([i['severity'] for i in issues if i['location'] == location])
                })
        
        # Time-based patterns (simulated)
        time_patterns = {
            'morning_peak': ['Market St', 'Mission St'],
            'evening_peak': ['Castro St', 'Haight St']
        }
        
        for time_period, affected_locations in time_patterns.items():
            patterns.append({
                'type': 'time_pattern',
                'period': time_period,
                'locations': affected_locations
            })
        
        return patterns
    
    def _predict_weather_impact(self, issues: List[Dict[str, Any]], weather: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Predict weather impact on street issues."""
        predictions = []
        
        if weather.get('rain_probability', 0) > 0.7:
            for issue in issues:
                if issue['type'] == 'gross':
                    predictions.append({
                        'type': 'weather_impact',
                        'issue_id': issue['id'],
                        'prediction': 'Increased severity due to rain',
                        'confidence': 0.8
                    })
        
        return predictions
    
    def _predict_rain_impact(self, weather: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Predict rain impact on street conditions."""
        rain_predictions = []
        
        if weather.get('rain_probability', 0) > 0.5:
            rain_predictions.append({
                'type': 'rain_impact',
                'prediction': 'Increased trash accumulation in low-lying areas',
                'affected_areas': ['Market St', 'Mission St'],
                'confidence': 0.75
            })
        
        return rain_predictions 