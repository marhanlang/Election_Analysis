# Election_Analysis
PyPoll analysis of election results
# Overview
  The purpose of this election audit is to determine the votes per county in addition to the votes per candidate. With this info we can find percentage of votes each county and candidate has and determine the county with the largest voting base and the winning candidate for the Election Board.
# Results
- Total amount of votes cast in the election: 369,711
- Vote breakdown by County:
  - Arapahoe recieved 24,801 votes which is 6.7% of the total votes.
  - Jefferson County recieved 38,855 votes which is 10.5% of the total votes.
  - Denver County recieved 306,055 votes which is 82.8% of the total votes.
- The county with the largest number of votes is Denver County.
- Vote breakdown by Candidate:
  - Raymon Anthony Doane recieved 11,606 votes which is 3.1% of the total votes.
  - Charles Casper Stockham recieved 85,213 votes which is 23.0% of the total votes.
  - Diana DeGette recieved 272,892 votes which is 73.8% of the total votes.
- The winning candidate is Diana DeGette with 272,892 votes or 73.8% of the total votes.
# Summary
  The code used for this analysis can be used for analysis of any election including larger-scale elections.  To use a different CSV file, all that has to be done is insure that the right file path is used to reference the new election data file. In the below portion of the code:
  ![File reference code portion](https://github.com/marhanlang/Election_Analysis/blob/main/Resources/Screenshot%20(7).png)

  In order for this code to be used on other databases that may include more information than given in this audit, additional code would need to be added to address and analyze this new info. For example, if info was provided on voter age demographic, the we could add code to sort votes by age groups to determine the age range with the largest number of voters.
