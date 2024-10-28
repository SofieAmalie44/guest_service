import json
import sqlite3

# load the data from JSON file
with open('guest_data.json', 'r') as f:
    guest_data = json.load(f)

# connect to sqlite (creates the database file if it dosent exist)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# creating the Guest table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Guest (
    GuestID INTEGER PRIMARY KEY,
    Firstname TEXT NOT NULL,
    Lastname TEXT NOT NULL,
    Email TEST NOT NULL,
    Phone INTEGER,
    LoyaltyPoints INTEGER           
)
''')

# inserting data from json into the guest table
for guest in guest_data:
    cursor.execute('''
INSERT INTO Guest (GuestID, Firstname, Lastname, Email, Phone, LoyaltyPoints)
    VALUES (?, ?, ?, ?, ?, ?)
''', (
    guest["GuestID"],
    guest["Firstname"],
    guest["Lastname"],
    guest["Email"],
    guest["Phone"],
    guest["LoyaltyPoints"]
))
    
# commit and close the connection
conn.commit()
conn.close()

print("Data successfully imported to SQLite database :)")