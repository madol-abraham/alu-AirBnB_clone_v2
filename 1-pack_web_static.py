import unittest
import MySQLdb

class TestDatabaseFunctionality(unittest.TestCase):
    def setUp(self):
        # Connect to the test database
        self.conn = MySQLdb.connect(
            user='hbnb_test',
            password='hbnb_test_pwd',
            host='localhost',
            database='hbnb_test_db'
        )
        self.cursor = self.conn.cursor()

    def tearDown(self):
        # Close the database connection
        self.cursor.close()
        self.conn.close()

    def test_create_state(self):
        # Get the initial number of records in the states table
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]

        # Execute the action (e.g., create a new state)
        # Assume that you have a function to create a state in your application
        create_state_function()  # Replace with the actual function call

        # Get the number of records in the states table again
        self.cursor.execute("SELECT COUNT(*) FROM states")
        final_count = self.cursor.fetchone()[0]

        # Validate the action
        self.assertEqual(final_count, initial_count + 1, "New state was not created")

if __name__ == '__main__':
    unittest.main()

