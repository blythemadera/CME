import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

parks_df = pd.read_csv("Parks-Locations.csv")
libraries_df = pd.read_csv("libraries-json.csv")
housing_df = pd.read_csv("Affordable-Rental-Housing-Developments.csv")

parks_agg = parks_df.groupby("ZIP").count().reset_index()
parks_agg = parks_agg[["ZIP", "PARK NAME"]]
parks_agg.rename(columns={'ZIP':'zip'}, inplace=True)
parks_agg.rename(columns={'PARK NAME':'park_count'}, inplace=True)

libraries_agg = libraries_df.groupby("Zip").count().reset_index()
libraries_agg = libraries_agg[["Zip", "Branch"]]
libraries_agg.rename(columns={'Zip':'zip'}, inplace=True)
libraries_agg.rename(columns={'Branch':'library_count'}, inplace=True)

housing_agg = housing_df.groupby("Zip Code").agg('sum').reset_index()
housing_agg = housing_agg[["Zip Code", "Units"]]
housing_agg.rename(columns={'Zip Code':'zip'}, inplace=True)
housing_agg.rename(columns={'Units':'housing_count'}, inplace=True)

merge1 = pd.merge(housing_agg[['zip', 'housing_count']], libraries_agg[['zip','library_count']], how='left', left_on=['zip'], right_on=['zip'])
merged_df = pd.merge(merge1[['zip', 'housing_count', 'library_count']], parks_agg[['zip','park_count']], how='left', left_on=['zip'], right_on=['zip'])


corr = merged_df.corr()
hp_corr = merged_df['housing_count'].corr(merged_df['park_count'])
hl_corr = merged_df['housing_count'].corr(merged_df['library_count'])

plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True, cmap='Blues', fmt=".2f")
plt.title("Correlation Between Housing, Libraries, and Parks")

if not os.path.exists("results"):
    os.path.makedirs("results", exists_ok=True)

results_file = 'results/correlation_results.txt'

with open(results_file, "wt") as f:
      f.write(f'Housing and Park Correlation: {round(hp_corr, 3)}\n'
        f'Housing and Library Correlation: {round(hl_corr, 3)}\n')

figure_file = 'results/correlation.pdf'
print(f'Writing figure to {figure_file}')
plt.figure.savefig(figure_file)

