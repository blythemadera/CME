import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

parks_df = pd.read_csv("Parks-Locations.csv")
libraries_df = pd.read_csv("libraries-json.csv")
housing_df = pd.read_csv("affordable-housing-json (2).csv")

parks_agg = parks_df.groupby("ZIP").count().reset_index()
parks_agg = parks_agg[["ZIP", "PARK NAME"]]
parks_agg.rename(columns={'ZIP':'zip'}, inplace=True)
parks_agg.rename(columns={'PARK NAME':'park_count'}, inplace=True)

libraries_agg = libraries_df.groupby("Zip").count().reset_index()
libraries_agg = libraries_agg[["Zip", "Branch"]]
libraries_agg.rename(columns={'Zip':'zip'}, inplace=True)
libraries_agg.rename(columns={'Branch':'library_count'}, inplace=True)

housing_agg = housing_df.groupby("ZIP").agg('sum').reset_index()
housing_agg = housing_agg[["ZIP", "UNITS"]]
housing_agg.rename(columns={'ZIP':'zip'}, inplace=True)
housing_agg.rename(columns={'UNITS':'housing_count'}, inplace=True)

merge1 = pd.merge(housing_agg[['zip', 'housing_count']], libraries_agg[['zip','library_count']], how='left', left_on=['zip'], right_on=['zip'])
merged_df = pd.merge(merge1[['zip', 'housing_count', 'library_count']], parks_agg[['zip','park_count']], how='left', left_on=['zip'], right_on=['zip'])


corr = merged_df.corr()
hp_corr = merged_df['housing_count'].corr(merged_df['park_count'])
hl_corr = merged_df['housing_count'].corr(merged_df['library_count'])


if not os.path.exists("results"):
    os.path.makedirs("results", exists_ok=True)

results_file = 'results/correlation_results.txt'

with open(results_file, "wt") as f:
      f.write(f'Housing and Park Correlation: {round(hp_corr, 5)}\n'
        f'Housing and Library Correlation: {round(hl_corr, 5)}')

#scatterplot
plt.scatter(merged_df['zip'], merged_df['library_count'],color='blue', label='Dataset A')
scatter_file = 'results/library_plot.pdf'
print(f'Writing figure to {scatter_file}')
plt.savefig(scatter_file)

plt.scatter(merged_df['zip'], merged_df['park_count'],color='red', label='Dataset B')
park_file = 'results/park_plot.pdf'
print(f'Writing figure to {park_file}')
plt.savefig(park_file)

plt.scatter(merged_df['zip'], merged_df['housing_count'],color='green', label='Dataset C')
housing_file = 'results/housing_plot.pdf'
print(f'Writing figure to {housing_file}')
plt.savefig(housing_file)

#heatmap
plt.figure(figsize=(8,5))
sns.heatmap(corr, annot=True, cmap='Blues', fmt=".2f")
plt.title("Correlation Between Housing, Libraries, and Parks")

figure_file = 'results/correlation.pdf'
print(f'Writing figure to {figure_file}')
plt.savefig(figure_file)
