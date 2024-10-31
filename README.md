# Guest Microservice

Here’s a structured and user-friendly README for a Guest Service repository, following the same style as the previous README:
Guest Service Microservice

This repository contains a Python-based microservice for managing guest information, built in Visual Studio Code (VSCode). The service provides REST API endpoints for creating, deleting, and retrieving guest records. Users can also filter guest information based on loyalty points and last name. Postman is recommended for testing and interacting with the API.

Getting Started

This microservice provides a straightforward API for managing guest records. It is built to handle guest creation, deletion, and retrieval, with additional filtering options based on last name and loyalty points. Designed for easy deployment in Docker containers, it is ideal for use in hotel management systems.
Prerequisites

    Python 3.8+
    VSCode with the Python extension
    Docker for containerized deployment
    Postman for API testing

Installation

    Clone the repository:

    bash

git clone <repository-url>
cd <repository-name>
Endpoints

1. Create a Guest

    URL: '/guests/<int:guest_id>'
    Method: POST
    Request Body:

    json

    {
      "first_name": "string",
      "last_name": "string",
      "email": "string",
      "loyalty_points": integer
    }

    Response:
        201 Created if successful, with the created guest information in the response.

2. Delete a Guest

    URL: 'guests/<int:guest_id>'
    Method: DELETE
    Response:
        200 OK if the guest was deleted.
        404 Not Found if the guest does not exist.

3. Get All Guests

    URL: '/guests'
    Method: GET
    Response:
        200 OK with a list of all guest records.

4. Get Guest by Last Name

    URL: /guests/search
    Method: GET
    Response:
        200 OK with guest records matching the specified last name.
        404 Not Found if no records match the last name.

5. Get Guests by Loyalty Points

    URL: /guests/loyalty/<int:points>
    Method: GET
    Query Parameters:
        min - Minimum loyalty points (optional)
        max - Maximum loyalty points (optional)
    Response:
        200 OK with a list of guests whose loyalty points fall within the specified range.
        404 Not Found if no records match the criteria.

Database

This service connects to a SQL database that stores guest information. The database schema includes:

    Guest ID: Unique identifier for each guest
    First Name: First name of the guest
    Last Name: Last name of the guest
    Country: Country of the guest
    Email: Contact email for the guest
    Phone: Guests phone number
    Loyalty Points: Loyalty points accumulated by the guest
    Review: Comment made by the guest through review microservice
