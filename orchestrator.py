from typing import Dict, List, Any, Optional
import numpy as np
import pandas as pd
import networkx as nx
from sympy import symbols, solve, Eq
from pulp import *
import requests
from agents.street_precog import StreetPrecog
from agents.housing_oracle import HousingOracle
from agents.budget_prophet import BudgetProphet
from agents.crisis_sage import CrisisSage
import streamlit as st

class Orchestrator:
    """Orchestrator: Coordinates all agents with ROI optimization and funding simulations."""
    
    def __init__(self):
        self.agents = {
            'street_precog': StreetPrecog(),
            'housing_oracle': HousingOracle(),
            'budget_prophet': BudgetProphet(),
            'crisis_sage': CrisisSage()
        }
        self.city_graph = nx.Graph()
        self.roi_threshold = 0.75
        self.funding_simulations = {}
        self.coordination_history = []
        
    def coordinate_agents(self, scenario_data: Dict[str, Any]) -> Dict[str, Any]:
        """Coordinate all agents in a predictive chain."""
        coordination_results = {}
        
        # Step 1: Detect phase
        st.write("🔍 **Phase 1: Detection**")
        detection_results = self._run_detection_phase(scenario_data)
        coordination_results['detection'] = detection_results
        
        # Step 2: Predict phase
        st.write("🔮 **Phase 2: Prediction**")
        prediction_results = self._run_prediction_phase(detection_results)
        coordination_results['prediction'] = prediction_results
        
        # Step 3: Prevent phase
        st.write("🛡️ **Phase 3: Prevention**")
        prevention_results = self._run_prevention_phase(prediction_results)
        coordination_results['prevention'] = prevention_results
        
        # Step 4: ROI optimization with funding simulations
        st.write("💰 **Phase 4: ROI Optimization**")
        roi_results = self._optimize_roi_with_funding(prevention_results)
        coordination_results['roi_optimization'] = roi_results
        
        # Step 5: Broadcast results
        st.write("📡 **Phase 5: Broadcasting**")
        broadcast_results = self._run_broadcast_phase(coordination_results)
        coordination_results['broadcast'] = broadcast_results
        
        return coordination_results
    
    def _run_detection_phase(self, scenario_data: Dict[str, Any]) -> Dict[str, Any]:
        """Run detection phase across all agents."""
        detection_results = {}
        
        for agent_name, agent in self.agents.items():
            agent.set_mode(agent.mode.__class__.DETECT)
            result = agent.execute(scenario_data)
            detection_results[agent_name] = result
            
            # Level-up: Show detection status with challenge alignments
            level_up_status = result.get('level_up_status', {})
            st.success(f"✅ {agent_name}: {result.get('level_up_message', 'Detection completed')}")
            
            if level_up_status.get('level_up_features'):
                for feature, data in level_up_status['level_up_features'].items():
                    st.info(f"🎯 Level-up: {feature} - {len(data) if isinstance(data, list) else data}")
        
        return detection_results
    
    def _run_prediction_phase(self, detection_results: Dict[str, Any]) -> Dict[str, Any]:
        """Run prediction phase with agent coordination."""
        prediction_results = {}
        
        # Combine detection data for cross-agent predictions
        combined_data = self._combine_detection_data(detection_results)
        
        for agent_name, agent in self.agents.items():
            agent.set_mode(agent.mode.__class__.PREDICT)
            result = agent.execute(combined_data)
            prediction_results[agent_name] = result
            
            # Level-up: Show prediction status with challenge alignments
            level_up_status = result.get('level_up_status', {})
            st.success(f"🔮 {agent_name}: {result.get('level_up_message', 'Prediction completed')}")
            
            if level_up_status.get('level_up_features'):
                for feature, data in level_up_status['level_up_features'].items():
                    st.info(f"🎯 Level-up: {feature} - {len(data) if isinstance(data, list) else data}")
        
        return prediction_results
    
    def _run_prevention_phase(self, prediction_results: Dict[str, Any]) -> Dict[str, Any]:
        """Run prevention phase with holistic strategies."""
        prevention_results = {}
        
        # Combine prediction data for coordinated prevention
        combined_data = self._combine_prediction_data(prediction_results)
        
        for agent_name, agent in self.agents.items():
            agent.set_mode(agent.mode.__class__.PREVENT)
            result = agent.execute(combined_data)
            prevention_results[agent_name] = result
            
            # Level-up: Show prevention status with challenge alignments
            level_up_status = result.get('level_up_status', {})
            st.success(f"🛡️ {agent_name}: {result.get('level_up_message', 'Prevention completed')}")
            
            if level_up_status.get('level_up_features'):
                for feature, data in level_up_status['level_up_features'].items():
                    st.info(f"🎯 Level-up: {feature} - {len(data) if isinstance(data, list) else data}")
        
        return prevention_results
    
    def _optimize_roi_with_funding(self, prevention_results: Dict[str, Any]) -> Dict[str, Any]:
        """Optimize ROI with federal funding simulations."""
        roi_results = {}
        
        # Level-up: Federal funding simulation
        funding_simulation = self._simulate_federal_funding(prevention_results)
        
        # Calculate ROI for each prevention strategy
        roi_calculations = self._calculate_roi(prevention_results, funding_simulation)
        
        # Optimize resource allocation
        optimization_result = self._optimize_resource_allocation(roi_calculations)
        
        roi_results = {
            'funding_simulation': funding_simulation,
            'roi_calculations': roi_calculations,
            'optimization_result': optimization_result,
            'total_roi': self._calculate_total_roi(roi_calculations),
            'funding_opportunities': len(funding_simulation.get('opportunities', [])),
            'level_up_message': f"ROI optimization with federal funding: {len(funding_simulation.get('opportunities', []))} opportunities"
        }
        
        st.success(f"💰 ROI Optimization: {roi_results['total_roi']:.2f}x return with {roi_results['funding_opportunities']} funding opportunities")
        
        return roi_results
    
    def _run_broadcast_phase(self, coordination_results: Dict[str, Any]) -> Dict[str, Any]:
        """Run broadcast phase to share results across agents."""
        broadcast_results = {}
        
        # Combine all results for broadcasting
        combined_data = self._combine_all_results(coordination_results)
        
        for agent_name, agent in self.agents.items():
            agent.set_mode(agent.mode.__class__.BROADCAST)
            result = agent.execute(combined_data)
            broadcast_results[agent_name] = result
            
            st.success(f"📡 {agent_name}: Broadcasting completed")
        
        return broadcast_results
    
    def _combine_detection_data(self, detection_results: Dict[str, Any]) -> Dict[str, Any]:
        """Combine detection data from all agents."""
        combined_data = {}
        
        for agent_name, result in detection_results.items():
            combined_data[f"{agent_name}_detection"] = result
        
        return combined_data
    
    def _combine_prediction_data(self, prediction_results: Dict[str, Any]) -> Dict[str, Any]:
        """Combine prediction data from all agents."""
        combined_data = {}
        
        for agent_name, result in prediction_results.items():
            combined_data[f"{agent_name}_prediction"] = result
        
        return combined_data
    
    def _combine_all_results(self, coordination_results: Dict[str, Any]) -> Dict[str, Any]:
        """Combine all results for broadcasting."""
        combined_data = {}
        
        for phase, results in coordination_results.items():
            combined_data[phase] = results
        
        return combined_data
    
    def _simulate_federal_funding(self, prevention_results: Dict[str, Any]) -> Dict[str, Any]:
        """Simulate federal funding opportunities."""
        opportunities = []
        
        # Level-up: Federal funding simulation for Bay Area
        federal_programs = [
            {
                'program': 'HUD Community Development Block Grant',
                'amount': 15000000,
                'eligibility_criteria': ['high_poverty_areas', 'housing_development'],
                'application_deadline': '2024-12-31',
                'roi_multiplier': 2.5
            },
            {
                'program': 'DOT Infrastructure Investment',
                'amount': 25000000,
                'eligibility_criteria': ['transportation_projects', 'infrastructure_improvement'],
                'application_deadline': '2024-10-15',
                'roi_multiplier': 3.0
            },
            {
                'program': 'HHS Social Services Block Grant',
                'amount': 8000000,
                'eligibility_criteria': ['social_services', 'healthcare_access'],
                'application_deadline': '2024-11-30',
                'roi_multiplier': 2.8
            }
        ]
        
        for program in federal_programs:
            opportunities.append({
                'program': program['program'],
                'amount': program['amount'],
                'eligibility_criteria': program['eligibility_criteria'],
                'deadline': program['application_deadline'],
                'roi_multiplier': program['roi_multiplier'],
                'probability': 0.7,
                'impact': 'high'
            })
        
        return {
            'opportunities': opportunities,
            'total_potential_funding': sum(o['amount'] for o in opportunities),
            'average_roi_multiplier': np.mean([o['roi_multiplier'] for o in opportunities])
        }
    
    def _calculate_roi(self, prevention_results: Dict[str, Any], funding_simulation: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Calculate ROI for prevention strategies."""
        roi_calculations = []
        
        for agent_name, result in prevention_results.items():
            strategies = result.get('strategies', [])
            
            for strategy in strategies:
                base_cost = 100000  # Base cost for strategy
                base_benefit = 250000  # Base benefit
                
                # Apply funding multiplier if applicable
                funding_multiplier = 1.0
                if funding_simulation.get('opportunities'):
                    funding_multiplier = funding_simulation['average_roi_multiplier']
                
                roi = (base_benefit * funding_multiplier) / base_cost
                
                roi_calculations.append({
                    'agent': agent_name,
                    'strategy': strategy.get('type', 'unknown'),
                    'cost': base_cost,
                    'benefit': base_benefit * funding_multiplier,
                    'roi': roi,
                    'funding_applied': funding_multiplier > 1.0
                })
        
        return roi_calculations
    
    def _optimize_resource_allocation(self, roi_calculations: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Optimize resource allocation using linear programming."""
        # Create optimization problem
        prob = LpProblem("Resource_Allocation", LpMaximize)
        
        # Decision variables
        strategy_vars = {}
        for i, calc in enumerate(roi_calculations):
            strategy_vars[i] = LpVariable(f"strategy_{i}", 0, 1, LpBinary)
        
        # Objective function: maximize total benefit
        prob += lpSum([calc['benefit'] * strategy_vars[i] for i, calc in enumerate(roi_calculations)])
        
        # Constraints
        total_budget = 1000000  # $1M budget
        prob += lpSum([calc['cost'] * strategy_vars[i] for i, calc in enumerate(roi_calculations)]) <= total_budget
        
        # Solve
        prob.solve()
        
        # Extract results
        selected_strategies = []
        total_cost = 0
        total_benefit = 0
        
        for i, calc in enumerate(roi_calculations):
            if strategy_vars[i].value() == 1:
                selected_strategies.append(calc)
                total_cost += calc['cost']
                total_benefit += calc['benefit']
        
        return {
            'selected_strategies': selected_strategies,
            'total_cost': total_cost,
            'total_benefit': total_benefit,
            'optimization_status': LpStatus[prob.status]
        }
    
    def _calculate_total_roi(self, roi_calculations: List[Dict[str, Any]]) -> float:
        """Calculate total ROI across all strategies."""
        if not roi_calculations:
            return 0.0
        
        total_cost = sum(calc['cost'] for calc in roi_calculations)
        total_benefit = sum(calc['benefit'] for calc in roi_calculations)
        
        if total_cost == 0:
            return 0.0
        
        return total_benefit / total_cost
    
    def get_agent_status(self) -> Dict[str, Any]:
        """Get status of all agents."""
        status = {}
        for agent_name, agent in self.agents.items():
            status[agent_name] = {
                'confidence': agent.get_confidence(),
                'threshold_met': agent.meets_threshold(),
                'mode': agent.mode.value,
                'level_up_features': agent.level_up_features
            }
        return status 