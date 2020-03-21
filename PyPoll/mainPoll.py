#load dependencies

import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

#read module
with open(csvpath) as csvfiles:
    csv_reader = csv.reader(csvfiles, delimiter =',')

    #header
    header_row = next(csv_reader, None)

    #Set variables
    vote = {}
    name = []

    for row in csv_reader:
        candidate = row[2]

        
#Thanks Maria for the helping with the total vote!!
        if candidate not in name:
            name.append(candidate)
            vote[candidate] = 1

        else:
            vote[candidate] = vote[candidate] + 1

    total_votes=sum(vote.values())
  

    # printing 

    print ("Election Results")
    print("--------------------------------------")
    print("Total Votes: " + str(total_votes))
    print("--------------------------------------")
    

    #votes per candidate
    for candidate in vote:
        percentage = ((vote[candidate]/total_votes)*100)
    

        print(str(candidate) + ": " + str(round(percentage, 3)) + "% (" + str(vote[candidate]) + ")")
    print("--------------------------------------")


    for winner in vote.keys():
        if vote[winner] == max(vote.values()):
                winning_candidate = winner
    
    print("--------------------------------------")
    print(" Winner: " + winning_candidate)