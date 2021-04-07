#import dependencies
import os
import csv

# Change to the current directory
os.chdir(os.path.dirname(__file__))


# set election_data_csv to the path for election_data.csv
election_data_csv = os.path.join("Resources","election_data.csv")

# Objective 3: Create the lists to store data. Initialize

count = 0
candidate_list = []
unique_candidates = []
votes_cast = 0
votes_cast_list = []
vote_percent = []
votes_per_candidate = 0
winner_list = []

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

        #count the number of times each candidate is in the list which will give us the total number of votes per candidate.
        Khan_votes = int(candidate_list.count("Khan"))
        Correy_votes = int(candidate_list.count("Correy"))
        Li_votes = int(candidate_list.count("Li"))
        O_Tooley_votes = int(candidate_list.count("O'Tooley"))

#get out of the with to perform our calculations.
Khan_percentage = (Khan_votes/votes_cast) * 100
Correy_percentage = (Correy_votes/votes_cast) * 100
Li_percentage = (Li_votes/votes_cast) * 100
O_Tooley_percentage = (O_Tooley_votes/votes_cast) * 100

winner_list.append(Khan_votes)
winner_list.append(Correy_votes)
winner_list.append(Li_votes)
winner_list.append(O_Tooley_votes)

#calculate the winner
winner = max(winner_list)


print("Election Results")
print("-------------------------")
print(f"Total Votes: {votes_cast}")
print("-------------------------")
print(f"Khan: {Khan_percentage}% ({Khan_votes})")
print(f"Correy: {Correy_percentage}% ({Correy_votes})")
print(f"Li: {Li_percentage}% ({Li_votes})")
print(f"O'Tooley: {O_Tooley_percentage}% ({O_Tooley_votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
 
election_results = os.path.join("analysis", "Election_results.txt")
with open(election_results, "w") as output_file:

    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {votes_cast}\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Khan: {Khan_percentage}% ({Khan_votes})\n")
    output_file.write(f"Correy: {Correy_percentage}% ({Correy_votes})\n")
    output_file.write(f"Li: {Li_percentage}% ({Li_votes})\n")
    output_file.write(f"O'Tooley: {O_Tooley_percentage}% ({O_Tooley_votes})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")   
