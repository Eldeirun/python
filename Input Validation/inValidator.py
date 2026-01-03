#validate user input
#username is not longer than 12 characters
#username must not contain spaces
#username must not contain digits

username = input("Please enter username:")
length = len(username)

check = username.isalpha() #Returns false when there is a digit or a space in the username

if length > 12 or not check:
    print("Invalid username (check for spaces and digits, they do not belong in usernames)!")
else:
    print("Username was accepted.")