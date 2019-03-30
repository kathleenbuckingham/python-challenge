## Dependencies
import os
#import os
import csv

os.chdir("PyPoll")

with open("PyPoll.CSV", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
    rows = []
    candidate_votercount = []
    candidatelist = []
    votercount = 0
    print("----------------")
    print("Election Results")
    print("-------------------")
    
    for x in csvreader:
       votercount = votercount + 1
       candidatelist.append(x[2])
       if x[2] not in rows:
           rows.append(x[2])
    print(f"Total Votes: {votercount}")
    print("---------------------")
    print("Candidate, Percentage of Votes, Number of Votes:")
    print("---------------------")
    for j in range(len(rows)):
       #candidatelist.count(rows[j])
       print(f"{(rows[j])} {(round((candidatelist.count(rows[j]))/(votercount)*100))} % ({candidatelist.count(rows[j])})")
print("--------------------")
print("The Winner is Khan")
print("--------------------")
       
