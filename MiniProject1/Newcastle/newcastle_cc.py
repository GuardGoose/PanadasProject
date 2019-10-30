import pandas as pd  # Imports pandas for data manipulation tools
import matplotlib.pyplot as plt  # Imports matplotlib.pylot for visualisation tools


class ColumnCalculation:
    """This houses the functions for all the column manipulation calculations"""

    def __init__(self):  # Loads the csv when the class is initalised
        self.df = pd.read_csv("2011-onwards-city-elec-consumption.csv", thousands=',')

    def total_electricity(self):
        """Calculates the total amount of electricity used per year"""
        self.df.set_index('Date', inplace=True)  # Sets index to months
        self.df.loc['Total'] = self.df.sum()  # Creates a new row for the totals of each year
        return print(self.df)  # Prints the dataframe

    def difference_months(self):
        """Difference Between 2011 and 2017 per month"""
        rdf = self.df[['2011', '2017']].copy()  # Copies these two columns to a new dataframe
        rdf['Difference'] = rdf['2011'] - rdf['2017']  # Calculates the difference
        print(rdf)  # Prints the dataframe

    def percent_difference(self):
        """Percent difference between 2012 and 2013"""
        rdf = self.df[['2012', '2013']].copy()  # Copies these two columns to a new dataframe
        rdf['Percent Change'] = ((rdf['2012'] - rdf['2013']) / rdf['2013']) * 100
        # Percent change calculated by taking the values away, dividing and multiplying
        # pct.change() wouldn't work for some reason
        print(rdf)

    def basic_statistics(self):
        """Calculates basic statistics for each year"""
        self.df.set_index('Date', inplace=True)  # Sets index to months
        self.df.loc['Max'] = self.df.max()  # Takes the max of each column
        self.df.loc['Min'] = self.df.min()  # Takes the min of each column
        self.df.loc['Mean'] = self.df.mean()  # Takes the mean of each column
        self.df.loc['Standard Dev.'] = self.df.std()  # Takes the standard dev of each column
        self.df.loc['Median'] = self.df.median()  # Takes the median of each column
        return print(self.df)  # prints dataframe


class GraphPlotting:
    """This houses the functions for plotting graphs"""

    def __init__(self):
        self.df = pd.read_csv("2011-onwards-city-elec-consumption.csv", thousands=',')

    def pie_chart(self):
        """Makes a pie chart to compare the average amount of electricity used per year"""
        self.df.drop(['Date'], axis=1, inplace=True)  # Excludes the date column
        rdf = self.df.mean()  # Calculates the mean
        rdf.plot(kind="pie", title="Average (mean) amount of electricity used each year", autopct='%1.1f%%')
        #  'autopct' displays the percentages
        # Generates the Pie Chart
        plt.show()  # Displays the pie chart

    def bar_chart(self):
        """Makes a bar chart to show how much electricity is used for each month per year"""
        self.df.set_index(['Date'], inplace=True)  # Sets index to date
        self.df.plot.bar(stacked=False, title="Electricity per month, per year")  # Plots a bar graph
        plt.show()  # Displays the bar graph

    def line_graph(self):
        """Makes a line graph comparing the electricity consumption of 2011 vs. 2017"""
        rdf_2011 = self.df[['Date', '2011']].copy()  # Creates a dataframe with only 2011 values
        rdf_2017 = self.df[['Date', '2017']].copy()  # Creates a dataframe with only 2017 value
        ax = rdf_2011.plot(title='2011 vs 2017 Electricity Usage')  # Plots a line graph
        rdf_2017.plot(ax=ax)  # Adds the 2017 values to the graph
        plt.show()  # Displays the graph

