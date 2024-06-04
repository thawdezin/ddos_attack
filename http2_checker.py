import httpx

def check_http2(url):
    try:
        # Create a client with HTTP/2 enabled
        with httpx.Client(http2=True) as client:
            response = client.get(url)
            # Checking if the response uses HTTP/2
            if response.http_version == "HTTP/2":
                print(f"The website {url} is using HTTP/2.")
            else:
                print(f"The website {url} is not using HTTP/2. It is using {response.http_version}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Ask for URL input
website_url = input("Please enter the website URL: ")
check_http2(website_url)
