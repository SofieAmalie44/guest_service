import json
import sqlite3

############   Database connection function   ##########

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

############   Fetch the guest data   ##########

def fetch_guests():
    # load json data from local file 
    with open('guest_data.json', 'r') as f:
        full_data = json.load(f)


        guests = full_data if isinstance(full_data, list) else full_data.get('guests', [])

        # filtering and transforming the guest data
        filstered_guests = [
            {
                "guestID": guest["GuestID"],
                "fiestname": guest["Firstname"],
                "lastname": guest["Lastname"],
                "email": guest["Email"],
                "phone": guest["Phone"],
                "loyaltyPoints": _calculate_loyaltyPoints(guest["LoyaltyPoints"])
            }
            for guest in guests
        ]

        return filstered_guests
    return []

def _calculate_loyaltyPoints(points):
    # something like this haha only added 10% (maybe something with number of bookings)
    return points * 1.1 if points else 0 

#fetch and print the filtered guest data
guests_data = fetch_guests()
print(guests_data)


############   Create new guest data   ##########

def create_guest(data):
    # take out the data from the request
    firstname = data.get("Firstname")
    lastname = data.get("Lastname")
    email = data.get("Email")
    phone = data.get("Phone")
    loyalty_points = data.get("LoyaltyPoints", 0) # default 0

    #varify the input
    if not firstname or not lastname or not email:
        return {"error": "Firstname, Lastname, Email are required fields"}, 400
    
    # insert data into database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Guest (Firstname, Lastname, Email, Phone, LoyaltyPoints) VALUES (?, ?, ?, ?, ?)",
        (firstname, lastname, email, phone, loyalty_points)
    )
    conn.commit()
    guest_id = cursor.lastrowid
    conn.close()

    # return the newly created guests id as confirmation
    return {"message": "Guest created successfully", "GuestID": guest_id}, 201


############   Update guest data   ##########

def update_guest(guest_id, data):
    firstname = data.get("Firstname")
    lastname = data.get("Lastname")
    email = data.get("Email")
    phone = data.get("Phone")
    loyalty_points = data.get("LoyaltyPoints")

    if not firstname or not lastname or not email:
        return {"error": "Fiestname, Lastname, and Email are required fields"}, 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Guest 
        SET Firstname = ?, Lastname = ?, Email = ?, Phone = ?, LoyaltyPoints = ?
        WHERE GuestID = ?
        ''', 
        (firstname, lastname, email, phone, loyalty_points, guest_id)
    )
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return {"error": "Guest not found"}, 404
    
    # return confirmation of successful update
    return {"message": "Guest updated successfully"}, 200


############   Delete guest    ##########

def delete_guest(guest_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'DELETE FROM Guest where GuestID = ?',
        (guest_id,)
    )
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return {"error": "Guest not found"}, 404
    
    # return confirmation of successful removel
    return {"message": "Guest deleted successfully"}, 200
