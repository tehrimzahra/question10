def get_user_input():
    user_list = []
    
    while True:
        user_input = input("Enter a value (or press enter to finish): ")
    
        if user_input == "":
            break
        user_list.append(user_input)
    print("The final list is:", user_list)
get_user_input()
