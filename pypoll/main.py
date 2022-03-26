#import and open csv file
from operator import indexOf
import os
import csv
from collections import Counter

csvpath = os.path.join('Resources', 'election_data.csv')

#Set variables
votes = []
candidates = []

with open(csvpath) as csvfile:  

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    # print(header)

    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[2])

# Find total number of votes cast in election
totalvotes = len(votes)
print(totalvotes)  

#List of candidates who received votes 
# and number of votes per candidate
eligible_candidate = {}
percent_vote = 0

for name in candidates:
       
    if name in eligible_candidate:
        eligible_candidate[name] += 1
    else:
        eligible_candidate[name] = 1
 
# print(eligible_candidate) 

#Percentage of votes won per candidate
for name in eligible_candidate:
    candidate_vote = eligible_candidate[name]
    percent_vote = float(candidate_vote) / float(totalvotes) * 100
    election_results = (f"{name}: {percent_vote:.1f}% ({candidate_vote:,})\n")
       
    print(election_results)


highest_vote = max(eligible_candidate.values())
lst=[i for i in eligible_candidate.keys() if eligible_candidate[i]==highest_vote]
print(sorted(lst)[0])
