"""
Data Cleaning Script for IT Support Team Performance Optimization
This script performs data cleaning and preprocessing operations on raw IT support data.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

# Set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

def load_data(file_path):
    """
    Load raw data from CSV or Excel file
    
    Args:
        file_path (str): Path to the raw data file
    
    Returns:
        pd.DataFrame: Loaded dataframe
    """
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith(('.xlsx', '.xls')):
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Use CSV or Excel files.")
    
    print(f"Data loaded successfully. Shape: {df.shape}")
    return df

def handle_missing_values(df):
    """
    Handle missing values in the dataset
    
    Args:
        df (pd.DataFrame): Input dataframe
    
    Returns:
        pd.DataFrame: Dataframe with handled missing values
    """
    print("\nMissing values before cleaning:")
    print(df.isnull().sum())
    
    # Strategy: Fill numerical columns with median, categorical with mode
    for col in df.columns:
        if df[col].dtype in ['float64', 'int64']:
            df[col].fillna(df[col].median(), inplace=True)
        else:
            df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else 'Unknown', inplace=True)
    
    print("\nMissing values after cleaning:")
    print(df.isnull().sum())
    
    return df

def remove_duplicates(df):
    """
    Remove duplicate records from the dataset
    
    Args:
        df (pd.DataFrame): Input dataframe
    
    Returns:
        pd.DataFrame: Dataframe without duplicates
    """
    initial_shape = df.shape
    df = df.drop_duplicates()
    final_shape = df.shape
    
    print(f"\nDuplicates removed: {initial_shape[0] - final_shape[0]} records")
    print(f"Final shape: {final_shape}")
    
    return df

def handle_outliers(df, numerical_columns):
    """
    Detect and handle outliers using IQR method
    
    Args:
        df (pd.DataFrame): Input dataframe
        numerical_columns (list): List of numerical column names
    
    Returns:
        pd.DataFrame: Dataframe with handled outliers
    """
    for col in numerical_columns:
        if col in df.columns:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
            print(f"\nOutliers detected in {col}: {len(outliers)} records")
            
            # Cap outliers instead of removing them
            df[col] = df[col].clip(lower_bound, upper_bound)
    
    return df

def validate_data(df):
    """
    Validate data integrity and consistency
    
    Args:
        df (pd.DataFrame): Input dataframe
    
    Returns:
        bool: True if validation passes
    """
    print("\nData Validation Report:")
    print(f"Total records: {len(df)}")
    print(f"Total columns: {len(df.columns)}")
    print(f"\nData types:\n{df.dtypes}")
    print(f"\nBasic statistics:\n{df.describe()}")
    
    return True

def save_cleaned_data(df, output_path):
    """
    Save cleaned data to file
    
    Args:
        df (pd.DataFrame): Cleaned dataframe
        output_path (str): Output file path
    """
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    if output_path.endswith('.csv'):
        df.to_csv(output_path, index=False)
    elif output_path.endswith(('.xlsx', '.xls')):
        df.to_excel(output_path, index=False)
    
    print(f"\nCleaned data saved to: {output_path}")

def main():
    """
    Main function to execute data cleaning pipeline
    """
    print("=" * 80)
    print("IT Support Team Performance - Data Cleaning Pipeline")
    print("=" * 80)
    
    # Define file paths
    raw_data_path = "../Data/raw/it_support_data.csv"
    processed_data_path = "../Data/processed/it_support_cleaned.csv"
    
    # Check if raw data exists
    if not os.path.exists(raw_data_path):
        print(f"\nWarning: Raw data file not found at {raw_data_path}")
        print("Please add your raw data file to continue.")
        return
    
    # Load data
    df = load_data(raw_data_path)
    
    # Data cleaning steps
    df = handle_missing_values(df)
    df = remove_duplicates(df)
    
    # Define numerical columns (update based on actual data)
    numerical_columns = df.select_dtypes(include=[np.number]).columns.tolist()
    df = handle_outliers(df, numerical_columns)
    
    # Validate data
    validate_data(df)
    
    # Save cleaned data
    save_cleaned_data(df, processed_data_path)
    
    print("\n" + "=" * 80)
    print("Data cleaning completed successfully!")
    print("=" * 80)

if __name__ == "__main__":
    main()
