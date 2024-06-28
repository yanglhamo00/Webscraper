import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL
url = 'https://www.edureka.co/blog/web-scraping-with-python/'

# Send a GET request to fetch the HTML content
response = requests.get(url)

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the data (assuming it's the only table on the page)
table = soup.find('table')

# Check if table is found
if table:
    # Extract data into a DataFrame
    df = pd.read_html(str(table))[0]

    # Save the DataFrame to an HTML file
    html_output = 'table_output.html'
    df.to_html(html_output, index=False)

    # Inform the user
    print(f"Table data has been saved to {html_output}. Open this file in a web browser to view the table.")
else:
    print("No table found on the page.")
