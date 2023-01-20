# Team Identifier - T006
#Written By:
#Nolan Kisser 101222376
#Manit Jawa 101215842
#Ishtiaque Khan 101227487
#Balkaran Karir 101229843

# Version 1.0, 12 April 2022

from T006_P5_load_data import book_category_dictionary
from T006_P2_add_remove_search_dataset import add_book, remove_book, get_books_by_category, get_books_by_rate, get_books_by_title, get_books_by_author, get_books_by_publisher, get_all_categories_for_book_title
from T006_P3_sorting_fun import sort_books_title, sort_books_publisher, sort_books_author, sort_books_ascending_rate

# To see each individual case working, the corresponding function is called.  

def display_UI() -> str:
    """
    Author and Student Number: Manit Jawa 101215842
    """
    
    print("The available commands are:")
    print("   1- L)oad data")
    print("   2- A)dd book")
    print("   3- R)emove book")
    print("   4- G)et books")
    print("        T)itle R)ate A)uthor P)ublisher C)ategory")
    print("   5- GCT) Get all Categories for book Title")
    print("   6- S)ort books")
    print("        T)itle R)ate P)ublisher A)uthor")
    print("   7- Q)uit")
    print()
    
    command = input("Please type your command: ")
    
    return command.upper()


def case1()-> None:
    """
    Nolan Kisser 101222376
    """
    count = 0
    inpt = display_UI()
    while inpt != 'Q': 
        if count != 0:
            inpt = display_UI()
        while inpt != 'L' and inpt != 'A'  and inpt != 'R' and inpt != 'G' and inpt != 'GCT' and inpt != 'S' and inpt != 'Q':
            print("No such command")
            inpt = display_UI()
        while inpt != 'Q':
            if inpt == 'L':
                file = input("Enter the file to be loaded: ")
                book_dict = book_category_dictionary(file)
                print("---------- File Loaded ---------")
                while inpt == 'L':
                    inpt2 = display_UI()
                    if inpt2 == 'Q':
                        return
                    if inpt2 == 'A':
                        title = input("Enter the title of the book you want to add: ")
                        author = input("Enter the author of the book you want to add: ")
                        language = input("Enter the language of the book you want to add: ")
                        publisher = input("Enter the publisher of the book you want to add: ")
                        category = input("Enter the category of the book you want to add: ")
                        rating = float(input("Enter the rating as a float value of the book you want to add: "))
                        pages = int(input("Enter the number pages of the book you want to add as an integer value: "))
                        book = (title,author,language,publisher,category,rating,pages)

                        while type(book) != tuple or len(book) != 7:
                            book = input("Error adding book.")
                            title = input("Enter the title of the book you want to add: ")
                            author = input("Enter the author of the book you want to add: ")
                            language = input("Enter the language of the book you want to add: ")
                            publisher = input("Enter the publisher of the book you want to add: ")
                            category = input("Enter the category of the book you want to add: ")
                            rating = float(input("Enter the rating as a float value of the book you want to add: "))
                            pages = int(input("Enter the number pages of the book you want to add as an integer value: "))                               
                            book = (title,author,language,publisher,category,rating,pages)
                            
                        book_dict = add_book(book_dict,book)
                            
                    elif inpt2 == 'R':
                        title = input("Enter the title of the book you want to remove: ")
                        category = input("Enter the category of the book you want to remove: ")
                        book_dict = remove_book(book_dict,title,category)
                    else:
                        print("Command not Found")
            else:
                print("-------File not loaded-------- ")
                inpt = display_UI()                        
        count += 1            
                  
    return



def case2():
    """
    Author and Student Number: Manit Jawa 101215842
    Case 2: A team member will work on commands get books by title, rate, and author.
    """
    counter = 1
    dataset = {}
    while counter == 1:
        command = display_UI()
        if command == "L":
            file_name = input("Enter the file name: ")
            dataset = book_category_dictionary(file_name)
            print(dataset)
            
        elif command == "G":
            if dataset == {}:
                print("No file loaded")
            else:
                next_command = input("Enter how you want get books - by title, rate or author ? ")
                
                if next_command.upper() == "T":
                    title = input("Enter the title: ")
                    result = get_books_by_title(dataset, title) 
                    print(result)
                    
                elif next_command.upper() == "R":
                    rate = int(input("Enter the rate (a positive integer only): "))
                    result = get_books_by_rate(dataset, rate)
                    print(result)
                    
                elif next_command.upper() == "A":
                    author = input("Enter the author: ")
                    result = get_books_by_author(dataset, author)
                    print(result)

                    
                
        elif command == "Q":
            print(command)
            counter = 0
        
        else:
            print("No such command")
    
    return None
        
    


def case3() -> None:
    """
    Ishtiaque Khan 101227487
    
    This program uses inputs and commands to get certain books for the user depending on which command is typed 
    in the input which is provided to the user.
    """    
    books_dataset = book_category_dictionary("google_books_dataset.csv")
    
    command = display_UI()
    
    if command == "G":
        
        subcommand_input = input("Please provide a sub-command: ")
        subcommand_input = subcommand_input.upper()   
        
        if subcommand_input == "C":
                category_input = input("Please provide the category you wish to find books for: ")
                get_books_by_category(books_dataset, category_input)
                
        elif subcommand_input == "P":
                publisher_input = input("Please provide the name of the publisher you wish to find books for: ")
                get_books_by_publisher(publisher_input, books_dataset)
        
        else:
                print("That was not a valid command.")
                
    elif command == "GCT":
            title_input = input("Please provide the title of the book you wish look for: ")
            get_all_categories_for_book_title(title_input, books_dataset)    
    else:
        print("That was not a valid command. ")
        

def case4() -> None:
    """
    Code for Sort Books Command - Balkaran Karir
    """
    command = display_UI()
    data_file_dictionary = book_category_dictionary("google_books_dataset.csv")
    if command == 'S':
        sub_command = input("How do you want to sort?: ").upper()
        while sub_command != 'T' and sub_command != 'R' and sub_command != 'P' and  sub_command != 'A':
            print('\nNo such command\n')
            sub_command = input("How do you want to sort?: ").upper()
        if sub_command == 'T':
            title_sort = sort_books_title(data_file_dictionary)
            print(title_sort)
            input('\nEnter to continue')            
        if sub_command == 'R':
            rate_sort = sort_books_ascending_rate(data_file_dictionary)
            print(rate_sort)
            input('\nEnter to continue')       
        if sub_command == 'P':
            publisher_sort = sort_books_publisher(data_file_dictionary)
            print(publisher_sort)
            input('\nEnter to continue')          
        if sub_command == 'A':
            author_sort = sort_books_author(data_file_dictionary)
            print(author_sort)
            input('\nEnter to continue')
    
