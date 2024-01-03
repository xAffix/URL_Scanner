import requests

SAFE_BROWSING_API_KEY = "AIzaSyCwyiJXhkQv0zCP5wmVUQVJ4dD0gPqA3KU" 
SAFE_BROWSING_API_URL = "https://safebrowsing.googleapis.com/v4/threatMatches:find"

def scan_url(url):
    params = {
        'key': SAFE_BROWSING_API_KEY,
    }

    data = {
        "client": {"clientId": "your_client_id", "clientVersion": "1.5.2"},
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }

    try:
        response = requests.post(SAFE_BROWSING_API_URL, params=params, json=data, timeout=5)
        response.raise_for_status()

        if response.status_code == 200:
            matches = response.json().get("matches", [])
            if matches:
                return "URL is potentially unsafe!"
            else:
                return "URL appears to be safe."
        else:
            return f"Error: API request failed with status code {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"Error scanning the URL '{url}': {e}"


if __name__ == "__main__":
    url_to_scan = input("Enter the URL to scan: ")
    result = scan_url(url_to_scan)
    print(result)