# DataAnalysis-Scripts
A collection of Python scripts for data analysis" 

# Data Analysis Scripts

This repository contains Python scripts used for data analysis. The main scripts are:

- `Comparing_Code.py`: Compares network metrics from different datasets and generates visualizations.
- `CubicSpline.py`: Performs cubic spline interpolation to fix extreme values in time-series datasets.

## Setup
To run the scripts, make sure to have the required libraries installed:
```bash
pip install numpy pandas matplotlib scipy

##Usage
1. Comparing_Code.py
This script loads multiple CSV datasets, computes key network metrics, and visualizes the comparison. Here is an example of how to use it:

Sample Data: You should have CSV files containing network data (e.g., throughput, volume).

2. CubicSpline.py
This script applies cubic spline interpolation to specific columns in a time-series dataset, fixing extreme values (e.g., 0, highly negative, or NaN).

Sample Data: You should have a time-series dataset with columns like "CQI", "RSRP", "RSRQ", etc.

Project Goals and Future Improvements
Current Goals:
To provide scripts that help with data analysis tasks such as comparing datasets and handling extreme values in time-series data.
Future Improvements:
Add more data cleaning and preprocessing functions.
Extend the script to support more complex interpolation methods.
Add automated tests to ensure the scripts work reliably.

Related Projects
Pandas Documentation
SciPy Documentation
Matplotlib Documentation
