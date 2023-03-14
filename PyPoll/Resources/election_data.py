import os

import csv

file_to_save = os.path.join("PyPoll\Resources", "election_analysis.txt")

csvpath = os.path.join("PyPoll\Resources", "election_data.csv")

# initiate variables
total_votes = 0
candidates_list = []
candidates_votes = {}
votes = []
percent_votes = 0

winner = ""
winner_votes = 0

#  open and read csv
with open(csvpath,encoding='utf') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #read header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    first_row = next(csvreader)   

    for row in csvreader:
        
        total_votes = total_votes + 1

        candidates = row[2]

        if candidates not in candidates_list:

            # add candidates name to the list
            candidates_list.append(candidates)
            # add votes per candidates to dict
            candidates_votes[candidates] = 0
            #add votes to corresponding candidates
        candidates_votes[candidates] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    

    for candidates in candidates_votes:
        # calculate percentage
        votes = candidates_votes[candidates]
        percent_votes = float(votes) / float(total_votes) * 100
        
        if (votes > winner_votes) :
            winner_votes = votes
            winner = candidates
        
        candidates_result = (f"{candidates}: {percent_votes:.1f}% ({votes:,})\n")
        print(candidates_result)    

        txt_file.write(candidates_result)

    winner = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n")
    print(winner)
         
    
    # Save the winning candidate's results to the text file.
    txt_file.write(winner)
      
        

    

