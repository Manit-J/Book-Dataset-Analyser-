# Team Identifier - T006
#Written By:
#Nolan Kisser 101222376
#Manit Jawa 101215842
#Ishtiaque Khan 101227487
#Balkaran Karir 101229843


# Version 1.0, 12 April 2022

# We are using the whole dataset so no csv file is attached in our submission.
#imports
from T006_P5_load_data import book_category_dictionary

#The eight functions from P2 – Task 1

#Nolan Kisser 101222376
def add_book(book_dictionary:dict,book:tuple)->dict:
    """Adds a book to a dictionary and returns the dictionary with that book
    inside the dictionary.
    
    >>> add_book(dictionary,("Title of Book","Author of Book","A random Language","Well known publisher","Random Category",6.0,900))
    The book has been added correctly
    >>> add_book(dictionary,("Title of Book", "Author of Book", "English", "Publisher of Book", "Comics",9.7,342))
    The book has been added correctly
    """
    (title,author,language,publisher,category,rating,pages) = book
    if category in book_dictionary.keys():
        book_dictionary[category] += [{"title": title,
                     "author": author,
                     "language": language,
                     "rating": rating,
                     "publisher": publisher,
                     "pages": pages
                     },] 
         
    
   
        final_dictionary = dict(book_dictionary)
        lst_of_category = final_dictionary.pop(category)
        
        tot = 0
        for i in range(len(lst_of_category)):
            if lst_of_category[i]['title'] == str(title):
                tot += 1
            
        if tot > 0:
            print("The book has been added correctly")
        else:
            print("There was an error adding the book")
                
    if category not in book_dictionary.keys():
        book_dictionary[category] = [{"title": title,
                     "author": author,
                     "language": language,
                     "rating": rating,
                     "publisher": publisher,
                     "pages": pages
                     },]         
        
        temp_dictionary = dict(book_dictionary)
        lst_of_categories = temp_dictionary.pop(category)
        
        tot = 0
        for i in range(len(lst_of_categories)):
            if lst_of_categories[i]['title'] == title:
                tot = 1
            
        if tot == 1:
            print("The book has been added correctly.\n")
        else:
            print("There was an error adding the book.\n")        
        
    return book_dictionary
    



def remove_book(book_dictionary:dict, title:str, category:str):
    """Removes a book from the dictionary based off the title and 
    category of that book. If the book has more than one category, only book under 
    the category selected will be removed from the dicitonary.
    
    >>> remove_book(dictionary,"Antiques Roadkill: A Trash 'n' Treasures Mystery","Fiction")
    The book has been removed correctly
    >>> remove_book(dictionary,"Not a title in the dictionary","Fiction")
    There was an error removing the book. Book not found.
    >>> remove_book(dictionary,"Antiques Roadkill: A Trash 'n' Treasures Mystery","Not a category in dicitonary")
    There was an error removing the book. Book not found.
    """
    if category in book_dictionary.keys():
        
        lst_of_categories = book_dictionary.pop(category)
        tot = 0
        for i in range(len(lst_of_categories)-1):
            if lst_of_categories[i]['title'] == title:
                del lst_of_categories[i] 
            tot += 1
            
        if tot >= len(lst_of_categories):
            print("The book has been removed correctly.")
        else:
            print("There was an error removing the book. Book not found.")
        book_dictionary[category] = lst_of_categories
    
    else:
        print("There was an error removing the book. Book not found.")
        
    return book_dictionary


# Author and Student Number: Manit Jawa 101215842
# Function definitions for Functions 3 and 4 of P2 Task 1
def get_books_by_category(book_dictionary: dict, category: str) -> int:
    """
    Returns the number of books in a category, given as a string argument(category), in the collection of books 
    ,given as a dictionary argument(book_dictionary)
    PRE-CONDITIONS: The category given as an argument must exist in the collection of books. 
    
    >>> get_books_by_category({'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544}, {another element} ....], 'Comics': [...] , ....}, "Comics")
    >>> The category Comics has 7 books. This is the list of books:
    Book 1: Deadpool Kills the Marvel Universe by Cullen Bunn
    Book 2: Young Justice Vol. 1 by Art Baltazar
    Book 3: Ultimate Spider-Man Vol. 11: Carnage by Brian Michael Bendis
    Book 4: Immortal Hulk Vol. 1: Or Is He Both? by Al Ewing
    Book 5: Watchmen (2019 Edition) by Alan Moore
    Book 6: The Joker by Brian Azzarello
    Book 7: Venomized by Cullen Bunn
    7 
    
    >>> get_books_by_category({'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544}, {another element} ....], 'Comics': [...] , ....}, "Biography")
    >>> The category Biography has 5 books. This is the list of books:
    Book 1: Boy Erased: A Memoir by Garrard Conley
    Book 2: No One Is Too Small to Make a Difference by Greta Thunberg
    Book 3: Tall Tales and Wee Stories: The Best of Billy Connolly by Billy Connolly
    Book 4: Permanent Record by Edward Snowden
    Book 5: Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader by Brent Schlender
    5
    
    >>> get_books_by_category({'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544}, {another element} ....], 'Comics': [...] , ....}, "Epic")
    >>> The category Epic has 4 books. This is the list of books:
    Book 1: A Feast for Crows (A Song of Ice and Fire. Book 4) by George R.R. Martin
    Book 2: The Tower of the Swallow: Witcher 6 by Andrzej Sapkowski
    Book 3: A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire) by George R.R. Martin
    Book 4: The Way Of Shadows: Book 1 of the Night Angel by Brent Weeks
    4
    """
    books_in_category = book_dictionary[category] 
    unique_books = []
    output_string_list = []
    count = 0 
    for j in books_in_category:
        title = j['title']
        author = j['author']
        book = [title, author]
        if book not in unique_books:
            unique_books += [book]
    for k in unique_books:
        count += 1
        output_string = ["Book " + str(count) + ": " + k[0] + " by " + k[1]]
        output_string_list += output_string
    print("The category " + category + " has " + str(count) + " books. This is the list of books:")
    for t in output_string_list:
        print(t)
        
    return count 
        

def get_books_by_rate(book_dictionary: dict, rate: int) -> int:
    """
    Return the number of books in the collection of books given as a dictionary argument(book_dictionary), 
    whose rating is greater than or equal to given integer argument (rate) and less than (rate+1)
    PRE-CONDITIONS: The rate must be a positive integer from 0 to 4, both inclusive. A rate of 5 cannot be 
    passed since a rating of greater than 5 does not exist. 
    
    >>> get_books_by_rate({'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544}, {another element} ....], 'Comics': [...] , ....}, 3)
    There are 8 books whose rate is between 3 and 4. This is the list of books:
    Book 1: Antiques Roadkill: A Trash 'n' Treasures Mystery by Barbara Allan
    Book 2: Bring Me Back by B A Paris
    Book 3: How to Understand Business Finance: Edition 2 by Bob Cinnamon
    Book 4: The Infinite Game by Simon Sinek
    Book 5: Mrs. Pollifax Unveiled by Dorothy Gilman
    Book 6: The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further by Alvin Hall
    Book 7: Selling 101: What Every Successful Sales Professional Needs to Know by Zig Ziglar
    Book 8: Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything by Steven D. Levitt
    
    >>> get_books_by_rate({'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544}, {another element} ....], 'Comics': [...] , ....}, 1)
    There are 0 books whose rate is betwen 1 and 2. This is the list of books:
    0
    
    >>> get_books_by_rate({'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544}, {another element} ....], 'Comics': [...] , ....}, 4)
    There are 67 books whose rate is between 4 and 5. This is the list of books:
    Book 1: The Painted Man (The Demon Cycle. Book 1) by Peter V. Brett
    Book 2: Edgedancer: From the Stormlight Archive by Brandon Sanderson
    ...
    ...
    Book 67: Happy: Why More or Less Everything is Absolutely Fine by Derren Brown
    67
    """
    all_books = []
    unique_books = []
    output_string_list = []
    count = 0
    for i in book_dictionary:
        all_books += book_dictionary[i]
    for j in all_books:
        if j['rating']!="N/A":
            if j['rating'] >= rate and j['rating'] < (rate+1):
                book = [j['title'] , j['author']]
                if book not in unique_books:
                    unique_books += [book]
    for k in unique_books:
        count += 1
        output_string = ["Book " + str(count) + ": " + k[0] + " by " + k[1]]
        output_string_list += output_string       
        
    print("There are " + str(count) + " books whose rate is between " + str(rate) + " and " + str(rate+1) + ". This is the list of books:")
    for t in output_string_list:
        print(t)
    
    return count 

#Ishtiaque Khan 101227487

#function 5
def get_books_by_title(books_dict: dict, book_title: str) -> bool:
    """
    Returns whether or not a book title was found in a given collection
    
    >>>get_books_by_title("Total Control", booklist)
    The book has been found 
    True
    >>>get_books_by_title("Mrs. Pollifax Unveiled", booklist)
    The book has been found 
    True
    >>>get_books_by_title("egg", booklist)
    The book has not been found 
    False
    """
    for category in books_dict:
        book_list = books_dict[category]
        
        for book in book_list:
            
            if book['title'] == book_title:
                print("The book has been found")
                return True
            
    print("The book has not been found")
    return False

#function 6
def get_books_by_author(books_dict: dict, author: str) -> list:
    """Returns a list of book titles from a given author
    >>>get_books_by_author("Peter  V. Brett",booklist)
    The author"Peter V. Brett"has published the following books:
      1- The Painted Man (The Demon Cycle. Book 1)
    ['The Painted Man (The Demon Cycle. Book 1)']

    >>>get_books_by_author("John Grisham",booklist)
    The author"John Grisham"has published the following books:
        1- The Guardians: The explosive new thriller from international bestseller John Grisham
    ['The Guardians: The explosive new thriller from international bestseller John Grisham']

    >>>get_books_by_author("egg",booklist)
    The author"egg"has published the following books:
    []
    """
    lst = []
    count = 0
    
    print('The author"' + author + '"has published the following books:')
    for category in books_dict:
        book_list = books_dict[category]
        for book in book_list:
            if book['author'] == author:
                if book['title'] not in lst:
                    print("  "+str(count+1)+"-",book['title'])
                    
                    lst.append(book['title'])
                    count += 1
    return len(lst)

# Balkaran Karir, 101229843
# Function 7 Definition 

def get_books_by_publisher(pub_name:str,dictionary:dict)->int:
    """
    This function takes the book_category_dictionary from lab 1 and a 
    publisher's name from which it returns the books published by that
    publisher and their authors. 
    
    >>> get_books_by_publisher('Kensington Publishing Corp.', dictionary)
    The publisher Kensington Publishing Corp. has published the following books:
    Book 1: Antiques Roadkill: A Trash 'n' Treasures Mystery by Barbara Allan
    Book 2: Antiques Knock-Off by Barbara Allan
    
    >>> get_books_by_publisher('Harper Collins', dictionary)
    The publisher Harper Collins has published the following books:
    Book 1: Little Girl Lost: A Lucy Black Thriller by Brian McGilloway
    Book 2: Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth by T. Harv Eker
    Book 3: Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything by Steven D. Levitt
    Book 4: Think Like a Freak: The Authors of Freakonomics Offer to Retrain Your Brain by Steven D. Levitt
    
    >>> get_books_by_publisher('DC', dictionary)
    The publisher DC has published the following books:
    Book 1: Young Justice Vol. 1 by Art Baltazar
    Book 2: The Joker by Brian Azzarello
    
    >>> get_books_by_publisher('D', dictionary)
    Sorry that publisher is not in this dataset or maybe check your spelling.
    """
    final_string = 'The publisher ' + pub_name + ' has published the following books:'
    book_count=1
    book_dictionary={}
    for category_keys in dictionary:
        for book_info in dictionary.get(category_keys):
            for key in book_info:
                if key == 'publisher' and book_info.get(key) == pub_name:
                    if book_info.get('title') not in book_dictionary:
                        book_dictionary[book_info.get('title')]= book_info.get('author')
    if len(book_dictionary) == 0:
        print('Sorry that publisher is not in this dataset or maybe check your spelling.') 
    else:
        for title in book_dictionary.keys():
            final_string += '\nBook ' + str(book_count) + ': ' + title + ' by ' + book_dictionary.get(title)
            book_count += 1
    print(final_string)
    return book_count - 1

# Function 8 Definition 

def get_all_categories_for_book_title(book_title:str,dictionary:dict)->int:
    """
    This function takes the book_category_dictionary from lab 1 and a 
    book title from which it returns the categories that book belongs to.
    
    >>> get_all_categories_for_book_title('Antiques Knock-Off',dictionary)
    The book title Antiques Knock-Off belongs to the following categories:
    Category 1: Fiction
    Category 2: Detective
    Category 3: Mystery
    
    >>> get_all_categories_for_book_title("Antiques Roadkill: A Trash 'n' Treasures Mystery",dictionary)
    The book title Antiques Roadkill: A Trash 'n' Treasures Mystery belongs to the following categories:
    Category 1: Fiction
    Category 2: Detective
    Category 3: Mystery
    
    >>> get_all_categories_for_book_title('The Joker',dictionary)
    The book title The Joker belongs to the following categories:
    Category 1: Comics
    
    >>> get_all_categories_for_book_title('The Joke',dictionary)
    Sorry that book is not in this dataset or maybe check your spelling.
    """
    final_string = 'The book title ' + book_title + ' belongs to the following categories:'
    category_list = []
    category_count = 1
    for p in dictionary:
        for i in dictionary.get(p):
            for j in i:
                if j == 'title' and i.get(j) == book_title:
                    category_list += [p]
    if len(category_list) == 0:
        print('Sorry that book is not in this dataset or maybe check your spelling.')
    else:
        for i in category_list:
            final_string += '\nCategory ' + str(category_count) + ': ' + i
            category_count += 1
    print(final_string)
    return category_count - 1 




#The test functions you developed for automated testing

# Balkaran Karir, 101229843
# Function Definition for Unit Testing

def testing_function(description: str, expected, outcome) -> int:
    """
    This function returns the integer 1 if the test passes and the integer
    0 if the test fails. A statement is also printed to indiciate whether
    the test has passed or failed.
    
    The function's code is used from the unit_testing file provided in the unit 
    testing lecture. It takes the string description of the function being 
    tested, the expected value and the actual value the function produces. It 
    then states whether this test has failed or passed.
    """
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:
        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '), 
                      outcome, str(outcome_type).strip('<class> ')))
        return 0
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
        return 0
    else:
        print("{0} PASSED".format(description))
        return 1
    print("------")

#Main script with automated testing. The main script should only run if the
#module is executed. It should not run when the module is imported. The main
#script should print the total number of tests that pass and fail.
if __name__ == "__main__":
    book_dictionary = book_category_dictionary("google_books_dataset.csv")
    
    # Bakaran Karir, 101229843
    
    # Function Tests
    
    # Main Script
    
    # --------------Tests for Function 1 -> add_book---------------
    
    function_1_dictionary = {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288}],'Fantasy': [{'title': "Percy Jackson & the Olympians: The Lightning Thief", 'author': 'Rick Riordan', 'language': 'English', 'rating': 4.3, 'publisher': 'Miramax Books', 'pages': 379},{'title': "Percy Jackson & the Olympians: The Battle of the Labyrinth", 'author': 'Rick Riordan', 'language': 'English', 'rating': 4.4, 'publisher': 'Miramax Books','pages': 361}]}
    
    tally_p1 = 0
    tally_f1 = 0
    
    test_result = testing_function("add_book(book_category_dictionary,(category_dictionary,('Percy Jackson: Sea of Monsters','Rick Riordan','English','Miramax Books','Fantasy',4.2,279))",{'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288}],'Fantasy': [{'title': "Percy Jackson & the Olympians: The Lightning Thief", 'author': 'Rick Riordan', 'language': 'English', 'rating': 4.3, 'publisher': 'Miramax Books', 'pages': 379},{'title': "Percy Jackson & the Olympians: The Battle of the Labyrinth", 'author': 'Rick Riordan', 'language': 'English', 'rating': 4.4, 'publisher': 'Miramax Books','pages': 361},{'title': "Percy Jackson: Sea of Monsters", 'author': 'Rick Riordan', 'language': 'English', 'rating': 4.2, 'publisher': 'Miramax Books', 'pages': 279}]}, add_book(function_1_dictionary,('Percy Jackson: Sea of Monsters','Rick Riordan','English','Miramax Books','Fantasy',4.2,279)))
    if test_result == 1:
        tally_p1 += 1
    elif test_result == 0:
        tally_f1 += 1
    
    test_result = testing_function("add_book(book_category_dictionary,(category_dictionary,('Percy Jackson & the Olympians: The Titan's Curse','Rick Riordan','English','Miramax Books','Fantasy',4.6,317))",{'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288}], 'Fantasy': [{'title': 'Percy Jackson & the Olympians: The Lightning Thief', 'author': 'Rick Riordan', 'language': 'English', 'rating': 4.3, 'publisher': 'Miramax Books', 'pages': 379}, {'title': 'Percy Jackson & the Olympians: The Battle of the Labyrinth', 'author': 'Rick Riordan', 'language': 'English', 'rating': 4.4, 'publisher': 'Miramax Books', 'pages': 361}, {'title': 'Percy Jackson: Sea of Monsters', 'author': 'Rick Riordan', 'language': 'English', 'rating': 4.2, 'publisher': 'Miramax Books', 'pages': 279}, {'title': "Percy Jackson & the Olympians: The Titan's Curse", 'author': 'Rick Riordan', 'language': 'English', 'rating': 4.6, 'publisher': 'Miramax Books', 'pages': 317}]}, add_book(function_1_dictionary,("Percy Jackson & the Olympians: The Titan's Curse",'Rick Riordan','English','Miramax Books','Fantasy',4.6,317)))
    if test_result == 1:
        tally_p1 += 1
    elif test_result == 0:
        tally_f1 += 1
    
    test_result = testing_function("add_book(book_category_dictionary,(category_dictionary,('From the Ashes','Jesse Thistle','English','Simon & Schuster Canada','Biography',4.5,384))",{'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288}], 'Fantasy': [{'title': 'Percy Jackson & the Olympians: The Lightning Thief', 'author': 'Rick Riordan', 'language': 'English', 'rating': 4.3, 'publisher': 'Miramax Books', 'pages': 379}, {'title': 'Percy Jackson & the Olympians: The Battle of the Labyrinth', 'author': 'Rick Riordan', 'language': 'English', 'rating': 4.4, 'publisher': 'Miramax Books', 'pages': 361}, {'title': 'Percy Jackson: Sea of Monsters', 'author': 'Rick Riordan', 'language': 'English', 'rating': 4.2, 'publisher': 'Miramax Books', 'pages': 279}, {'title': "Percy Jackson & the Olympians: The Titan's Curse", 'author': 'Rick Riordan', 'language': 'English', 'rating': 4.6, 'publisher': 'Miramax Books', 'pages': 317}], 'Biography': [{'title': 'From the Ashes', 'author': 'Jesse Thistle', 'language': 'English', 'rating': 4.5, 'publisher': 'Simon & Schuster Canada', 'pages': 384}]}, add_book(function_1_dictionary,("From the Ashes",'Jesse Thistle','English','Simon & Schuster Canada','Biography',4.5,384)))
    if test_result == 1:
        tally_p1 += 1
    elif test_result == 0:
        tally_f1 += 1
    
    print(tally_p1, "tests passed for Function 1")
    print(tally_f1, "tests failed for Function 1")
    
    # ------------Tests for Function 2 -> remove_book-------------
    
    function_2_dictionary = {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288},{'title': "Antiques Con", 'author': 'Barbara Allan', 'language': 'English', 'rating': 4.8, 'publisher': 'Kensington Books', 'pages': 288}],'Fantasy': [{'title': "Percy Jackson & the Olympians: The Lightning Thief", 'author': 'Rick Riordan', 'language': 'English', 'rating': 4.3, 'publisher': 'Miramax Books', 'pages': 379},{'title': "Percy Jackson & the Olympians: The Battle of the Labyrinth", 'author': 'Rick Riordan', 'language': 'English', 'rating': 4.4, 'publisher': 'Miramax Books','pages': 361}]}
        
    tally_p2 = 0
    tally_f2 = 0
    
    test_result = testing_function("remove_book(book_category_dictionary,(category_dictionary,'Percy Jackson & the Olympians: The Lightning Thief','Fantasy')",{'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288}, {'title': 'Antiques Con', 'author': 'Barbara Allan', 'language': 'English', 'rating': 4.8, 'publisher': 'Kensington Books', 'pages': 288}], 'Fantasy': [{'title': 'Percy Jackson & the Olympians: The Battle of the Labyrinth', 'author': 'Rick Riordan', 'language': 'English', 'rating': 4.4, 'publisher': 'Miramax Books', 'pages': 361}]}, remove_book(function_2_dictionary,'Percy Jackson & the Olympians: The Lightning Thief','Fantasy'))
    if test_result == 1:
        tally_p2 += 1
    elif test_result == 0:
        tally_f2 += 1
    
    test_result = testing_function("remove_book(book_category_dictionary,(category_dictionary,'Percy Jackson & the Olympians: The Lightning Thief','Fantasy')",{'Fantasy': [{'title': 'Percy Jackson & the Olympians: The Battle of the Labyrinth', 'author': 'Rick Riordan', 'language': 'English', 'rating': 4.4, 'publisher': 'Miramax Books', 'pages': 361}], 'Fiction': [{'title': 'Antiques Con', 'author': 'Barbara Allan', 'language': 'English', 'rating': 4.8, 'publisher': 'Kensington Books', 'pages': 288}]}, remove_book(function_2_dictionary,"Antiques Roadkill: A Trash 'n' Treasures Mystery",'Fiction'))
    if test_result == 1:
        tally_p2 += 1
    elif test_result == 0:
        tally_f2 += 1
    
    test_result = testing_function("remove_book(book_category_dictionary,(category_dictionary,'Percy Jackson & the Olympians: The Lightning Thief','Fantasy')",{'Fantasy': [{'title': 'Percy Jackson & the Olympians: The Battle of the Labyrinth', 'author': 'Rick Riordan', 'language': 'English', 'rating': 4.4, 'publisher': 'Miramax Books', 'pages': 361}], 'Fiction': [{'title': 'Antiques Con', 'author': 'Barbara Allan', 'language': 'English', 'rating': 4.8, 'publisher': 'Kensington Books', 'pages': 288}]}, remove_book(function_2_dictionary,"Antiques Roadkill: A Trash 'n' Treasures Mystery",'a typo'))
    if test_result == 1:
            tally_p2 += 1
    elif test_result == 0:
        tally_f2 += 1
    
    test_result = testing_function("remove_book(book_category_dictionary,(category_dictionary,'Percy Jackson & the Olympians: The Lightning Thief','Fantasy')",{'Fantasy': [{'title': 'Percy Jackson & the Olympians: The Battle of the Labyrinth', 'author': 'Rick Riordan', 'language': 'English', 'rating': 4.4, 'publisher': 'Miramax Books', 'pages': 361}], 'Fiction': [{'title': 'Antiques Con', 'author': 'Barbara Allan', 'language': 'English', 'rating': 4.8, 'publisher': 'Kensington Books', 'pages': 288}]}, remove_book(function_2_dictionary,"a typo or a book that's not in the list",'Fiction'))
    if test_result == 1:
        tally_p2 += 1
    elif test_result == 0:
        tally_f2 += 1
    
    print(tally_p2, "tests passed for Function 2")
    print(tally_f2, "tests failed for Function 2")
    
    
    
    total_test = 0
    test_pass = 0
    
    #------------- Testing for get_books_by_category -------------
    total_test = 0
    test_pass = 0
    
    #Testing for a Pass
    outcome = get_books_by_category(book_dictionary,"Fiction")
    description = 'get_books_by_category(book_dictionary, "Fiction")'
    expected = 39 
    test = testing_function(description, outcome, expected)
    total_test +=1
    test_pass += testing_function("test 1" , outcome, expected)
    
    #Testing for a Fail
    outcome = get_books_by_category(book_dictionary,"Fantasy")
    description = 'get_books_by_category(book_dictionary, "Fantasy")'
    expected = 15 
    test = testing_function(description, outcome, expected)
    total_test += 1
    test_pass += testing_function("test 2", outcome, expected) 
    
    #Testing for a Fail by type
    outcome = get_books_by_category(book_dictionary,"Comics")
    description = 'get_books_by_category(book_dictionary, "Comics")'
    expected = 7 
    test = testing_function(description, outcome, expected)
    total_test += 1
    test_pass += testing_function("test 3", outcome, expected)
    
    print(str(total_test) + " total tests for function 3.")
    print(str(test_pass) +" tests passed for function 3.")
    test_fails = total_test - test_pass
    print(str(test_fails) + " tests failed for function 3.")
    
    #------------- Testing for get_books_by_rate -------------
    total_test = 0
    test_pass = 0
    #Testing for a Pass
    outcome = get_books_by_rate(book_dictionary,5)
    description = 'get_books_by_category(book_dictionary, 5)'
    expected = 5 
    test = testing_function(description, outcome, expected)
    total_test +=1
    test_pass += testing_function("test 1" , outcome, expected)
    
    #Testing for a Fail
    outcome = get_books_by_rate(book_dictionary,7)
    description = 'get_books_by_category(book_dictionary, 7)'
    expected = 0 
    test = testing_function(description, outcome, expected)
    total_test += 1
    test_pass += testing_function("test 2", outcome, expected) 
    
    #Testing for a Fail by type
    outcome = get_books_by_rate(book_dictionary,3.4)
    description = 'get_books_by_category(book_dictionary, 3.4)'
    expected = 37
    test = testing_function(description, outcome, expected)
    total_test += 1
    test_pass += testing_function("test 3", outcome, expected)
    
    # Tests for function get_books_by_title
    tests_passed = 0
    tests_failed = 0
    
    actual = get_books_by_title(book_dictionary, "After Anna")
    expected = True
    test = testing_function("Test 1", actual, expected)
    if test == 1:
        tests_passed += 1
    else:
        tests_failed += 1
        
    actual = get_books_by_title(book_dictionary, "A Man Called Ove")
    expected = False
    test = testing_function("Test 2", actual, expected)
    if test == 1:
        tests_passed += 1
    else:
        tests_failed += 1
        
    actual = get_books_by_title(book_dictionary, "Bring Me Back")
    expected = True 
    test = testing_function("Test 3" , actual, expected)
    if test == 1:
        tests_passed += 1
    else:
        tests_failed += 1
    
    print(tests_passed, "tests passed for Function get_books_by_title")
    print(tests_failed, "tests failed for Function get_books_by_title")
    
    # Tests for function get_books_by_author
    
    
    tests_passed = 0
    tests_failed = 0
    
    actual = get_books_by_author(book_dictionary, "Barbara Allan")
    expected = 4
    test = testing_function("Test 1", actual, expected)
    if test == 1:
        tests_passed += 1
    else:
        tests_failed += 1
        
    actual = get_books_by_author(book_dictionary, "Brandon Sanderson")
    expected = 2
    test = testing_function("Test 2", actual, expected)
    if test == 1:
        tests_passed += 1
    else:
        tests_failed += 1
        
    actual = get_books_by_author(book_dictionary, "Andrzej Sapkowski")
    expected = 3
    test = testing_function("Test 3", actual, expected)
    if test == 1:
        tests_passed += 1
    else:
        tests_failed += 1
        
    print(tests_passed, "tests passed for Function get_books_by_author")
    print(tests_failed, "tests failed for Function get_books_by_author")
    
    
    #function 7
        
    passed_test = 0
    failed_test = 0 
    
    
    
    result = testing_function("Testing get_books_by_publisher('Kensington Publishing Corp.', books)",2, get_books_by_publisher('Kensington Publishing Corp.', book_dictionary))
    if (result ==1):
        passed_test += 1
    else:
        failed_test +=1
    
    result = testing_function("Testing get_books_by_publisher('Harper Collins', books)",4, get_books_by_publisher('Harper Collins', book_dictionary))
    if (result ==1):
        passed_test += 1
    else:
        failed_test +=1
    
        
    result = testing_function("Testing get_books_by_publisher('DC', books)", 2, get_books_by_publisher('DC', book_dictionary))
    if (result ==1):
        passed_test += 1
    else:
        failed_test +=1
    
    
    result = testing_function("get_books_by_publisher('D', books)",0, get_books_by_publisher('D', book_dictionary))
    if (result ==1):
        passed_test += 1
    else:
        failed_test +=1
    
    
    print("Amount of tests passed for function 7", passed_test)
    print("Amount of tests failed for function 7", failed_test)
    
    
    
    #function 8
    passed_test = 0
    failed_test = 0 
    
    result = testing_function("Testing get_all_categories_for_book_title('Antiques Knock-Off',books)",3, get_all_categories_for_book_title('Antiques Knock-Off', book_dictionary))
    if (result ==1):
        passed_test += 1
    else:
        failed_test +=1
    
    result = testing_function("Testing get_all_categories_for_book_title('Antiques Roadkill: A Trash 'n' Treasures Mystery', books)",3,get_all_categories_for_book_title("Antiques Roadkill: A Trash 'n' Treasures Mystery",book_dictionary))
    if (result ==1):
        passed_test += 1
    else:
        failed_test +=1
    
    result = testing_function("Testing get_all_categories_for_book_title('The Joker',books)",1,get_all_categories_for_book_title('The Joker', book_dictionary))
    if (result ==1):
        passed_test += 1
    else:
        failed_test +=1
    
    result = testing_function("Testing get_all_categories_for_book_title('The Joker',books)",0,get_all_categories_for_book_title('The Joke', book_dictionary))
    if (result ==1):
        passed_test += 1
    else:
        failed_test +=1
        
    print("Amount of tests passed for function 8", passed_test)
    print("Amount of tests failed for function 8", failed_test)