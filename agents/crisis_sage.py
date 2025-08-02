from typing import Dict, List, Any
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import requests
from .base_agent import BaseAgent, AgentMode

class CrisisSage(BaseAgent):
    """Crisis Sage Agent: Coordinates emergency response and holistic prevention chains."""
    
    def __init__(self):
        super().__init__("Crisis Sage", threshold=0.85)
        self.crisis_types = {
            'medical': ['overdose', 'mental_health', 'medical_emergency'],
            'safety': ['fire', 'accident', 'violence'],
            'infrastructure': ['power_outage', 'water_main', 'building_collapse'],
            'environmental': ['flood', 'earthquake', 'air_quality']
        }
        self.response_coordination = {
            'emergency_services': ['police', 'fire', 'ambulance'],
            'support_services': ['mental_health', 'social_services', 'housing'],
            'infrastructure': ['utilities', 'transportation', 'communications']
        }
        
    def detect(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Detect crisis events and coordinate response."""
        # Simulate crisis event data
        crisis_events = self._fetch_crisis_data(data.get('location', 'San Francisco'))
        
        # Detect escalation patterns
        escalation_patterns = self._detect_escalation_patterns(crisis_events)
        
        # Coordinate response teams
        response_coordination = self._coordinate_response_teams(crisis_events)
        
        # Calculate confidence
        confidence = min(0.9, len(crisis_events) * 0.1 + len(escalation_patterns) * 0.2)
        self.update_confidence(confidence)
        
        return {
            'crisis_events': crisis_events,
            'escalation_patterns': escalation_patterns,
            'response_coordination': response_coordination,
            'confidence': confidence,
            'mode': 'detect',
            'level_up_message': f"Holistic prevention chains detected: {len(response_coordination)} coordinated responses"
        }
    
    def predict(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Predict crisis escalation and resource needs."""
        crisis_events = data.get('crisis_events', [])
        escalation_patterns = data.get('escalation_patterns', [])
        
        # Predict crisis escalation
        escalation_predictions = self._predict_crisis_escalation(crisis_events)
        
        # Predict resource needs
        resource_predictions = self._predict_resource_needs(crisis_events)
        
        # Predict response effectiveness
        response_predictions = self._predict_response_effectiveness(crisis_events)
        
        # Combine all predictions
        all_predictions = escalation_predictions + resource_predictions + response_predictions
        
        confidence = min(0.85, len(all_predictions) * 0.15)
        self.update_confidence(confidence)
        
        return {
            'escalation_predictions': all_predictions,
            'crisis_escalation': escalation_predictions,
            'resource_needs': resource_predictions,
            'response_effectiveness': response_predictions,
            'confidence': confidence,
            'mode': 'predict',
            'level_up_message': f"Predicted {len(escalation_predictions)} crisis escalations"
        }
    
    def prevent(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate holistic prevention strategies."""
        crisis_events = data.get('crisis_events', [])
        escalation_predictions = data.get('escalation_predictions', [])
        
        # Generate crisis prevention strategies
        crisis_strategies = self._generate_crisis_strategies(crisis_events)
        
        # Generate holistic coordination strategies
        holistic_strategies = self._generate_holistic_strategies(crisis_events, escalation_predictions)
        
        # Generate resource allocation strategies
        resource_strategies = self._generate_resource_strategies(crisis_events)
        
        # Combine all strategies
        all_strategies = crisis_strategies + holistic_strategies + resource_strategies
        
        confidence = min(0.8, len(all_strategies) * 0.15)
        self.update_confidence(confidence)
        
        return {
            'strategies': all_strategies,
            'crisis_strategies': crisis_strategies,
            'holistic_strategies': holistic_strategies,
            'resource_strategies': resource_strategies,
            'confidence': confidence,
            'mode': 'prevent',
            'level_up_message': f"Coordinated {len(holistic_strategies)} holistic strategies"
        }
    
    def broadcast(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Broadcast crisis coordination findings to other agents."""
        crisis_events = data.get('crisis_events', [])
        escalation_predictions = data.get('escalation_predictions', [])
        strategies = data.get('strategies', [])
        
        broadcast_data = {
            'crisis_events': crisis_events,
            'escalation_predictions': escalation_predictions,
            'prevention_strategies': strategies,
            'response_coordination': data.get('response_coordination', []),
            'escalation_patterns': data.get('escalation_patterns', [])
        }
        
        confidence = min(0.9, len(broadcast_data) * 0.1)
        self.update_confidence(confidence)
        
        return {
            'broadcast_data': broadcast_data,
            'confidence': confidence,
            'mode': 'broadcast',
            'level_up_message': f"Broadcasting {len(crisis_events)} crisis events with coordination"
        }
    
    def _fetch_crisis_data(self, location: str) -> List[Dict[str, Any]]:
        """Simulate crisis event data fetch."""
        mock_crisis_events = [
            {'id': 1, 'type': 'medical', 'location': 'Tenderloin', 'severity': 0.8, 'description': 'Overdose incident'},
            {'id': 2, 'type': 'safety', 'location': 'Mission District', 'severity': 0.6, 'description': 'Fire emergency'},
            {'id': 3, 'type': 'infrastructure', 'location': 'Downtown', 'severity': 0.9, 'description': 'Power outage'}
        ]
        return mock_crisis_events
    
    def _detect_escalation_patterns(self, crisis_events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Detect escalation patterns in crisis events."""
        patterns = []
        
        # Detect patterns by type
        type_counts = {}
        for event in crisis_events:
            event_type = event['type']
            if event_type not in type_counts:
                type_counts[event_type] = 0
            type_counts[event_type] += 1
        
        # Identify escalating patterns
        for event_type, count in type_counts.items():
            if count > 1:
                patterns.append({
                    'type': 'escalation_pattern',
                    'crisis_type': event_type,
                    'frequency': count,
                    'severity': np.mean([e['severity'] for e in crisis_events if e['type'] == event_type]),
                    'description': f"Escalating {event_type} crisis pattern"
                })
        
        return patterns
    
    def _coordinate_response_teams(self, crisis_events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Coordinate response teams for crisis events."""
        coordination = []
        
        for event in crisis_events:
            if event['type'] == 'medical':
                coordination.append({
                    'type': 'response_coordination',
                    'crisis_id': event['id'],
                    'teams': ['ambulance', 'mental_health', 'social_services'],
                    'priority': 'high' if event['severity'] > 0.7 else 'medium'
                })
            elif event['type'] == 'safety':
                coordination.append({
                    'type': 'response_coordination',
                    'crisis_id': event['id'],
                    'teams': ['fire', 'police', 'emergency_services'],
                    'priority': 'high'
                })
            elif event['type'] == 'infrastructure':
                coordination.append({
                    'type': 'response_coordination',
                    'crisis_id': event['id'],
                    'teams': ['utilities', 'emergency_services', 'communications'],
                    'priority': 'high' if event['severity'] > 0.8 else 'medium'
                })
        
        return coordination
    
    def _predict_crisis_escalation(self, crisis_events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Predict crisis escalation patterns."""
        predictions = []
        
        # Predict based on severity patterns
        high_severity_events = [e for e in crisis_events if e['severity'] > 0.7]
        if len(high_severity_events) > 1:
            predictions.append({
                'type': 'crisis_escalation',
                'prediction': 'Escalating high-severity crisis pattern',
                'affected_areas': [e['location'] for e in high_severity_events],
                'confidence': 0.8
            })
        
        # Predict individual escalations
        for event in crisis_events:
            if event['severity'] > 0.8:
                predictions.append({
                    'type': 'crisis_escalation',
                    'location': event['location'],
                    'prediction': f"High risk of {event['type']} crisis escalation",
                    'confidence': 0.75
                })
        
        return predictions
    
    def _predict_resource_needs(self, crisis_events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Predict resource needs for crisis response."""
        predictions = []
        
        # Predict medical resource needs
        medical_events = [e for e in crisis_events if e['type'] == 'medical']
        if medical_events:
            predictions.append({
                'type': 'resource_needs',
                'category': 'medical',
                'prediction': 'Increased medical response resources needed',
                'affected_areas': [e['location'] for e in medical_events],
                'confidence': 0.7
            })
        
        # Predict safety resource needs
        safety_events = [e for e in crisis_events if e['type'] == 'safety']
        if safety_events:
            predictions.append({
                'type': 'resource_needs',
                'category': 'safety',
                'prediction': 'Increased safety response resources needed',
                'affected_areas': [e['location'] for e in safety_events],
                'confidence': 0.7
            })
        
        return predictions
    
    def _predict_response_effectiveness(self, crisis_events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Predict response effectiveness for crisis events."""
        predictions = []
        
        for event in crisis_events:
            if event['severity'] > 0.7:
                predictions.append({
                    'type': 'response_effectiveness',
                    'crisis_id': event['id'],
                    'prediction': 'High-priority response coordination needed',
                    'response_time': 'immediate',
                    'confidence': 0.8
                })
        
        return predictions
    
    def _generate_crisis_strategies(self, crisis_events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate crisis prevention strategies."""
        strategies = []
        
        for event in crisis_events:
            if event['type'] == 'medical':
                strategies.append({
                    'type': 'crisis_prevention',
                    'target': event['location'],
                    'action': 'Deploy medical response teams',
                    'priority': 'high' if event['severity'] > 0.7 else 'medium'
                })
            elif event['type'] == 'safety':
                strategies.append({
                    'type': 'crisis_prevention',
                    'target': event['location'],
                    'action': 'Deploy safety patrols',
                    'priority': 'high'
                })
            elif event['type'] == 'infrastructure':
                strategies.append({
                    'type': 'crisis_prevention',
                    'target': event['location'],
                    'action': 'Infrastructure maintenance check',
                    'priority': 'high' if event['severity'] > 0.8 else 'medium'
                })
        
        return strategies
    
    def _generate_holistic_strategies(self, crisis_events: List[Dict[str, Any]], escalation_predictions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate holistic coordination strategies."""
        strategies = []
        
        # Generate cross-agency coordination strategies
        if len(crisis_events) > 2:
            strategies.append({
                'type': 'holistic_coordination',
                'action': 'Establish cross-agency crisis response protocol',
                'agencies': ['police', 'fire', 'medical', 'social_services'],
                'priority': 'high'
            })
        
        # Generate escalation prevention strategies
        for prediction in escalation_predictions:
            if prediction['type'] == 'crisis_escalation':
                strategies.append({
                    'type': 'holistic_coordination',
                    'action': 'Deploy escalation prevention teams',
                    'target_areas': prediction.get('affected_areas', []),
                    'priority': 'high'
                })
        
        return strategies
    
    def _generate_resource_strategies(self, crisis_events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate resource allocation strategies."""
        strategies = []
        
        # Generate resource allocation based on crisis types
        medical_events = [e for e in crisis_events if e['type'] == 'medical']
        if medical_events:
            strategies.append({
                'type': 'resource_allocation',
                'category': 'medical',
                'action': 'Increase medical response capacity',
                'target_areas': [e['location'] for e in medical_events],
                'priority': 'high'
            })
        
        safety_events = [e for e in crisis_events if e['type'] == 'safety']
        if safety_events:
            strategies.append({
                'type': 'resource_allocation',
                'category': 'safety',
                'action': 'Increase safety response capacity',
                'target_areas': [e['location'] for e in safety_events],
                'priority': 'high'
            })
        
        return strategies 