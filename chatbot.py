import datetime
import random


# ---------------------------
# Smart Python Chatbot
# ---------------------------

def chatbot():

    print("=" * 70)
    print("🤖 SMART PYTHON CHATBOT")
    print("Your Personal Assistant")
    print("Type 'help' to see all commands")
    print("Type 'bye' to exit")
    print("=" * 70)

    user_name = ""

    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why was the Python developer calm? Because he had exception handling.",
        "Why do Java developers wear glasses? Because they don't C#.",
        "Debugging: Being the detective in a crime movie where you're also the criminal."
    ]

    quotes = [
        "Success is the sum of small efforts repeated daily.",
        "Believe in yourself and all that you are.",
        "Every expert was once a beginner.",
        "Practice makes progress.",
        "Dream big. Start small. Act now."
    ]

    study_tips = [
        "Study for 25 minutes and take a 5-minute break (Pomodoro Technique).",
        "Make short notes while studying.",
        "Practice coding every day.",
        "Revise before sleeping for better memory retention.",
        "Focus on understanding concepts instead of memorizing."
    ]

    career_advice = [
        "Build projects to strengthen your resume.",
        "Learn communication skills along with technical skills.",
        "Keep your LinkedIn profile updated.",
        "Contribute to open-source projects.",
        "Never stop learning new technologies."
    ]

    interview_tips = [
        "Research the company before the interview.",
        "Practice common interview questions.",
        "Be confident and maintain eye contact.",
        "Prepare examples of your projects.",
        "Always ask thoughtful questions at the end."
    ]

    health_tips = [
        "Drink at least 2-3 liters of water daily.",
        "Take short breaks from screens every hour.",
        "Sleep 7-8 hours regularly.",
        "Exercise for at least 30 minutes daily.",
        "Eat healthy and avoid excessive junk food."
    ]

    while True:

        user = input("\nYou: ").lower().strip()

        # ---------------------------------
        # Greetings
        # ---------------------------------
        if user in ["hello", "hi", "hey"]:

            current_hour = datetime.datetime.now().hour

            if current_hour < 12:
                greeting = "Good Morning ☀️"
            elif current_hour < 18:
                greeting = "Good Afternoon 🌤️"
            else:
                greeting = "Good Evening 🌙"

            print(f"🤖 Chatbot: {greeting}! Nice to meet you.")

        # ---------------------------------
        # Save User Name
        # ---------------------------------
        elif user == "my name":

            user_name = input("Enter your name: ")

            print(f"🤖 Chatbot: Nice to meet you, {user_name}! 😊")

        elif user == "what is my name":

            if user_name:
                print(f"🤖 Chatbot: Your name is {user_name}.")
            else:
                print("🤖 Chatbot: I don't know your name yet.")

        # ---------------------------------
        # How Are You
        # ---------------------------------
        elif user == "how are you":
            print("🤖 Chatbot: I'm doing great! Thanks for asking.")

        # ---------------------------------
        # Bot Name
        # ---------------------------------
        elif user == "what is your name":
            print("🤖 Chatbot: I am Smart Python Chatbot.")

        # ---------------------------------
        # Date
        # ---------------------------------
        elif user == "date":

            today = datetime.datetime.now().strftime("%d-%m-%Y")

            print("🤖 Chatbot: Today's date is", today)

        # ---------------------------------
        # Time
        # ---------------------------------
        elif user == "time":

            current_time = datetime.datetime.now().strftime("%H:%M:%S")

            print("🤖 Chatbot: Current time is", current_time)

        # ---------------------------------
        # Joke
        # ---------------------------------
        elif user == "joke":
            print("🤖 Chatbot:", random.choice(jokes))

        # ---------------------------------
        # Motivation
        # ---------------------------------
        elif user == "motivate me":
            print("🤖 Chatbot:", random.choice(quotes))

        # ---------------------------------
        # Mood Check
        # ---------------------------------
        elif user == "mood":

            mood = input("How are you feeling today? ").lower()

            if mood in ["happy", "good", "great"]:
                print("🤖 Chatbot: That's wonderful! Keep smiling 😊")

            elif mood in ["sad", "upset", "depressed"]:
                print("🤖 Chatbot: Tough days happen. Keep moving forward 💪")

            elif mood in ["angry"]:
                print("🤖 Chatbot: Try taking deep breaths and relaxing.")

            elif mood in ["tired"]:
                print("🤖 Chatbot: Take some rest and stay hydrated.")

            else:
                print("🤖 Chatbot: Thank you for sharing your feelings.")

        # ---------------------------------
        # Study Tips
        # ---------------------------------
        elif user == "study tip":
            print("📚 Study Tip:")
            print(random.choice(study_tips))

        # ---------------------------------
        # Career Advice
        # ---------------------------------
        elif user == "career advice":
            print("💼 Career Advice:")
            print(random.choice(career_advice))

        # ---------------------------------
        # Interview Tips
        # ---------------------------------
        elif user == "interview tip":
            print("🎯 Interview Tip:")
            print(random.choice(interview_tips))

        # ---------------------------------
        # Health Tips
        # ---------------------------------
        elif user == "health tip":
            print("🍎 Health Tip:")
            print(random.choice(health_tips))

        # ---------------------------------
        # Age Calculator
        # ---------------------------------
        elif user == "age":

            try:
                birth_year = int(input("Enter your birth year: "))

                current_year = datetime.datetime.now().year

                age = current_year - birth_year

                print(f"🤖 Chatbot: Your age is approximately {age} years.")

            except ValueError:
                print("Please enter a valid year.")

        # ---------------------------------
        # Calculator
        # ---------------------------------
        elif user == "calculator":

            try:
                num1 = float(input("Enter first number: "))
                operator = input("Enter operator (+ - * /): ")
                num2 = float(input("Enter second number: "))

                if operator == "+":
                    print("Result =", num1 + num2)

                elif operator == "-":
                    print("Result =", num1 - num2)

                elif operator == "*":
                    print("Result =", num1 * num2)

                elif operator == "/":

                    if num2 == 0:
                        print("Cannot divide by zero.")

                    else:
                        print("Result =", num1 / num2)

                else:
                    print("Invalid operator.")

            except ValueError:
                print("Please enter valid numbers.")

        # ---------------------------------
        # Help Menu
        # ---------------------------------
        elif user == "help":

            print("""
================= COMMAND LIST =================

hello / hi / hey
my name
what is my name
how are you
what is your name

date
time

joke
motivate me

mood
study tip
career advice
interview tip
health tip

age
calculator

help
bye

================================================
""")

        # ---------------------------------
        # Exit
        # ---------------------------------
        elif user == "bye":

            if user_name:
                print(f"🤖 Chatbot: Goodbye {user_name}! Have a great day. 😊")
            else:
                print("🤖 Chatbot: Goodbye! Have a wonderful day. 😊")

            break

        # ---------------------------------
        # Unknown Command
        # ---------------------------------
        else:
            print("🤖 Chatbot: Sorry, I don't understand that command.")
            print("Type 'help' to see available commands.")


# ---------------------------
# Run Chatbot
# ---------------------------
chatbot()