import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    url = input("🔗 Enter the news website URL: ").strip()
    tag = input("🏷️  Enter the HTML tag used for headlines (e.g., h2, h3, title): ").strip()

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("❌ Failed to fetch the page:", e)
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(tag)

    headlines = [elem.get_text(strip=True) for elem in elements if elem.get_text(strip=True)]

    if headlines:
        with open("headlines.txt", "w", encoding="utf-8") as file:
            for i, headline in enumerate(headlines, 1):
                file.write(f"{i}. {headline}\n")

        print(f"\n✅ {len(headlines)} headlines saved to 'headlines.txt'")
        print("\n📰 Headlines:\n")
        for i, headline in enumerate(headlines, 1):
            print(f"{i}. {headline}")
    else:
        print("⚠️ No headlines found. Try using a different tag.")

if __name__ == "__main__":
    scrape_headlines()
