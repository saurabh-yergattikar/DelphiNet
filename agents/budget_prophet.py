from typing import Dict, List, Any
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import requests
from .base_agent import BaseAgent, AgentMode

class BudgetProphet(BaseAgent):
    """Budget Prophet Agent: Predicts funding allocation with federal simulation for Bay Area disparities."""
    
    def __init__(self):
        super().__init__("Budget Prophet", threshold=0.8)
        self.funding_categories = {
            'housing': ['homeless_services', 'affordable_housing', 'rental_assistance'],
            'infrastructure': ['street_maintenance', 'public_transport', 'utilities'],
            'social_services': ['healthcare', 'education', 'food_assistance']
        }
        self.federal_funding_sources = {
            'hud': 'Housing and Urban Development',
            'dot': 'Department of Transportation',
            'hhs': 'Health and Human Services'
        }
        # Level-up: Funding maps with homeless alignment
        self.funding_maps = {
            'homeless_hotspots': ['Tenderloin', 'Mission District', 'South of Market', 'Civic Center'],
            'funding_priorities': ['emergency_shelter', 'permanent_housing', 'support_services', 'prevention'],
            'geographic_impact': ['high', 'medium', 'low']
        }
        
    def detect(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Detect current funding allocations and gaps."""
        # Simulate current budget data
        current_allocations = self._fetch_current_allocations(data.get('location', 'San Francisco'))
        funding_gaps = self._detect_funding_gaps(current_allocations)
        
        # Level-up: Federal funding simulation
        federal_opportunities = self._simulate_federal_funding(current_allocations)
        
        confidence = min(0.9, len(current_allocations) * 0.1 + len(funding_gaps) * 0.15 + len(federal_opportunities) * 0.2)
        self.update_confidence(confidence)
        
        self.add_level_up_feature('federal_simulation', federal_opportunities)
        
        return {
            'current_allocations': current_allocations,
            'funding_gaps': funding_gaps,
            'federal_opportunities': federal_opportunities,
            'confidence': confidence,
            'mode': 'detect',
            'level_up_message': f"Federal funding sim: {len(federal_opportunities)} opportunities detected"
        }
    
    def predict(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Predict funding drops/spikes with federal simulation."""
        current_allocations = data.get('current_allocations', [])
        federal_opportunities = data.get('federal_opportunities', [])
        
        # Predict funding trends
        funding_predictions = self._predict_funding_trends(current_allocations)
        
        # Level-up: Federal funding maps for Bay Area disparities
        bay_area_disparities = self._simulate_bay_area_disparities(federal_opportunities)
        
        confidence = min(0.85, len(funding_predictions) * 0.1 + len(bay_area_disparities) * 0.15)
        self.update_confidence(confidence)
        
        self.add_level_up_feature('bay_area_disparities', bay_area_disparities)
        
        return {
            'funding_predictions': funding_predictions,
            'bay_area_disparities': bay_area_disparities,
            'confidence': confidence,
            'mode': 'predict',
            'level_up_message': f"Bay Area disparities mapped - {len(bay_area_disparities)} funding gaps"
        }
    
    def prevent(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate reallocation strategies with federal funding integration."""
        funding_gaps = data.get('funding_gaps', [])
        federal_opportunities = data.get('federal_opportunities', [])
        bay_area_disparities = data.get('bay_area_disparities', [])
        
        reallocation_strategies = []
        
        # Generate reallocation strategies
        for gap in funding_gaps:
            if gap.get('severity', 0) > 0.7:
                strategy = {
                    'type': 'reallocation',
                    'category': gap.get('category'),
                    'amount': gap.get('shortfall'),
                    'source': 'general_fund',
                    'priority': 'high'
                }
                reallocation_strategies.append(strategy)
        
        # Level-up: Federal funding integration
        federal_strategies = self._generate_federal_strategies(federal_opportunities, bay_area_disparities)
        
        confidence = min(0.8, len(reallocation_strategies) * 0.15 + len(federal_strategies) * 0.1)
        self.update_confidence(confidence)
        
        self.add_level_up_feature('federal_strategies', federal_strategies)
        
        return {
            'strategies': reallocation_strategies,
            'federal_strategies': federal_strategies,
            'confidence': confidence,
            'mode': 'prevent',
            'level_up_message': f"Federal funding integration - {len(federal_strategies)} strategies"
        }
    
    def broadcast(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Broadcast budget findings to other agents."""
        allocations = data.get('current_allocations', [])
        predictions = data.get('funding_predictions', [])
        strategies = data.get('strategies', [])
        federal_strategies = data.get('federal_strategies', [])
        
        broadcast_data = {
            'budget_allocations': allocations,
            'predictions': predictions,
            'reallocation_strategies': strategies,
            'federal_strategies': federal_strategies,
            'bay_area_disparities': data.get('bay_area_disparities', [])
        }
        
        confidence = min(0.9, len(broadcast_data) * 0.1)
        self.update_confidence(confidence)
        
        return {
            'broadcast_data': broadcast_data,
            'confidence': confidence,
            'mode': 'broadcast',
            'level_up_message': f"Broadcasting budget data with federal funding maps"
        }
    
    def _fetch_current_allocations(self, location: str) -> List[Dict[str, Any]]:
        """Simulate current budget allocation data."""
        mock_allocations = [
            {'category': 'housing', 'amount': 50000000, 'year': 2024, 'source': 'general_fund'},
            {'category': 'infrastructure', 'amount': 75000000, 'year': 2024, 'source': 'general_fund'},
            {'category': 'social_services', 'amount': 30000000, 'year': 2024, 'source': 'general_fund'},
            {'category': 'homeless_services', 'amount': 25000000, 'year': 2024, 'source': 'federal'},
            {'category': 'public_transport', 'amount': 40000000, 'year': 2024, 'source': 'federal'}
        ]
        return mock_allocations
    
    def _detect_funding_gaps(self, allocations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Detect funding gaps and shortfalls."""
        gaps = []
        
        # Simulate gap detection
        expected_funding = {
            'housing': 60000000,
            'infrastructure': 80000000,
            'social_services': 35000000
        }
        
        for allocation in allocations:
            category = allocation['category']
            if category in expected_funding:
                expected = expected_funding[category]
                actual = allocation['amount']
                shortfall = expected - actual
                
                if shortfall > 0:
                    gaps.append({
                        'category': category,
                        'shortfall': shortfall,
                        'severity': min(1.0, shortfall / expected),
                        'description': f"Underfunded {category} by ${shortfall:,}"
                    })
        
        return gaps
    
    def _simulate_federal_funding(self, allocations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Simulate federal funding opportunities."""
        opportunities = []
        
        # Level-up: Federal funding simulation for Bay Area
        federal_programs = [
            {
                'program': 'HUD Community Development Block Grant',
                'amount': 15000000,
                'eligibility': 'high_poverty_areas',
                'application_deadline': '2024-12-31'
            },
            {
                'program': 'DOT Infrastructure Investment',
                'amount': 25000000,
                'eligibility': 'transportation_projects',
                'application_deadline': '2024-10-15'
            },
            {
                'program': 'HHS Social Services Block Grant',
                'amount': 8000000,
                'eligibility': 'social_services',
                'application_deadline': '2024-11-30'
            }
        ]
        
        for program in federal_programs:
            opportunities.append({
                'program': program['program'],
                'amount': program['amount'],
                'eligibility': program['eligibility'],
                'deadline': program['application_deadline'],
                'probability': 0.7,  # 70% chance of approval
                'impact': 'high'
            })
        
        return opportunities
    
    def _predict_funding_trends(self, allocations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Predict funding drops and spikes."""
        predictions = []
        
        # Simulate funding trend predictions
        for allocation in allocations:
            category = allocation['category']
            current_amount = allocation['amount']
            
            # Predict based on category and current funding
            if category == 'housing':
                predicted_change = 0.15  # 15% increase
            elif category == 'infrastructure':
                predicted_change = 0.10  # 10% increase
            else:
                predicted_change = 0.05  # 5% increase
            
            predictions.append({
                'category': category,
                'current_amount': current_amount,
                'predicted_change': predicted_change,
                'predicted_amount': current_amount * (1 + predicted_change),
                'confidence': 0.8
            })
        
        return predictions
    
    def _simulate_bay_area_disparities(self, federal_opportunities: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Simulate Bay Area funding disparities with homeless alignment."""
        disparities = []
        
        # Level-up: Bay Area disparities mapping with homeless hotspots
        bay_area_regions = [
            {'region': 'San Francisco', 'poverty_rate': 0.12, 'funding_per_capita': 2500, 'homeless_population': 8000},
            {'region': 'Oakland', 'poverty_rate': 0.18, 'funding_per_capita': 1800, 'homeless_population': 4000},
            {'region': 'San Jose', 'poverty_rate': 0.08, 'funding_per_capita': 2200, 'homeless_population': 6000},
            {'region': 'Richmond', 'poverty_rate': 0.22, 'funding_per_capita': 1500, 'homeless_population': 2000}
        ]
        
        for region in bay_area_regions:
            # Enhanced disparity calculation with homeless alignment
            homeless_factor = region['homeless_population'] / 10000  # Normalize to 0-1 scale
            poverty_factor = region['poverty_rate']
            
            # Calculate composite need score
            need_score = (homeless_factor * 0.6) + (poverty_factor * 0.4)
            
            if need_score > 0.15 and region['funding_per_capita'] < 2000:
                disparities.append({
                    'region': region['region'],
                    'poverty_rate': region['poverty_rate'],
                    'homeless_population': region['homeless_population'],
                    'need_score': need_score,
                    'funding_gap': 2000 - region['funding_per_capita'],
                    'priority': 'high' if need_score > 0.2 else 'medium',
                    'recommended_funding': region['funding_per_capita'] * (1 + need_score),
                    'funding_priorities': self._get_funding_priorities(region['region'])
                })
        
        return disparities
    
    def _get_funding_priorities(self, region: str) -> List[str]:
        """Get funding priorities based on region characteristics."""
        if region == 'San Francisco':
            return ['permanent_housing', 'support_services', 'emergency_shelter']
        elif region == 'Oakland':
            return ['emergency_shelter', 'permanent_housing', 'prevention']
        elif region == 'San Jose':
            return ['support_services', 'permanent_housing', 'prevention']
        else:
            return ['emergency_shelter', 'support_services', 'prevention']
    
    def _generate_federal_strategies(self, opportunities: List[Dict[str, Any]], disparities: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate federal funding strategies."""
        strategies = []
        
        for opportunity in opportunities:
            if opportunity.get('probability', 0) > 0.6:
                strategies.append({
                    'type': 'federal_grant',
                    'program': opportunity['program'],
                    'amount': opportunity['amount'],
                    'target_regions': [d['region'] for d in disparities],
                    'application_strategy': 'high_priority',
                    'expected_roi': 2.5  # 250% return on application effort
                })
        
        return strategies 