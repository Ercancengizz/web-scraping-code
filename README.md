Simple Web Scraper
A simple Python script that fetches and prints the HTML content of a webpage given a URL. This is a basic web scraper designed to help you understand how to fetch web pages and display their content.

Features
Fetches HTML content from a given URL.

Validates if the URL starts with http:// or https://.

Displays the HTML content of the page.

Handles errors gracefully with proper error messages.

Requirements
Python 3.x

requests library

Installation
Clone or download the repository.

You can either clone the repository using Git or download it as a ZIP file.

bash
Copy
Edit
git clone https://github.com/yourusername/simple-web-scraper.git
Install the dependencies (if you don't already have them).

Install the requests library using pip:

bash
Copy
Edit
pip install requests
Usage
Open your terminal or command prompt.

Navigate to the directory where the script is saved.

bash
Copy
Edit
cd path/to/simple-web-scraper
Run the script:

bash
Copy
Edit
python scraper.py
When prompted, enter the URL of the webpage you want to scrape. For example:

bash
Copy
Edit
Please enter the URL: https://example.com
If the request is successful, the HTML content of the page will be printed in the terminal. For example:

bash
Copy
Edit
HTML Content:

<!DOCTYPE html>
<html>
<head>
    <title>Example Domain</title>
</head>
<body>
    <div>
        <h1>Example Domain</h1>
        <p>This domain is for use in illustrative examples in documents.</p>
    </div>
</body>
</html>
Error Handling
Invalid URL: If the URL doesn't start with http:// or https://, you'll see an error message.

Example:

bash
Copy
Edit
Invalid URL! Please make sure the URL starts with 'http://' or 'https://'.
Page Load Error: If the page cannot be loaded (e.g., the server returns a 404 or 500 status), the status code will be printed.

Example:

bash
Copy
Edit
Page could not be loaded. HTTP Status Code: 404
Network Errors: If there are issues with the network (e.g., no internet connection), you'll get an error message explaining the problem.

Example:

bash
Copy
Edit
Error: NetworkError: Could not connect to the site.
