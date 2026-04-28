import random

# Song database based on mood
songs = {
    "happy": [
        "Happy - Pharrell Williams",
        "Kala Chashma - Badshah",
        "Uptown Funk - Bruno Mars",
        "Gallan Goodiyan - Dil Dhadakne Do"
    ],
    "sad": [
        "Channa Mereya - Arijit Singh",
        "Someone Like You - Adele",
        "Tadap Tadap - Hum Dil De Chuke Sanam",
        "Let Her Go - Passenger"
    ],
    "angry": [
        "Believer - Imagine Dragons",
        "Zinda - Bhaag Milkha Bhaag",
        "Lose Yourself - Eminem",
        "Kar Har Maidaan Fateh - Sanju"
    ]
}

# User input
mood = input("Enter your mood (happy/sad/angry): ").lower()

# Check mood and show songs
if mood in songs:
    print("\n🎧 Suggested Songs:")
    for song in songs[mood]:
        print("- " + song)

    print("\n⭐ Recommended Song:")
    print(random.choice(songs[mood]))
else:
    print("❌ Mood not found! Please try again.")

# Program end hone se pehle rukega
input("\nPress Enter to exit...")