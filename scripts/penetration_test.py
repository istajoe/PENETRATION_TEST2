import requests

def check_headers(url):

    # checks for common security headers

    try:
        response = requests.get(url, timeout=5)
        print(f"\n[+] checking security headers for {url}\n")

        security_headers = [
            "Content-security-policy",
            "x-frame-options",
            "x-content-type-options",
            "strict-transport-security",
            "Referrer-policy"
        ]

        for header in security_headers:
            if header in response.headers:
                print(f"[OK] {header}: {response.headers[header]}")
            else:
                print(f"[MISSING] {header}")

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Could not connect: {e}")

def check_https(url):
    # Ensure HTTPS is enforced

    if not url.startswith("https://"):
        print(f"[WARNING] {url} is not using HTTPS")
    else: 
        print(f"[OK] {url} is using HTTPS")

if __name__ == "__main__":
    target = input("Enter target URL (e.g. https://localhost:5000): ").strip()
    check_https(target)
    check_headers(target)