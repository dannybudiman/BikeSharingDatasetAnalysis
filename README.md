# Project Title: Bike Sharing Dataset Analysis

## Description
This project analyzes the Bike Sharing Dataset to uncover trends in bike rentals based on time, seasons, and user types. It includes a Jupyter Notebook with data wrangling, exploratory data analysis (EDA), and visualizations, as well as a Streamlit dashboard for interactive exploration.

## Files in this Repository
- `notebook.ipynb`: Jupyter Notebook containing the full analysis.
- `dashboard.py`: Python script for the Streamlit dashboard.
- `requirements.txt`: List of dependencies to run the project.
- `data/hour.csv` and `data/day.csv`: Datasets used in the analysis.

## How to Run the Jupyter Notebook
1. Make sure you have Python 3 installed on your system.
2. Install Jupyter Notebook:
   pip install notebook
3. Clone this repository and navigate to the folder:
   git clone <repository-url>
   cd <repository-folder>
4. Launch Jupyter Notebook:
   jupyter notebook
5. Open the file notebook.ipynb in the Jupyter interface.
6. Execute the cells step by step for a guided analysis.

## How to Run the Streamlit Dashboard
Install dependencies:
pip install -r requirements.txt

Run the Streamlit app:
streamlit run dashboard.py
Open the link provided in your terminal (e.g., http://localhost:8501) to explore the interactive dashboard.

## Insights from the Analysis
Key Insights:
Peak Hours: Bike rentals peak at 8 AM and 5 PM, aligning with commuting hours.
Seasonal Trends: Rentals are highest in Spring (Season 2) and Summer (Season 3) and lowest in Winter (Season 1).
Casual vs Registered Users: Registered users show consistent usage patterns, while casual users show more variability depending on weekends and seasons.

## Prerequisites
Ensure you have the following installed:
Python 3.7+
Jupyter Notebook
Streamlit

## Dataset
The dataset used in this project is the Bike Sharing Dataset. Place the dataset in the data/ directory for the project to run successfully.

## Author
Name: Danny Budiman
Email: Danny.Budiman@gmail.com
ID Dicoding: Danny.Budiman@gmail.com
