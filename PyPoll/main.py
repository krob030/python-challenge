{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import glob\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [],
   "source": [
    "csv_path= \"C:/Users/karsa_000/Desktop/election_data.csv\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [],
   "source": [
    "election_pd= pd.read_csv(csv_path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [],
   "source": [
    "election_pd.columns = [\"Voter ID\", \"County\", \"Candidate\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [],
   "source": [
    "TotVote= election_pd[\"Voter ID\"].count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Khan        2218231\n",
      "Correy       704200\n",
      "Li           492940\n",
      "O'Tooley     105630\n",
      "Name: Candidate, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "tr= (election_pd[\"Candidate\"]).value_counts()\n",
    "print(tr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Khan        63.0\n",
      "Correy      20.0\n",
      "Li          14.0\n",
      "O'Tooley     3.0\n",
      "Name: Candidate, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "pct= (election_pd[\"Candidate\"]).value_counts(normalize=True).round(2)*100\n",
    "print(pct)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          Candidate  Candidate\n",
      "Khan           63.0    2218231\n",
      "Correy         20.0     704200\n",
      "Li             14.0     492940\n",
      "O'Tooley        3.0     105630\n"
     ]
    }
   ],
   "source": [
    "j= pd.concat(([pct,tr]), axis=1)\n",
    "print(j)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "----------------------------\n",
      "Total Votes: 3521001\n",
      "----------------------------\n",
      "          Candidate  Candidate\n",
      "Khan           63.0    2218231\n",
      "Correy         20.0     704200\n",
      "Li             14.0     492940\n",
      "O'Tooley        3.0     105630\n",
      "----------------------------\n",
      "Winner: Khan\n",
      "----------------------------\n"
     ]
    }
   ],
   "source": [
    "title= (\"Election Results\")\n",
    "spaces= (\"----------------------------\")\n",
    "print(title)\n",
    "print(spaces)\n",
    "print(\"Total Votes: \" + str(TotVote))\n",
    "print(spaces)\n",
    "print(j)\n",
    "print(spaces)\n",
    "print(\"Winner: Khan\")\n",
    "print(spaces)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [],
   "source": [
    "title= (\"Election Results\")\n",
    "spaces= (\"----------------------------\")\n",
    "text_file = open(\"Output.txt\", \"w\")\n",
    "text_file.write(title+'\\n')\n",
    "text_file.write(spaces+'\\n')\n",
    "text_file.write(\"Total Votes: \" + str(TotVote)+'\\n')\n",
    "text_file.write(spaces+'\\n')\n",
    "text_file.write(str(j)+'\\n')\n",
    "text_file.write(spaces+'\\n')\n",
    "text_file.write(\"Winner: Khan\"+'\\n')\n",
    "text_file.write(spaces+'\\n')\n",
    "text_file.close()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
