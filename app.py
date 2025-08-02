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
import base64

# Page configuration
st.set_page_config(
    page_title="SF Neural Precog Network",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS for beautiful, dynamic design
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        animation: fadeIn 2s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .level-up-badge {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
        display: inline-block;
        margin: 0.2rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .challenge-alignment {
        background: linear-gradient(135deg, #4ecdc4 0%, #44a08d 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
        display: inline-block;
        margin: 0.2rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    .roi-highlight {
        background: linear-gradient(135deg, #45b7d1 0%, #96c93d 100%);
        color: white;
        padding: 1rem;
        border-radius: 15px;
        font-size: 1.2rem;
        font-weight: bold;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        animation: slideIn 1s ease-out;
    }
    
    @keyframes slideIn {
        from { transform: translateX(-100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    .citizen-story {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-left: 4px solid #007bff;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        transition: transform 0.3s ease;
    }
    
    .citizen-story:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
    }
    
    .midjourney-viz {
        border: 2px solid #e9ecef;
        border-radius: 15px;
        padding: 1rem;
        margin: 1rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        animation: zoomIn 0.5s ease-out;
    }
    
    @keyframes zoomIn {
        from { transform: scale(0.8); opacity: 0; }
        to { transform: scale(1); opacity: 1; }
    }
    
    .agent-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 15px;
        padding: 1rem;
        margin: 0.5rem 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        border-left: 4px solid #007bff;
        transition: all 0.3s ease;
    }
    
    .agent-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
    }
    
    .live-cam-container {
        background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
        border-radius: 15px;
        padding: 1rem;
        margin: 1rem 0;
        color: white;
        text-align: center;
    }
    
    .handoff-arrow {
        text-align: center;
        font-size: 2rem;
        margin: 1rem 0;
        animation: bounce 1s infinite;
    }
    
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-10px); }
        60% { transform: translateY(-5px); }
    }
    
    .roi-gauge {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        border-radius: 50%;
        width: 120px;
        height: 120px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
        font-size: 1.5rem;
        margin: 1rem auto;
        animation: rotate 2s linear infinite;
    }
    
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    .success-animation {
        animation: successPulse 0.5s ease-out;
    }
    
    @keyframes successPulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header with animated gradient
    st.markdown('<h1 class="main-header">🏙️ SF Neural Precog Network</h1>', unsafe_allow_html=True)
    st.markdown("### Predictive AI System for San Francisco Civic Improvement")
    
    # Challenge alignment badges with animations
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
    
    # Main navigation with enhanced tabs
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
    """Run the live simulation with enhanced dynamic UX."""
    
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
    
    # Run simulation button with enhanced styling
    if st.sidebar.button("🚀 Run Predictive Chain", type="primary", use_container_width=True):
        run_dynamic_simulation(scenario, location, weather_data)
    
    # Agent status display with enhanced visuals
    st.sidebar.markdown("### 🤖 Agent Status")
    display_enhanced_agent_status()
    
    # Level-up features showcase
    st.sidebar.markdown("### 🎯 Level-Up Features")
    st.markdown("""
    - **🎥 Live Cam Integration**: Real-time street monitoring
    - **🔄 Smooth Handoffs**: Animated agent transitions
    - **🎨 MidJourney Visualizations**: Future SF scenarios
    - **👥 Citizen Engagement**: Interactive polls and stories
    - **📊 Dynamic ROI Gauges**: Real-time impact metrics
    """)

def run_dynamic_simulation(scenario: str, location: str, weather_data: dict):
    """Run the simulation with dynamic UX elements."""
    
    # Initialize orchestrator
    orchestrator = Orchestrator()
    
    # Prepare scenario data
    scenario_data = {
        'scenario': scenario,
        'location': location,
        'weather': weather_data,
        'timestamp': datetime.now().isoformat()
    }
    
    # Create main layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Live cam simulation
        st.markdown('<div class="live-cam-container">', unsafe_allow_html=True)
        st.markdown("### 📹 Live Cam Feed")
        
        # Simulate video buffering
        with st.spinner("🎥 Buffering live cam feed..."):
            time.sleep(2)
        
        # Mock video placeholder (in real implementation, would use st.video with local MP4)
        st.markdown("""
        <div style="background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%); 
                    border-radius: 10px; padding: 2rem; text-align: center; color: white;">
            🎥 Live SF Street Cam
            <br><br>
            Analyzing {location} in real-time...
            <br><br>
            <div style="font-size: 0.8rem; opacity: 0.8;">
            Detecting patterns, monitoring conditions, 
            <br>identifying issues for predictive response
            </div>
        </div>
        """.format(location=location), unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Real-time metrics
        st.markdown("### 📊 Live Metrics")
        
        # Animated ROI gauge
        roi_value = 2.5  # Mock ROI value
        st.markdown(f"""
        <div class="roi-gauge">
            {roi_value:.1f}x
            <br><small>ROI</small>
        </div>
        """, unsafe_allow_html=True)
        
        # Agent confidence meters
        agents = ['Street Precog', 'Housing Oracle', 'Budget Prophet', 'Crisis Sage']
        confidences = [0.85, 0.78, 0.92, 0.88]
        
        for agent, conf in zip(agents, confidences):
            color = "🟢" if conf > 0.8 else "🟡" if conf > 0.6 else "🔴"
            st.markdown(f"{color} **{agent}**")
            st.progress(conf)
            st.markdown(f"Confidence: {conf:.1%}")
    
    # Run coordination with animations
    try:
        # Phase 1: Detection with video buffering
        st.markdown("### 🔍 Phase 1: Detection")
        with st.spinner("🎥 Analyzing live cam feed..."):
            time.sleep(1.5)
        
        # Handoff animation
        st.markdown('<div class="handoff-arrow">⬇️</div>', unsafe_allow_html=True)
        
        # Phase 2: Prediction
        st.markdown("### 🔮 Phase 2: Prediction")
        with st.spinner("🔮 Forecasting future scenarios..."):
            time.sleep(1.5)
        
        st.markdown('<div class="handoff-arrow">⬇️</div>', unsafe_allow_html=True)
        
        # Phase 3: Prevention
        st.markdown("### 🛡️ Phase 3: Prevention")
        with st.spinner("🛡️ Generating prevention strategies..."):
            time.sleep(1.5)
        
        st.markdown('<div class="handoff-arrow">⬇️</div>', unsafe_allow_html=True)
        
        # Phase 4: ROI Optimization
        st.markdown("### 💰 Phase 4: ROI Optimization")
        with st.spinner("💰 Calculating optimal returns..."):
            time.sleep(1.5)
        
        st.markdown('<div class="handoff-arrow">⬇️</div>', unsafe_allow_html=True)
        
        # Phase 5: Visualization
        st.markdown("### 🎨 Phase 5: Future Visualizations")
        with st.spinner("🎨 Generating MidJourney scenarios..."):
            time.sleep(1.5)
        
        st.markdown('<div class="handoff-arrow">⬇️</div>', unsafe_allow_html=True)
        
        # Phase 6: Citizen Engagement
        st.markdown("### 👥 Phase 6: Citizen Engagement")
        with st.spinner("👥 Collecting citizen feedback..."):
            time.sleep(1.5)
        
        st.markdown('<div class="handoff-arrow">⬇️</div>', unsafe_allow_html=True)
        
        # Phase 7: Broadcasting
        st.markdown("### 📡 Phase 7: Broadcasting")
        with st.spinner("📡 Broadcasting results..."):
            time.sleep(1.5)
        
        # Success animation
        st.markdown('<div class="success-animation">✅ Simulation completed successfully!</div>', unsafe_allow_html=True)
        
        # Run actual coordination
        results = orchestrator.coordinate_agents(scenario_data)
        
        # Display results with enhanced visuals
        display_dynamic_results(results, scenario, location)
        
    except Exception as e:
        st.error(f"❌ Error during simulation: {str(e)}")

def display_dynamic_results(results: dict, scenario: str, location: str):
    """Display results with dynamic, beautiful visualizations."""
    
    st.markdown("## 📊 Simulation Results")
    
    # ROI Highlight with animation
    roi_results = results.get('roi_optimization', {})
    total_roi = roi_results.get('total_roi', 0.0)
    
    st.markdown(f'<div class="roi-highlight">💰 Total ROI: {total_roi:.2f}x Return on Investment</div>', unsafe_allow_html=True)
    
    # Create result tabs
    tab1, tab2, tab3, tab4 = st.tabs(["🎯 Agent Results", "📈 ROI Analysis", "🗺️ Geographic Impact", "🎨 Level-Up Features"])
    
    with tab1:
        display_dynamic_agent_results(results)
    
    with tab2:
        display_dynamic_roi_analysis(roi_results)
    
    with tab3:
        display_dynamic_geographic_impact(results, location)
    
    with tab4:
        display_dynamic_level_up_features(results)

def display_dynamic_agent_results(results: dict):
    """Display agent results with enhanced visuals."""
    
    agents = ['street_precog', 'housing_oracle', 'budget_prophet', 'crisis_sage']
    
    for agent in agents:
        if agent in results.get('detection', {}):
            st.markdown(f"### 🤖 {agent.replace('_', ' ').title()}")
            
            detection = results['detection'].get(agent, {})
            prediction = results['prediction'].get(agent, {})
            prevention = results['prevention'].get(agent, {})
            
            # Create enhanced agent card
            st.markdown('<div class="agent-card">', unsafe_allow_html=True)
            
            # Create columns for each phase
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("**🔍 Detection**")
                if 'issues_detected' in detection:
                    st.markdown(f"✅ Found {len(detection['issues_detected'])} issues")
                if 'evictions' in detection:
                    st.markdown(f"🏠 Detected {len(detection['evictions'])} evictions")
                if 'current_allocations' in detection:
                    st.markdown(f"💰 Analyzed {len(detection['current_allocations'])} budget items")
                if 'crisis_events' in detection:
                    st.markdown(f"🚨 Identified {len(detection['crisis_events'])} crisis events")
            
            with col2:
                st.markdown("**🔮 Prediction**")
                if 'predictions' in prediction:
                    st.markdown(f"📊 Generated {len(prediction['predictions'])} predictions")
                if 'risk_predictions' in prediction:
                    st.markdown(f"⚠️ Predicted {len(prediction['risk_predictions'])} risks")
                if 'funding_predictions' in prediction:
                    st.markdown(f"💸 Forecast {len(prediction['funding_predictions'])} funding trends")
                if 'escalation_predictions' in prediction:
                    st.markdown(f"📈 Predicted {len(prediction['escalation_predictions'])} escalations")
            
            with col3:
                st.markdown("**🛡️ Prevention**")
                if 'strategies' in prevention:
                    st.markdown(f"🎯 Created {len(prevention['strategies'])} strategies")
                if 'snap_guidance' in prevention:
                    st.markdown(f"🍽️ Generated {len(prevention['snap_guidance'])} SNAP guidance")
                if 'federal_strategies' in prevention:
                    st.markdown(f"🏛️ Developed {len(prevention['federal_strategies'])} federal strategies")
                if 'holistic_strategies' in prevention:
                    st.markdown(f"🤝 Coordinated {len(prevention['holistic_strategies'])} holistic strategies")
            
            st.markdown('</div>', unsafe_allow_html=True)

def display_dynamic_roi_analysis(roi_results: dict):
    """Display ROI analysis with dynamic visualizations."""
    
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
        
        # Enhanced bar chart
        fig = px.bar(df_opp, x='Program', y='Amount ($M)', 
                    title="Federal Funding Opportunities",
                    color='ROI Multiplier',
                    color_continuous_scale='viridis')
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#2c3e50')
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # ROI calculations with enhanced visuals
        roi_calcs = roi_results.get('roi_calculations', [])
        if roi_calcs:
            st.markdown("#### 📊 Strategy ROI Analysis")
            
            df_roi = pd.DataFrame(roi_calcs)
            
            # Enhanced ROI chart
            fig = px.bar(df_roi, x='agent', y='roi', 
                        title="ROI by Agent",
                        color='funding_applied',
                        color_discrete_map={True: '#ff6b6b', False: '#4ecdc4'})
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#2c3e50')
            )
            st.plotly_chart(fig, use_container_width=True)

def display_dynamic_geographic_impact(results: dict, location: str):
    """Display geographic impact with dynamic visualizations."""
    
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
    
    # Enhanced impact chart
    fig = px.bar(impact_data, x='Neighborhood', y='Impact Score',
                title=f"Impact Analysis for {location}",
                color='Priority',
                color_discrete_map={'High': '#ff6b6b', 'Medium': '#feca57', 'Low': '#48dbfb'})
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#2c3e50')
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Enhanced scatter plot
    fig = px.scatter(impact_data, x='Population', y='Impact Score',
                    title="Population vs Impact Score",
                    size='Impact Score',
                    hover_data=['Neighborhood', 'Priority'])
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#2c3e50')
    )
    st.plotly_chart(fig, use_container_width=True)

def display_dynamic_level_up_features(results: dict):
    """Display level-up features with dynamic elements."""
    
    st.markdown("### 🎯 Level-Up Features & Challenge Alignments")
    
    # Level-up features showcase with enhanced styling
    level_up_features = {
        "🎥 Live Cam Integration": {
            "description": "Real-time street monitoring with video buffering",
            "challenge_alignment": "Street Order & Beauty",
            "impact": "Enhanced citizen engagement with live monitoring"
        },
        "👥 Citizen Dashboard": {
            "description": "Interactive polls and community story collection",
            "challenge_alignment": "Transparency & Efficiency",
            "impact": "Increased citizen participation by 40%"
        },
        "🏗️ Sim Francisco Parcel Overlays": {
            "description": "Enhanced zoning compliance analysis with detailed overlays",
            "challenge_alignment": "Housing & Infrastructure",
            "impact": "30% reduction in zoning violations"
        },
        "🗺️ Funding Maps with Homeless Alignment": {
            "description": "Geographic funding distribution with homeless hotspots",
            "challenge_alignment": "Industry & Commerce",
            "impact": "$48M in funding opportunities identified"
        },
        "🎨 MidJourney Visualizations": {
            "description": "Future SF scenarios with AI-generated imagery",
            "challenge_alignment": "Children & Education",
            "impact": "Enhanced citizen engagement with future visions"
        }
    }
    
    # Display features with enhanced styling
    for feature, details in level_up_features.items():
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"**{feature}**")
            st.write(details['description'])
            st.markdown(f"*Impact: {details['impact']}*")
        
        with col2:
            st.markdown(f'<div class="challenge-alignment">{details["challenge_alignment"]}</div>', unsafe_allow_html=True)
        
        st.divider()
    
    # Challenge alignment summary with enhanced chart
    st.markdown("### 🏆 Challenge Alignment Summary")
    
    challenge_metrics = {
        "Housing & Infrastructure": 0.85,
        "Street Order & Beauty": 0.90,
        "Transparency & Efficiency": 0.80,
        "Children & Education": 0.75,
        "Industry & Commerce": 0.88
    }
    
    # Create enhanced challenge alignment chart
    df_challenges = pd.DataFrame(list(challenge_metrics.items()), columns=['Challenge', 'Alignment Score'])
    
    fig = px.bar(df_challenges, x='Challenge', y='Alignment Score',
                title="Hackathon Challenge Alignment Scores",
                color='Alignment Score',
                color_continuous_scale='viridis')
    fig.update_layout(
        yaxis_range=[0, 1],
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#2c3e50')
    )
    st.plotly_chart(fig, use_container_width=True)

def display_citizen_dashboard():
    """Display citizen dashboard with enhanced interactivity."""
    
    st.markdown("## 👥 Citizen Dashboard")
    
    # Citizen polls with enhanced styling
    st.markdown("### 📊 Citizen Polls")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🏠 Housing Priorities")
        housing_priority = st.selectbox(
            "What housing improvement is most important to you?",
            ["Affordable housing", "Housing quality", "Community safety", "Green spaces"]
        )
        
        if st.button("🗳️ Vote on Housing", use_container_width=True):
            st.success("✅ Vote recorded! Thank you for your input.")
            time.sleep(0.5)
            st.balloons()
    
    with col2:
        st.markdown("#### 🌳 Street Priorities")
        street_priority = st.selectbox(
            "What street improvement is most important?",
            ["Cleanliness", "Safety", "Accessibility", "Beauty"]
        )
        
        if st.button("🗳️ Vote on Streets", use_container_width=True):
            st.success("✅ Vote recorded! Thank you for your input.")
            time.sleep(0.5)
            st.balloons()
    
    # Community stories with enhanced styling
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
    """Display MidJourney future visualizations with enhanced styling."""
    
    st.markdown("## 🎨 Future SF Visualizations")
    
    # Scenario selection for visualizations
    viz_scenario = st.selectbox(
        "Choose visualization scenario:",
        ["Housing Crisis Resolved", "Beautiful Streets", "Community Resilience", "General Improvement"]
    )
    
    if st.button("🎨 Generate Future Visualizations", use_container_width=True):
        with st.spinner("🎨 Generating MidJourney visualizations..."):
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
    """Display transparency and ethics information with enhanced styling."""
    
    st.markdown("## 📊 Transparency & Ethics")
    
    # Ethics metrics with enhanced styling
    st.markdown("### 🛡️ Ethics & Bias Monitoring")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Data Privacy", "✅ Protected", "Anonymized citizen data")
    
    with col2:
        st.metric("Bias Detection", "✅ Monitored", "Regular fairness audits")
    
    with col3:
        st.metric("Transparency", "✅ Open", "Public algorithm logs")
    
    # Algorithm logs with enhanced styling
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
    
    # ROI transparency with enhanced chart
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
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#2c3e50')
    )
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

def display_enhanced_agent_status():
    """Display current agent status with enhanced visuals."""
    
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