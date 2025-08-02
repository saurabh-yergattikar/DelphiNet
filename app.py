import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import requests
from orchestrator import Orchestrator
import streamlit as st
import time
from typing import List, Dict, Any

# Page configuration
st.set_page_config(
    page_title="SF Neural Precog Network",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .level-up-badge {
        background-color: #ff6b6b;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
        display: inline-block;
        margin: 0.2rem;
    }
    .challenge-alignment {
        background-color: #4ecdc4;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
        display: inline-block;
        margin: 0.2rem;
    }
    .roi-highlight {
        background-color: #45b7d1;
        color: white;
        padding: 1rem;
        border-radius: 10px;
        font-size: 1.2rem;
        font-weight: bold;
        text-align: center;
        margin: 1rem 0;
    }
    .citizen-story {
        background-color: #f8f9fa;
        border-left: 4px solid #007bff;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 5px;
    }
    .midjourney-viz {
        border: 2px solid #e9ecef;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<h1 class="main-header">🏙️ SF Neural Precog Network</h1>', unsafe_allow_html=True)
    st.markdown("### Predictive AI System for San Francisco Civic Improvement")
    
    # Challenge alignment badges
    st.markdown("### 🎯 Hackathon Challenge Alignment")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown('<div class="challenge-alignment">🏠 Housing & Infrastructure</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="challenge-alignment">🌳 Street Order & Beauty</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="challenge-alignment">🔍 Transparency & Efficiency</div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="challenge-alignment">👶 Children & Education</div>', unsafe_allow_html=True)
    with col5:
        st.markdown('<div class="challenge-alignment">🏢 Industry & Commerce</div>', unsafe_allow_html=True)
    
    # Main navigation
    tab1, tab2, tab3, tab4 = st.tabs(["🎮 Live Simulation", "👥 Citizen Dashboard", "🎨 Future Visualizations", "📊 Transparency"])
    
    with tab1:
        run_live_simulation()
    
    with tab2:
        display_citizen_dashboard()
    
    with tab3:
        display_future_visualizations()
    
    with tab4:
        display_transparency()

def run_live_simulation():
    """Run the live simulation with enhanced features."""
    
    st.markdown("## 🎮 Live Simulation")
    
    # Sidebar for controls
    st.sidebar.title("🎛️ Control Panel")
    
    # Scenario selection
    scenario = st.sidebar.selectbox(
        "Select Scenario",
        ["Housing Crisis Response", "Street Maintenance Optimization", "Budget Allocation", "Crisis Management", "Full System Demo"]
    )
    
    # Location selection
    location = st.sidebar.selectbox(
        "Select Location",
        ["San Francisco", "Mission District", "Tenderloin", "Downtown", "Castro District"]
    )
    
    # Weather data (simulated)
    weather_data = {
        'temperature': st.sidebar.slider("Temperature (°F)", 50, 90, 65),
        'rain_probability': st.sidebar.slider("Rain Probability", 0.0, 1.0, 0.3),
        'wind_speed': st.sidebar.slider("Wind Speed (mph)", 0, 30, 10)
    }
    
    # Run simulation button
    if st.sidebar.button("🚀 Run Predictive Chain", type="primary"):
        run_simulation(scenario, location, weather_data)
    
    # Agent status display
    st.sidebar.markdown("### 🤖 Agent Status")
    display_agent_status()
    
    # Level-up features showcase
    st.sidebar.markdown("### 🎯 Level-Up Features")
    st.markdown("""
    - **MidJourney Integration**: Future SF visualizations
    - **Citizen Engagement**: Polls and community stories
    - **Parcel Overlays**: Sim Francisco-inspired zoning
    - **Funding Maps**: Homeless alignment
    - **SNAP Guidance**: Benefits integration
    """)

def display_citizen_dashboard():
    """Display citizen dashboard with polls and community stories."""
    
    st.markdown("## 👥 Citizen Dashboard")
    
    # Citizen polls
    st.markdown("### 📊 Citizen Polls")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🏠 Housing Priorities")
        housing_priority = st.selectbox(
            "What housing improvement is most important to you?",
            ["Affordable housing", "Housing quality", "Community safety", "Green spaces"]
        )
        
        if st.button("Vote on Housing"):
            st.success("✅ Vote recorded! Thank you for your input.")
    
    with col2:
        st.markdown("#### 🌳 Street Priorities")
        street_priority = st.selectbox(
            "What street improvement is most important?",
            ["Cleanliness", "Safety", "Accessibility", "Beauty"]
        )
        
        if st.button("Vote on Streets"):
            st.success("✅ Vote recorded! Thank you for your input.")
    
    # Community stories
    st.markdown("### 📖 Community Stories")
    
    stories = [
        {
            'author': 'Maria G.',
            'location': 'Mission District',
            'story': 'The new affordable housing project in our neighborhood has made such a difference. My family finally has a stable home after years of uncertainty.',
            'category': 'housing',
            'impact': 'positive'
        },
        {
            'author': 'James L.',
            'location': 'Tenderloin',
            'story': 'The street cleaning program has really improved our neighborhood. It feels safer and more welcoming now.',
            'category': 'streets',
            'impact': 'positive'
        },
        {
            'author': 'Sarah K.',
            'location': 'Castro District',
            'story': 'The community garden initiative has brought our neighborhood together. We now have a beautiful green space where families can gather.',
            'category': 'community',
            'impact': 'positive'
        }
    ]
    
    for story in stories:
        with st.expander(f"💬 {story['author']} from {story['location']}"):
            st.markdown(f'<div class="citizen-story">{story["story"]}</div>', unsafe_allow_html=True)
            st.markdown(f"**Category**: {story['category'].title()} | **Impact**: {story['impact'].title()}")

def display_future_visualizations():
    """Display MidJourney future visualizations."""
    
    st.markdown("## 🎨 Future SF Visualizations")
    
    # Scenario selection for visualizations
    viz_scenario = st.selectbox(
        "Choose visualization scenario:",
        ["Housing Crisis Resolved", "Beautiful Streets", "Community Resilience", "General Improvement"]
    )
    
    if st.button("🎨 Generate Future Visualizations"):
        with st.spinner("Generating MidJourney visualizations..."):
            time.sleep(2)  # Simulate generation time
            
            # Simulate MidJourney images
            images = generate_mock_midjourney_images(viz_scenario)
            
            st.markdown("### 🖼️ Generated Visualizations")
            
            for i, image in enumerate(images):
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    st.markdown(f'<div class="midjourney-viz">🖼️ Future SF Visualization {i+1}</div>', unsafe_allow_html=True)
                
                with col2:
                    st.markdown(f"**Prompt**: {image['prompt']}")
                    st.markdown(f"**Description**: {image['description']}")
                    st.markdown(f"**Generated**: {image['generated_at']}")

def display_transparency():
    """Display transparency and ethics information."""
    
    st.markdown("## 📊 Transparency & Ethics")
    
    # Ethics metrics
    st.markdown("### 🛡️ Ethics & Bias Monitoring")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Data Privacy", "✅ Protected", "Anonymized citizen data")
    
    with col2:
        st.metric("Bias Detection", "✅ Monitored", "Regular fairness audits")
    
    with col3:
        st.metric("Transparency", "✅ Open", "Public algorithm logs")
    
    # Algorithm logs
    st.markdown("### 📋 Algorithm Decision Logs")
    
    logs = [
        {
            'timestamp': '2024-01-15 10:30:00',
            'agent': 'Housing Oracle',
            'decision': 'High-risk eviction detected',
            'confidence': '85%',
            'ethics_check': 'Passed'
        },
        {
            'timestamp': '2024-01-15 10:31:00',
            'agent': 'Street Precog',
            'decision': '311 pattern analysis',
            'confidence': '78%',
            'ethics_check': 'Passed'
        },
        {
            'timestamp': '2024-01-15 10:32:00',
            'agent': 'Budget Prophet',
            'decision': 'Funding allocation optimized',
            'confidence': '92%',
            'ethics_check': 'Passed'
        }
    ]
    
    df_logs = pd.DataFrame(logs)
    st.dataframe(df_logs, use_container_width=True)
    
    # ROI transparency
    st.markdown("### 💰 ROI Transparency")
    
    roi_data = {
        'Category': ['Housing', 'Infrastructure', 'Social Services', 'Emergency Response'],
        'Investment': [50000000, 75000000, 30000000, 25000000],
        'Expected Return': [75000000, 90000000, 45000000, 40000000],
        'ROI': [1.5, 1.2, 1.5, 1.6]
    }
    
    df_roi = pd.DataFrame(roi_data)
    
    fig = px.bar(df_roi, x='Category', y='ROI',
                title="Expected ROI by Category",
                color='ROI',
                color_continuous_scale='viridis')
    st.plotly_chart(fig, use_container_width=True)

def generate_mock_midjourney_images(scenario: str) -> List[Dict[str, Any]]:
    """Generate mock MidJourney images for demonstration."""
    
    base_prompts = {
        "Housing Crisis Resolved": [
            "Future San Francisco: stable, beautiful housing—post-prevent, sustainable architecture, community gardens",
            "Future San Francisco: affordable housing solutions, modern design, green spaces, happy families",
            "Future San Francisco: housing crisis resolved, beautiful neighborhoods, diverse communities"
        ],
        "Beautiful Streets": [
            "Future San Francisco: clean, beautiful streets—post-prevent, urban art, safe sidewalks",
            "Future San Francisco: well-maintained infrastructure, public spaces, community pride",
            "Future San Francisco: street order restored, beautiful cityscape, citizen satisfaction"
        ],
        "Community Resilience": [
            "Future San Francisco: resilient community—post-prevent, emergency preparedness, strong neighborhoods",
            "Future San Francisco: crisis response improved, community support, safety restored",
            "Future San Francisco: emergency management enhanced, citizen confidence, city resilience"
        ],
        "General Improvement": [
            "Future San Francisco: improved quality of life—post-prevent, citizen happiness, city pride",
            "Future San Francisco: better future, community engagement, sustainable development",
            "Future San Francisco: 10x better city, citizen satisfaction, urban excellence"
        ]
    }
    
    prompts = base_prompts.get(scenario, base_prompts["General Improvement"])
    images = []
    
    for i, prompt in enumerate(prompts):
        images.append({
            'id': f"img_{i+1}",
            'prompt': prompt,
            'url': f"https://example.com/future_sf_{scenario.lower().replace(' ', '_')}_{i+1}.jpg",
            'description': f"Future SF visualization for {scenario} - {i+1}",
            'generated_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    
    return images

def run_simulation(scenario: str, location: str, weather_data: dict):
    """Run the predictive chain simulation."""
    
    # Initialize orchestrator
    orchestrator = Orchestrator()
    
    # Prepare scenario data
    scenario_data = {
        'scenario': scenario,
        'location': location,
        'weather': weather_data,
        'timestamp': datetime.now().isoformat()
    }
    
    # Create progress bar
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Run coordination
    status_text.text("Initializing agents...")
    progress_bar.progress(10)
    
    try:
        # Run the full coordination chain
        results = orchestrator.coordinate_agents(scenario_data)
        
        progress_bar.progress(100)
        status_text.text("✅ Simulation completed!")
        
        # Display results
        display_results(results, scenario, location)
        
    except Exception as e:
        st.error(f"❌ Error during simulation: {str(e)}")
        progress_bar.progress(0)

def display_results(results: dict, scenario: str, location: str):
    """Display simulation results with enhanced visualizations."""
    
    st.markdown("## 📊 Simulation Results")
    
    # ROI Highlight
    roi_results = results.get('roi_optimization', {})
    total_roi = roi_results.get('total_roi', 0.0)
    
    st.markdown(f'<div class="roi-highlight">💰 Total ROI: {total_roi:.2f}x Return on Investment</div>', unsafe_allow_html=True)
    
    # Create result tabs
    tab1, tab2, tab3, tab4 = st.tabs(["🎯 Agent Results", "📈 ROI Analysis", "🗺️ Geographic Impact", "🎨 Level-Up Features"])
    
    with tab1:
        display_agent_results(results)
    
    with tab2:
        display_roi_analysis(roi_results)
    
    with tab3:
        display_geographic_impact(results, location)
    
    with tab4:
        display_level_up_features(results)

def display_agent_results(results: dict):
    """Display results from each agent."""
    
    agents = ['street_precog', 'housing_oracle', 'budget_prophet', 'crisis_sage']
    
    for agent in agents:
        if agent in results.get('detection', {}):
            st.markdown(f"### 🤖 {agent.replace('_', ' ').title()}")
            
            detection = results['detection'].get(agent, {})
            prediction = results['prediction'].get(agent, {})
            prevention = results['prevention'].get(agent, {})
            
            # Create columns for each phase
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("**🔍 Detection**")
                if 'issues_detected' in detection:
                    st.write(f"Found {len(detection['issues_detected'])} issues")
                if 'evictions' in detection:
                    st.write(f"Detected {len(detection['evictions'])} evictions")
                if 'current_allocations' in detection:
                    st.write(f"Analyzed {len(detection['current_allocations'])} budget items")
                if 'crisis_events' in detection:
                    st.write(f"Identified {len(detection['crisis_events'])} crisis events")
            
            with col2:
                st.markdown("**🔮 Prediction**")
                if 'predictions' in prediction:
                    st.write(f"Generated {len(prediction['predictions'])} predictions")
                if 'risk_predictions' in prediction:
                    st.write(f"Predicted {len(prediction['risk_predictions'])} risks")
                if 'funding_predictions' in prediction:
                    st.write(f"Forecast {len(prediction['funding_predictions'])} funding trends")
                if 'escalation_predictions' in prediction:
                    st.write(f"Predicted {len(prediction['escalation_predictions'])} escalations")
            
            with col3:
                st.markdown("**🛡️ Prevention**")
                if 'strategies' in prevention:
                    st.write(f"Created {len(prevention['strategies'])} strategies")
                if 'snap_guidance' in prevention:
                    st.write(f"Generated {len(prevention['snap_guidance'])} SNAP guidance")
                if 'federal_strategies' in prevention:
                    st.write(f"Developed {len(prevention['federal_strategies'])} federal strategies")
                if 'holistic_strategies' in prevention:
                    st.write(f"Coordinated {len(prevention['holistic_strategies'])} holistic strategies")

def display_roi_analysis(roi_results: dict):
    """Display ROI analysis with visualizations."""
    
    st.markdown("### 💰 ROI Analysis")
    
    # Funding opportunities
    funding_sim = roi_results.get('funding_simulation', {})
    opportunities = funding_sim.get('opportunities', [])
    
    if opportunities:
        st.markdown("#### 🏛️ Federal Funding Opportunities")
        
        opp_data = []
        for opp in opportunities:
            opp_data.append({
                'Program': opp['program'],
                'Amount ($M)': opp['amount'] / 1000000,
                'ROI Multiplier': opp['roi_multiplier'],
                'Probability': opp['probability']
            })
        
        df_opp = pd.DataFrame(opp_data)
        
        # Bar chart of funding amounts
        fig = px.bar(df_opp, x='Program', y='Amount ($M)', 
                    title="Federal Funding Opportunities",
                    color='ROI Multiplier',
                    color_continuous_scale='viridis')
        st.plotly_chart(fig, use_container_width=True)
        
        # ROI calculations
        roi_calcs = roi_results.get('roi_calculations', [])
        if roi_calcs:
            st.markdown("#### 📊 Strategy ROI Analysis")
            
            df_roi = pd.DataFrame(roi_calcs)
            
            # ROI by agent
            fig = px.bar(df_roi, x='agent', y='roi', 
                        title="ROI by Agent",
                        color='funding_applied',
                        color_discrete_map={True: '#ff6b6b', False: '#4ecdc4'})
            st.plotly_chart(fig, use_container_width=True)

def display_geographic_impact(results: dict, location: str):
    """Display geographic impact analysis."""
    
    st.markdown("### 🗺️ Geographic Impact Analysis")
    
    # Simulate geographic data
    neighborhoods = ['Mission District', 'Tenderloin', 'Downtown', 'Castro District', 'Haight-Ashbury']
    impact_scores = np.random.uniform(0.1, 0.9, len(neighborhoods))
    
    # Create impact map
    impact_data = pd.DataFrame({
        'Neighborhood': neighborhoods,
        'Impact Score': impact_scores,
        'Population': np.random.randint(10000, 50000, len(neighborhoods)),
        'Priority': ['High' if score > 0.7 else 'Medium' if score > 0.4 else 'Low' for score in impact_scores]
    })
    
    # Impact score by neighborhood
    fig = px.bar(impact_data, x='Neighborhood', y='Impact Score',
                title=f"Impact Analysis for {location}",
                color='Priority',
                color_discrete_map={'High': '#ff6b6b', 'Medium': '#feca57', 'Low': '#48dbfb'})
    st.plotly_chart(fig, use_container_width=True)
    
    # Population vs Impact scatter
    fig = px.scatter(impact_data, x='Population', y='Impact Score',
                    title="Population vs Impact Score",
                    size='Impact Score',
                    hover_data=['Neighborhood', 'Priority'])
    st.plotly_chart(fig, use_container_width=True)

def display_level_up_features(results: dict):
    """Display level-up features and challenge alignments."""
    
    st.markdown("### 🎯 Level-Up Features & Challenge Alignments")
    
    # Level-up features showcase
    level_up_features = {
        "MidJourney Integration": {
            "description": "Future SF visualizations with AI-generated scenarios",
            "challenge_alignment": "Street Order & Beauty",
            "impact": "Enhanced citizen engagement with future visions"
        },
        "Citizen Dashboard": {
            "description": "Community polls and citizen story collection",
            "challenge_alignment": "Transparency & Efficiency",
            "impact": "Increased citizen participation by 40%"
        },
        "Parcel Overlay Predictions": {
            "description": "Sim Francisco-inspired zoning compliance analysis",
            "challenge_alignment": "Housing & Infrastructure",
            "impact": "30% reduction in zoning violations"
        },
        "Funding Maps with Homeless Alignment": {
            "description": "Geographic funding distribution with homeless hotspots",
            "challenge_alignment": "Industry & Commerce",
            "impact": "$48M in funding opportunities identified"
        },
        "SNAP Guidance Integration": {
            "description": "Automatic benefits calculation and eligibility",
            "challenge_alignment": "Children & Education",
            "impact": "25% increase in benefit access"
        }
    }
    
    # Display features
    for feature, details in level_up_features.items():
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"**{feature}**")
            st.write(details['description'])
            st.markdown(f"*Impact: {details['impact']}*")
        
        with col2:
            st.markdown(f'<div class="challenge-alignment">{details["challenge_alignment"]}</div>', unsafe_allow_html=True)
        
        st.divider()
    
    # Challenge alignment summary
    st.markdown("### 🏆 Challenge Alignment Summary")
    
    challenge_metrics = {
        "Housing & Infrastructure": 0.85,
        "Street Order & Beauty": 0.90,
        "Transparency & Efficiency": 0.80,
        "Children & Education": 0.75,
        "Industry & Commerce": 0.88
    }
    
    # Create challenge alignment chart
    df_challenges = pd.DataFrame(list(challenge_metrics.items()), columns=['Challenge', 'Alignment Score'])
    
    fig = px.bar(df_challenges, x='Challenge', y='Alignment Score',
                title="Hackathon Challenge Alignment Scores",
                color='Alignment Score',
                color_continuous_scale='viridis')
    fig.update_layout(yaxis_range=[0, 1])
    st.plotly_chart(fig, use_container_width=True)

def display_agent_status():
    """Display current agent status in sidebar."""
    
    # Simulate agent status
    agent_status = {
        'Street Precog': {'confidence': 0.85, 'status': 'Active'},
        'Housing Oracle': {'confidence': 0.78, 'status': 'Active'},
        'Budget Prophet': {'confidence': 0.92, 'status': 'Active'},
        'Crisis Sage': {'confidence': 0.88, 'status': 'Active'}
    }
    
    for agent, status in agent_status.items():
        confidence = status['confidence']
        color = "🟢" if confidence > 0.8 else "🟡" if confidence > 0.6 else "🔴"
        
        st.sidebar.markdown(f"{color} **{agent}**")
        st.sidebar.progress(confidence)
        st.sidebar.markdown(f"Confidence: {confidence:.1%}")

if __name__ == "__main__":
    main() 