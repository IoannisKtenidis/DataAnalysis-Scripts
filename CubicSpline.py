import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def load_dataset(file_path):
    """
    Loads the dataset, converts timestamps, and returns a DataFrame.
    """
    df = pd.read_csv(file_path, encoding='utf-8')
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    df.sort_values("Timestamp", inplace=True)
    return df

def cubic_spline_interpolation(df, column_name, save_output=False):
    """
    Applies Cubic Spline Interpolation to a specified column in a time-series dataset.
    
    Parameters:
        df (pd.DataFrame): DataFrame with a 'Timestamp' column.
        column_name (str): Column where extreme values should be interpolated.
        save_output (bool): Whether to save the cleaned dataset as a CSV file.

    Returns:
        pd.DataFrame: Updated DataFrame with interpolated values.
    """
    df = df.copy()  # Avoid modifying the original DataFrame

    # Identify extreme/missing values (e.g., 0, highly negative, NaN)
    extreme_mask = (df[column_name] == 0) | (df[column_name] < -1e6) | (df[column_name].isna())

    # Select valid data points for interpolation
    valid_x = df.loc[~extreme_mask, "Timestamp"].astype(int) / 1e9  # Convert to seconds
    valid_y = df.loc[~extreme_mask, column_name]

    # Apply Cubic Spline Interpolation
    if len(valid_x) > 3:  # Ensure enough points for spline fitting
        spline = CubicSpline(valid_x, valid_y)
        interpolated_values = spline(df["Timestamp"].astype(int) / 1e9)
        df.loc[extreme_mask, column_name] = interpolated_values[extreme_mask]

    # Plot results for visualization
    plt.figure(figsize=(10, 5))
    plt.plot(df["Timestamp"], df[column_name], label="Interpolated Data", linestyle='-', marker='o', color='b')
    plt.scatter(df.loc[extreme_mask, "Timestamp"], df.loc[extreme_mask, column_name], color='r', label="Fixed Values")
    plt.title(f"Cubic Spline Interpolation for {column_name}")
    plt.xlabel("Timestamp")
    plt.ylabel(column_name)
    plt.legend()
    plt.show()

    # Save the cleaned dataset if requested
    if save_output:
        df.to_csv(f"cleaned_{column_name}.csv", index=False)
        print(f"Cleaned dataset saved as cleaned_{column_name}.csv")

    return df

# === Example Usage ===
# Load dataset
file_path = r"UsersFile1Path.csv"
df_tiktok = load_dataset(file_path)

# Apply interpolation to fix extreme values in specific columns
columns_to_fix = ["CQI", "RSRP", "RSRQ", "DRB.AirIfDelayUl"]  # Add any other columns to fix

for col in columns_to_fix:
    df_tiktok = cubic_spline_interpolation(df_tiktok, col, save_output=True)

# Display cleaned dataset
print(df_tiktok.head())