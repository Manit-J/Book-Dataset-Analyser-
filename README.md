ECOR 1042 Data Analyser Project Version 1.0
Date: 12/04/2022

Contact Information
--------------------

Team Leader Name: Manit Jawa

Description
------------

The project contains a user interface in which the user is
prompted to input a command. The user is prompted to upload a file containing
a dataset of books for interpretation. Then is able to choose commands to be done with
the file, such as adding, deleting,finding, and sorting books. The user is able to quit at 
anytime by entering "Q".

The project is made up of the following files:	
- T006_check_equal.py				_A Python Script_
- T006_P2_add_remove_search_dataset.py    _A Python Script_
- T006_P3_sorting_fun.py                  _A Python Script_
- T006_P4_booksUI.py                      _A Python Script_
- T006_P5_load_data.py                    _A Python Script_
- T006_main.py 					_A Python Script
- google_books_dataset.csv                _Excel dataset with book information_

Installation
-------------

Python 3.7.4 or a later model must be installed.
Only built-in Python modules are being used. 
Therefore, no external modules must be loaded.

Usage
------

>python T006_main.py

Follow the prompts and choose which of the four cases you would like to run. 
case1 is add/remove book, case2 is getting books by title, rate, and author, 
case3 is getting books by category and publisher, case4 is for sorting books.
After choosing a case, follow the prompt and input which operation you would like to perform 
on the dataset. It is possible to end the program by entering "Q".

There is no error control, therefore if a dataset is not found, the program will end.
If a wrong type input is entered the program will end.



Credits
--------

**Manit Jawa Wrote:**
- book_category_dictionary
- get_books_by_category
- get_books_by_rate
- check_get_books_by_title
- check_get_books_by_author
- sort_books_publisher
- dictionary_to_list
- case2
- display_UI
- check_equal

**Nolan Kisser Wrote:**
- book_category_dictionary
- add_book
- remove_book
- check_get_books_by_category
- check_get_books_by_rate
- sort_books_author
- dictionary_to_list
- case1
- check_equal
- main

**Ishtiaque Khan Wrote:**
- book_category_dictionary
- get_books_by_title
- get_books_by_author
- check_get_books_by_publisher
- check_get_all_categories_for_book_title
- sort_books_title
- dictionary_to_list
- case3
- check_equal

**Balkaran Karir Wrote:**
- book_category_dictionary
- get_books_by_publisher
- get_all_categories_for_book_title
- testing_function
- check_add_book
- check_remove_book
- sort_books_ascending_rate
- dictionary_to_list
- case4
- check_equal

Copyright 2022 Manit Jawa, Nolan Kisser, Ishtiaque Khan, and Balkaran Karir.
