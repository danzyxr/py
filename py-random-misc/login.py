uid = "Danzyxr"
key = "password123"

# f = open('workfile', 'r+')
# with open('workfile') as f:
#     read_data = f.read()
# f.closed

print("Log in")

username = input("Please enter your username: ")
while (len(username) == 0) and (username.lower() != uid.lower()):
    username = input("Please enter your username: ")

password = input("Please enter your password: ")
while (len(password) == 0) and (password != key):
    password = input("Please enter your password: ")

print(f"Welcome, {username}")
