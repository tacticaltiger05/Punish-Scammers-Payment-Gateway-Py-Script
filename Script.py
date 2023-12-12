# Import the requests library to enable HTTP requests in Python
import requests
import threading  # Import threading to allow concurrent execution

# Define the URL where the POST request will be sent
url = "..."  # Replace "..." with the actual URL

# Define the data to be sent with each POST request
data = {
    # Other data objects can be included here as needed
    'cc_number': '4007000000027',   # Example credit card number
    'cc_expmonth': '08',            # Expiry month of the credit card
    'cc_expyear': '21',             # Expiry year of the credit card
    'cc_cvv': '234'                 # CVV of the credit card
}

# Define a function to perform the POST request
def do_request():
    while True:  # Infinite loop to continuously send requests
        # Fix: Replace 'response' with 'requests' to use the requests library correctly
        response = requests.post(url, data=data).text  # Send a POST request to the specified URL with the provided data
        print(response)  # Print the server's response to the request

# List to store thread objects
threads = []

# Create 1000 threads to perform the request concurrently
for i in range(1000):
    t = threading.Thread(target=do_request)  # Create a new thread targeting the do_request function
    t.daemon = True  # Set the thread as a daemon (background thread)
    threads.append(t)  # Add the thread to the threads list

# Start each thread
for i in range(1000):
    threads[i].start()  # Start the thread at index i

# Wait for all threads to complete
for i in range(1000):
    threads[i].join()  # Wait for the thread at index i to finish execution



