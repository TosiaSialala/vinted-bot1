import requests
import os

# ---- KONFIG ----
KEYWORDS = ["Ed Hardy", "Ecko", "Billabong", "Southpole", "Fubu"]
MAX_PRICE = 50
DISCORD_WEBHOOK = os.environ["DISCORD_WEBHOOK"]

def check_vinted(keyword):
    url = (
        f"https://www.vinted.pl/vetements?"
        f"search_text={keyword}&price_to={MAX_PRICE}&order=newest_first"
    )
    return url

def main():
    for brand in KEYWORDS:
        link = check_vinted(brand)
        payload = {
            "content": (
                f"🆕 Nowe oferty dla marki **{brand}** "
                f"(max {MAX_PRICE} zł, sortowanie: najnowsze):\n{link}"
            )
        }
        requests.post(DISCORD_WEBHOOK, json=payload)

if __name__ == "__main__":
    main()
