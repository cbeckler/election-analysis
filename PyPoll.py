# 1 Retrieve Data
# 2 Total N votes
# 3 List of candidates
# 4 % votes each candidate won
# 5 total N votes per candidate
# 6 election winner (popular vote)

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
    txt_file.write("Counties in the Election\n-----------------------\nArapahoe\nDenver\nJefferson")

# Close the file
txt_file.close()