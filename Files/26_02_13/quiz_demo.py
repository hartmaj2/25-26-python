import time

# List of countries and their capitals
countries = ["France", "Germany", "Italy", "Spain", "Portugal", "Netherlands", "Belgium", "Austria", "Sweden", "Norway"]
capitals = ["Paris", "Berlin", "Rome", "Madrid", "Lisbon", "Amsterdam", "Brussels", "Vienna", "Stockholm", "Oslo"]

# Initialize score and timing
score = 0
total_time = 0

# Quiz loop
for round_number in range(10):
    print(f"Round {round_number + 1}")
    country = countries[round_number]
    correct_capital = capitals[round_number]

    start_time = time.time()
    answer = input(f"What is the capital of {country}? ")
    end_time = time.time()

    # Check answer
    if answer.strip().lower() == correct_capital.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {correct_capital}.")

    # Calculate time taken
    round_time = end_time - start_time
    total_time += round_time
    print(f"You took {round_time:.2f} seconds.\n")

# Calculate average time
average_time = total_time / 10

# Print final results
print(f"Your final score is {score}/10.")
print(f"Your average time per question was {average_time:.2f} seconds.")