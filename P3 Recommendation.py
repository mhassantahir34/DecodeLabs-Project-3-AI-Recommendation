import pandas as pd

# ==========================================
# LOAD EXCEL DATASET
# ==========================================

file_name = "movies_dataset.xlsx"
data = pd.read_excel(file_name)

print("=" * 65)
print("             AI MOVIE RECOMMENDATION SYSTEM")
print("=" * 65)
print("\nDataset loaded successfully!")
print("\nDataset shape:")
print(data.shape)
print("\nFirst 5 movies:")
print(data.head())

# ==========================================
# CHECK DATASET
# ==========================================

print("\nDataset columns:")
print(list(data.columns))

print("\nMissing values:")
print(data.isnull().sum())

# ==========================================
# PREPARE GENRES
# ==========================================

data["Genre"] = data["Genre"].astype(str)
data["Genre"] = data["Genre"].apply(
    lambda x: [genre.strip() for genre in x.split("|")]
)

# ==========================================
# AVAILABLE GENRES
# ==========================================

all_genres = sorted(
    set(
        genre
        for genres in data["Genre"]
        for genre in genres
    )
)

print("\nAvailable Genres:")
print(", ".join(all_genres))

# ==========================================
# USER PREFERENCES
# ==========================================

print("\n" + "=" * 65)
print("             ENTER YOUR PREFERENCES")
print("=" * 65)

user_input = input(
    "\nEnter your favorite genres separated by commas: "
)
user_genres = [
    genre.strip().title()
    for genre in user_input.split(",")
    if genre.strip()
]

# ==========================================
# MINIMUM RATING
# ==========================================

while True:
    try:
        minimum_rating = float(
            input(
                "Enter your minimum rating (1-5): "
            )
        )
        if 1 <= minimum_rating <= 5:
            break

        print(
            "Please enter a rating between 1 and 5."
        )
    except ValueError:
        print(
            "Please enter a valid number."
        )

# ==========================================
# RECOMMENDATION LOGIC
# ==========================================

recommendations = []
selected_genres = set(user_genres)

for index, movie in data.iterrows():
    movie_genres = set(movie["Genre"])

    # Find matching genres
    matching_genres = (
        movie_genres.intersection(
            selected_genres
        )
    )

    # Calculate similarity score
    if len(selected_genres) > 0:
        similarity_score = (
            len(matching_genres)
            / len(selected_genres)
        ) * 100
    else:
        similarity_score = 0

    # Check rating
    rating_matches = (
        movie["Rating"] >= minimum_rating
    )

    # Add movie to recommendations
    if (
        similarity_score > 0
        and rating_matches
    ):
        recommendations.append({
            "Title": movie["Title"],
            "Genre": "|".join(
                movie["Genre"]
            ),
            "Rating": movie["Rating"],
            "Year": int(movie["Year"]),
            "Match Score": round(
                similarity_score,
                2
            ),
            "Matched Genres": ", ".join(
                sorted(matching_genres)
            )
        })

# ==========================================
# SORT RECOMMENDATIONS
# ==========================================

recommendations.sort(
    key=lambda movie: (
        movie["Match Score"],
        movie["Rating"]
    ),
    reverse=True
)

# ==========================================
# DISPLAY RESULTS
# ==========================================

print("\n" + "=" * 65)
print("                  RECOMMENDATIONS")
print("=" * 65)

if len(recommendations) == 0:
    print(
        "\nNo movies matched your preferences."
    )
    print(
        "Try different genres or lower "
        "your minimum rating."
    )
else:
    # Show top 10 recommendations
    top_movies = recommendations[:10]

    for number, movie in enumerate(
        top_movies,
        start=1
    ):
        print(
            f"\n{number}. {movie['Title']}"
        )
        print(
            f"   Genre: {movie['Genre']}"
        )
        print(
            f"   Rating: {movie['Rating']}/5"
        )
        print(
            f"   Year: {movie['Year']}"
        )
        print(
            f"   Match Score: "
            f"{movie['Match Score']}%"
        )
        print(
            f"   Matched Genres: "
            f"{movie['Matched Genres']}"
        )

# ==========================================
# SAVE RECOMMENDATIONS
# ==========================================

if len(recommendations) > 0:
    results = pd.DataFrame(
        recommendations
    )
    results.to_excel(
        "recommendations.xlsx",
        index=False
    )
    print(
        "\nRecommendations saved to "
        "'recommendations.xlsx'"
    )

# ==========================================
# FINAL SUMMARY
# ==========================================

print(
    "\nTotal matching movies:",
    len(recommendations)
)
print(
    "\nRecommendation process completed!"
)
print("=" * 65)