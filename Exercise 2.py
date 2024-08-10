import time

questions = [
    ["Who is PM of India?", "Narendra Modi", "Rahul Gandhi", "Vijay Rupani", "Arvind Kejriwal", 1],
    ["What is the capital of India?", "Mumbai", "Delhi", "Ahmedabad", "Bangalore", 2]
]
levels = [1000, 2000, 4000, 8000]

current_level = 0  # Initialize the current level

for i in range(0, len(questions)):
    question = questions[i]
    
    # Update the level for the current question
    level = levels[current_level]
    
    print(f"Question: for Rs.{level} {question[0]}")
    
    for j in range(1, 5):
        print(f"{j}. {question[j]}")
    
    start_time = time.time()  # Record the start time
    
    # Get user input within the time limit
    user_answer = None
    while time.time() - start_time < 10:
        try:
            user_answer = int(input("Enter your answer (1-4): "))
            break  # Break the loop if user input is received
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    if user_answer is None:
        print("Time's up! The correct answer is not provided.")
    elif user_answer == question[5]:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {question[5]}.")
    
    # Move to the next level for the next question
    current_level += 1
