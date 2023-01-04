# import modules
import os
import csv

# path to csv file
csvpath = os.path.join("Resources","election_data.csv")

# create lists
candidate = []
candidate_list = []
vote_count = []
text_file = []

# read csv data 
with open (csvpath, encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    
# loop through to collect candidate data in a list
    for row in csvreader:
        candidate.append(row[2])
        

print()
print("Election Results")
print("-----------------------------------------------------------------")
print(f"Total Votes: {len(candidate):,}")
print()

text_file.append("Election Results")
text_file.append("-----------------------------------------------------------------")
text_file.append((f"Total Votes: {len(candidate):,}"))
text_file.append("")

# find the list of candidates and store in a list
for x in range(0, len(candidate)):
    if candidate[x] not in candidate_list:
        candidate_list.append(candidate[x])
        
print(f"Candidates receiving votes in the election were:")
text_file.append(f"Candidates receiving votes in the election were:")

for x in range(0,len(candidate_list)):
    print(candidate_list[x])
    text_file.append(candidate_list[x])

print("-----------------------------------------------------------------")
text_file.append("-----------------------------------------------------------------")


# find total and percentage of votes by each candidate
vote_high = 0

# loop through each candidate and total their votes from list [candidate]
for n in range(0,len(candidate_list)):
    for x in range(0, len(candidate)):
        if candidate[x] == candidate_list[n]:
            vote_count.append(candidate[x])
    vote_percent = len(vote_count)/len(candidate)*100
    
# store the highest percentage & candidate name
    if vote_percent > vote_high:
        vote_name = candidate_list[n]
        vote_high = vote_percent

# print results before looping to next candidate
    print(f"{candidate_list[n]} received {round(vote_percent,2)}% of the votes ({len(vote_count):,} votes)")
    text_file.append(f"{candidate_list[n]} received {round(vote_percent,2)}% of the votes ({len(vote_count):,} votes)")
    vote_count = []

# print winner information
print("-----------------------------------------------------------------")
print (f"{vote_name} is the winner with {round(vote_high,2)}% of the votes")
text_file.append("-----------------------------------------------------------------")
text_file.append(f"{vote_name} is the winner with {round(vote_high,2)}% of the votes")

# write election results to a text file
output_path = os.path.join("analysis","election_analysis.txt")

with open(output_path, 'w') as text:
    for line in text_file:
        text.write(line)
        text.write('\n')
        
