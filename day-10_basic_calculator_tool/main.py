# Calculator!

def add (n1, n2):
    added_sums = n1 + n2
    return added_sums

def subtract (n1, n2):
    subtracted_sums = n1 - n2
    return subtracted_sums

def multiply (n1, n2):
    multiplied_sums = n1 * n2
    return multiplied_sums

def divide (n1, n2):
    divided_sums = n1 / n2
    return divided_sums

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Working theory... let first 2 number inputs be outside of the while loop...?

def main():
    
    num_1 = int(input("\nPlease enter the 1st number: "))
    chosen_math_operator = input("\nEnter a math operator symbol to execute your calculations => [+] [-] [*] [/]: ")
    num_next = int(input("\nPlease enter the next number: "))

    previous_calculated_sum = operations[chosen_math_operator](num_1, num_next)
    print(f"\nCalculations: {num_1} {chosen_math_operator} {num_next} = {previous_calculated_sum}")

    # -- END OF 1ST "CALCULATIONS" --

    ended_go_again_question = False
    ended_program = False

    while not ended_program:
        while not ended_go_again_question:

            # [!] BIG BUG [!] SHOULD LOOP BACK BELOW HERE; CURRENTLY DOES NOT!
            # update: fixed all bugs. triumphant. tired. leaving comment here as a memento.
            # for my first 2+ hour bug-fix...
             
            ask_to_go_again = input(f"\nCurrent value is {previous_calculated_sum}. Continue? [YES] [NO]: ").lower()
            if ask_to_go_again == "no" or ask_to_go_again == "n":
                print("\n[SESSION TERMINATED] Thank you for using Brendan's first calculator tool! ;D")
                # This part should smoothly terminate. [!] SMALL BUG [!] - DOES NOT IMMEDIATELY TERMINATE
                ended_program = True
                ended_go_again_question = True
                

            elif ask_to_go_again == "yes" or ask_to_go_again == "ye" or ask_to_go_again == "y":
                # This part should loop back to asking for operator & next number.
                ended_program = False
                ended_go_again_question = True               

            else:
                print("\nDude. That's not an option. Pick a valid option, please.")
                ended_go_again_question = False
                # This part should look back to "ask to go again"
        
        # Stopgap solution, but it worked!!
        if ended_program:
            break

        chosen_math_operator = input("\nEnter a math operator symbol to execute your calculations => [+] [-] [*] [/]: ")
        num_next = int(input("\nPlease enter the next number: "))

        calculated_sum = operations[chosen_math_operator](previous_calculated_sum, num_next)
        print(f"\nCalculations: {previous_calculated_sum} {chosen_math_operator} {num_next} = {calculated_sum}")
        previous_calculated_sum = calculated_sum

        ended_go_again_question = False

        # Program is currently NOT looping back to segment I marked with [!] BIG BUG [!], but it really should... :(

if __name__ == "__main__":
    main()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

