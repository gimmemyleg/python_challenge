# importing modules that allow to handle and use file pathing
import os
import csv
from collections import Counter

# create path to the csv file
filepath = os.path.join("Resources", "election_data.csv")
resultpath = os.path.join("analysis", "analysis.txt")
# print(filepath) <- This was used to print filepath as a reference

# before going through loop, going to set some list and variable.
# this will separate each column and store values for Ballot_ID and Candidate
Candidates = []
Ballot_ID = []
Total_result = []
# this will addup each vote for each candidate
charles_vote = 0
diana_vote = 0
raymon_vote = 0
winner = ""

# open the file using the file path above, read original file
with open(filepath, 'r', encoding = "utf-8") as file :
    # create the reader object(file stream)
    csvReader = csv.reader(file, delimiter = ",")
    # grab header (skips header)
    csvheader = next(csvReader)
    # read each row of data from the file
    for row in csvReader:
        Candidates.append(row[2])
        Ballot_ID.append(row[0])
    for Candidate in Candidates:
        if Candidate.lower() == "charles casper stockham":
            charles_vote += 1
        elif Candidate.lower() == "diana degette":
            diana_vote += 1
        elif Candidate.lower() == "raymon anthony doane":
            raymon_vote += 1


# will be using *Counter (unique Counter function) to select unique value from Candidate list
# this will give list of unique values of Candidate. 
New_Candidates = [*Counter(Candidates)]
#print(New_Candidates)
vote_Candidates = [charles_vote, diana_vote, raymon_vote]
winner = New_Candidates[vote_Candidates.index(max(vote_Candidates))]

# define percentage function before generating output.
def percentage(part,whole):
    return round(100 * float(part)/float(whole),3)

# define output to put out in terminal and analysis.txt file
output = (
    f"\n Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {len(Ballot_ID)}\n"
    f"-------------------------\n"
    f"Charles Casper Stockham: {percentage(charles_vote, len(Ballot_ID))}% ({charles_vote})\n"
    f"Diana DeGette: {percentage(diana_vote, len(Ballot_ID))}% ({diana_vote})\n"
    f"Raymon Anthony Doanes : {percentage(raymon_vote, len(Ballot_ID))}% ({raymon_vote})\n"
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)
# print above output
print (output)

# open the output file and write the data into it and save to analysis.txt
with open(resultpath ,"w") as outfile:
    outfile.writelines(output)


