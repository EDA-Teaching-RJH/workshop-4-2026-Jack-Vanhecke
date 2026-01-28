def append_list_names(names, change_name):

    names.append(change_name)

    return names

def append_list_scores(scores, change_score):

    scores.append(change_score)

    return scores

def main():
    # Ask how many students are in the class - force to be integer instead of default string
    student_count = int(input("How many students to enter? "))

    # Lists to store data
    names = []
    scores = []

    # Loop to get student details - force i+1 to string for concatination
    for i in range(student_count):
        print("Student " + str(i + 1))
        
        # Clean up the name input - missing syntax () after .strip
        name_input = input("Name: ").strip().title()
        append_list_names(names, name_input)

        # Keep asking for score until valid (0-100)
        while True:
            score_input = int(input("Score: ")) # Force input to integer data type rather than defaut string
            
            # Check for valid range
            if (score_input <= 0) or (score_input >=100):
                print("Invalid score. Must be 0-100.")
                continue
            else:
                break
        
        append_list_scores(scores, score_input)

    # Print results
    print("--- Class Summary ---")
    
    # Loop through the lists and print pass/fail
    # Pass mark is 40
    i = 0
    for i in range(len(names)):
        if scores[i] < 40:
            result = "Fail"
            i += 1 # Adds 1 to variable i each loop
        else:
            result = "Pass"
            print(str(i + 1), ": " + str(names[i]), " - ", str(scores[i]), " - " + str(result))
            i += 1 # Adds 1 to variable i each loop

# Call the main function - fixed syntax missing ()
main()
