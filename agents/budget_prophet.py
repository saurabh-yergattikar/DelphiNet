from typing import Dict, List, Any
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import requests
from .base_agent import BaseAgent, AgentMode

class BudgetProphet(BaseAgent):
    """Budget Prophet Agent: Predicts funding allocation with federal simulations and Bay Area disparities."""
    
    def __init__(self):
        super().__init__("Budget Prophet", threshold=0.8)
        self.funding_maps = {
            'homeless_hotspots': ['Tenderloin', 'Mission District', 'South of Market', 'Civic Center'],
            'funding_priorities': ['emergency_shelter', 'permanent_housing', 'support_services', 'prevention'],
            'geographic_impact': ['high', 'medium', 'low']
        }
        self.federal_programs = {
            'HUD': ['Section 8', 'CDBG', 'HOME'],
            'HHS': ['SNAP', 'TANF', 'Medicaid'],
            'DOT': ['Highway Trust Fund', 'Transit Grants']
        }
        
    def detect(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Detect current budget allocations and funding opportunities."""
        # Simulate current budget data
        current_allocations = self._fetch_budget_data(data.get('location', 'San Francisco'))
        
        # Simulate federal funding opportunities
        federal_opportunities = self._fetch_federal_opportunities()
        
        # Detect funding disparities
        disparities = self._detect_funding_disparities(current_allocations)
        
        # Calculate confidence
        confidence = min(0.9, len(current_allocations) * 0.1 + len(federal_opportunities) * 0.15)
        self.update_confidence(confidence)
        
        # Level-up: Federal simulation
        self.add_level_up_feature('federal_simulation', len(federal_opportunities))
        
        return {
            'current_allocations': current_allocations,
            'federal_opportunities': federal_opportunities,
            'funding_disparities': disparities,
            'confidence': confidence,
            'mode': 'detect',
            'level_up_message': f"Federal funding sim: {len(federal_opportunities)} opportunities detected"
        }
    
    def predict(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Predict funding trends and budget impacts."""
        current_allocations = data.get('current_allocations', [])
        federal_opportunities = data.get('federal_opportunities', [])
        
        # Predict funding trends
        funding_trends = self._predict_funding_trends(current_allocations)
        
        # Predict budget shortfalls
        budget_shortfalls = self._predict_budget_shortfalls(current_allocations)
        
        # Predict ROI for different programs
        roi_predictions = self._predict_program_roi(federal_opportunities)
        
        # Combine all predictions
        all_predictions = funding_trends + budget_shortfalls + roi_predictions
        
        confidence = min(0.85, len(all_predictions) * 0.15)
        self.update_confidence(confidence)
        
        return {
            'funding_predictions': all_predictions,
            'funding_trends': funding_trends,
            'budget_shortfalls': budget_shortfalls,
            'roi_predictions': roi_predictions,
            'confidence': confidence,
            'mode': 'predict',
            'level_up_message': f"Funding trends predicted with {len(roi_predictions)} ROI forecasts"
        }
    
    def prevent(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate budget reallocation strategies with federal funding."""
        current_allocations = data.get('current_allocations', [])
        federal_opportunities = data.get('federal_opportunities', [])
        funding_predictions = data.get('funding_predictions', [])
        
        # Generate reallocation strategies
        reallocation_strategies = self._generate_reallocation_strategies(current_allocations, funding_predictions)
        
        # Generate federal funding strategies
        federal_strategies = self._generate_federal_strategies(federal_opportunities)
        
        # Generate homeless alignment strategies
        homeless_strategies = self._generate_homeless_strategies(current_allocations)
        
        # Combine all strategies
        all_strategies = reallocation_strategies + federal_strategies + homeless_strategies
        
        confidence = min(0.8, len(all_strategies) * 0.15)
        self.update_confidence(confidence)
        
        return {
            'strategies': all_strategies,
            'federal_strategies': federal_strategies,
            'reallocation_strategies': reallocation_strategies,
            'homeless_strategies': homeless_strategies,
            'confidence': confidence,
            'mode': 'prevent',
            'level_up_message': f"Developed {len(federal_strategies)} federal strategies"
        }
    
    def broadcast(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Broadcast budget findings to other agents."""
        current_allocations = data.get('current_allocations', [])
        funding_predictions = data.get('funding_predictions', [])
        strategies = data.get('strategies', [])
        
        broadcast_data = {
            'budget_allocations': current_allocations,
            'funding_predictions': funding_predictions,
            'prevention_strategies': strategies,
            'federal_opportunities': data.get('federal_opportunities', []),
            'funding_disparities': data.get('funding_disparities', [])
        }
        
        confidence = min(0.9, len(broadcast_data) * 0.1)
        self.update_confidence(confidence)
        
        return {
            'broadcast_data': broadcast_data,
            'confidence': confidence,
            'mode': 'broadcast',
            'level_up_message': f"Broadcasting {len(current_allocations)} budget items with federal opportunities"
        }
    
    def _fetch_budget_data(self, location: str) -> List[Dict[str, Any]]:
        """Simulate budget data fetch."""
        mock_budget_items = [
            {'id': 1, 'category': 'homeless_services', 'amount': 50000000, 'location': 'Tenderloin', 'priority': 'high'},
            {'id': 2, 'category': 'housing_development', 'amount': 75000000, 'location': 'Mission District', 'priority': 'high'},
            {'id': 3, 'category': 'street_maintenance', 'amount': 30000000, 'location': 'Downtown', 'priority': 'medium'},
            {'id': 4, 'category': 'public_safety', 'amount': 45000000, 'location': 'Civic Center', 'priority': 'high'},
            {'id': 5, 'category': 'social_services', 'amount': 25000000, 'location': 'South of Market', 'priority': 'medium'}
        ]
        return mock_budget_items
    
    def _fetch_federal_opportunities(self) -> List[Dict[str, Any]]:
        """Simulate federal funding opportunities."""
        mock_opportunities = [
            {'id': 1, 'program': 'HUD Section 8', 'amount': 20000000, 'roi_multiplier': 1.5, 'probability': 0.8},
            {'id': 2, 'program': 'CDBG Grant', 'amount': 15000000, 'roi_multiplier': 1.3, 'probability': 0.7},
            {'id': 3, 'program': 'HOME Investment', 'amount': 10000000, 'roi_multiplier': 1.4, 'probability': 0.6}
        ]
        return mock_opportunities
    
    def _detect_funding_disparities(self, current_allocations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Detect funding disparities using Bay Area simulation."""
        disparities = []
        
        # Simulate Bay Area regions with homeless alignment
        bay_area_regions = [
            {'region': 'San Francisco', 'poverty_rate': 0.12, 'homeless_population': 8000, 'funding_per_capita': 1500},
            {'region': 'Oakland', 'poverty_rate': 0.18, 'homeless_population': 4000, 'funding_per_capita': 1200},
            {'region': 'San Jose', 'poverty_rate': 0.10, 'homeless_population': 6000, 'funding_per_capita': 1800},
            {'region': 'Berkeley', 'poverty_rate': 0.15, 'homeless_population': 2000, 'funding_per_capita': 2000}
        ]
        
        for region in bay_area_regions:
            homeless_factor = region['homeless_population'] / 10000
            poverty_factor = region['poverty_rate']
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
            return ['emergency_shelter', 'permanent_housing', 'support_services']
        elif region == 'Oakland':
            return ['permanent_housing', 'prevention', 'support_services']
        elif region == 'San Jose':
            return ['support_services', 'emergency_shelter', 'prevention']
        else:
            return ['prevention', 'support_services', 'emergency_shelter']
    
    def _predict_funding_trends(self, current_allocations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Predict funding trends based on current allocations."""
        trends = []
        
        # Predict trends by category
        categories = {}
        for allocation in current_allocations:
            category = allocation['category']
            if category not in categories:
                categories[category] = []
            categories[category].append(allocation['amount'])
        
        for category, amounts in categories.items():
            avg_amount = np.mean(amounts)
            trend = 'increasing' if avg_amount > 40000000 else 'stable' if avg_amount > 20000000 else 'decreasing'
            
            trends.append({
                'type': 'funding_trend',
                'category': category,
                'prediction': f"{trend.capitalize()} funding trend",
                'current_average': avg_amount,
                'confidence': 0.75
            })
        
        return trends
    
    def _predict_budget_shortfalls(self, current_allocations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Predict budget shortfalls."""
        shortfalls = []
        
        total_budget = sum(allocation['amount'] for allocation in current_allocations)
        projected_needs = total_budget * 1.2  # 20% increase needed
        
        if projected_needs > total_budget:
            shortfalls.append({
                'type': 'budget_shortfall',
                'prediction': 'Projected budget shortfall',
                'current_budget': total_budget,
                'projected_needs': projected_needs,
                'shortfall_amount': projected_needs - total_budget,
                'confidence': 0.8
            })
        
        return shortfalls
    
    def _predict_program_roi(self, federal_opportunities: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Predict ROI for different federal programs."""
        roi_predictions = []
        
        for opportunity in federal_opportunities:
            roi_predictions.append({
                'type': 'program_roi',
                'program': opportunity['program'],
                'prediction': f"ROI multiplier: {opportunity['roi_multiplier']}x",
                'amount': opportunity['amount'],
                'probability': opportunity['probability'],
                'confidence': 0.7
            })
        
        return roi_predictions
    
    def _generate_reallocation_strategies(self, current_allocations: List[Dict[str, Any]], funding_predictions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate budget reallocation strategies."""
        strategies = []
        
        # Generate strategies based on funding trends
        for prediction in funding_predictions:
            if prediction['type'] == 'funding_trend':
                if 'decreasing' in prediction['prediction']:
                    strategies.append({
                        'type': 'reallocation',
                        'target': prediction['category'],
                        'action': 'Increase funding allocation',
                        'priority': 'high' if prediction['current_average'] < 20000000 else 'medium'
                    })
        
        return strategies
    
    def _generate_federal_strategies(self, federal_opportunities: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate federal funding strategies."""
        strategies = []
        
        for opportunity in federal_opportunities:
            if opportunity['probability'] > 0.6:
                strategies.append({
                    'type': 'federal',
                    'target': opportunity['program'],
                    'action': f"Apply for {opportunity['program']} funding",
                    'amount': opportunity['amount'],
                    'priority': 'high' if opportunity['roi_multiplier'] > 1.4 else 'medium'
                })
        
        return strategies
    
    def _generate_homeless_strategies(self, current_allocations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Generate homeless alignment strategies."""
        strategies = []
        
        homeless_allocations = [a for a in current_allocations if a['category'] == 'homeless_services']
        if homeless_allocations:
            total_homeless_funding = sum(a['amount'] for a in homeless_allocations)
            
            if total_homeless_funding < 60000000:  # Threshold for adequate funding
                strategies.append({
                    'type': 'homeless',
                    'action': 'Increase homeless services funding',
                    'current_amount': total_homeless_funding,
                    'recommended_amount': 60000000,
                    'priority': 'high'
                })
        
        return strategies 