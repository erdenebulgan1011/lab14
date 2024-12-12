
import unittest
from io import StringIO
import sys
from utils.greeting_utils import hello, bye, welcome

class TestGreetings(unittest.TestCase):
    def setUp(self):
        """Capture stdout for testing print statements."""
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        """Restore stdout."""
        sys.stdout = self.held

    def test_hello(self):
        """Test the hello function."""
        hello()
        self.assertEqual(sys.stdout.getvalue().strip(), "Hi there!")

    def test_bye(self):
        """Test the bye function."""
        bye()
        self.assertEqual(sys.stdout.getvalue().strip(), "Goodbye!")

    def test_welcome(self):
        """Test the welcome function with a name."""
        welcome("Alice")
        self.assertEqual(sys.stdout.getvalue().strip(), "Welcome, Alice! Nice to meet you.")

if __name__ == '__main__':
    unittest.main()
