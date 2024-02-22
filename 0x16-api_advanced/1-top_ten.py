import requests
import sys
import json

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/top.json?limit=10"
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        r = r.json()
    except json.decoder.JSONDecodeError:
        print("Error: Invalid JSON response from Reddit API")
        return

    if "data" not in r or "children" not in r["data"]:
        print("Error: Invalid JSON response from Reddit API")
        return

    for post in r["data"]["children"]:
        print(post["data"]["title"])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-main.py <subreddit>")
        sys.exit(1)

    top_ten(sys.argv[1])

