email = input("Enter email address: ")

if "@" in email:
    domain = email.split("@")[1]
    print("\nDomain:", domain)
else:
    print("Invalid email address")
