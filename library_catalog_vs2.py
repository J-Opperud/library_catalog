"""
Library Catalog Version 2

Added:
- Book comparison with ==
- Book sorting with sorted()
- Page count support with len()
- Title searching with "keyword in book"
"""

class Book:
    """Represents a library book"""

    def __init__(self, title, author, year, pages):
        if not isinstance(year, int) or year <= 0:
            raise ValueError (f"Year must be valid ex. 2000  {year}")
        # A.I. suggested isinstance() for scope *see foot note
        self.title = title 
        self.author = author
        self.year = year
        self.checked_out = False # book starts as not checked
        self.pages = pages

    def __eq__(self, other):#comparing  by author and title
        """compared by author"""
        return self.title == other.title and self.author == other.author # needs to be equal to return 
    
    def __lt__(self, other):#alphabetical sorting
        """Sorting alphabetically"""
        return self.title < other.title
    
    def __len__(self):
        """Page lenght"""
        return self.pages
    
    def __contains__(self, keyword):
        """Title search"""
        
        return keyword.lower() in self.title.lower()
    
    

      

    
    
    def check_out(self):
         """Checking out a book"""
         self.checked_out = True

    def return_book(self):
        """Returning book"""
        self.checked_out = False

    
    
    
    def __repr__(self):
        """Displays the status of a book"""
        status = "Checked Out" if self.checked_out else "Available"
        return f"[{status}] {self.title} By {self.author}"


    
class EBook(Book):
    """Represents an electronic book that inherits from the Book class."""
    


    def __init__(self, title, author, year, pages, file_size_mb):
        """Initialize an EBook object"""
        super().__init__(title, author, year, pages)
        # Calls the parent Book constructor to initialize title, author, and year
        self.file_size_mb = file_size_mb
        # add the new parameters to define self.
        self.count = 0 #Empty counter 
       
    def check_out(self):
        """Increase the checkout count for the EBook."""
    # updates the counter   
        self.count += 1 

    def __repr__(self):
        """Return a string representation of the EBook object"""
        return f"EBook('{self.title}', '{self.author}', '{self.year}', {self.file_size_mb}MB )"
    

class Catalog:
    """Stores and manages a collection of books."""


    def __init__(self):
        """Manages a catalog"""
        self.books = []#initempty list
    
    def add_book(self, book):
        """Adding books object to the list"""
        self.books.append(book)
        return self.books

    def search_by_author(self, author):
        """Author look up """
        results = []
        
        
        for book in self.books:
        
            if book.author.lower() == author.lower():
                results.append(book)
        
        return results
        
    def search_by_title(self, keyword):
        """Search by keyword"""
        results = []
        for book in self.books:
            if keyword.lower() in book.title.lower():
                results.append(book)
        
        return results 
    
                
    def get_available(self):
        """Pull request for available books"""
        return [book for book in self.books if isinstance(book,EBook) or not book.checked_out]
        
    def summary(self):
        """Print a summary of the catalog."""
        print("Catalog Summary")
        print(f"Total books: {len(self.books)}")
        print(f"Available books: {len(self.get_available())}")
        print(f"Checked out books: {len(self.books) - len(self.get_available())}")
        print("\nBooks:")
        for book in self.books: # varifies inheritance works
            print(book)

#AI helped me tweak the test code (Not my work) I wanted to see the output of the new dunder's
# not included in the challenge.
catalog = Catalog()

catalog.add_book(Book("Python Crash Course", "Eric Matthes", 2019, 544))
catalog.add_book(Book("Clean Code", "Robert Martin", 2008, 464))
catalog.add_book(EBook("AI Engineering", "Chip Huyen", 2025, 350, 15.2))

# Search
results = catalog.search_by_title("python")
print(results)  # Should find "Python Crash Course"

# Check out
catalog.books[0].check_out()
available = catalog.get_available()
print(f"Available: {len(available)} books")

catalog.summary()

# Demonstrate dunder methods
print("\nDunder Method Tests")

# __eq__
book1 = Book("Clean Code", "Robert Martin", 2008, 464)
book2 = Book("Clean Code", "Robert Martin", 2020, 500)
print(book1 == book2)  # True

# __len__
print(len(book1))  # 464

# __contains__
print("clean" in book1)   # True
print("python" in book1)  # False

# __lt__ with sorted()
books = [
    Book("Python Crash Course", "Eric Matthes", 2019, 544),
    Book("Clean Code", "Robert Martin", 2008, 464),
    Book("Automate the Boring Stuff", "Al Sweigart", 2015, 504)
]

print("\nSorted Books:")
for book in sorted(books):
    print(book)
