import json

def rw_credentials():
    choice = input("[1] use current defaults\n[2] create new credentials\n")
    credential_dictionary = {}
    with open("credentials.json") as file:
        defaults = json.load(file)
        # print is just for testing
        print("current defaults")
        print(defaults)

    if int(choice) == 1:
        with open("credentials.json") as file:
            defaults = json.load(file)
        return defaults

    if int(choice) == 2:
        credential_dictionary["firstName"] = input("\nfirst name: ")
        credential_dictionary["lastName"] = input("last name: ")
        credential_dictionary["street"] = input("street: ")
        credential_dictionary["house_number"] = input("house number: ")
        credential_dictionary["city"] = input("city: ")
        credential_dictionary["ZIP"] = input("ZIP: ")
        credential_dictionary["state"] = input("state: ")
        credential_dictionary["email"] = input("email: ")
        credential_dictionary["cellphone"] = input("cellphone: ")

        with open("credentials_new.json", "w") as file:
            json.dump(credential_dictionary, file, indent=4)

        return credential_dictionary

#rw_credentials()
