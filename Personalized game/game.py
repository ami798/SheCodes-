# Global variable to track the score from 0
score = 0

# Greeting function
def greet_player(name="Player"):
    print(f"Hello, {name}! Welcome to the Quiz Game!")

# Question functions
def question_one(answer):
    correct_answer = "Addis Ababa"
    return answer.lower() == correct_answer.lower()

def question_two(answer):
    correct_answer = "Haile GebreSelassie"
    return answer.lower() == correct_answer.lower()

def question_three(answer):
    correct_answer = "2"
    return answer.lower() == correct_answer.lower()

# Score tracker function
def update_score(is_correct):
    global score
    if is_correct:
        score += 1

# The  Main quiz function
def play_quiz():
    greet_player(input("What's your name? ") or "Player")

    answer = input("What is the capital of Ethiopia? ")
    if question_one(answer):
        print("Correct!")
        update_score(True)
    else:
        print("Wrong answer.")
    print(f"Score: {score}")

    answer = input("Who is the well known Ethiopian long distance runner ? ")
    if question_two(answer):
        print("Correct!")
        update_score(True)
    else:
        print("Wrong answer.")
    print(f"Score: {score}")

    answer = input("What is the smallest prime number? ")
    if question_three(answer):
        print("Correct!")
        update_score(True)
    else:
        print("Wrong answer.")
    print(f"Score: {score}")

    print(f"Your final score is: {score}")

if __name__ == "__main__":
    play_quiz()
    # Final announcement based on your score
if score == 3:
    print("Brilliant, you have answered all questions correctly!")
elif score == 0:
    print("poor!")
else:
    print("Good, but try to answer all questions correctly for the next time.")

