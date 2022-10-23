# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given me the following tasks to complete the election audit of a recent local congressional election.

 1. Calculate the total number of votes cast.
 2. Get a complete list of candidates who received votes.
 3. Calculate the total number of votes each candidate received.
 4. Calculate the percentage of votes each candidate won.
 5. Determine the winner of the election based on popular vote.
 
 ## Resources
 * Data Source: election_results.csv
 * Software: Python 3.7.1, Visual Studio Code, 
 
 ## Summary
The analysis of the election shows that:
  * There were 369,711 votes cast in the election
  * The candidates were:
    * Charles Casper Stockham
    * Diana DeGette
    * Raymon Anthony Doane
    
The candidate results were:
    * Charles Casper Stockham received 23.0% of the vote with 85,213 votes
    * Diana DeGette received 73.8% of the vote with 272,892 votes
    * Raymon Anthony Doane received 3.1% of the vote with 11,606 votes
    
The winner of the election was Diana DeGette, who received 73.8% of the vote with 272,892 votes!

## Challenge Overview
The Election Board challenged me to repeat the previouse analysis with the Colorado counties instead of candidates. The specifications of the challenge were as follows:
1. Calculate the voter turnout for each county
2. Calculate the percentage of votes from each county out of the total count.
3. Calculate the county with the highest voter turnout. 

## Challenge Summary
By simply changing one line of code:

candidate_name = row[2]  >>>>>>>>> candidate_name = row[1]

I was able to quickly and easily calculate the voting statistics for each county. Of course, I changed the wording in my code, so that the word "candidate" was replaced with "county". The results are as follows:

* Jefferson County had 10.5% of voter turnout with 38,855 votes cast.
* Denver County had 82.8% of voter turnout with 306,055 votes cast.
* Arapahoe County had 6.7% of voter turnout with 24,801 votes cast.

* Denver County had the highest voter turnout with 306,055 votes or 82.8% of the total vote. 



