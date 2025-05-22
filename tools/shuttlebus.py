\
import requests
import json

def get_latest_shuttle_info():
    """
    Fetches the latest shuttlebus location for Sungkyunkwan University.

    Returns:
        dict: The JSON response as a Python dictionary if successful.
        str: An error message string if fetching or parsing fails.
    """
    url = "http://route.hellobus.co.kr:8787/pub/routeView/skku/getSkkuLoc.aspx"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4XX or 5XX)
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.ConnectionError as conn_err:
        return f"Connection error occurred: {conn_err}"
    except requests.exceptions.Timeout as timeout_err:
        return f"Timeout error occurred: {timeout_err}"
    except requests.exceptions.RequestException as req_err:
        return f"An unexpected error occurred with the request: {req_err}"
    except json.JSONDecodeError:
        return "Error: Failed to decode JSON from response."

if __name__ == "__main__":
    result = get_latest_shuttle_info()
    if isinstance(result, dict):
        # Pretty print the JSON
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        # Print the error message
        print(result)
