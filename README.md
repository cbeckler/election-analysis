# PyPoll with Python

## Overview of Project

### Purpose

The purpose of this analysis was to provide the client with an audit of election results to be provided to the election commission in Colorado following a Congressional District race. Automating this process will make certifying elections easier and more reliable. The analyst was asked to provide total votes cast in the election, a breakdown of votes cast by county in order to assess county turnout, and a breakdown of the percentage of votes recieved by each candidate, with a winner declared based on who recieved the greatest percentage of the votes.

### Results

* Total Votes Cast in Congressional Election: 369,711
* Vote Breakdown by County:

  ![Country Vote Breakdown](https://github.com/cbeckler/election-analysis/blob/main/Resources/county_votes.png)
* The county with the largest number of votes, and therefore the greatest turnout, is **Denver**, with 82.8% of all votes cast in the election (N = 306,055).
* Vote Breakdown by Candidate:

  ![Candidate Vote Breakdown](https://github.com/cbeckler/election-analysis/blob/main/Resources/candidate_votes.png)
 * The candidate **Diana DeGette** won the election, with 73.8% of the vote (N = 272,892)
 
 ### Method
 
The script used to generate the election results can be found [here](https://github.com/cbeckler/election-analysis/blob/main/PyPoll_Challenge.py). A list of counties was created by iterating over the data and adding the county name to an empty list (`county_list`) if the name value was not already present. One vote was then added to the overall count of votes for that county for every row in the data matching the name of the county in the list. An abbreviated version of the code to demostrate to programming logic below:

```
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:
    
      # Add to the total vote count
      total_votes = total_votes + 1
        
      #Extract the county name from each row.
      county_name = row[1]
      
      # check if county does not match any existing county in the county list.
       if county_name not in county_list:

            # Add the existing county to the list of counties.
            county_list.append(county_name)

            # Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # Then, add a vote to that county's vote count.
        county_votes[county_name] += 1
 ```
The same process was followed for candidate votes. As seen above, the total votes had already been calculated by simply adding one for every row before looping through county or candidate conditionals. To get county vote percentages, the number of votes for each county (stored in `county_votes`) was simply divided byt the total votes and then multipled by 100. The same process was followed for candidates. 

A summary of all results was then written to a text file for ease of viewing and distribution.

## Summary

Though this project was prototyped on a local Congressional election, the fundamentals of it can be scaled up to larger races. For example, this script could be used even on the biggest national election, the Presidential race. If county were to replaced with state, it would be possible to use this code to both call the winning Presidential candidate and track voter turnout by state. Given the discrepancies in voter access and election infrastructure, the ability to analyze turnout by state is of critical importance when deciding policy and allocating resources.

On the other hand, this project can also be scaled down, for elections that are no less critical, given their impacts on the daily lives of the people they affect. In a school board election held by a singular county, the county analysis here could be replaced by zip code, to determine which areas of the county are most and least engaged in local government educational decisions. Furthermore, an impersonal, automated way to call the results of elections in which all participants may know each other personally is likely desireable.

As shown by these examples, this script is a viable option for many different kinds of elections, given a little modification.      
      
