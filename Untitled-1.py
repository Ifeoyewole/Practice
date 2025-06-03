def score_to_point(score):
    if 70 <= score <= 100:
        return 5
    elif 60 <= score < 70:
        return 4
    elif 50 <= score < 60:
        return 3
    elif 45 <= score < 50:
        return 2
    elif 40 <= score < 45:
        return 1
    else:
        return 0

def determine_class_of_degree(cgpa):
    if 4.50 <= cgpa <= 5.00:
        return "First Class"
    elif 3.50 <= cgpa < 4.50:
        return "Second Class Upper"
    elif 2.40 <= cgpa < 3.50:
        return "Second Class Lower"
    elif 1.50 <= cgpa < 2.40:
        return "Third Class"
    elif 1.00 <= cgpa < 1.50:
        return "Pass"
    else:
        return "Fail"

def main():
    print("Welcome to the CGPA Calculator")
    scores = []

    for i in range(1, 6):
        while True:
            try:
                score = float(input(f"Enter score for course {i} (0-100): "))
                if 0 <= score <= 100:
                    scores.append(score_to_point(score))
                    break
                else:
                    print("Score must be between 0 and 100. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    total_points = sum(scores)
    cgpa = round(total_points / 5, 2)
    degree_class = determine_class_of_degree(cgpa)

    print("\nResults")
    print("=======")
    print(f"CGPA: {cgpa}")
    print(f"Class of Degree: {degree_class}")

if __name__ == "__main__":
    main()