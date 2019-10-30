"""
This is a menu giving the user options on how
they would like to manipulate the data.
Written here and imported to avoid writing the same code
multiple times.
"""


def secondary_selection():
    """This prints the options the user has to manipulate the data"""
    print("---------------------------")
    print("Column Statistics        [C]")
    print("Graph Plotting       [G]")
    d = input(str("Please select how you want the data to be processed: ")).lower()
    #  Returns as a true/false boolean as it's easier
    if d == "c":
        return True
    elif d == "g":
        return False
    else:
        print("Please enter a valid input")
