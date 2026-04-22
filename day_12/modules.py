"""Day 12: 30 Days of python programming"""

# main.py file
import random
import string
import mymodule

print(mymodule.generate_full_name("Asabeneh", "Yetayeh"))  # Asabeneh Yetayeh

# Level 1


def random_user_id():
    """Generate a six digit/character random user ID."""
    characters = string.ascii_letters + string.digits
    user_id = "".join(random.choice(characters) for _ in range(6))
    return user_id


print(random_user_id())


def user_id_gen_by_user():
    """Generate a user ID by asking user for the number of characters and the number of IDs."""
    num_characters = int(input("Enter the number of characters for the user ID: "))
    num_ids = int(input("Enter the number of user IDs to generate: "))
    characters = string.ascii_letters + string.digits
    user_ids = []
    for _ in range(num_ids):
        user_id = "".join(random.choice(characters) for _ in range(num_characters))
        user_ids.append(user_id)
    return user_ids


print("User IDs:", user_id_gen_by_user())
