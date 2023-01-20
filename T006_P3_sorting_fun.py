# Team Identifier - T006
#Written By:
#Nolan Kisser 101222376
#Manit Jawa 101215842
#Ishtiaque Khan 101227487
#Balkaran Karir 101229843

# Version 1.0, 12 April 2022

#imports
from T006_check_equal import check_equal
from T006_P5_load_data import book_category_dictionary

#The four functions from P3 – Task 1 (and extra function that arise from
#refactoring)

# dictionary to list 
def dictionary_to_list(book_category_dictionary:dict)->list:
    """
    This function takes the book category category dictionary from P1 case 1
    and returns a list of books with no duplicate entries.
    >>> dictionary_to_list(book_category_dictionary)
    [
    {
      "title":"Antiques Roadkill: A Trash 'n' Treasures Mystery",
      "author":"Barbara Allan",
      "language":"English",
      "rating":3.3,
      "publisher":"Kensington Publishing Corp.",
      "category":["Fiction","Detective","Mystery"]
      "pages":288,
    },
    {
      "title":"The Painted Man (The Demon Cycle. Book 1)",
      "author":"Peter V. Brett",
      "language":"English",
      "rating":4.5,
      "publisher":"HarperCollins UK",
      "category":["Fiction","Fantasy","Thrillers"]
      "pages":544,
    }
    ...
    ]
    """
    books_list = []
    new_books_list = []
    for category_keys in book_category_dictionary:
        for book_info in book_category_dictionary.get(category_keys):
            if book_info not in books_list:
                book_info['category'] = category_keys
                x = book_info['pages']
                book_info.pop('pages')
                book_info['pages']= x                
                books_list += [book_info]
                    
    for books in books_list:
        category_list = []
        for categories in book_category_dictionary:
            for book_data in book_category_dictionary.get(categories):
                for keys in book_data:
                    if keys == 'title' and book_data.get(keys) == books.get('title'):
                        category_list += [categories]       
        books['category'] = category_list  
        
    for books in books_list:
        if books not in new_books_list:
            new_books_list += [books]    
    
    return new_books_list

# -------------- The Main 4 functions of P3 Task 1 -------------

# Function 1: sort_books_title
def sort_books_title(dictionary:dict)->dict:
    
    """
    Ishtiaque Khan 101227487
    Returns a list of dictionary and sorts them alphabetically according to the title.
    >>>book_category_dictionary("google_books_dataset.csv")
    [{'title': "'Salem's Lot", 'author': 'Stephen King', 'language': 'English', 'rating': '4.4', 'publisher': 'Hachette UK', 'category': 'Thrillers', 'pages': '300'}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'language': 'English', 'rating': '4.5', 'publisher': 'HarperCollins UK', 'category': 'Fantasy', 'pages': '864'}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'language': 'English', 'rating': '4.5', 'publisher': 'HarperCollins UK', 'category': 'Adventure', 'pages': '864'},.... and the rest of the books. 
    >>>book_category_dictionary("test_dataset.csv")
    [{'title': 'After Anna', 'author': 'Alex Lake', 'language': 'English', 'rating': '4.1', 'publisher': 'HarperCollins UK', 'category': 'Fiction', 'pages': '416'}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English', 'rating': '4.2', 'publisher': 'Marvel Entertainment', 'category': 'Comics', 'pages': '96'}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English', 'rating': '4.3', 'publisher': 'Simon and Schuster', 'category': 'Economics', 'pages': '320'}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'language': 'English', 'rating': '4', 'publisher': 'Harper Collins', 'category': 'Fiction', 'pages': '336'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': '4.8', 'publisher': 'Hachette UK', 'category': 'Fiction', 'pages': '400'}]
    
    """
    lst = dictionary_to_list(dictionary)
          
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j]['title']> lst[j+1]['title']:
                lst[j], lst[j+1] = lst[j+1], lst[j]
             
    return lst

# Function 2: sort_books_publisher
def sort_books_publisher(book_dictionary: dict) -> list:
    """
    Author and Student Number: Manit Jawa 101215842
    Returns the given books in a dictionary (book_dictionary) as a list, ordered by publisher and ordered by title for each publisher. 
    
    import T006_P1_load_data
    book_dictionary1 = T006_P1_load_data.book_category_dictionary("google_books_dataset.csv") #the whole dataset
    book_dictionary2 = T006_P1_load_data.book_category_dictionary("test_006.csv") # first 50 books of the dataset
    
    >>> sort_books_publisher(book_dictionary1)
    >>> [{'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English', 'rating': 'N/A', 'publisher': 'AMACOM', 'category': ['Economics', 'Business'], 'pages': 112}, {'title': 'Management (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English', 'rating': 'N/A', 'publisher': 'AMACOM', 'category': ['Economics', 'Management'], 'pages': 112}, ...{another book} .... ]

    >>> sort_books_publisher(book_dictionary2)
    >>> [{'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English', 'rating': 'N/A', 'publisher': 'AMACOM', 'category': ['Economics'], 'pages': 112}, {'title': 'Mrs. Pollifax Unveiled', 'author': 'Dorothy Gilman', 'language': 'English', 'rating': 3.9, 'publisher': 'Ballantine Books', 'category': ['Fiction'], 'pages': 208}, {'title': 'Goals!: How to Get Everything You Want -- Faster Than You Ever Thought Possible. Edition 2', 'author': 'Brian Tracy', 'language': 'English', 'rating': 4.3, 'publisher': 'Berrett-Koehler Publishers', 'category': ['Economics'], 'pages': 288}, ... {another book} ....]

    """
    book_data_list = []
    book_data_list_unique = dictionary_to_list(book_dictionary)
                    
    number_of_books = len(book_data_list_unique)
    for y in range(number_of_books):
        for z in range(0, number_of_books-1-y):
            if book_data_list_unique[z]['publisher'] > book_data_list_unique[z+1]['publisher']:
                book_data_list_unique[z] , book_data_list_unique[z+1] = book_data_list_unique[z+1] , book_data_list_unique[z]
                
    for e in range(number_of_books):
        for u in range(0,number_of_books-1-e):
            if book_data_list_unique[u]['publisher'] == book_data_list_unique[u+1]['publisher']:
                if book_data_list_unique[u]['title'] > book_data_list_unique[u+1]['title']:
                    book_data_list_unique[u] , book_data_list_unique[u+1] = book_data_list_unique[u+1] , book_data_list_unique[u]
                    
    
    
    return book_data_list_unique

# Function 3: sort_books_author
def sort_books_author(dictionary:dict)->list:
    """
    Nolan Kisser 101222376
    The function takes a dictionary input and uses
    the bubble sort method to sort the books based on their author 
    alphabetically.
    >>> sort_books_author(book_dictionary)
    [{'title': 'Twas The Nightshift Before Christmas: Festive hospital diaries from the author of million-copy hit This is Going to Hurt', 'author': 'Adam Kay', 'language': 'English', 'rating': 4.7, 'publisher': 'Pan Macmillan', 'category': ['Humor'], 'pages': 112}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'language': 'English', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'category': ['Fiction', 'Detective', 'Thrillers', 'Mystery'], 'pages': 224}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'language': 'English', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'category': 'Detective', 'pages': 224}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'language': 'English', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'category': 'Thrillers', 'pages': 224}... cont.
    """
    lst_books = dictionary_to_list(dictionary)
    n = len(lst_books)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst_books[j]['author'] > lst_books[j+1]['author']:
                lst_books[j],lst_books[j+1] = lst_books[j+1],lst_books[j]
            if lst_books[j]['author'] == lst_books[j+1]['author']:
                if lst_books[j]['title'] > lst_books[j+1]['title']:
                    lst_books[j],lst_books[j+1] = lst_books[j+1],lst_books[j]            
    
    return lst_books

# Function 4: sort_books_ascending_rate
def sort_books_ascending_rate(book_category_dictionary:dict)->list:
    """
    Balkaran Karir, 101229843
    
    This function takes the book_category_dictionary from P1 Case 1 and returns
    a list of all of the books in ascending order or rating. The books which
    do not have a rating appear at the beginning and the books with the same 
    rating are ordered alphabetically by the title. 
    >>> sort_books_ascending_rate(book_category_dictionary)
    [
    {
      "title":"The Guardians: The explosive new thriller from international bestseller John Grisham",
      "author":"John Grisham",
      "language":"English",
      "rating":"N/A",
      "publisher":"Hachette UK",
      "category":["Fiction","Thrillers","Legal"],
      "pages":384
    },
    {
      "title":"No Mercy: The brand new novel from the Queen of Crime",
      "author":"Martina Cole",
      "language":"English",
      "rating":"N/A",
      "publisher":"Hachette UK",
      "category":["Fiction","Thrillers"],
      "pages":416
    }
    ...
    ]
    """
    unrated_list = []
    
    new_books_list = dictionary_to_list(book_category_dictionary)
    
    for books in new_books_list:
        for information in books:
            if information == 'rating' and books.get(information) == 'N/A':
                unrated_list += [books]
                
    for books in new_books_list:
        for information in books:
            if information == 'rating' and books.get(information) == 'N/A':   
                index = new_books_list.index(books)
                new_books_list.pop(index)
                
    if new_books_list[-1]['rating'] == 'N/A':
        books_list.pop(-1)
        
    list_length = len(new_books_list)
    
    for indices in range(list_length):
        for j in range(0,list_length-1):
            rating_1 = new_books_list[j]['rating']
            rating_2= new_books_list[j+1]['rating']
            if type(rating_1) != str and type(rating_2) != str:
                if (new_books_list[j]['rating']) > (new_books_list[j+1]['rating']):
                    new_books_list[j],new_books_list[j+1] = new_books_list[j+1],new_books_list[j]
            elif type(rating_1) != str and type(rating_2) == str:
                new_books_list[j],new_books_list[j+1] = new_books_list[j+1],new_books_list[j]
            if rating_1 == rating_2:
                if (new_books_list[j]['title']) > (new_books_list[j+1]['title']):
                    new_books_list[j],new_books_list[j+1] = new_books_list[j+1],new_books_list[j]
                
    unrated_list.extend(new_books_list)
    return unrated_list

# ---------------- END ---------------------------

#Main script with automated testing. The main script should only run if the
#module is executed. It should not run when the module is imported. The main
#script should print the total number of tests that pass and fail.
if __name__ == "__main__":
    dictionary = book_category_dictionary("google_books_dataset.csv") #Use for testing
    total_test = 0
    test_pass = 0
        
    #------------- Testing for sort_books_title -------------
        
    #TEST 1
    dictionary = {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544}], 'Fantasy': [{'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 96}, {'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Patrick Rothfuss', 'language': 'English', 'rating': 4.3, 'publisher': 'Hachette UK', 'pages': 672}]}
    outcome = sort_books_title(dictionary)
    description = "sort_books_title(dictionary)"
    expected = [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'category': ['Fiction'], 'pages': 288}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'category': ['Fantasy'], 'pages': 96}, {'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Patrick Rothfuss', 'language': 'English', 'rating': 4.3, 'publisher': 'Hachette UK', 'category': ['Fantasy'], 'pages': 672}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'category': ['Fiction'], 'pages': 544}]   
    test = check_equal(description, outcome, expected)
    total_test +=1
    test_pass += check_equal("test 1" , outcome, expected)
    
    #TEST 2
    dictionary2 = {'Comics': [{'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96}, {'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'language': 'English', 'rating': 4.1, 'publisher': 'DC', 'pages': 164}], 'Fantasy': [{'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 96}, {'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Patrick Rothfuss', 'language': 'English', 'rating': 4.3, 'publisher': 'Hachette UK', 'pages': 672}]}
    outcome = sort_books_title(dictionary2)
    description = "sort_books_title(dictionary2)"
    expected = [{'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'category': ['Comics'], 'pages': 96}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'category': ['Fantasy'], 'pages': 96}, {'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Patrick Rothfuss', 'language': 'English', 'rating': 4.3, 'publisher': 'Hachette UK', 'category': ['Fantasy'], 'pages': 672}, {'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'language': 'English', 'rating': 4.1, 'publisher': 'DC', 'category': ['Comics'], 'pages': 164}]
    
    test = check_equal(description, outcome, expected)
    total_test +=1
    test_pass += check_equal("test 2" , outcome, expected)
    
    #TEST 3
    dictionary3 = {'Fantasy': [{'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 96}, {'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Patrick Rothfuss', 'language': 'English', 'rating': 4.3, 'publisher': 'Hachette UK', 'pages': 672}],'Comics': [{'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96}, {'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'language': 'English', 'rating': 4.1, 'publisher': 'DC', 'pages': 164}]}
    outcome = sort_books_title(dictionary3)
    description = "sort_books_title(dictionary3)"
    expected = [{'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'category': ['Comics'], 'pages': 96}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'category': ['Fantasy'], 'pages': 96}, {'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Patrick Rothfuss', 'language': 'English', 'rating': 4.3, 'publisher': 'Hachette UK', 'category': ['Fantasy'], 'pages': 672}, {'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'language': 'English', 'rating': 4.1, 'publisher': 'DC', 'category': ['Comics'], 'pages': 164}]
    test = check_equal(description, outcome, expected)
    total_test +=1
    test_pass += check_equal("test 3" , outcome, expected)
    
    print(str(total_test) + " total tests.")
    print(str(test_pass) +" tests passed.")
    test_fails = total_test - test_pass
    print(str(test_fails) + " tests failed.")
    
    # Testing for Function 2
    
    tally_p1 = 0
    tally_f1 = 0
    
    test_dict_1 = {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288},{'title': "Antiques Con", 'author': 'Barbara Allan', 'language': 'English', 'rating': 4.8, 'publisher': 'Kensington Books', 'pages': 288},{'title': "Percy Jackson & the Olympians: The Battle of the Labyrinth", 'author': 'Rick Riordan', 'language': 'English', 'rating': 'N/A', 'publisher': 'Miramax Books','pages': 361}],'Fantasy': [{'title': "Percy Jackson & the Olympians: The Lightning Thief", 'author': 'Rick Riordan', 'language': 'English', 'rating': 3.3, 'publisher': 'Miramax Books', 'pages': 379},{'title': "Percy Jackson & the Olympians: The Battle of the Labyrinth", 'author': 'Rick Riordan', 'language': 'English', 'rating': 'N/A', 'publisher': 'Miramax Books','pages': 361}]}
    
    test_dict_2 = {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544},{'title': 'Ultimate Spider-Man Vol. 11: Carnage', 'author': 'Brian Michael Bendis', 'language': 'English', 'rating': 4.1, 'publisher': 'Marvel Entertainment', 'pages': 144}],'Comics': [{'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96}, {'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'language': 'English', 'rating': 4.1, 'publisher': 'DC', 'pages': 164}, {'title': 'Ultimate Spider-Man Vol. 11: Carnage', 'author': 'Brian Michael Bendis', 'language': 'English', 'rating': 4.1, 'publisher': 'Marvel Entertainment', 'pages': 144}]}
    
    test_dict_3 = {'Fiction': [{'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': 'English', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400}],'Economics': [{'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'pages': 320}, {'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112}]}
    
    test_result = check_equal('sort_books_publisher(test_dict_1)',[{'title': "Antiques Con", 'author': 'Barbara Allan', 'language': 'English', 'rating': 4.8, 'publisher': 'Kensington Books', 'pages': 288,'category':['Fiction']},{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category':['Fiction']},{'title': "Percy Jackson & the Olympians: The Battle of the Labyrinth", 'author': 'Rick Riordan', 'language': 'English', 'rating': 'N/A', 'publisher': 'Miramax Books','pages': 361, 'category':['Fiction','Fantasy']},{'title': "Percy Jackson & the Olympians: The Lightning Thief", 'author': 'Rick Riordan', 'language': 'English', 'rating': 3.3, 'publisher': 'Miramax Books', 'pages': 379, 'category':['Fantasy']}],sort_books_publisher(test_dict_1))
    if test_result == 1:
        tally_p1 += 1
    elif test_result == 0:
        tally_f1 += 1
    
    test_result = check_equal('sort_books_publisher(test_dict_2)',[{'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'language': 'English', 'rating': 4.1, 'publisher': 'DC', 'pages': 164,'category':['Comics']},{'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544,'category':['Fiction']},{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288,'category':['Fiction']},{'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96,'category':['Comics']},{'title': 'Ultimate Spider-Man Vol. 11: Carnage', 'author': 'Brian Michael Bendis', 'language': 'English', 'rating': 4.1, 'publisher': 'Marvel Entertainment', 'pages': 144,'category':['Fiction','Comics']}],sort_books_publisher(test_dict_2))
    if test_result == 1:
        tally_p1 += 1
    elif test_result == 0:
        tally_f1 += 1
    
    test_result = check_equal('sort_books_publisher(test_dict_1)',[{'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112,'category':['Economics']},{'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400,'category':['Fiction']},{'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'pages': 320,'category':['Economics']},{'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': 'English', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226,'category':['Fiction']}],sort_books_publisher(test_dict_3))
    if test_result == 1:
        tally_p1 += 1
    elif test_result == 0:
        tally_f1 += 1
    
    
    print(tally_p1, "tests passed for Function 2: sort_books_publisher")
    print(tally_f1, "tests failed for Function 2: sort_books_publisher")
    
    # Testing for Function 3
    tally_p3 = 0
    tally_f3 = 0
    
    test_result = check_equal('sort_books_author(test_dict_1)',[{'title': 'Antiques Con', 'author': 'Barbara Allan', 'language': 'English', 'rating': 4.8, 'publisher': 'Kensington Books', 'category': ['Fiction'], 'pages': 288}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'category': ['Fiction'], 'pages': 288}, {'title': 'Percy Jackson & the Olympians: The Battle of the Labyrinth', 'author': 'Rick Riordan', 'language': 'English', 'rating': 'N/A', 'publisher': 'Miramax Books', 'category': ['Fiction', 'Fantasy'], 'pages': 361}, {'title': 'Percy Jackson & the Olympians: The Lightning Thief', 'author': 'Rick Riordan', 'language': 'English', 'rating': 3.3, 'publisher': 'Miramax Books', 'category': ['Fantasy'], 'pages': 379}],sort_books_author(test_dict_1))
    if test_result == 1:
        tally_p3 += 1
    elif test_result == 0:
        tally_f3 += 1
    
    test_result = check_equal('sort_books_author(test_dict_2)',[{'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'language': 'English', 'rating': 4.1, 'publisher': 'DC', 'category': ['Comics'], 'pages': 164}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'category': ['Fiction'], 'pages': 288}, {'title': 'Ultimate Spider-Man Vol. 11: Carnage', 'author': 'Brian Michael Bendis', 'language': 'English', 'rating': 4.1, 'publisher': 'Marvel Entertainment', 'category': ['Fiction', 'Comics'], 'pages': 144}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'category': ['Comics'], 'pages': 96}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'category': ['Fiction'], 'pages': 544}],sort_books_author(test_dict_2))
    if test_result == 1:
        tally_p3 += 1
    elif test_result == 0:
        tally_f3 += 1
    
    test_result = check_equal('sort_books_author(test_dict_3)',[{'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'category': ['Fiction'], 'pages': 400}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': 'English', 'rating': 4.8, 'publisher': 'Tor Books', 'category': ['Fiction'], 'pages': 226}, {'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English', 'rating': 'N/A', 'publisher': 'AMACOM', 'category': ['Economics'], 'pages': 112}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'category': ['Economics'], 'pages': 320}],sort_books_author(test_dict_3))
    if test_result == 1:
        tally_p3 += 1
    elif test_result == 0:
        tally_f3 += 1
    
    print(tally_p3, "tests passed for Function 3: sort_books_author")
    print(tally_f3, "tests failed for Function 3: sort_books_author")
    
    # Testing for Function 4
    
    book_dictionary1 = book_category_dictionary("dataset1.csv")
    book_dictionary2 = book_category_dictionary("dataset2.csv")
    book_dictionary3 = book_category_dictionary("dataset3.csv")
    
    
    tests_passed = 0
    tests_failed = 0
    
    actual = sort_books_ascending_rate(book_dictionary1)
    expected = [{'title': 'After Anna', 'author': 'Alex Lake', 'language': 'English', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'category': ['Fiction'], 'pages': 416},{'title': 'Antiques Chop', 'author': 'Barbara Allan', 'language': 'English', 'rating': 4.5, 'publisher': 'Kensington Books', 'category': ['Fiction'], 'pages': 240},{'title': 'And Then There Were None', 'author': 'Agatha Christie', 'language': 'English', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'category': ['Fiction'], 'pages': 224},{'title': 'A Trace of Vice (a Keri Locke Mystery Book #3)', 'author': 'Blake Pierce', 'language': 'English', 'rating': 4.8, 'publisher': 'Blake Pierce', 'category': ['Fiction'], 'pages': 250}]
    test = check_equal("Test 1", actual, expected)
    if test == 1:
        tests_passed += 1
    else:
        tests_failed += 1
        
    actual = sort_books_ascending_rate(book_dictionary2)
    expected = [{'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English', 'rating': 'N/A', 'publisher': 'AMACOM', 'category': ['Economics'], 'pages': 112},{'title': 'No Mercy: The brand new novel from the Queen of Crime', 'author': 'Martina Cole', 'language': 'English', 'rating': 'N/A', 'publisher': 'Hachette UK', 'category': ['Fiction'], 'pages': 416},{'title': 'Mrs. Pollifax Unveiled', 'author': 'Dorothy Gilman', 'language': 'English', 'rating': 3.9, 'publisher': 'Ballantine Books', 'category': ['Fiction'], 'pages': 208}]
    test = check_equal("Test 2", actual, expected)
    if test == 1:
        tests_passed += 1
    else:
        tests_failed += 1
        
    actual = sort_books_ascending_rate(book_dictionary3)
    expected = [{'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'language': 'English', 'rating': 'N/A', 'publisher': 'Hachette UK', 'category': ['Fiction'], 'pages': 384},{'title': 'The Infinite Game', 'author': 'Simon Sinek', 'language': 'English', 'rating': 3.8, 'publisher': 'Penguin', 'category': ['Business'], 'pages': 272}]
    test = check_equal("Test 3" , actual, expected)
    if test == 1:
        tests_passed += 1
    else:
        tests_failed += 1
    
    print(tests_passed, "tests passed for Function sort_books_ascending_rate")
    print(tests_failed, "tests failed for Function sort_books_ascending_rate")




