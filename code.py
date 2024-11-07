# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 22:34:45 2024

@author: chandrika_udara
"""

# Import required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_avg_calories_by_experience(df):
    """
    Groups the data by 'Experience_Level' and calculates the average calories 
        burned for each level. Plots a bar chart showing the average calories 
    burned across experience levels.

    Parameters:
        df (pd.DataFrame): A pandas DataFrame containing columns 
                'Experience_Level' and 'Calories_Burned'.

    Returns:
        None
    """
    # Group by 'Experience_Level' and calculate the mean of 'Calories_Burned'
    avg_calories_by_experience = df.groupby("Experience_Level")[
        "Calories_Burned"].mean()

    # Set up the plot figure size
    plt.figure(figsize=(8, 6))

    # Create a bar plot with 'Experience_Level' on x-axis and average calories
    # burned on y-axis
    sns.barplot(x=avg_calories_by_experience.index,
                y=avg_calories_by_experience.values)

    # Set x-axis label
    plt.xlabel("Experience Level")

    # Set y-axis label
    plt.ylabel("Average Calories Burned")

    # Set plot title
    plt.title("Average Calories Burned by Experience Level")

    # Display the plot
    plt.show()


def plot_age_vs_bmi_by_experience(df):
    """
    Plots a scatter plot showing the relationship between 'Age' and 'BMI' 
        across different 'Experience_Level'.

    Parameters:
        df (pd.DataFrame): A pandas DataFrame containing columns 'Age', 'BMI', 
                and 'Experience_Level'.

    Returns:
        None
    """
    # Set up the plot figure size
    plt.figure(figsize=(10, 8))

    # Create a scatter plot with 'Age' on x-axis and 'BMI' on y-axis,
    # color-coded by 'Experience_Level'
    sns.scatterplot(
        data=df, x="Age", y="BMI", hue="Experience_Level",
        palette="cool", s=70, edgecolor="w", alpha=0.8
    )

    # Set x-axis label
    plt.xlabel("Age")

    # Set y-axis label
    plt.ylabel("BMI")

    # Set plot title
    plt.title("Age vs BMI by Experience Level")

    # Add a legend with title 'Experience Level'
    plt.legend(title="Experience Level")

    # Display the plot
    plt.show()


def plot_correlation_heatmap(df):
    """
    Selects relevant numerical columns from the DataFrame, calculates the 
        correlation matrix, and plots a heatmap of correlations among the 
        selected numerical features.

    Parameters:
        df (pd.DataFrame): A pandas DataFrame containing various gym member 
        data, including numerical columns such as 'Age', 'Weight (kg)', 
        'Height (m)', etc.

    Returns:
        None
    """
    # Select relevant numerical columns from the DataFrame
    numeric_columns = df[[
        "Age", "Weight (kg)", "Height (m)", "Max_BPM", "Avg_BPM",
        "Resting_BPM", "Session_Duration (hours)", "Calories_Burned",
        "Fat_Percentage", "Water_Intake (liters)",
        "Workout_Frequency (days/week)", "BMI"
    ]]

    # Calculate the correlation matrix for the selected numerical columns
    correlation_matrix = numeric_columns.corr()

    # Set up the plot figure size
    plt.figure(figsize=(12, 10))

    # Create a heatmap to visualize the correlation matrix with annotations
    # and a color map
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")

    # Set the title of the plot
    plt.title("Correlation Heatmap of Gym Member Data")

    # Display the plot
    plt.show()


def main():
    # Read the dataset
    df = pd.read_csv("gym_members_exercise_tracking.csv")

    # Info of dataset
    print("Info of data:", df.info(), sep="\n")

    # Describe dataset
    print("Describing the data:", df.describe(), sep='\n')

    # Check for null values
    print("Checking for null values:", df.isnull().sum(), sep="\n")

    # Skewness of data
    print("Skewness: ", df.skew(numeric_only=True), sep="\n")

    # Kurtosis of data
    print("Kurtosis: ", df.kurt(numeric_only=True), sep="\n")

    # Calling the function
    plot_avg_calories_by_experience(df)

    # Calling the function
    plot_age_vs_bmi_by_experience(df)

    # Calling the function
    plot_correlation_heatmap(df)


if __name__ == "__main__":
    # Start of the program from here by calling main()
    main()
