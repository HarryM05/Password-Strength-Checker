import string
def password_check(password):
    #Check password length
    if len(password) < 8:
        print("Password should be contain more than 8 characters.")
        return
    
    #Check password contains digits
    if not any(char.isdigit() for char in password):
        print("Password should contain digit's.")
        return
    
    #Check password contains upper/lower case letters
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        print("Password should contain upper and lower case letters.")
        return
    
    #Check password contains special characters
    if not any(char in string.punctuation for char in password):
        print("Password should contain special characters.")
        return
    
    print("Password passes criteria")
    print("Calculating Strength...")
    calculate_strength(password)

def calculate_strength(password):
    #Sum of all unique characters that can be used in the password
    total_character_set = len(string.ascii_letters + string.digits + string.punctuation)

    #Calculates the total amount of combinations
    combinations = total_character_set ** len(password)

    #Calculates strength value, which is the same as time to crack
    #attempts_per_second value is based on a 2020 article
    attempts_per_second = 100000000000
    strength = combinations / attempts_per_second

    #Converts time
    if strength < 60:
        print(str(round(strength, 2)) + " seconds to crack")

    elif strength < 3600:
        print(str(round(strength/60, 2)) + " minutes to crack")

    elif strength < 86400:
        print(str(round(strength/3600, 2)) + " hours to crack")

    elif strength < 604800:
        print(str(round(strength/86400, 2)) + " days to crack")

    elif strength < 31536000:
        print(str(round(strength/604800, 2)) + " weeks to crack")

    else:
        print(str(round(strength/31536000, 2)) + " years to crack")

    
password_input = input("Enter Password: ")
password_check(password_input)