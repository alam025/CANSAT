import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
import plotly.graph_objects as go
from datetime import datetime

# Function to generate random UAV data for testing
def generate_random_uav_data(num_uavs=5):
    uav_data = []
    for i in range(num_uavs):
        uav_data.append({
            'ID': f'UAV-{i+1}',
            'Status': np.random.choice(['ONLINE', 'OFFLINE']),
            'Altitude (m)': np.random.uniform(0, 725),
            'Speed (m/s)': np.random.uniform(0, 15),
            'Battery Level (%)': np.random.uniform(20, 100),
            'Voltage (V)': np.random.uniform(11.0, 14.8),
            'Mode': np.random.choice(['GUIDED', 'AUTO', 'MANUAL']),
            'Latitude': round(np.random.uniform(28.4, 28.5), 5),
            'Longitude': round(np.random.uniform(77.5, 77.6), 5),
        })
    return pd.DataFrame(uav_data)

# Function to generate random notifications
def generate_notifications(num_notifications=3):
    notifications = []
    for i in range(num_notifications):
        notifications.append(f"Notification {i+1}: UAV-{np.random.randint(1, 6)} has changed status.")
    return notifications

# Main function to run the Streamlit app
def main():
    st.set_page_config(page_title="Ground Control Station", layout="wide")

    # Custom CSS for enhanced UI
    st.markdown("""
        <style>
            body {
                background-color: #121212;
                color: #ffffff;
                font-family: 'Arial', sans-serif;
                margin: 0;
            }
            .header {
                text-align: center;
                color: #00ff00;
                font-size: 2em;
                margin-bottom: 0.5em;
            }
            .container {
                display: flex;
                justify-content: space-between;
                transition: all 0.5s ease; /* Smooth transition for the container */
            }
            .sidebar {
                width: 25%;
                padding: 20px;
                background-color: #1e1e1e;
                border-radius: 10px;
                animation: slideInLeft 0.5s; /* Animation for sidebar */
            }
            .notification {
                background-color: #2c2c2c;
                border-radius: 10px;
                padding: 10px;
                margin-bottom: 10px;
                animation: fadeIn 0.5s ease-in-out; /* Animation for notifications */
            }
            .trackbar {
                width: 100%;
                height: 25px;
                background-color: #333333;
                border-radius: 5px;
                position: relative;
            }
            .track {
                height: 100%;
                background-color: cyan;
                border-radius: 5px;
                transition: width 0.3s ease-in-out; /* Smooth transition */
            }
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            @keyframes slideInLeft {
                from { transform: translateX(-100%); opacity: 0; }
                to { transform: translateX(0); opacity: 1; }
            }
            button:hover {
                background-color: #00ff00; /* Change color on hover */
                transition: background-color 0.3s ease; /* Smooth transition on hover */
            }
        </style>
    """, unsafe_allow_html=True)

    # Top Bar with Date and Time
    st.markdown("<h1 class='header'>Ground Control Station</h1>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='text-align:center; color:white;'>{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</h4>", unsafe_allow_html=True)

    # Generate random UAV data for the map
    uav_data = generate_random_uav_data()

    # Layout with Flexbox
    st.markdown("<div class='container'>", unsafe_allow_html=True)
    
    with st.sidebar:
        st.header("UAV List")
        
        selected_uav = st.selectbox("Select UAV:", uav_data['ID'])
        
        # Display selected UAV details
        selected_uav_data = uav_data[uav_data['ID'] == selected_uav].iloc[0]
        
        st.subheader(f"Details for {selected_uav}")
        st.write(f"Status: {selected_uav_data['Status']}")
        st.write(f"Battery Level: {selected_uav_data['Battery Level (%)']:.2f}%")
        st.write(f"Voltage: {selected_uav_data['Voltage (V)']:.2f} V")

        commands = ['Resume Mission', 'Go Home', 'Land', 'Dim', 'Spot On', 'Video On']
        
        selected_command = st.selectbox("Available Commands:", commands)
        
        if st.button("Execute Command"):
            st.success(f"Command '{selected_command}' executed for {selected_uav}!")

    with st.container():
        # Status Indicators
        st.subheader("Telemetry Data")

        # Animated Speedometer for Speed
        speed = selected_uav_data['Speed (m/s)']
        
        fig_speed = go.Figure(go.Indicator(
            mode="gauge+number",
            value=speed,
            title={'text': "Speed (m/s)"},
            gauge={
                'axis': {'range': [0, 15], 'tickcolor': "white"},
                'bar': {'color': "cyan"},
                'bgcolor': "black",
                'steps': [
                    {'range': [0, 5], 'color': "green"},
                    {'range': [5, 10], 'color': "yellow"},
                    {'range': [10, 15], 'color': "red"},
                ],
            },
            number={'font': {'size': 48}}, # Increase font size for visibility
        ))
        
        st.plotly_chart(fig_speed)

        altitude = selected_uav_data['Altitude (m)']
        
        trackbar_height = int((altitude / 725) * 100)
        
        st.markdown("<h5>Altitude (m)</h5>", unsafe_allow_html=True)
        st.markdown(f"""
            <div class='trackbar'>
                <div class='track' style='width:{trackbar_height}%;'></div>
            </div>
            <p style='text-align:center; color:white;'>{altitude:.2f} m</p>
        """, unsafe_allow_html=True)

    # OpenStreetMap Section using Folium
    st.subheader("Real-time OpenStreetMap")

    # Create a Folium map centered on the selected UAV's location
    m = folium.Map(location=[selected_uav_data['Latitude'], selected_uav_data['Longitude']], zoom_start=15)

    # Add a marker for UAV location
    folium.Marker(
        location=[selected_uav_data['Latitude'], selected_uav_data['Longitude']],
        popup=f"{selected_uav} Location",
        icon=folium.Icon(color='blue')
    ).add_to(m)

    # Render the map in Streamlit using folium_static
    folium_static(m)

    # Notifications Section
    st.subheader("Notifications")
    
    notifications = generate_notifications()
    
    for notification in notifications:
        st.markdown(f"<div class='notification'>{notification}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()