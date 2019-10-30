import pandas as pd  # Imports pandas for data manipulation tools
import matplotlib.pyplot as plt  # Imports matplotlib.pylot for visualisation tools


class ColumnCalculation:
    """This houses the functions for all the column manipulation calculations"""

    def __init__(self):  # Loads the csv when the class is initalised
        self.df = pd.read_csv("carrier_bag_19072017_v2.csv", encoding="ISO-8859-1", nrows=263)
        # Encoding to handle scientific notation
        # nrows prevents the 'notes' at the bottom being factored into any calculations

    def basic_statistics(self):
        """Calculates the basic statistics for donations raised"""
        rdf = self.df[['Company name', 'Amount donated to good causes (£)']].copy()
        # Made a new dataframe with only these columns
        rdf.set_index(['Company name'], inplace=True)  # Sets the index to company names
        rdf.fillna(0, inplace=True)  # Replaces all NaN values with 0
        rdf.loc['Max'] = rdf.max()  # Takes the max of each column
        rdf.loc['Min'] = rdf.min()  # Takes the min of each column
        rdf.loc['Mean'] = rdf.mean()  # Takes the mean of each column
        rdf.loc['Standard Dev.'] = rdf.std()  # Takes the standard dev of each column
        rdf.loc['Median'] = rdf.median()  # Takes the median of each column
        pd.set_option('display.float_format', lambda x: '%.2f' % x)  # Suppresses scientific notation
        print(rdf)  # Prints the dataframe

    def total_bag(self):
        """Calculates the grand total of single usage plastic bags"""
        rdf = self.df[['Company name', ' Number of single use plastic bags issued ']].copy()
        # Made a new dataframe with only these columns
        rdf.set_index(['Company name'], inplace=True)  # Sets the index to company names
        rdf.fillna(0, inplace=True)  # Replaces all NaN values with 0
        rdf.loc['Grand Total'] = rdf.sum()
        pd.set_option('display.float_format', lambda x: '%.2f' % x)  # Suppresses scientific notation
        print(rdf)

    def net_vs_donation(self):
        """Calculates the difference between bags and bags for life for Asda"""
        rdf = self.df[['Company name', 'Net proceeds  (£) (Gross less VAT and costs)',
                       'Amount donated to good causes (£)']].copy()  # Made a new dataframe with only these columns
        rdf.set_index(['Company name'], inplace=True)  # Sets the index to company names
        rdf.fillna(0, inplace=True)  # Replaces all NaN values with 0
        rdf['Difference'] = rdf['Net proceeds  (£) (Gross less VAT and costs)']\
                            - rdf['Amount donated to good causes (£)']  # Does the difference
        print(rdf)

    def vat_calc(self):
        """Calculates the percentage vat"""
        rdf = self.df[[' Gross proceeds of charge (£) ', 'VAT (£)']].copy()  # Made a new dataframe with only these columns
        rdf.fillna(0, inplace=True)  # Sets the index to company names
        rdf['VAT %'] = ((rdf[' Gross proceeds of charge (£) '] - rdf['VAT (£)']) / rdf['VAT (£)'])
        pd.set_option('display.float_format', lambda x: '%.2f' % x)  # Suppresses scientific notation
        print(rdf)


class GraphPlotting:
    """This houses the functions for plotting graphs"""

    def __init__(self):
        self.df = pd.read_csv("carrier_bag_19072017_v2.csv", encoding="ISO-8859-1", nrows=263)
    # Encoding to handle scientific notation
    # nrows prevents the 'notes' at the bottom being factored into any calculations

    def pie_chart(self):
        """Shows whether proceeds we're donated or not"""
        rdf = self.df['Use of net proceeds']  # Creates a dataframe with only this column
        rdf.value_counts().plot(kind='pie', title='Donators vs None Donators', autopct='%1.1f%%')
        #  Counts the values of the column, puts them in a pie chart
        #  autopct displays the percentage of each segment
        plt.show()  # Shows the graph

    def bar_chart(self):
        """Number of plastic bags produced by bottom 5 companies"""
        rdf = self.df[['Company name', ' Number of single use plastic bags issued ']].copy()
        # Creates a dataframe with only 2 columns
        rdf.set_index(['Company name'], inplace=True)  # Sets index to company name
        rdf.tail().plot(kind='bar', stacked=False, figsize=(15, 8))
        # Plots the graph as a bar, figsize increases the window display
        # .tail() so it only shows the bottom 5 values
        plt.tight_layout()  # Makes it so we can see the company names
        plt.show()  # Shows the graph

    def line_graph(self):
        """Use of net proceeds of a company"""
        rdf = self.df['Use of net proceeds']
        rdf.value_counts().plot(kind='line', title="Number of Donations (left to right)")
        plt.show()


