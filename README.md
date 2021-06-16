# PyBank and PyPoll Analysis


## PyBank


The [PyBank Python Script](./PyBank/main.py) contains the code for analyzing the financial records of a company from the [Budget Data CSV](./PyBank/budget_data.csv) which contains two columns: Date and Profit/Losses. The Python script above analyzes the CSV and calculate each of the following:

* The total number of months included in the dataset

* The net total amount of "Profit/Losses" over the entire period

* Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

* The greatest increase in profits (date and amount) over the entire period

* The greatest decrease in losses (date and amount) over the entire period


## PyPoll

The [PyPoll Python Script](./PyPoll/main.py) contains the code to automate a vote counting process based on the results in the [Election Result Data CSV](./PyPoll/election_data.csv). This dataset is composed of three columns: Voter ID, County, and Candidate. The Python script will analyze the votes and calculates each of the following:

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote.
