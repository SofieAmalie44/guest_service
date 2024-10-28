"""
Product Catalog Service:
Styrer listen over tilgængelige produkter, inklusive detaljer såsom navn, beskrivelse, pris og billeder.
Tilbyder funktionalitet til at søge, filtrere og kategorisere produkter.
"""
from flask import Flask, jsonify, request
from services.guests import fetch_guests

app = Flask(__name__)


@app.route('/guests', methods=['GET'])
def get_all_guests():
    guests = fetch_guests()
    return jsonify(guests)

@app.route('/guests/<int:id>', methods=['GET'])
def get_guests(id):
    guests = fetch_guests()
    
    return jsonify([guest for guest in guests if guest['guestID'] == id])

# Søg efter gæster på efternavn
@app.route('/guests/search', methods=['GET'])
def search_guest():
    query = request.args.get('lastname', '').lower()
    guests = fetch_guests()
    
    filtered_guests = [guest for guest in guests if query in guest['lastname'].lower()]
    return jsonify(filtered_guests)

@app.route('/guests/loyalty/<int:points>', methods=['GET'])
def get_guest_by_loyalty(points):
    guests = fetch_guests()
    
    filtered_guests = [guest for guest in guests if guest['loyaltyPoints'] == points]
    return jsonify(filtered_guests)


app.run(host='0.0.0.0', port=4000)