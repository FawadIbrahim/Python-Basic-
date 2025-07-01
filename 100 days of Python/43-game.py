import random
def check(comp,user): 
    if comp==user:
        return 0
    if (comp==0)and(user==2):
        return -1
    if (comp==1)and(user==0):
        return -1
    if (comp==2)and(user==1):
        return -1
    return 1
comp=random.randint(0,2)

user=int(input("Enter 0 for Gun Enter 1 for water and Enter 2 for Snake:\n"))
score=check(comp,user)
print("You:",user)
print("Computer:",comp)
if score==1:
    print("You win")
elif score==0:
    print("It's a draw")
else :
    print("You lose")
print("The game is over")











books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": "1960", "genre": "Fiction"},
    {"title": "1984", "author": "George Orwell", "year": "1949", "genre": "Dystopian"},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "year": "1813", "genre": "Romance"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": "1925", "genre": "Fiction"},
    {"title": "Moby Dick", "author": "Herman Melville", "year": "1851", "genre": "Fiction"},
]

def recommend_genre(genre):
    return [book for book in books if book["genre"].lower() == genre.lower()]

def recommend_author(author_name):
    return [book for book in books if book["author"].lower() == author_name.lower()]

def recommend_year(year):
    return [book for book in books if book["year"].lower() == year.lower()]

choice = input("How would you like to get recommendations? (genre/author/year): ").strip().lower()

if choice == "genre":
    genre = input("Enter the genre: ").strip()
    recommendations = recommend_genre(genre)

elif choice == "author":
    author = input("Enter the author's name: ").strip()
    recommendations = recommend_author(author)
    
elif choice == "year":
    year = input("Enter the publish year: ").strip()
    recommendations = recommend_year(year)
    
else:
    print("Invalid choice.")
    recommendations = []

if recommendations:
    for book in recommendations:
        print(f"{book['title']} by {book['author']} and published in {book['year']}.")
else:
    print("No recommendations found.")
