#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 16:57:57 2025

@author: junga1
"""

import pandas as pd

def load_feature_matrix(filepath):
    """
    Load weather data from CSV and return a feature matrix with:
    year, month, day, hour, minute, min temp, max temp

    Parameters:
    filepath (str): Path to the CSV file.

    Returns:
    np.ndarray: Feature matrix.
    """
    # Load CSV and treat "-" as missing values
    df = pd.read_csv(filepath, na_values="-")

    # Parse datetime
    df["datetime"] = pd.to_datetime(
        df[["Year", "Month", "Day"]].astype(str).agg("-".join, axis=1) + " " + df["Time [Local time]"],
        errors="coerce"
    )

    # Extract features
    feature_df = pd.DataFrame({
        "year": df["datetime"].dt.year,
        "month": df["datetime"].dt.month,
        "day": df["datetime"].dt.day,
        "hour": df["datetime"].dt.hour,
        "minute": df["datetime"].dt.minute,
        "min_temperature": pd.to_numeric(df["Minimum temperature [°C]"], errors="coerce"),
        "max_temperature": pd.to_numeric(df["Maximum temperature [°C]"], errors="coerce")
    })

    # Replace NaNs with 0 and convert to numpy array
    feature_array = feature_df.fillna(0).to_numpy()

    return feature_array

if __name__ == "__main__":
    filepath = "../data/assignment_1.csv"
    features = load_feature_matrix(filepath)
    print(features)