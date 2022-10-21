# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv

import os


file_to_load = 'C:/Users/chris/Desktop/Election_Analysis/Resources/election_results.csv'

file_to_save = 'C:/Users/chris/Desktop/Election_Analysis/election_analysis.txt'

total_votes = 0

candidate_options = []

candidate_votes = {}

# Winning Candidate and Winning Count Tracker

winning_candidate = ""

winning_count = 0

winning_percentage = 0


with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    print(headers)

    for row in file_reader:

        total_votes +=1

        candidate_name = row[2]

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            candidate_votes[candidate_name]  = 0

        candidate_votes[candidate_name] += 1

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

# Determine the percentage of votes for each candidate by looping through the counts
# 1. Iterate through the candidate list.

    for candidate_name in candidate_votes:

        # 2. Retrieve vote count of a candidate.

        votes = candidate_votes[candidate_name]

        #3. Calculate the percentage of votes.

        vote_percentage = float(votes) / float(total_votes) * 100

        #4. Print the candidate name and percentage of votes.

        print(f"{candidate_name}: received {round(vote_percentage,1)} of the vote.")


        #Determine the winning vote count and candidate

        #Determine if the votes is greater than the winning count

        if (votes > winning_count) and (vote_percentage > winning_percentage):

            winning_count = votes

            winning_percentage = vote_percentage

            winning_candidate = candidate_name

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        txt_file.write(candidate_results)

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)



    



