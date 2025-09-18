import requests
import os

# ---- KONFIG ----
KEYWORDS = ["ed hardy", "ecko", "billabong", "southpole", "fubu"]
MAX_PRICE = 50
DISCORD_WEBHOOK = os.environ["DISCORD_WEBHOOK"]

def check_vinted(keyword):
    url = (
        f"https://www.vinted.pl/vetements?"
        f"search_text={keyword}&price_to={MAX_PRICE}&order=newest_first"
    )
    return url

def main():
    for word in KEYWORDS:
        link = check_vinted(word)
        payload = {
            "content": f"🔎 Nowe oferty dla **{word}** (do {MAX_PRICE} zł, najnowsze): {link}"
        }
        requests.post(DISCORD_WEBHOOK, json=payload)

if __name__ == "__main__":
    main()
