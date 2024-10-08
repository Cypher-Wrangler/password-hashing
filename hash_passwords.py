import bcrypt

# function to hash a password

def hash_password(plain_password):
    salt = bcrypt.gensalt() #generate a salt
    hashed_password = bcrypt.hashpw(plain_password.encode(), salt) #hash the password with salt
    return hashed_password

#function to verify a password
def verify_password(plain_password, hashed_password)
     return bcrypt.checkpw(plain_password.encode(), hashed_password) #verify password against hash

if _name_ == "_main_":
    #input password
    password = input("Enter a password to hash: ")

    #hash password
    hashed = hash_password(password)
    print(f"Hashed password: {hashed.decode()}")

    #verify the password
    check_password = input("Enter the password again to verify:")
    if verify_password(check_password, hashed):
        print("password matches!")
    else:
        print("password does not match")
