# import pandas as pd


# books=pd.read_csv('dataset.csv')


#def recommend_genre(genre):
    #return [book for book in books if book["genre"].lower() == genre.lower()]
#def recommend_author(author_name):
    #return [book for book in books if book["author"].lower() == author_name.lower()]
#def recommend_year(years):
    #return [book for book in books if book["year"].lower() == years.lower()]
# def recommend_genre(genre):
#     return books[books['genre'].str.lower() == genre.lower()]

# # Recommendation by author
# def recommend_author(author_name):
#     return books[books['author'].str.lower() == author_name.lower()]

# # Recommendation by year
# def recommend_year(year):
#     return books[books['year'].astype(str) == str(year)]

# choice = input("How would you like to get recommendations? (genre/author/year): ")

# if choice == "genre":
#     genre = input("Enter the genre: ")
#     recommendations = recommend_genre(genre)

# elif choice == "author":
#     author = input("Enter the author's name: ")
#     recommendations = recommend_author(author)
# elif choice == "year":
#     year = input("Enter the Publish year: ")
#     recommendations = recommend_year(year)
# else:
#     print("Invalid choice")
#     recommendations = []

# if recommendations:
#     for book in recommendations:
#         print(f"{book['title']} by {book['author']} and Published in {book['year']}.")
# else:
#     print("No recommendations found.")





# import pandas as pd

# # Load your dataset
# books = pd.read_csv('dataset.csv')


# books.columns

# # Recommendation by genre
# def recommend_genre(genre):
#     return books[books['genre'].str.lower() == genre.lower()]

# # Recommendation by author
# def recommend_author(author_name):
#     return books[books['author'].str.lower() == author_name.lower()]

# # Recommendation by year
# def recommend_year(year):
#     return books[books['year'].astype(str) == str(year)]

# # User input
# choice = input("How would you like to get recommendations? (genre/author/year): ").lower()

# if choice == "genre":
#     genre = input("Enter the genre: ")
#     recommendations = recommend_genre(genre)

# elif choice == "author":
#     author = input("Enter the author's name: ")
#     recommendations = recommend_author(author)

# elif choice == "year":
#     year = input("Enter the publish year: ")
#     recommendations = recommend_year(year)

# else:
#     print("Invalid choice")
#     recommendations = pd.DataFrame()

# # Print results
# if not recommendations.empty:
#     for _, book in recommendations.iterrows():
#         print(f"{book['title']} by {book['author']} (Published in {book['year']})")
# else:
#     print("No recommendations found.")


import pandas as pd



# Load dataset
df = pd.read_csv('dataset.csv')

# Keep only required columns
df = df[['id', 'title', 'genre']]


# Drop rows with missing values in required columns
df.dropna(subset=['id', 'title', 'genre'], inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

def recommend_by_genre(genre):
    # Filter the DataFrame by genre (case-insensitive)
    genre_movies = df[df['genre'].str.lower() == genre.lower()]
    
    if genre_movies.empty:
        print("No movies found for this genre.")
    else:
        print(f"Movies in genre '{genre}':")
        for index, row in genre_movies.iterrows():
            print(f"🎬 {row['title']} (ID: {row['id']})")
# Ask user for genre input
user_genre = input("Enter a movie genre to get recommendations: ")
# Call the function
recommend_by_genre(user_genre)
