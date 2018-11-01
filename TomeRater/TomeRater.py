class User(object):
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.books = {}
        
  def get_email(self):
    return self.email

  def change_email(self, address):
    self.email = address
    print("Email updated to: {addr} for User {name}.".format(addr=self.email, name=self.name))

  def __repr__(self):
    return "User {name}, email: {addr}, books read:  {num}.".format(name=self.name, addr=self.email, num=len(self.books))

  def __eq__(self, other_user):
    if self.name == other_user.name and self.email == other_user.email:
      return True
    else:
      return False

  def read_book(self, book, rating="None"):
    self.books[book] = rating

  def get_average_rating(self):
    total = 0
    count = 0
    for book in self.books:
      if self.books[book] != "None":
        total += self.books[book]
        count += 1
    return total / count

#----end of class(User)------

class Book(object):
  def __init__(self, title, isbn):
    self.title = title
    self.isbn = isbn
    self.ratings = []

  def __repr__(self):
    return self.title

  def get_title(self):
    return self.title

  def get_isbn(self):
    return self.isbn

  def set_isbn(self, new_isbn):
    self.isbn = new_isbn
    print ("ISBN updated to: {isbn} for Book {title}.".format(isbn=self.isbn, title=self.title))

  def add_rating(self, rating):
    if rating != "None":
      if rating >= 0 and rating <= 4:
        self.ratings.append(rating)
      else:
        print("Invalid Rating")

  def __eq__(self, other_book):
    if self.title == other_book.title and self.isbn == other_book.isbn:
      return True
    else:
      return False

  def get_average_rating(self):
    if len(self.ratings) == 0:
      print("No ratings available for book {title}.".format(title=self.title))
      return 0
    total = 0
    for rating in self.ratings:
      total += rating
    return total / len(self.ratings)

  def __hash__(self):
    return hash((self.title, self.isbn))

#----end of class(Book)------

class Fiction(Book):
  def __init__(self, title, author, isbn):
    super().__init__(title, isbn)
    self.author = author

  def get_author(self):
    return self.author

  def __repr__(self):
    return "{title} by {author}".format(title=self.title, author=self.author)

#----end of class(Fiction)------

class Non_Fiction(Book):
  def __init__(self, title, subject, level, isbn):
    super().__init__(title, isbn)
    self.subject = subject
    self.level = level

  def get_subject(self):
    return self.subject

  def get_level(self):
    return self.level

  def __repr__(self):
    return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)

#----end of class(Non_Fiction)------

class TomeRater(object):
  def __init__(self):
    self.users = {}
    self.books = {}

  def __repr__(self):
    return "Tome Rater Project"

  def create_book(self, title, isbn):
    new_book = Book(title, isbn)
    self.books[new_book] = 0
    return new_book

  def create_novel(self, title, author, isbn):
    new_novel = Fiction(title, author, isbn)
    self.books[new_novel] = 0
    return new_novel

  def create_non_fiction(self, title, subject, level, isbn):
    new_non_fiction = Non_Fiction(title, subject, level, isbn)
    self.books[new_non_fiction] = 0
    return new_non_fiction

  def add_book_to_user(self, book, email, rating="None"):
    if email in self.users.keys():
      user = self.users[email]
      user.read_book(book, rating)
      book.add_rating(rating)
      if book in self.books:
        self.books[book] += 1
      else:
        self.books[book] = 1
    else:
      print("No user with email {email}!".format(email=email))

  def check_email(self, email):
    email_good = True
    if not "@" in email:
      email_good = False
    if email[-4:] not in [".com", ".edu", ".org"]:
      email_good = False
    return email_good

  def add_user(self, name, email, user_books="None"):
    if not self.check_email(email):
      print ("{email} is not a valid email address.".format(email=email))
      return
    if email not in self.users.keys():
      new_user = User(name, email)
      self.users[email] = new_user
      if user_books != "None":
        for book in user_books:
          self.add_book_to_user(book, email)
      print ("User {user} added.".format(user=name))
    else:
      print("User already exists with email {addr}.".format(addr=email))

  def print_catalog(self):
    for book in self.books:
      print(book)

  def print_users(self):
    for user in self.users:
      print(self.users[user])

  def most_read_book(self):
    max_value = 0
    for book in self.books:
      if self.books[book] > max_value:
        max_book = book
        max_value = self.books[book]
    return max_book

  def highest_rated_book(self):
    highest_rating = 0
    for book in self.books:
      if book.get_average_rating() > highest_rating:
        highest_rating = book.get_average_rating()
        highest_book = book
    return highest_book

  def most_positive_user(self):
    highest_rating = 0
    highest_user = ""
    for user in self.users:
      if self.users[user].get_average_rating() > highest_rating:
        highest_rating = self.users[user].get_average_rating()
        highest_user = self.users[user]
    return highest_user

