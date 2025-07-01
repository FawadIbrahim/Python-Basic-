# class book:
#     def __init__(self, title, author, publication_year):
#         self.title = title
#         self.author = author
#         self.publication_year = publication_year
#     def info(self):
#         print(f"Title: {self.title}, Author: {self.author}, Publication Year: {self.publication_year}")
# a=book("Romance","Jane Austen","1813")
# b=book("To Kill a Mockingbird"," Harper Lee","1960")
# a.info()
# b.info()



def recommend_books(user_genres):
  """Recommends books based on user's preferred genres."""

  books = [
      {"title": "GOT", "genre": "Fantasy"},
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
''
# Get user input
user_genres = input("Enter your preferred genres (separated by commas): ").split(",")

# Generate recommendations
recommended_books = recommend_books(user_genres)

# Print recommendations
print("Recommended books:")
for book in recommended_books:
  print("- " + book)