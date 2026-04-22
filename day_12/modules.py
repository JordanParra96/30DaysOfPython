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
