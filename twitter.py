import re

url = input("URL:  ").strip()
print(url)

# username = url.replace("https://twitter.com/", "")
# username = url.removeprefix("https://twitter.com/")
# username = re.sub(r"^https?://(www\.)?twitter\.com/", "", url)
# print(f"Username: {username}")

# username = re.search(r"^https?://(www\.)?twitter\.com/([A-Za-z0-9_]+)$", url, re.IGNORECASE)
# if username:
#     print(f"Username: {username.group(2)}")    

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([A-Za-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")