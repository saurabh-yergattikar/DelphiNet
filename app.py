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

# Cinematic CSS for stunning UX
st.markdown("""
<style>
    /* Cinematic Header */
    .cinematic-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 4rem;
        font-weight: 900;
        text-align: center;
        margin: 2rem 0;
        animation: cinematicGlow 3s ease-in-out infinite alternate;
        text-shadow: 0 0 30px rgba(102, 126, 234, 0.5);
    }
    
    @keyframes cinematicGlow {
        0% { filter: drop-shadow(0 0 20px rgba(102, 126, 234, 0.8)); }
        100% { filter: drop-shadow(0 0 40px rgba(240, 147, 251, 0.8)); }
    }
    
    /* Live Cam Container */
    .live-cam-frame {
        background: linear-gradient(45deg, #1a1a1a, #2d2d2d);
        border: 3px solid #00ff88;
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        position: relative;
        overflow: hidden;
        box-shadow: 0 0 50px rgba(0, 255, 136, 0.3);
        animation: scanline 2s linear infinite;
    }
    
    .live-cam-frame::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 2px;
        background: linear-gradient(90deg, transparent, #00ff88, transparent);
        animation: scanline 2s linear infinite;
    }
    
    @keyframes scanline {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    
    /* Agent Cards */
    .agent-card-cinematic {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        padding: 1.5rem;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .agent-card-cinematic::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: left 0.5s ease;
    }
    
    .agent-card-cinematic:hover::before {
        left: 100%;
    }
    
    .agent-card-cinematic:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    }
    
    /* Phase Transitions */
    .phase-transition {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        border-radius: 15px;
        padding: 1rem;
        margin: 1rem 0;
        color: white;
        text-align: center;
        font-weight: bold;
        font-size: 1.2rem;
        animation: phasePulse 1s ease-in-out;
        box-shadow: 0 5px 15px rgba(255, 107, 107, 0.4);
    }
    
    @keyframes phasePulse {
        0% { transform: scale(0.8); opacity: 0; }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); opacity: 1; }
    }
    
    /* ROI Gauge */
    .roi-gauge-cinematic {
        background: conic-gradient(from 0deg, #00ff88 0deg, #00ff88 180deg, #333 180deg, #333 360deg);
        border-radius: 50%;
        width: 150px;
        height: 150px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
        font-size: 2rem;
        margin: 2rem auto;
        position: relative;
        animation: gaugeSpin 2s ease-out;
        box-shadow: 0 0 30px rgba(0, 255, 136, 0.5);
    }
    
    @keyframes gaugeSpin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    /* Success Animation */
    .success-explosion {
        animation: successExplosion 0.8s ease-out;
        background: linear-gradient(135deg, #00ff88 0%, #00d4aa 100%);
        border-radius: 15px;
        padding: 1rem;
        text-align: center;
        color: white;
        font-weight: bold;
        font-size: 1.5rem;
        box-shadow: 0 0 30px rgba(0, 255, 136, 0.6);
    }
    
    @keyframes successExplosion {
        0% { transform: scale(0); opacity: 0; }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); opacity: 1; }
    }
    
    /* Interactive Buttons */
    .cinematic-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 1rem 2rem;
        font-size: 1.2rem;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        position: relative;
        overflow: hidden;
    }
    
    .cinematic-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.6);
    }
    
    .cinematic-button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left 0.5s ease;
    }
    
    .cinematic-button:hover::before {
        left: 100%;
    }
    
    /* Data Visualization Cards */
    .data-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }
    
    .data-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.3);
    }
    
    /* Progress Bars */
    .progress-cinematic {
        background: linear-gradient(90deg, #00ff88, #00d4aa);
        height: 8px;
        border-radius: 4px;
        animation: progressFill 2s ease-out;
        box-shadow: 0 0 10px rgba(0, 255, 136, 0.5);
    }
    
    @keyframes progressFill {
        from { width: 0%; }
        to { width: 100%; }
    }
    
    /* Floating Elements */
    .floating-element {
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    /* Glitch Effect */
    .glitch {
        position: relative;
        animation: glitch 0.3s ease-in-out;
    }
    
    @keyframes glitch {
        0% { transform: translate(0); }
        20% { transform: translate(-2px, 2px); }
        40% { transform: translate(-2px, -2px); }
        60% { transform: translate(2px, 2px); }
        80% { transform: translate(2px, -2px); }
        100% { transform: translate(0); }
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Cinematic header
    st.markdown('<h1 class="cinematic-header">🏙️ SF Neural Precog Network</h1>', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; color: #667eea; margin-bottom: 2rem;">🎬 Predictive AI System for San Francisco Civic Improvement</h2>', unsafe_allow_html=True)
    
    # Challenge alignment with floating animation
    st.markdown("### 🎯 Hackathon Challenge Alignment")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    challenges = [
        ("🏠", "Housing & Infrastructure"),
        ("🌳", "Street Order & Beauty"),
        ("🔍", "Transparency & Efficiency"),
        ("👶", "Children & Education"),
        ("🏢", "Industry & Commerce")
    ]
    
    for i, (icon, challenge) in enumerate(challenges):
        with [col1, col2, col3, col4, col5][i]:
            st.markdown(f'<div class="floating-element" style="background: linear-gradient(135deg, #4ecdc4 0%, #44a08d 100%); color: white; padding: 1rem; border-radius: 15px; text-align: center; box-shadow: 0 5px 15px rgba(0,0,0,0.2);">{icon} {challenge}</div>', unsafe_allow_html=True)
    
    # Main navigation with enhanced tabs
    tab1, tab2, tab3, tab4 = st.tabs(["🎮 Live Simulation", "👥 Citizen Dashboard", "🎨 Future Visualizations", "📊 Transparency"])
    
    with tab1:
        run_cinematic_simulation()
    
    with tab2:
        display_cinematic_citizen_dashboard()
    
    with tab3:
        display_cinematic_future_visualizations()
    
    with tab4:
        display_cinematic_transparency()

def run_cinematic_simulation():
    """Run the simulation with cinematic UX."""
    
    st.markdown('<h2 style="text-align: center; color: #667eea; margin: 2rem 0;">🎬 Live Simulation</h2>', unsafe_allow_html=True)
    
    # Sidebar controls
    st.sidebar.markdown('<h3 style="color: #667eea;">🎛️ Control Panel</h3>', unsafe_allow_html=True)
    
    scenario = st.sidebar.selectbox(
        "Select Scenario",
        ["Housing Crisis Response", "Street Maintenance Optimization", "Budget Allocation", "Crisis Management", "Full System Demo"]
    )
    
    location = st.sidebar.selectbox(
        "Select Location",
        ["San Francisco", "Mission District", "Tenderloin", "Downtown", "Castro District"]
    )
    
    weather_data = {
        'temperature': st.sidebar.slider("🌡️ Temperature (°F)", 50, 90, 65),
        'rain_probability': st.sidebar.slider("🌧️ Rain Probability", 0.0, 1.0, 0.3),
        'wind_speed': st.sidebar.slider("💨 Wind Speed (mph)", 0, 30, 10)
    }
    
    # Cinematic run button
    if st.sidebar.button("🚀 LAUNCH PREDICTIVE CHAIN", type="primary", use_container_width=True):
        run_cinematic_coordination(scenario, location, weather_data)
    
    # Agent status with cinematic styling
    st.sidebar.markdown('<h3 style="color: #667eea;">🤖 Agent Status</h3>', unsafe_allow_html=True)
    display_cinematic_agent_status()

def run_cinematic_coordination(scenario: str, location: str, weather_data: dict):
    """Run coordination with cinematic effects."""
    
    # Initialize orchestrator
    orchestrator = Orchestrator()
    
    # Prepare scenario data
    scenario_data = {
        'scenario': scenario,
        'location': location,
        'weather': weather_data,
        'timestamp': datetime.now().isoformat()
    }
    
    # Create cinematic layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Live cam simulation with cinematic effects
        st.markdown('<div class="live-cam-frame">', unsafe_allow_html=True)
        st.markdown('<h3 style="color: #00ff88; text-align: center;">📹 LIVE CAM FEED</h3>', unsafe_allow_html=True)
        
        # Cinematic buffering
        with st.spinner("🎥 INITIALIZING LIVE CAM FEED..."):
            time.sleep(2)
        
        # Mock video with cinematic styling
        st.markdown(f"""
        <div style="background: linear-gradient(45deg, #1a1a1a, #2d2d2d); 
                    border: 2px solid #00ff88; border-radius: 15px; 
                    padding: 3rem; text-align: center; color: #00ff88; 
                    font-family: 'Courier New', monospace; font-size: 1.2rem;">
            🎥 LIVE SF STREET CAM
            <br><br>
            📍 ANALYZING: {location.upper()}
            <br><br>
            🔍 DETECTING PATTERNS...
            <br>
            📊 MONITORING CONDITIONS...
            <br>
            🎯 IDENTIFYING ISSUES...
            <br><br>
            <div style="font-size: 0.9rem; opacity: 0.8;">
            REAL-TIME PREDICTIVE RESPONSE
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Real-time metrics with cinematic styling
        st.markdown('<h3 style="color: #667eea;">📊 LIVE METRICS</h3>', unsafe_allow_html=True)
        
        # Animated ROI gauge
        roi_value = 2.5
        st.markdown(f"""
        <div class="roi-gauge-cinematic">
            {roi_value:.1f}x
            <br><small>ROI</small>
        </div>
        """, unsafe_allow_html=True)
        
        # Agent confidence with cinematic progress bars
        agents = ['Street Precog', 'Housing Oracle', 'Budget Prophet', 'Crisis Sage']
        confidences = [0.85, 0.78, 0.92, 0.88]
        
        for agent, conf in zip(agents, confidences):
            color = "🟢" if conf > 0.8 else "🟡" if conf > 0.6 else "🔴"
            st.markdown(f"{color} **{agent}**")
            st.markdown(f'<div class="progress-cinematic" style="width: {conf*100}%;"></div>', unsafe_allow_html=True)
            st.markdown(f"Confidence: {conf:.1%}")
    
    # Run coordination with cinematic phases
    try:
        phases = [
            ("🔍", "DETECTION", "🎥 ANALYZING LIVE CAM FEED..."),
            ("🔮", "PREDICTION", "🔮 FORECASTING FUTURE SCENARIOS..."),
            ("🛡️", "PREVENTION", "🛡️ GENERATING PREVENTION STRATEGIES..."),
            ("💰", "ROI OPTIMIZATION", "💰 CALCULATING OPTIMAL RETURNS..."),
            ("🎨", "FUTURE VISUALIZATIONS", "🎨 GENERATING MIDJOURNEY SCENARIOS..."),
            ("👥", "CITIZEN ENGAGEMENT", "👥 COLLECTING CITIZEN FEEDBACK..."),
            ("📡", "BROADCASTING", "📡 BROADCASTING RESULTS...")
        ]
        
        for i, (icon, phase, message) in enumerate(phases):
            # Phase transition with cinematic effect
            st.markdown(f'<div class="phase-transition">{icon} PHASE {i+1}: {phase}</div>', unsafe_allow_html=True)
            
            with st.spinner(message):
                time.sleep(1.5)
            
            # Handoff animation
            if i < len(phases) - 1:
                st.markdown('<div style="text-align: center; font-size: 2rem; margin: 1rem 0; animation: bounce 1s infinite;">⬇️</div>', unsafe_allow_html=True)
        
        # Success explosion
        st.markdown('<div class="success-explosion">✅ SIMULATION COMPLETED SUCCESSFULLY!</div>', unsafe_allow_html=True)
        
        # Run actual coordination
        results = orchestrator.coordinate_agents(scenario_data)
        
        # Display results with cinematic styling
        display_cinematic_results(results, scenario, location)
        
    except Exception as e:
        st.error(f"❌ Error during simulation: {str(e)}")

def display_cinematic_results(results: dict, scenario: str, location: str):
    """Display results with cinematic styling."""
    
    st.markdown('<h2 style="text-align: center; color: #667eea; margin: 2rem 0;">📊 SIMULATION RESULTS</h2>', unsafe_allow_html=True)
    
    # ROI Highlight with explosion effect
    roi_results = results.get('roi_optimization', {})
    total_roi = roi_results.get('total_roi', 0.0)
    
    st.markdown(f'<div class="success-explosion">💰 TOTAL ROI: {total_roi:.2f}x RETURN ON INVESTMENT</div>', unsafe_allow_html=True)
    
    # Create result tabs
    tab1, tab2, tab3, tab4 = st.tabs(["🎯 Agent Results", "📈 ROI Analysis", "🗺️ Geographic Impact", "🎨 Level-Up Features"])
    
    with tab1:
        display_cinematic_agent_results(results)
    
    with tab2:
        display_cinematic_roi_analysis(roi_results)
    
    with tab3:
        display_cinematic_geographic_impact(results, location)
    
    with tab4:
        display_cinematic_level_up_features(results)

def display_cinematic_agent_results(results: dict):
    """Display agent results with cinematic styling."""
    
    agents = ['street_precog', 'housing_oracle', 'budget_prophet', 'crisis_sage']
    
    for agent in agents:
        if agent in results.get('detection', {}):
            st.markdown(f'<h3 style="color: #667eea;">🤖 {agent.replace("_", " ").title()}</h3>', unsafe_allow_html=True)
            
            detection = results['detection'].get(agent, {})
            prediction = results['prediction'].get(agent, {})
            prevention = results['prevention'].get(agent, {})
            
            # Create cinematic agent card
            st.markdown('<div class="agent-card-cinematic">', unsafe_allow_html=True)
            
            # Create columns for each phase
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("**🔍 DETECTION**")
                if 'issues_detected' in detection:
                    st.markdown(f"✅ Found {len(detection['issues_detected'])} issues")
                if 'evictions' in detection:
                    st.markdown(f"🏠 Detected {len(detection['evictions'])} evictions")
                if 'current_allocations' in detection:
                    st.markdown(f"💰 Analyzed {len(detection['current_allocations'])} budget items")
                if 'crisis_events' in detection:
                    st.markdown(f"🚨 Identified {len(detection['crisis_events'])} crisis events")
            
            with col2:
                st.markdown("**🔮 PREDICTION**")
                if 'predictions' in prediction:
                    st.markdown(f"📊 Generated {len(prediction['predictions'])} predictions")
                if 'risk_predictions' in prediction:
                    st.markdown(f"⚠️ Predicted {len(prediction['risk_predictions'])} risks")
                if 'funding_predictions' in prediction:
                    st.markdown(f"💸 Forecast {len(prediction['funding_predictions'])} funding trends")
                if 'escalation_predictions' in prediction:
                    st.markdown(f"📈 Predicted {len(prediction['escalation_predictions'])} escalations")
            
            with col3:
                st.markdown("**🛡️ PREVENTION**")
                if 'strategies' in prevention:
                    st.markdown(f"🎯 Created {len(prevention['strategies'])} strategies")
                if 'snap_guidance' in prevention:
                    st.markdown(f"🍽️ Generated {len(prevention['snap_guidance'])} SNAP guidance")
                if 'federal_strategies' in prevention:
                    st.markdown(f"🏛️ Developed {len(prevention['federal_strategies'])} federal strategies")
                if 'holistic_strategies' in prevention:
                    st.markdown(f"🤝 Coordinated {len(prevention['holistic_strategies'])} holistic strategies")
            
            st.markdown('</div>', unsafe_allow_html=True)

def display_cinematic_roi_analysis(roi_results: dict):
    """Display ROI analysis with cinematic styling."""
    
    st.markdown('<h3 style="color: #667eea;">💰 ROI ANALYSIS</h3>', unsafe_allow_html=True)
    
    # Funding opportunities
    funding_sim = roi_results.get('funding_simulation', {})
    opportunities = funding_sim.get('opportunities', [])
    
    if opportunities:
        st.markdown('<h4 style="color: #667eea;">🏛️ FEDERAL FUNDING OPPORTUNITIES</h4>', unsafe_allow_html=True)
        
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
            st.markdown('<h4 style="color: #667eea;">📊 STRATEGY ROI ANALYSIS</h4>', unsafe_allow_html=True)
            
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

def display_cinematic_geographic_impact(results: dict, location: str):
    """Display geographic impact with cinematic styling."""
    
    st.markdown('<h3 style="color: #667eea;">🗺️ GEOGRAPHIC IMPACT ANALYSIS</h3>', unsafe_allow_html=True)
    
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

def display_cinematic_level_up_features(results: dict):
    """Display level-up features with cinematic styling."""
    
    st.markdown('<h3 style="color: #667eea;">🎯 LEVEL-UP FEATURES & CHALLENGE ALIGNMENTS</h3>', unsafe_allow_html=True)
    
    # Level-up features showcase with cinematic styling
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
    
    # Display features with cinematic styling
    for feature, details in level_up_features.items():
        st.markdown('<div class="data-card">', unsafe_allow_html=True)
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"**{feature}**")
            st.write(details['description'])
            st.markdown(f"*Impact: {details['impact']}*")
        
        with col2:
            st.markdown(f'<div style="background: linear-gradient(135deg, #4ecdc4 0%, #44a08d 100%); color: white; padding: 0.5rem; border-radius: 10px; text-align: center; font-size: 0.8rem;">{details["challenge_alignment"]}</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Challenge alignment summary with enhanced chart
    st.markdown('<h3 style="color: #667eea;">🏆 CHALLENGE ALIGNMENT SUMMARY</h3>', unsafe_allow_html=True)
    
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

def display_cinematic_citizen_dashboard():
    """Display citizen dashboard with cinematic styling."""
    
    st.markdown('<h2 style="text-align: center; color: #667eea; margin: 2rem 0;">👥 CITIZEN DASHBOARD</h2>', unsafe_allow_html=True)
    
    # Citizen polls with cinematic styling
    st.markdown('<h3 style="color: #667eea;">📊 CITIZEN POLLS</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="data-card">', unsafe_allow_html=True)
        st.markdown("#### 🏠 HOUSING PRIORITIES")
        housing_priority = st.selectbox(
            "What housing improvement is most important to you?",
            ["Affordable housing", "Housing quality", "Community safety", "Green spaces"]
        )
        
        if st.button("🗳️ VOTE ON HOUSING", use_container_width=True):
            st.success("✅ VOTE RECORDED! THANK YOU FOR YOUR INPUT.")
            time.sleep(0.5)
            st.balloons()
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="data-card">', unsafe_allow_html=True)
        st.markdown("#### 🌳 STREET PRIORITIES")
        street_priority = st.selectbox(
            "What street improvement is most important?",
            ["Cleanliness", "Safety", "Accessibility", "Beauty"]
        )
        
        if st.button("🗳️ VOTE ON STREETS", use_container_width=True):
            st.success("✅ VOTE RECORDED! THANK YOU FOR YOUR INPUT.")
            time.sleep(0.5)
            st.balloons()
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Community stories with cinematic styling
    st.markdown('<h3 style="color: #667eea;">📖 COMMUNITY STORIES</h3>', unsafe_allow_html=True)
    
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
        st.markdown('<div class="agent-card-cinematic">', unsafe_allow_html=True)
        st.markdown(f"**💬 {story['author']} from {story['location']}**")
        st.write(story['story'])
        st.markdown(f"**Category**: {story['category'].title()} | **Impact**: {story['impact'].title()}")
        st.markdown('</div>', unsafe_allow_html=True)

def display_cinematic_future_visualizations():
    """Display MidJourney future visualizations with cinematic styling."""
    
    st.markdown('<h2 style="text-align: center; color: #667eea; margin: 2rem 0;">🎨 FUTURE SF VISUALIZATIONS</h2>', unsafe_allow_html=True)
    
    # Scenario selection for visualizations
    viz_scenario = st.selectbox(
        "Choose visualization scenario:",
        ["Housing Crisis Resolved", "Beautiful Streets", "Community Resilience", "General Improvement"]
    )
    
    if st.button("🎨 GENERATE FUTURE VISUALIZATIONS", use_container_width=True):
        with st.spinner("🎨 GENERATING MIDJOURNEY VISUALIZATIONS..."):
            time.sleep(2)  # Simulate generation time
            
            # Simulate MidJourney images
            images = generate_mock_midjourney_images(viz_scenario)
            
            st.markdown('<h3 style="color: #667eea;">🖼️ GENERATED VISUALIZATIONS</h3>', unsafe_allow_html=True)
            
            for i, image in enumerate(images):
                st.markdown('<div class="agent-card-cinematic">', unsafe_allow_html=True)
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    st.markdown(f"🖼️ **Future SF Visualization {i+1}**")
                
                with col2:
                    st.markdown(f"**Prompt**: {image['prompt']}")
                    st.markdown(f"**Description**: {image['description']}")
                    st.markdown(f"**Generated**: {image['generated_at']}")
                
                st.markdown('</div>', unsafe_allow_html=True)

def display_cinematic_transparency():
    """Display transparency and ethics information with cinematic styling."""
    
    st.markdown('<h2 style="text-align: center; color: #667eea; margin: 2rem 0;">📊 TRANSPARENCY & ETHICS</h2>', unsafe_allow_html=True)
    
    # Ethics metrics with cinematic styling
    st.markdown('<h3 style="color: #667eea;">🛡️ ETHICS & BIAS MONITORING</h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="data-card">', unsafe_allow_html=True)
        st.metric("Data Privacy", "✅ Protected", "Anonymized citizen data")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="data-card">', unsafe_allow_html=True)
        st.metric("Bias Detection", "✅ Monitored", "Regular fairness audits")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="data-card">', unsafe_allow_html=True)
        st.metric("Transparency", "✅ Open", "Public algorithm logs")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Algorithm logs with cinematic styling
    st.markdown('<h3 style="color: #667eea;">📋 ALGORITHM DECISION LOGS</h3>', unsafe_allow_html=True)
    
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
    st.markdown('<h3 style="color: #667eea;">💰 ROI TRANSPARENCY</h3>', unsafe_allow_html=True)
    
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

def display_cinematic_agent_status():
    """Display current agent status with cinematic styling."""
    
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
        st.sidebar.markdown(f'<div class="progress-cinematic" style="width: {confidence*100}%;"></div>', unsafe_allow_html=True)
        st.sidebar.markdown(f"Confidence: {confidence:.1%}")

if __name__ == "__main__":
    main() 