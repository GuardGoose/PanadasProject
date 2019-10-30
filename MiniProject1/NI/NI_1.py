"""
This is the main interface if the user has chosen
to process the NI dataset
This will give them options for what they want to process.
"""


from interfaces.s_selection import SecondarySelection as SS  # Imports the secondary_selection function from selections
import interfaces.ni_cm as IT  # Imports the interfaces for the choices the user makes
from NI.ni_cc import ColumnCalculation as CC  # Imports the ColumnCalculation class
from NI.ni_cc import GraphPlotting as GP  # Imports the GraphPlotting class


class Bag:

    def __init__(self):
        self.key_typed = int(input("Select what you want to do: "))

    @staticmethod  # Static method as it only displays
    def column_or_graph():
        SS.display_input()  # Calls the @staticmethod display_input from s_selection.py
        if SS.get_input(SS()) is True:
            IT.column_manipulation()
            return True  # If SS.get_input returns True, then it returns True
        IT.graph_plotting()
        return False

    def column_selection(self):
        """Gives the user a selection of which column manipulation they would like to do"""
        if self.key_typed == 1:
            CC.basic_statistics(CC())  # Calls the basic_statistic method from ni_cc.py
        elif self.key_typed == 2:
            CC.total_amount_searched(CC())  # Calls the total_amount_searched method from ni_cc.py
        elif self.key_typed == 3:
            CC.fquarter_squarter_total(CC())  # Calls the fquarter_squarter_total from ni_cc.py

    def graph_plotting(self):
        """Gives the user a selection on which graphs to plot"""
        if self.key_typed == 1:
            GP.pie_chart(GP())  # Calls the pie_chart method from ni_cc.py
        elif self.key_typed == 2:
            GP.bar_chart(GP())  # Calls the bar_chart method from ni_cc.py
        elif self.key_typed == 3:
            GP.line_graph(GP())  # Calls the line_graph method from ni_cc.py
        else:
            raise TypeError("Please try again")


def main():
    """This calls the @staticmethod which allows users to make choices based on the interface"""
    if Bag.column_or_graph() is True:
        return Bag.column_selection(Bag())
    return Bag.graph_plotting(Bag())


if __name__ == "__main__":
    main()

