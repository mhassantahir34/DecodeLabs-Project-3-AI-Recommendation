# DecodeLabs Project 3 - AI Movie Recommendation System

An AI-based movie recommendation system developed using Python as part of my DecodeLabs AI Internship.

## Project Overview

This project implements a simple recommendation system that recommends movies based on the user's preferences.

The system takes the user's favorite genres and minimum preferred rating as input. It then compares these preferences with the movie dataset, calculates a similarity score, and displays the most relevant movies.

## Objectives

- Take user preferences as input
- Match user preferences with movie attributes
- Calculate similarity scores
- Filter movies according to the preferred rating
- Rank movies based on their match score
- Display the top movie recommendations
- Save recommendation results for further analysis

## Features

- User-friendly command-line interaction
- Genre-based movie recommendations
- Minimum rating preference
- Similarity/match score calculation
- Ranked recommendations
- Top 10 movie recommendations
- Excel-based dataset
- Automatic recommendation results export

## Dataset

The project uses a separate Excel dataset named:

`movies_dataset.xlsx`

The dataset contains **77 movies** with the following attributes:

| Column | Description |
|---|---|
| Title | Name of the movie |
| Genre | Movie genres |
| Rating | Movie rating from 1 to 5 |
| Year | Movie release year |

## Recommendation Logic

The recommendation process works in the following steps:

```text
User Preferences
       ↓
Read Movie Dataset
       ↓
Compare Genres
       ↓
Calculate Match Score
       ↓
Apply Minimum Rating
       ↓
Rank Recommendations
       ↓
Display Top 10 Movies
