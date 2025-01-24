def get_username():
    while True:
        username = input("Please enter your name: ").strip()
        if username == "":
            print("You didn't enter a name. Please try again.")
        else:
            confirmation = input(f"Is this your name? {username} (yes/no): ").strip().lower()
            
            if confirmation == "yes":
                print("Complete!")
                
# Start the process
get_username()
