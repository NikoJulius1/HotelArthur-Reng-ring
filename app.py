import requests

# Fetch and print room bookings
def fetch_bookings():
    try:
        response = requests.get("http://localhost:5000/bookings")
        response.raise_for_status()  # Raise an error for bad status codes
        bookings = response.json()
        print("Rooms that need cleaning or preparation:")
        for booking in bookings:
            print("Room:", booking[1], "| Check-In:", booking[4], "| Check-Out:", booking[5])
    except requests.exceptions.RequestException as e:
        print("Error fetching bookings:", e)

if __name__ == "__main__":
    fetch_bookings()
