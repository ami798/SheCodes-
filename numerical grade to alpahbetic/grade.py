def grade():
    while True:
        # Input: Ask the user to enter a grade
        grade_input = input("Please enter a grade between 0% and 100%: ").strip()

        # Check for Empty Input
        if grade_input == "":
            print("You didn't enter a grade. Please try again.")
            continue

        # Check if the input is a valid number
        try:
            grade = float(grade_input)
        except ValueError:
            print("Invalid input. Please enter a numerical grade.")
            continue

        # Ensure the grade is within the valid range
        if 0 <= grade <= 100:
            # Conversion: Transform the number into a letter grade
            if grade >= 90:
                print("🎉 ‘A’ - Awesome!")
            elif grade >= 80:
                print("🌟 ‘B’ - Brilliant!")
            elif grade >= 65:
                print("👍 ‘C’ - Cool!")
            elif grade >= 50:
                print("😐 ‘D’ - Dandy!")
            else:
                print("🚫 ‘F’ - Frown town!")
            break
        else:
            print("Grade must be between 0% and 100%. Please try again.")

# Start the process
grade()
