import json

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