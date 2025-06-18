name=input("enter your name: ")
email=input("enter your email: ")
if len(name)<=2:
    print("the name length must be more than 2 characters, please provide a valid name.")
elif "@" not in email or "." not in email:
    print("the email is not valid , please provide a valid email .")
else:
    print(f"welcome {name}, you registered with the email{email}")