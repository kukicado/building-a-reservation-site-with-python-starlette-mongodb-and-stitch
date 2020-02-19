# Building a Property Booking Website with Starlette, MongoDB, and Twilio

This codebase is the completed code for an article that covers how to build a web application with Starlette, MongoDB and Twilio. The app you will build is called MongoBnB. The app is a an AirBnB style application that allows users to view bookings and make reservations. Read the article to find out how and why.

![MongoBnB](./article/images/mongobnb.png)

## Prerequisites

- Python 3+
- MongoDB. Try [MongoDB Atlas](https://www.mongodb.com/atlas) for free. You can use code **ADO200** for a $200 credit.
- Twilio

## Building the Application

1. Clone the repo
2. Navigate to the `mongobnb` directory.
3. Install dependencies
4. Run `uvicorn app:app` to start the local development server.
5. Update the `{YOUR-CONNECTION-STRING}` string in the `middleware.py` file 
6. Ensure the `client['{DATABASE-NAME}']` string in the `middleware.py` file matches the database name you wish to use.

Navigate to `localhost:8000` to see your application in action. 
