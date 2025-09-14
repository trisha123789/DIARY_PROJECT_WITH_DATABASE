from database import create_table
import sqlite3
menu = """
Please select one of the following options:
1) Add new entry for today
2) View entries
3) Exit
Your Selection:
"""

welcome = "Welcome to the programming diary!"
print(welcome)
def create_table():
    with sqlite3.connect("diary_data.db", timeout=10) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS entries(work TEXT, date TEXT);")
# make sure table exists
create_table()

while (user := input(menu)) != "3":
    if user == "1":
        input_content = input("Enter what you learned today: ")
        input_date = input("Enter the date: ")
        with sqlite3.connect("diary_data.db",timeout = 30) as connection:
            connection.execute("INSERT INTO entries VALUES (?, ?);", (input_content, input_date))
    
            print("Adding...")
    elif user == "2":
        with sqlite3.connect("diary_data.db",timeout = 30) as connection:
            cursor = connection.execute("SELECT * FROM entries;")
            print("Entries:", cursor.fetchall())

            print("Viewing...")
        # (we can add view_entries() later)
    else:
        print("Invalid option, please try again")

