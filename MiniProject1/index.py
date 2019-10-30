"""
This is the basic interface of the program
"""
from interfaces.index_selection import interface  # Imports index_selection from selections.py
from selections import index_selection

interface()
key_typed = input(str("Please select the dataset you wish to process: ")).lower()  # Makes the input lower case
index_selection(key_typed)  # Imported function used




