import requests
import time

# List your Nightingale subdomains
URLS = [
    "https://vault.nightingaleint.com",
    "https://hh.nightingaleint.com",
    "https://living.nightingaleint.com",
    "https://twn.nightingaleint.com"
]

def wake_up():
    for url in URLS:
        try:
            response = requests.get(url, timeout=10)
            print(f"Pinged {url}: Status {response.status_code}")
        except Exception as e:
            print(f"Failed to ping {url}: {e}")

if __name__ == "__main__":
    while True:
        wake_up()
        # Ping every 14 minutes (Render sleeps after 15)
        time.sleep(14 * 60)
