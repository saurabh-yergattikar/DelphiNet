from typing import Dict, List, Any
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import requests
from .base_agent import BaseAgent, AgentMode

class CrisisSage(BaseAgent):
    """Crisis Sage Agent: Coordinates emergency response with holistic prevention chains."""
    
    def __init__(self):
        super().__init__("Crisis Sage", threshold=0.85)
        self.crisis_types = {
            'natural_disaster': ['earthquake', 'fire', 'flood'],
            'public_health': ['outbreak', 'contamination'],
            'infrastructure': ['power_outage', 'water_main_break'],
            'social': ['protest', 'civil_unrest']
        }
        self.response_coordination = {
            'first_responders': ['police', 'fire', 'ems'],
            'support_services': ['shelter', 'food', 'medical'],
            'communication': ['alerts', 'updates', 'coordination']
        }
        
    def detect(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Detect crisis situations and coordinate initial response."""
        # Simulate crisis detection
        crisis_events = self._detect_crisis_events(data.get('location', 'San Francisco'))
        coordination_needs = self._assess_coordination_needs(crisis_events)
        
        # Level-up: Holistic prevention chain detection
        prevention_chains = self._detect_prevention_chains(crisis_events)
        
        confidence = min(0.95, len(crisis_events) * 0.1 + len(coordination_needs) * 0.15 + len(prevention_chains) * 0.2)
        self.update_confidence(confidence)
        
        self.add_level_up_feature('prevention_chains', prevention_chains)
        
        return {
            'crisis_events': crisis_events,
            'coordination_needs': coordination_needs,
            'prevention_chains': prevention_chains,
            'confidence': confidence,
            'mode': 'detect',
            'level_up_message': f"Holistic prevention chains detected: {len(prevention_chains)} coordinated responses"
        }
    
    def predict(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Predict crisis escalation and resource needs."""
        crisis_events = data.get('crisis_events', [])
        prevention_chains = data.get('prevention_chains', [])
        
        # Predict crisis escalation
        escalation_predictions = self._predict_crisis_escalation(crisis_events)
        
        # Level-up: Resource prediction with prevention integration
        resource_predictions = self._predict_resource_needs(crisis_events, prevention_chains)
        
        confidence = min(0.9, len(escalation_predictions) * 0.1 + len(resource_predictions) * 0.15)
        self.update_confidence(confidence)
        
        self.add_level_up_feature('resource_predictions', resource_predictions)
        
        return {
            'escalation_predictions': escalation_predictions,
            'resource_predictions': resource_predictions,
            'confidence': confidence,
            'mode': 'predict',
            'level_up_message': f"Resource prediction with prevention integration - {len(resource_predictions)} needs identified"
        }
    
    def prevent(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate prevention strategies with holistic coordination."""
        crisis_events = data.get('crisis_events', [])
        prevention_chains = data.get('prevention_chains', [])
        resource_predictions = data.get('resource_predictions', [])
        
        prevention_strategies = []
        
        # Generate coordinated prevention strategies
        for chain in prevention_chains:
            strategy = {
                'type': 'coordinated_prevention',
                'crisis_type': chain.get('crisis_type'),
                'coordination_plan': chain.get('coordination_plan'),
                'resources_needed': chain.get('resources'),
                'priority': 'high'
            }
            prevention_strategies.append(strategy)
        
        # Level-up: Holistic prevention integration
        holistic_strategies = self._generate_holistic_strategies(crisis_events, prevention_chains)
        
        confidence = min(0.85, len(prevention_strategies) * 0.15 + len(holistic_strategies) * 0.1)
        self.update_confidence(confidence)
        
        self.add_level_up_feature('holistic_strategies', holistic_strategies)
        
        return {
            'strategies': prevention_strategies,
            'holistic_strategies': holistic_strategies,
            'confidence': confidence,
            'mode': 'prevent',
            'level_up_message': f"Holistic prevention integration - {len(holistic_strategies)} coordinated strategies"
        }
    
    def broadcast(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Broadcast crisis coordination data to other agents."""
        crisis_events = data.get('crisis_events', [])
        prevention_chains = data.get('prevention_chains', [])
        strategies = data.get('strategies', [])
        holistic_strategies = data.get('holistic_strategies', [])
        
        broadcast_data = {
            'crisis_events': crisis_events,
            'prevention_chains': prevention_chains,
            'prevention_strategies': strategies,
            'holistic_strategies': holistic_strategies,
            'resource_predictions': data.get('resource_predictions', [])
        }
        
        confidence = min(0.9, len(broadcast_data) * 0.1)
        self.update_confidence(confidence)
        
        return {
            'broadcast_data': broadcast_data,
            'confidence': confidence,
            'mode': 'broadcast',
            'level_up_message': f"Broadcasting crisis coordination with holistic prevention chains"
        }
    
    def _detect_crisis_events(self, location: str) -> List[Dict[str, Any]]:
        """Detect crisis events in the area."""
        # Simulate crisis event detection
        mock_crises = [
            {
                'id': 1,
                'type': 'natural_disaster',
                'subtype': 'fire',
                'location': 'Mission District',
                'severity': 0.8,
                'status': 'active',
                'resources_needed': ['fire_trucks', 'evacuation_support']
            },
            {
                'id': 2,
                'type': 'infrastructure',
                'subtype': 'power_outage',
                'location': 'Downtown',
                'severity': 0.6,
                'status': 'resolved',
                'resources_needed': ['generators', 'technical_support']
            },
            {
                'id': 3,
                'type': 'public_health',
                'subtype': 'outbreak',
                'location': 'Tenderloin',
                'severity': 0.7,
                'status': 'monitoring',
                'resources_needed': ['medical_supplies', 'testing_equipment']
            }
        ]
        return mock_crises
    
    def _assess_coordination_needs(self, crisis_events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Assess coordination needs for crisis response."""
        coordination_needs = []
        
        for crisis in crisis_events:
            if crisis.get('severity', 0) > 0.6:
                coordination_needs.append({
                    'crisis_id': crisis['id'],
                    'coordination_type': 'multi_agency',
                    'agencies_needed': ['police', 'fire', 'ems'],
                    'communication_priority': 'high',
                    'resource_coordination': crisis.get('resources_needed', [])
                })
        
        return coordination_needs
    
    def _detect_prevention_chains(self, crisis_events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Detect holistic prevention chains for crisis coordination."""
        prevention_chains = []
        
        # Level-up: Holistic prevention chain detection
        for crisis in crisis_events:
            if crisis.get('severity', 0) > 0.7:
                chain = {
                    'crisis_type': crisis['type'],
                    'location': crisis['location'],
                    'coordination_plan': {
                        'immediate_response': ['first_responders', 'evacuation'],
                        'secondary_response': ['support_services', 'communication'],
                        'prevention_measures': ['early_warning', 'preparedness_training']
                    },
                    'resources': crisis.get('resources_needed', []),
                    'prevention_effectiveness': 0.85
                }
                prevention_chains.append(chain)
        
        return prevention_chains
    
    def _predict_crisis_escalation(self, crisis_events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Predict crisis escalation patterns."""
        escalation_predictions = []
        
        for crisis in crisis_events:
            if crisis.get('status') == 'active':
                escalation_predictions.append({
                    'crisis_id': crisis['id'],
                    'escalation_probability': 0.6,
                    'time_to_escalation': '2-4 hours',
                    'affected_area_expansion': 'likely',
                    'resource_intensification': 'high'
                })
        
        return escalation_predictions
    
    def _predict_resource_needs(self, crisis_events: List[Dict[str, Any]], prevention_chains: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Predict resource needs with prevention integration."""
        resource_predictions = []
        
        # Level-up: Resource prediction with prevention integration
        for chain in prevention_chains:
            resource_predictions.append({
                'crisis_type': chain['crisis_type'],
                'location': chain['location'],
                'immediate_resources': chain['resources'],
                'prevention_resources': ['training_materials', 'early_warning_systems'],
                'coordination_resources': ['communication_systems', 'coordination_platforms'],
                'estimated_cost': 500000,
                'prevention_roi': 3.2  # 320% return on prevention investment
            })
        
        return resource_predictions
    
    def _generate_holistic_strategies(self, crisis_events: List[Dict[str, Any]], prevention_chains: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate holistic prevention strategies."""
        holistic_strategies = []
        
        # Level-up: Holistic prevention integration
        for chain in prevention_chains:
            strategy = {
                'type': 'holistic_prevention',
                'crisis_type': chain['crisis_type'],
                'coordination_approach': 'multi_agency_integration',
                'prevention_measures': [
                    'early_warning_systems',
                    'community_preparedness_training',
                    'resource_prepositioning',
                    'cross_agency_coordination'
                ],
                'expected_outcome': 'reduced_response_time_and_impact',
                'implementation_timeline': '6-12 months'
            }
            holistic_strategies.append(strategy)
        
        return holistic_strategies 