print("Welcome to CLI Meadia Tracker App")

media_list = [] # An empty array / list to store all the titles
is_running = True # Program running state

while (is_running): # The program will continue to run in a loop until is_running is set to False
    print("\n --- Choose any Option --- \n")
    print("1. Add new title \n2. Remove a title \n3. View all titles \n4. Exit")
    print("Choose from the above options #enter index no. of the option")
    choice = input("I choose: ")

    #Case based option / function execution
    #Option 1
    if choice == "1":
        new_title = input("Enter the title to add: ")
        media_list.append(new_title) # Append (insert) a new title in the main media_list array/list
        print(f"<<< Successfully added {new_title} >>>")

    # Option 2
    elif choice == "2":
        print("\n\nSaved titles:")
        
        # Checking wheather the media_list array is empty or not 
        if (len(media_list) == 0): # First check if list is empty
            print("<<< No titles found ! Please add new titles before >>>")

        else: # If list is not empty
            index = 1 
            for title in media_list: # To print titles one by one with index no. from the main array e.g: 1. title
                print(f"{index}. {title}")
                index += 1
            try:  # To handle most obvious errors/exceptions and stop program from crashing due to error
                rem_indx = int(input("\nEnter the index of the title to remove: "))
                media_list.pop(rem_indx - 1) # Using user provided index no. to remove title from main array
                print("<<< Successfully removed the title >>>")

            # Using except keyword to display custom safe error messages when the following Errors occurs
            except ValueError: 
                print("<<< Invalid input passed, only numbers are allowed. Please try Again. >>>")
            except IndexError:
                print(f"<<< Title with index no. {rem_indx} doesn't exist. Please try agin >>>")              
    
    # Option 3
    elif choice == "3":
        print("\n\nSaved titles:")

        if (len(media_list) == 0): # First check if list is empty
            print("<<< No titles found ! Please add new titles before >>>")
        else:
            for title in media_list:
                print(title)

    # Option 4
    elif choice =="4":
        print("<<< Closing App... GoodBye ! >>>")
        is_running = False # While loop is terminated and program is finished
    
    else: #If any unexpected input is passed during main option menu then display this message and loop back
        print("<<< Invalid option entered. Please try Again ! >>>")