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
votes_cast_list =[]


# Open the election data csv
with open(election_data_csv, newline="\n") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #skip headers
    next(csv_reader)

    for row in csv_reader:
        
        #unique_candidates = [row[2] for row[2] in csv_reader if row[2] not in unique_candidates]
        #count the total number of votes cast
        votes_cast += 1
        
        #store the candidate names to the candidate_list
        candidate_list.append(row[2])
        votes_cast_list.append(row[0])

    #claculate the total votesfor each candidate
Khan = int(candidate_list.count("Khan"))
Correy = int(candidate_list.count("Correy"))
Li = int(candidate_list.count("Li"))
O_Tooley = int(candidate_list.count("O'Tooley"))
   
   #calculate the percent of votes for each candidate and round to 3 decimals
Khan_percent = round(float((Khan/votes_cast) * 100),3)
Correy_percent = round(float((Correy/votes_cast) * 100),3)
Li_percent = round(float((Li/votes_cast) * 100),3)
O_Tooley_percent = round(float((O_Tooley/votes_cast) * 100),3)

#if statement to find out the winner 
if Khan > Correy > Li  > O_Tooley:
       winner = "Khan"
elif O_Tooley > Khan  > Correy > Li:
       winner = "O'Tooley"
elif Correy > Khan > Li > O_Tooley:
       winner = "Correy"
elif Li > Khan > Correy > O_Tooley:
       winner = "Li"
   
#print results to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {votes_cast}")
print("-------------------------")
print(f"Khan: {Khan_percent}% ({Khan})")
print(f"Correy: {Correy_percent}% ({Correy})")
print(f"Li: {Li_percent}% ({Li})")
print(f"O'Tooley: {O_Tooley_percent}% ({O_Tooley})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#write the results to a text file
election_results = os.path.join("analysis", "Election_results.txt")
with open(election_results, "w") as output_file:

    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {votes_cast}\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Khan: {Khan_percent}% ({Khan})\n")
    output_file.write(f"Correy: {Correy_percent}% ({Correy})\n")
    output_file.write(f"Li: {Li_percent}% ({Li})\n")
    output_file.write(f"O'Tooley: {O_Tooley_percent}% ({O_Tooley})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")