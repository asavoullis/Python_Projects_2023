# World Bank Science and Technology Data Analysis

## Description

This Python script is designed to analyze science and technology data from the World Bank. It performs various data cleaning and exploratory data analysis tasks on two datasets from different years (2018 and 2009) to uncover insights and relationships within the data.

This Jupyter Notebook, named "Basic_Statistics_in_Python_Correction_and_T_test.ipynb," is designed to analyze science and technology data from the World Bank. It performs various data cleaning and exploratory data analysis tasks on two datasets from different years (2018 and 2009) to uncover insights and relationships within the data.

### Prerequisites

Before running the script, ensure you have the following libraries installed:

- Jupyter Notebook
- pandas
- numpy
- matplotlib
- seaborn
- scipy

You can install these libraries using pip:

```bash
pip install pandas numpy matplotlib seaborn scipy notebook
```

## Usage

1. Place the CSV files for the science and technology data for the years 2018 and 2009 in the same directory as this script.
2. Run the script using Python 3.x:

```bash
python your_script_name.py
```

## Script Overview

- The script starts by importing necessary libraries, reading the data from CSV files, and performing basic data exploration.

### Data Cleaning

- Null or NaN values are removed from both datasets to ensure data quality.

### Exploratory Data Analysis (EDA)

- Descriptive statistics are calculated for the cleaned datasets.
- Box plots are used to identify outliers in the data.

### Exploring Relationships

- Correlations between different variables are calculated using Pearson and Spearman methods.
- Scatter plots are created to visualize relationships between specific variables.

### T-tests

- Independent t-tests are conducted to compare data between the years 2009 and 2018 for various variables.

## Notes

- The script mentions that independent t-tests were used due to different numbers of countries in the two datasets.
- It suggests using relative t-tests (ttest_rel) for more accurate comparisons if the datasets contain the same countries in the same years.

Feel free to modify the script to suit your specific needs and to add more detailed explanations or visualizations if required.

For any questions or issues, please contact me, Charilaos.

##
