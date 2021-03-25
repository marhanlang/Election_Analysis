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

#initialize variable to zero
total_votes = 0

# Declare new list
candidate_options = []

#Create dictionary
candidate_votes = {}

#Winning candidate and Winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open election results and read file
with open(file_to_load) as election_data:

    #read file object with reader function
    file_reader = csv.reader(election_data)
    #read header row
    headers= next(file_reader)
    
    #Print each row in csv file
    for row in file_reader:
        #add to total vote count
        total_votes += 1
        #print candidate name from each row
        candidate_name = row[2]
        #check if candidate name matches one already listed
        if candidate_name not in candidate_options:
            #add candidate name to candidate list
            candidate_options.append(candidate_name)
            #track candidates vote count
            candidate_votes[candidate_name] = 0
        #add vote to candidates count
        candidate_votes[candidate_name] += 1
    

    # Iterate through candidate list
    for candidate_name in candidate_votes:
        #retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #calculate percentage
        vote_percentage = (float(votes) / float(total_votes)) *100
        
        # print each candidate name votes and %
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #determine winning vote count and candidate
        #determine if votes are greater then winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true set winning_count=votes and winning_percentage = vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #set winning candidate = to candidate's name
            winning_candidate = candidate_name
    #print winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print (winning_candidate_summary)