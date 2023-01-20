# Team Identifier - T006
#Written By:
#Nolan Kisser 101222376
#Manit Jawa 101215842
#Ishtiaque Khan 101227487
#Balkaran Karir 101229843

# Version 1.0, 12 April 2022

def book_category_dictionary(filename:str)->dict:
    """Returns a dictionary of books under their category header from data
    in a given google books dataset.
    
    Preconditions:
    File must be accessible by the program
    
    >>> book_category_dictionary(google_books_dataset)
    book_dictionary = {
    "Fiction":[ {"title": "Antiques Roadkill: A Trash 'n' Treasures Mystery",
                  "author": " Barbara Allan",
                  "language ": "English",
                  "rating": 3.3,
                  "publisher": " Kensington Publishing Corp.",
                  "pages": 288
                  },
                  {another element},
                  …
               ],
    "Biography":[ {"title": "The Nightshift Before Christmas: Festive hospital
                             diaries from the author of million-copy hit",
                   "author": " Adam Kay",
                   "language": "English",
                   "rating": 4.7,
                   "publisher": "Pan Macmillan",
    """
    o_file = open(filename, "r")
    
    lst_books = []
    book_dictionary = {}
    for line in o_file:
        line = line.split(",")
        if line not in lst_books:
            lst_books += [line]
        categories = line[5]        
        book_dictionary[categories] = []
    
    book_dictionary.pop('category')
    lst_books.pop(0)
    for line in lst_books:
        title = line[0]
        author = line[1]
        rating = line[2]
        if line[2] != 'N/A' and line[2] != 'rating':
            rating = float(rating)        
        publisher = line[3]
        pages = line[4]
        if line[4] != 'N/A' and line[4] != 'rating':
            pages = int(pages)        
        categories = line[5]
        language = line[6]
        if categories in book_dictionary.keys():
            book_dictionary[categories] += [{"title": title,
                         "author": author,
                         "language": language.strip(),
                         "rating": rating,
                         "publisher": publisher,
                         "pages": pages
                         },]
            
            
          
        
     
    
    o_file.close()
    return book_dictionary
