"""

The match-case statement in Python is a new feature introduced in version 3.10 that provides a more concise and expressive way to perform pattern matching compared to traditional if-elif-else statements. It resembles the switch-case statement found in other programming languages, allowing you to evaluate different cases based on the value of an expression.


The syntax for the match-case statement in Python is as follows:

match <expression>:
    case <pattern_1>:
        <block_1>
    case <pattern_2>:
        <block_2>
    case <pattern_3>:
        <block_3>
    case _:
        <default_block>

Here's a breakdown of the syntax:

<expression>: The expression to be evaluated for pattern matching.

<pattern_1>, <pattern_2>, <pattern_3>: Patterns to be matched against the expression.

<block_1>, <block_2>, <block_3>: Code blocks to be executed when the corresponding pattern matches.

<default_block>: The default code block to be executed if no pattern matches. The underscore (_) is used as a wildcard pattern to match any value not explicitly covered by the previous patterns.


"""
# def calculate_shipping_cost(order_size):
#     match order_size:
#         case 1:
#             shipping_cost = 10
#             print(f"Shipping cost: ${shipping_cost}")
#         case 2:
#             shipping_cost = 15
#             print(f"Shipping cost: ${shipping_cost}")
#         case 3:
#             shipping_cost = 20
#             print(f"Shipping cost: ${shipping_cost}")
#         case _:
#             shipping_cost = 30
#             print(f"Shipping cost: ${shipping_cost}")
#
# order_size = 2
# calculate_shipping_cost(order_size)



# def process_user_input(user_choice):
#     match user_choice:
#         case "start":
#             print("Starting the game...")
#         case "pause":
#             print("Pausing the game...")
#         case "quit":
#             print("Exiting the game...")
#         case _:
#             print("Invalid input. Please choose from 'start', 'pause', or 'quit'.")
#
# user_choice = input("Enter your choice: ")
# process_user_input(user_choice)



user_choice = "start"
match user_choice:
        case "start":
            print("Starting the game...")
        case "pause":
            print("Pausing the game...")
        case "quit":
            print("Quiting the game...")
        case _ :
           print("Invalid input. Please choose from 'start', 'pause', or 'quit'.")






