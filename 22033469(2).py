

import pandas as py

def read_worldbank_data(filename):
    # Read Excel file into a dataframe
    df = pd.read_excel(filename, sheet_name='Data')

    # Transpose the dataframe and set the first column as the index
    df_transposed = df.transpose()
    df_transposed.columns = df_transposed.iloc[0]
    df_transposed = df_transposed.iloc[1:]

    # Split the transposed dataframe into two dataframes
    df_years = df_transposed.iloc[:, :-1]
    df_countries = df_transposed.iloc[:, -1:]

    # Clean the dataframes
    df_countries = df_countries.rename(columns={df_countries.columns[0]: "Country"})

    return df_years, df_countries

filename = "/content/API_19_DS2_en_excel_v2_5252304.xls"
df_years, df_countries = read_worldbank_data(filename)

# Use the dataframes as needed
print(df_years)
print(df_countries)

df = pd.read_excel('/content/API_19_DS2_en_excel_v2_5252304.xls')
indicators = ['SP.POP.TOTL', 'NY.GDP.PCAP.CD', 'NY.GDP.MKTP.KD.ZG']
df_filtered = df[df['Unnamed: 3'].isin(indicators)]

# Group the filtered dataframe by country and compute summary statistics
df_country_summary = df_filtered.groupby(df['World Development Indicators']).describe()

# Group the filtered dataframe by year and compute summary statistics
df_year_summary = df_filtered.describe()

# Compute correlation between indicators
df_corr = df_filtered.corr()

# Compute mean and standard deviation of indicators by region
df_region_summary = df_filtered.groupby(df['Unnamed: 4']).agg(['mean', 'std'])

# Print the summary statistics and correlation matrix
print(df_country_summary)
print(df_year_summary)
print(df_corr)
print(df_region_summary)

import seaborn as sns
import matplotlib.pyplot as plt
indicators = ['SP.POP.TOTL', 'NY.GDP.PCAP.CD', 'NY.GDP.MKTP.KD.ZG']
df_filtered = df[df['Unnamed: 3'].isin(indicators)]
# Compute correlation between indicators
df_corr = df_filtered.corr()

# Plot a heatmap of the correlation matrix
sns.heatmap(df_corr, cmap="YlGnBu")
plt.title("Correlation Heatmap of World Bank Indicators")
plt.show()



df_country_corr = df_filtered.groupby(df['Data Source']).corr()

# Plot a scatterplot matrix of correlations for a few countries
countries = ['United States', 'China', 'India', 'Brazil']
g = sns.PairGrid(df_country_corr.loc[countries], diag_sharey=False)
g.map_lower(sns.scatterplot)
g.map_upper(sns.kdeplot, cmap="Blues_d")
g.map_diag(sns.kdeplot, lw=2)
plt.show()

x = df['Unnamed: 13']
y = df['Unnamed: 7']

plt.plot(x, y)

# add title and axis labels
plt.title("Line Graph")
plt.xlabel("1963")
plt.ylabel("1969")

# show the graph
plt.show()

plt.hist(df['Unnamed: 65'], bins=30, density=True, alpha=0.5, color='blue')

# Add labels and title
plt.xlabel('2022')
plt.ylabel('Frequency')
plt.title('Histogram of 22 YEAR Data')

# Show plot
plt.show()

sns.kdeplot(x)
plt.xlabel('X Label')
plt.ylabel('Density')
plt.title('Density Plot')

# show the plot
plt.show()