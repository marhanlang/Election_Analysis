# Data we need to retrieve.
# 1. Total number of votes cast
# 2. Complete list of candidates who recieved votes
# 3. Percentage of votes each candidate won
# 4. Total number of votes each candidate won
# 5. Winner of the election based on popular vote

#add dependencies
import csv
import os

#assign variable for file to load and path
file_to_load = os.path.join("Resources", "election_results.csv")
#assign variable to save file to path
file_to_save= os.path.join("Analysis", "election_analysis.txt")

# open election results and read file
with open(file_to_load) as election_data:

    #read file object with reader function
    file_reader = csv.reader(election_data)
    #print header row
    headers= next(file_reader)
    print(headers)

