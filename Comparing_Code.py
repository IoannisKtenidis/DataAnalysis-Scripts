import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def load_datasets(file_paths):
    """
    Loads multiple CSV datasets and returns a dictionary of DataFrames.
    """
    dataframes = {}
    for file_path in file_paths:
        df = pd.read_csv(file_path, encoding='utf-8')
        df["Timestamp"] = pd.to_datetime(df["Timestamp"])
        df.sort_values("Timestamp", inplace=True)
        dataframes[os.path.basename(file_path)] = df
    return dataframes

def compute_summary_metrics(dataframes):
    """
    Computes key network metrics (throughput & data volume) for multiple datasets.
    """
    key_metrics = ["DRB.UEThpDl", "DRB.UEThpUl", "DRB.RlcSduTransmittedVolumeDL", "DRB.RlcSduTransmittedVolumeUL"]
    summary_stats = {}
    for name, df in dataframes.items():
        summary_stats[name] = df[key_metrics].describe()
    return summary_stats

def save_metrics_to_csv(summary_stats, output_file="network_metrics_comparison.csv"):
    """
    Saves the computed metrics to a CSV file for comparison.
    """
    comparison_df = pd.concat(summary_stats, axis=1)
    comparison_df.to_csv(output_file)
    print(f"Metrics comparison saved to {output_file}")

def plot_metrics(summary_stats):
    """
    Generates bar plots comparing key metrics across multiple CSVs.
    """
    metrics = ["DRB.UEThpDl", "DRB.UEThpUl", "DRB.RlcSduTransmittedVolumeDL", "DRB.RlcSduTransmittedVolumeUL"]
    labels = list(summary_stats.keys())
    
    for metric in metrics:
        values = [summary_stats[label][metric]['mean'] for label in labels]
        
        plt.figure(figsize=(8, 5))
        plt.bar(labels, values, color=['blue', 'red'])
        plt.xlabel("Dataset")
        plt.ylabel(metric)
        plt.title(f"Comparison of {metric}")
        plt.xticks(rotation=45)
        plt.show()

def main():
    # List of CSV files to analyze
    file_paths = [
        r"UsersFile1Path.csv", 
        r"UsersFile2Path.csv"
    ]
    
    # Load datasets
    dataframes = load_datasets(file_paths)
    
    # Compute metrics
    summary_stats = compute_summary_metrics(dataframes)
    
    # Save results to CSV
    save_metrics_to_csv(summary_stats)
    
    # Print summary
    print(pd.concat(summary_stats, axis=1))
    
    # Generate comparison plots
    plot_metrics(summary_stats)

if __name__ == "__main__":
    main()
