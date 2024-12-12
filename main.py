
from utils.greeting_utils import hello, bye, welcome

def main():
    """Main entry point of the application."""
    print("Welcome to our Greeting Application!")
    hello()
    welcome("User")
    bye()

if __name__ == "__main__":
    main()
