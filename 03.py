def get_person_details():
    """
function to read a persons details from the keyboard.
    """
    name =input ("enter your name:")
    address =input("enter your address:")
    email=input ("enter your email:")
    phone =input ("enter your phone number:")
    return name,address,email,phone
def print_person_details(name,address,email,phone):
    """
    function to print a preson s details"
    """
    print("\n--personal Details---")
    print(f"Address:{address}")
    print(f"Email:{email}")
    print(f"phone number:{phone}")
#Getdetails from the user
name,address,email,phone = get_person_details()
#print the details
print_person_details(name,address,email,phone)
