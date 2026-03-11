import re

email = input("Enter your email address: ").strip();

# if "@" not in email or "." not in email:
#     print("Invalid email address")
# else:
#     print("Valid email address")    

# username, domain = email.split("@")

# if username and "." in domain:
#     print(f"Username: {username}")
# else:
#     print("Invalid email address: missing username")

if re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
    print("Valid email address")
else:
    print("Invalid email address")


