import requests

def main():
    # Ask the user for the URL
    url = input("Please enter the URL: ")

    # Validate the URL
    if not url.startswith(('http://', 'https://')):
        print("Invalid URL! Please make sure the URL starts with 'http://' or 'https://'.")
        return

    try:
        # Fetch the HTML content from the URL
        response = requests.get(url)

        # If the request was successful, print the HTML content
        if response.status_code == 200:
            print("HTML Content:\n")
            print(response.text)
        else:
            print(f"Page could not be loaded. HTTP Status Code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
