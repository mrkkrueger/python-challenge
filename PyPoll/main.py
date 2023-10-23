import pandas as pd
from pathlib import Path

election_data=Path("PyPoll/Resources/election_data.csv")
election_data_df=pd.read_csv(election_data)

#calculate total votes cast
total_votes=len(election_data_df.index)

#determine candidates who received votes
candidates=election_data_df["Candidate"].unique()
print(candidates)

#calculate number of votes received by Stockham and the percentage of votes recieved rounded to three decimal places
stockham_df=election_data_df.loc[election_data_df["Candidate"]=="Charles Casper Stockham",["Candidate","Ballot ID","County"]]
stockham_votes=len(stockham_df)
stockham_votes_percent=stockham_votes/total_votes*100
stockham_votes_percent=round(stockham_votes_percent,3)

#calculate number of votes received by DeGette and the percentage of votes recieved rounded to three decimal places
degette_df=election_data_df.loc[election_data_df["Candidate"]=="Diana DeGette",["Candidate","Ballot ID","County"]]
degette_votes=len(degette_df)
degette_votes_percent=degette_votes/total_votes*100
degette_votes_percent=round(degette_votes_percent,3)

#calculate number of votes received by Doane and the percentage of votes recieved rounded to three decimal places
doane_df=election_data_df.loc[election_data_df["Candidate"]=="Raymon Anthony Doane",["Candidate","Ballot ID","County"]]
doane_votes=len(doane_df)
doane_votes_percent=doane_votes/total_votes*100
doane_votes_percent=round(doane_votes_percent,3)

#calculate who had the most votes
if stockham_votes>max(degette_votes,doane_votes):
    winner="Winner: Charles Casper Stockham"
elif degette_votes>max(stockham_votes,doane_votes):
    winner="Winner: Diana DeGette"
elif doane_votes>max(stockham_votes,degette_votes):
    winner="Winner: Raymon Anthony Doane"

#printing analysis in terminal
print("Election Results")
print("-------------------------")
print("Total Votes: ",total_votes)
print("-------------------------")
print("Charles Casper Stockham: ",stockham_votes_percent,"% (", stockham_votes,")")
print("Diana DeGette: ",degette_votes_percent,"% (", degette_votes,")")
print("Raymon Anthony Doane: ",doane_votes_percent,"% (", doane_votes,")")
print("-------------------------")
print(winner)
print("-------------------------")

#exporting analysis to text file
import sys
with open('PyPoll/analysis/Election_Data.txt','w') as file:
    sys.stdout=file
    print("Election Results")
    print("-------------------------")
    print("Total Votes: ",total_votes)
    print("-------------------------")
    print("Charles Casper Stockham: ",stockham_votes_percent,"% (", stockham_votes,")")
    print("Diana DeGette: ",degette_votes_percent,"% (", degette_votes,")")
    print("Raymon Anthony Doane: ",doane_votes_percent,"% (", doane_votes,")")
    print("-------------------------")
    print(winner)
    print("-------------------------")
