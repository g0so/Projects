# leetcode_api.py
# Handles fetching the daily coding problem from LeetCode's public GraphQL API.

import requests
from bs4 import BeautifulSoup

LEETCODE_GRAPHQL_URL = "https://leetcode.com/graphql"

# The GraphQL query we send to LeetCode, asking for today's daily challenge.
# This is just a text string - GraphQL queries are written in plain text.
DAILY_QUESTION_QUERY = """
query questionOfToday {
  activeDailyCodingChallengeQuestion {
    date
    link
    question {
      title
      difficulty
      content
    }
  }
}
"""


def clean_description(html_content, max_length=300):
    """
    Takes raw HTML (like '<p>Given an array...</p>') and returns
    clean, short plain text suitable for a Discord message.
    """
    # BeautifulSoup parses the HTML and lets us extract just the text,
    # throwing away all the <p>, <code>, <ul> etc. tags.
    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text(separator=" ", strip=True)

    # Trim it down so it doesn't make the Discord message too long.
    if len(text) > max_length:
        text = text[:max_length].rsplit(" ", 1)[0] + "..."

    return text


def get_daily_problem():
    """
    Fetches today's LeetCode daily challenge.
    Returns a dictionary with title, difficulty, link, and description.
    Returns None if something goes wrong (so the bot can handle it gracefully).
    """
    try:
        # We send a POST request because GraphQL always uses POST,
        # with our query placed in the JSON body under the "query" key.
        response = requests.post(
            LEETCODE_GRAPHQL_URL,
            json={"query": DAILY_QUESTION_QUERY},
            timeout=10,  # give up after 10 seconds if LeetCode doesn't respond
        )
        response.raise_for_status()  # raises an error if the request failed (e.g. 500 error)

        data = response.json()
        challenge = data["data"]["activeDailyCodingChallengeQuestion"]
        question = challenge["question"]

        return {
            "title": question["title"],
            "difficulty": question["difficulty"],
            "link": "https://leetcode.com" + challenge["link"],
            "description": clean_description(question["content"]),
        }

    except Exception as e:
        # If anything goes wrong (network issue, LeetCode API change, etc.),
        # we print the error for debugging and return None.
        # The bot code will check for None and skip posting rather than crash.
        print(f"[leetcode_api] Failed to fetch daily problem: {e}")
        return None