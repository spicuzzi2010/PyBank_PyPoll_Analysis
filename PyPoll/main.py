#import dependencies
import os
import csv

# Change to the current directory
os.chdir(os.path.dirname(__file__))


# set election_data_csv to the path for election_data.csv
election_data_csv = os.path.join("Resources","election_data.csv")

# Objective 3: Create the lists to store data. Initialize

candidate_list = []
unique_candidates = []
votes_cast = 0
votes_cast_list = []
vote_percent = 0
vote_percent_list = []
votes_per_candidate = []
candidate_votes = 0

# Open the election data csv
with open(election_data_csv, newline="\n") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #skip headers
    next(csv_reader)
    
    for row in csv_reader:
        
        #count the total number of votes cast
        votes_cast += 1
        
        #store the candidate names to the candidate_list
        candidate_list.append(row[2])
        votes_cast_list.append(row[0])

        for i in set(candidate_list):
            unique_candidates.append(i)
            candidate_votes = candidate_list.count(i)
            votes_per_candidate.append(candidate_votes)

            vote_percent = (candidate_votes/votes_cast)*100
            vote_percent_list.append(vote_percent)

            
winning_vote_count = max(candidate_votes)
winning_candidate = unique_candidates[votes_per_candidate.index(winning_vote_count)]


print("Election Results")
print("-------------------------")
print(f"Total Votes: {votes_cast}")
print("-------------------------")
for i in range(len(unique_candidates)):
            print(f"{unique_candidates[i]}: {vote_percent[i]} % {votes_per_candidate[i]}")
print("-------------------------")
print(f"Winner: {winning_candidate}")
print("-------------------------")
 
election_results = os.path.join("analysis", "Election_results.txt")
with open(election_results, "w") as output_file:

    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {votes_cast}\n")
    output_file.write("-------------------------\n")
    for i in range(len(unique_candidates)):
            output_file.write(f"{unique_candidates[i]}: {vote_percent[i]} % {votes_per_candidate[i]}\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winning_candidate}\n")
    output_file.write("-------------------------\n")   
