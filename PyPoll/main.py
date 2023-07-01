import os
import csv

# path to collect data from the resources folder
election_data = os.path.join('resources','election_data.csv')

#counter for total votes
total_votes = 0

#creating arrays for each candidate's total votes
charles_votes = []
diana_votes = []
raymon_votes = []

#read in csvfile
with open(election_data,'r') as csvfile:

    #split data on commas
    csvreader = csv.reader(csvfile,delimiter=',')

    #skip header
    header = next(csvreader)

    for row in csvreader:
        #counting total votes
        total_votes = total_votes + 1
        
        #counting votes for each candidate
        candidate = row[2]
        if candidate == 'Charles Casper Stockham':
            charles_votes.append(candidate)
        elif candidate == 'Diana DeGette':
            diana_votes.append(candidate)
        elif candidate == 'Raymon Anthony Doane':
            raymon_votes.append(candidate)
    
    #calculating the %'s
    charles_percentage = round((len(charles_votes) / total_votes),5) * 100
    diana_percentage = round((len(diana_votes) / total_votes),5) * 100
    raymon_percentage = round((len(raymon_votes) / total_votes),5) * 100

    #determining the winner of the popular vote
    popular_vote = max(charles_percentage,diana_percentage,raymon_percentage)

    if popular_vote == charles_percentage:
        winner = 'Charles Casper Stockham'
    elif popular_vote == diana_percentage:
        winner = 'Diana DeGette'
    elif popular_vote == raymon_percentage:
        winner = 'Anthony Doane'


        
#print out message

print("Election Results")

print("------------------------")

print(f"Total Votes: {total_votes}")

print("------------------------")

print(f"Charles Casper Stockham: {charles_percentage}% ({len(charles_votes)})")

print(f"Diana Degette: {diana_percentage}% ({len(diana_votes)}) ")

print(f"Raymon Anthony Doane: {raymon_percentage}% ({len(raymon_votes)})")

print(f"Winner: {winner}")

print("------------------------")
      






      



