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
MTeams = pd.read_csv("data/MTeans.csv")
MTeamsSpellings = pd.read_csv("data/MTeamsSpellings.csv")
MTeamConferences = pd.read_csv("data//MTeamConferences.csv")
MTeamCoaches = pd.read_csv("data//MTeamCoaches.csv")
MSeasons = pd.read_csv("data//MSeasons.csv")
MRegularSeasonDetailedResults = pd.read_csv("data//MRegularSeasonDetailedResults.csv")
MRegularSeasonCompactResults = pd.read_csv("data//MRegularSeasonCompactResults.csv")
MGameCities = pd.read_csv("data/MGameCities.csv")
MMasseyOrdinals = pd.read_csv("data/MMasseyOrdinals.csv")
MConferenceTourneyGames = pd.read_csv("data/MConferenceTourneyGames.csv")
MNCAATourneySeeds = pd.read_csv("data/MNCAATourneySeeds.csv")
MNCAATourneySlots = pd.read_csv("data/MNCAATourneySlots.csv")
MNCAATourneyRoundSlots = pd.read_csv("data/MNCAATourneyRoundSlots.csv")
MSecondaryTourneyTeams = pd.read_csv("data/MSecondaryTourneyTeams.csv")
MSecondaryTourneyCompactReults = pd.read_csv("data/MSecondaryTourneyCompactResults.csv")
MNCAATourneyDetailedResults = pd.read_csv("data/MNCAATourneyDetailedResults.csv")
MNCAAToruneyCompactResults = pd.read_csv("data/MNCAATourneyCompactResults.csv")

# ----------------------
# Make a key column with date and team names
# ----------------------



# ---------------------
# Preparing the womens data
# ---------------------

# Load in all womens datasets
