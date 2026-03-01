# ---------------------
# Cleaning and joining data for March Madness 2026 
# Last updated: 02/28/26
# Notes: 
# ---------------------

# Import libraries 
import pandas as pd
import numpy as np
import math 
import datetime as dt 

# ---------------------
# Preparing the mens data
# ---------------------

# Load in all mens datasets 
MTeams = pd.read_csv("/Users/mollymccann/Downloads/MarchMadness/Data/Mens/MTeans.csv")
MTeamsSpellings = pd.read_csv("/Users/mollymccann/Downloads/MarchMadness/Data/Mens/MTeamsSpellings.csv")
MTeamConferences = pd.read_csv("/Users/mollymccann/Downloads/MarchMadness/Data/Mens/MTeamConferences.csv")
MTeamCoaches = pd.read_csv("/Users/mollymccann/Downloads/MarchMadness/Data/Mens/MTeamCoaches.csv")
MSeasons = pd.read_csv("/Users/mollymccann/Downloads/MarchMadness/Data/Mens/MSeasons.csv")
MRegularSeasonDetailedResults = pd.read_csv("/Users/mollymccann/Downloads/MarchMadness/Data/Mens/MRegularSeasonDetailedResults.csv")
MRegularSeasonCompactResults = pd.read_csv("/Users/mollymccann/Downloads/MarchMadness/Data/Mens/MRegularSeasonCompactResults.csv")
MGameCities = pd.read_csv("/Users/mollymccann/Downloads/MarchMadness/Data/Mens/MGameCities.csv")
MMasseyOrdinals = pd.read_csv("/Users/mollymccann/Downloads/MarchMadness/Data/Mens/MMasseyOrdinals.csv")
MConferenceTourneyGames = pd.read_csv("/Users/mollymccann/Downloads/MarchMadness/Data/Mens/MConferenceTourneyGames.csv")
MNCAATourneySeeds = pd.read_csv("/Users/mollymccann/Downloads/MarchMadness/Data/Mens/MNCAATourneySeeds.csv")
MNCAATourneySlots = pd.read_csv("/Users/mollymccann/Downloads/MarchMadness/Data/Mens/MNCAATourneySlots.csv")
MNCAATourneyRoundSlots = pd.read_csv("/Users/mollymccann/Downloads/MarchMadness/Data/Mens/MNCAATourneyRoundSlots.csv")
MSecondaryTourneyTeams = pd.read_csv("/Users/mollymccann/Downloads/MarchMadness/Data/Mens/MSecondaryTourneyTeams.csv")
MSecondaryTourneyCompactReults = pd.read_csv("/Users/mollymccann/Downloads/MarchMadness/Data/Mens/MSecondaryTourneyCompactResults.csv")
MNCAATourneyDetailedResults = pd.read_csv("/Users/mollymccann/Downloads/MarchMadness/Data/Mens/MNCAATourneyDetailedResults.csv")
MNCAAToruneyCompactResults = pd.read_csv("/Users/mollymccann/Downloads/MarchMadness/Data/Mens/MNCAATourneyCompactResults.csv")

# ----------------------
# Make a key column with date and team names
# ----------------------



# ---------------------
# Preparing the womens data
# ---------------------

# Load in all womens datasets
