def recommend_books(user_genres):
  """Recommends books based on user's preferred genres."""

  books = [
      {"title": "GOT", "Publish year": 2010, "genre": "Fantasy"},
      {"title": "Pride and Prejudice", "genre": "Romance"},
      {"title": "The Hitchhiker's Guide to the Galaxy", "genre": "Science Fiction"},
      {"title": "The Hitchhiker's Guide to the Galaxy", "genre": "Science Fiction"},
      # Add more books
      {"title": "The Hitchhiker's Guide to the Galaxy", "genre": "Science Fiction"},
      {"title": "The Hitchhiker's Guide to the Galaxy", "genre": "Science Fiction"},
  ]

  recommendations = []
  for book in books:
    if book["genre"] in user_genres:
      recommendations.append(book["title"])

  return recommendations

# Get user input
user_genres = input("Enter your preferred genres (separated by commas): ").split(",")

# Generate recommendations
recommended_books = recommend_books(user_genres)

# Print recommendations
print("Recommended books:")
for book in recommended_books:
  print("- " + book)


class Recommended :
   def recommend_books(self,authors,year,titles):
     self.author = authors
     self.published_year = year
     self.title = titles
   def detail(self):
      print(f"Title: {self.title}, Author: {self.author}, Published Year: {self.published_year}")
e1=Recommended
e1.recommend_books("H","Harry", "Harry poter",str(2010))
e1.detail()





def recomended():

    books=[
        {"Title": "Got", "Author" : "George R. R. Martin" , "Published": "2015", "Category" : "Fantacy"},
        {"Title" :"Pride and Prejudice", "Author" : "Jane Austen" ,"Published": "1813", "Category" : "Romance"},
        {"Title" :"The Hitchhiker's Guide to the Galaxy", "Author" : "Douglas Adams", "Published": "1979", "Category" : "Science Fiction"},
        {"Title": "To Kill a Mockingbird", "Author": "Harper Lee", "Published": "1960", "Category": "Classic"}

]
    recomendation=[]
    for book in books:
     if book["Category"] in ["Fantacy","Science Fiction"]:
        recomendation.append(book["Title","Author","Published","category"])
         
    return recomendation
books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction"},
    {"title": "1984", "author": "George Orwell", "genre": "Dystopian"},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance"},
    # Add more books as needed
]
def recommend_by_genre(genre):
    return [book for book in books if book["genre"].lower() == genre.lower()]
# def recommend_by_rating(min_rating):
#     return [book for book in books if book["rating"] >= min_rating]
# def recommend_by_author(author_name):
#     return [book for book in books if book["author"].lower() == author_name.lower()]
choice = input("How would you like to get recommendations? (genre/rating/author): ")

if choice == "genre":
    genre = input("Enter the genre: ")
    recommendations = recommend_by_genre(genre)
# elif choice == "rating":
#     rating = float(input("Enter the minimum rating: "))
#     recommendations = recommend_by_rating(rating)
# elif choice == "author":
#     author = input("Enter the author's name: ")
#     recommendations = recommend_by_author(author)
else:
    print("Invalid choice")
    recommendations = []

if recommendations:
    for book in recommendations:
        print(f"{book['title']} by {book['author']} (Rating: {book['rating']})")
else:
    print("No recommendations found.")

