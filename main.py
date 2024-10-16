from library import Library
from book import Book
from member import Member

def main():
    library = Library()

    # Adding books
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    library.add_book(book1)
    library.add_book(book2)

    # Adding members
    member1 = Member("Alice", 1)
    member2 = Member("Bob", 2)
    library.add_member(member1)
    library.add_member(member2)

    # Display books and members
    print("Books in the library:")
    library.display_books()
    print("\nLibrary members:")
    library.display_members()

if __name__ == "__main__":
    main()
