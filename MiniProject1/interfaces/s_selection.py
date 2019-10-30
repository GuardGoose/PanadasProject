"""
This is a menu giving the user options on how
they would like to manipulate the data.
Written here and imported to avoid writing the same code
multiple times.
"""


class SecondarySelection:
    """This prints the options the user has to manipulate the data, and takes input"""
    def __init__(self):
        self.key_typed = input(str("Please select how you want the data to be processed: ")).lower()

    @staticmethod  # Doesn't need to take any arguments as it only displays
    def display_input():
        print("---------------------------")
        print("Column Statistics        [C]")
        print("Graph Plotting       [G]")

    def get_input(self):
        if self.key_typed == "c":
            return True
        elif self.key_typed == "g":
            return False
        else:
            raise TypeError("Please try again")
