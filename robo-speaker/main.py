# Import the pyttsx3 library, which is a text-to-speech conversion library in Python
import pyttsx3

# Check if this script is the main program being run
if __name__ == '__main__':
    # Print a welcome message to the console
    print("Welcome to Robo-Speaker 1.1")

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Start an infinite loop for continuous user interaction
    while True:
        # Prompt the user to input text to be spoken
        x = input("Input what you want me to speak: ")

        # Check if the user input is 'q' to exit the program
        if x.lower() == "q":
            # Speak a farewell message
            engine.say("Bye Bye Friend")

            # Wait for the speech to finish before proceeding
            engine.runAndWait()

            # Break out of the loop to end the program
            break

        # If the user input is not 'q', speak the input text
        engine.say(x)

        # Wait for the speech to finish before allowing further input
        engine.runAndWait()
