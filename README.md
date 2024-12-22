#CanSat Ground Control Station (GCS) Software
This project is a Ground Control Station (GCS) software developed for monitoring and controlling the CanSat during its mission. The software was designed to track and visualize real-time telemetry data of the CanSat, which includes parameters like temperature, pressure, and altitude. It uses Python and Streamlit for the front-end and incorporates powerful visualization tools like Matplotlib, Seaborn, and Plotly.

#Project Overview
The CanSat mission is a mini satellite simulation, where a small satellite payload (CanSat) is launched on a weather balloon and transmits data back to the ground station. The goal of the GCS software is to receive and display telemetry data in real-time, allowing the team to monitor the CanSat's performance and ensure mission success.

#Key Features
Real-Time Data Visualization: Displays telemetry data such as temperature, pressure, and altitude in real-time.
Interactive Dashboards: Provides an interactive interface with charts and graphs to monitor data trends during the mission.
Data Processing: Includes essential data processing techniques to clean, validate, and ensure the accuracy of the telemetry data.
Customizable Visualizations: Built with Plotly and Matplotlib for dynamic graphs and charts.
Responsive Design: The software is designed to be user-friendly, with a responsive interface for easy access to real-time data.
Technologies Used
Python: For back-end data processing and analysis.
Streamlit: For building an interactive, real-time front-end application.
Matplotlib: For creating static, interactive, and animated visualizations in Python.
Seaborn: For statistical data visualization built on top of Matplotlib.
Plotly: For interactive plots and dynamic data visualizations.
Setup Instructions
To run this project locally, you will need to have Python and the required dependencies installed on your machine.

#Prerequisites
Install Python (version 3.7 or higher).

Install the necessary Python packages by running the following command:

bash
Copy code
pip install -r requirements.txt
Make sure you have Streamlit installed for the web interface.

bash
Copy code
pip install streamlit
Running the Application
Once the setup is complete, you can run the Ground Control Station software by executing the following command in your terminal:

bash
Copy code
streamlit run app.py
This will start a local server, and you can access the application through your web browser by navigating to http://localhost:8501.

How It Works
Telemetry Data Ingestion: The software receives telemetry data from the CanSat via a simulated or real-time data feed.
Data Preprocessing: The data is cleaned and processed using Python libraries to ensure accuracy.
Visualization: The processed data is then visualized in real-time through various charts and graphs using Plotly, Matplotlib, and Seaborn.
Interaction: The user can interact with the visualizations to get detailed views of the telemetry data.
