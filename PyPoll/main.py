# import modules
import os
import csv

# path to csv file
csvpath = os.path.join("Resources","election_data.csv")

# create lists
candidate = []
candidate_list = []
vote_count = []

# read csv data 
with open (csvpath, encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    
# loop through to collect candidate data in a list
    for row in csvreader:
        candidate.append(row[2])
        
print("Election Results")
print(f"Total Votes: {len(candidate):,}")

# find the list of candidates and store in a list
for x in range(0, len(candidate)):
    if candidate[x] not in candidate_list:
        candidate_list.append(candidate[x])
        
print(f"Candidates reciving votes in the election were:")
for x in range(0,len(candidate_list)):
    print(candidate_list[x])