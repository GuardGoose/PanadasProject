"""
These will be imported to other modules
it gives functions for the user's general choice.
It would also direct the users choices towards the
correct locations.
"""

from Newcastle import Newcastle_1 as nc  # Imports the Newcastle_1 as nc to reduce global namespace clutter
from NI import NI_1 as ni  # Imports the NI as ni to reduce global namespace clutter
from Plastic_Bag import Bag_1 as bg  # Imports Hawaii_1 as hw to reduce global namespace clutter


def index_selection(x):
    """This takes the users selections from the index page"""
    if x == "r":  # Newcastle Dataset
        nc.main()  # Goes to Newcastle dataset's display function
    elif x == "w":  # Northern Ireland Dataset
        ni.main()  # Goes to the Northern Ireland datasets's display function
    elif x == "q":  # State of Hawaii Dataset
        bg.main()  # Goes to the Hawaii dataset's display function
    elif x == "e":  # Exit Button
        exit()
    else:
        return False
