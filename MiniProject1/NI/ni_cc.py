import pandas as pd  # Imports pandas for data manipulation tools
import matplotlib.pyplot as plt  # Imports matplotlib.pylot for visualisation tools


class ColumnCalculation:
    """This houses the functions for all the column manipulation calculations"""

    def __init__(self):  # Loads the csv when the class is initalised
        self.df = pd.read_csv("stop-and-search-open-data-201617.csv")

    def basic_statistics(self):
        """This calculates the basic statistics, divided by quarters"""
        rdf_quarters = pd.DataFrame(self.df.Quarter.value_counts().reset_index())
        # Creates a new dataframe with the total from each quarter
        # This makes it easier to do statistical analysis on the data as a whole
        rdf_quarters.columns = ['Quarters', 'Count']  # Sets the columns of the new dataframe
        rdf_quarters.set_index(['Quarters'], inplace=True)  # Sets the index
        print(rdf_quarters.describe())  # Prints the dataframe, with basic statistics

    def total_amount_searched(self):
        """Calculated the total amount of people searched"""
        self.df = self.df.rename(index=str, columns=({'Geographical Level': 'Total Searched'}))
        # Changes the name of Geographical Level to Total Searched
        # This allows us to count the total number of people searched
        self.df = pd.DataFrame(self.df['Total Searched'].value_counts())
        # Counts the values in this column to provide a total
        print(self.df)

    def fquarter_squarter_total(self):
        """Total Searched Each Half"""
        #rdf_quarters = pd.DataFrame(self.df.Quarter.value_counts().reset_index())
        rdf = pd.DataFrame(self.df.Quarter.value_counts())
        #rdf.set_index(['index'], inplace=True)
        rdf1 = rdf.drop(['January to March', 'April to June'])
        rdf1.loc['FirstQuarter'] = rdf1.sum()
        rdf2 = rdf.drop(['July to September', 'October to December'])
        rdf2.loc['SecondQuarter'] = rdf2.sum()
        print(rdf1, rdf2)


class GraphPlotting:
    """This houses the functions for plotting graphs"""

    def __init__(self):
        self.df = pd.read_csv("stop-and-search-open-data-201617.csv")

    def pie_chart(self):
        """Difference Between Male and Females"""
        rdf = pd.DataFrame(self.df.Gender.value_counts())  # Counts occurrences of gender
        rdf.plot(kind='pie', title="Male vs. Female", autopct='%1.1f%%', subplots=True)
        # Plots them in a pie chart
        plt.show()

    def bar_chart(self):
        """Under which Legislation were they searched under"""
        rdf = pd.DataFrame(self.df.Legislation.value_counts())
        # Counts occurrences of each legislation
        rdf.plot(kind='bar', stacked=True)
        plt.show()

    def line_graph(self):
        """Number of people searched over financial year"""
        self.df = pd.DataFrame(self.df['Quarter'].value_counts())
        # Counts each person searched over the financial year
        self.df.plot()
        plt.show()

