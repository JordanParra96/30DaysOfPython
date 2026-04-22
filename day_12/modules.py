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


def rgb_color_gen():
    """Generate a random RGB color."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r}, {g}, {b})"


print("RGB Color:", rgb_color_gen())


# Level 2
def list_of_hexa_colors(num_colors):
    """Generate a list of hexadecimal colors."""
    hex_colors = []
    for _ in range(num_colors):
        color = f"#{random.randint(0, 0xFFFFFF):06x}"
        hex_colors.append(color)
    return hex_colors


print("Hexadecimal Colors:", list_of_hexa_colors(5))


def list_of_rgb_colors(num_colors):
    """Generate a list of RGB colors."""
    rgb_colors = []
    for _ in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb_colors.append(f"rgb({r}, {g}, {b})")
    return rgb_colors


print("RGB Colors:", list_of_rgb_colors(5))


def generate_colors(color_type, num_colors):
    """Generate a list of colors based on the specified type (hexa or rgb)."""
    if color_type == "hexa":
        return list_of_hexa_colors(num_colors)
    if color_type == "rgb":
        return list_of_rgb_colors(num_colors)
    raise ValueError("Invalid color type. Use 'hexa' or 'rgb'.")


print("Generated Colors:", generate_colors("hexa", 5))
print("Generated Colors:", generate_colors("rgb", 5))


# Level 3
def shuffle_list(items):
    """Shuffle a list of items."""
    random.shuffle(items)
    return items


print("Shuffled List:", shuffle_list([1, 2, 3, 4, 5]))


def unique_random_numbers():
    """Generate an array of seven unique random numbers in the range of 0-9."""
    numbers = random.sample(range(10), 7)
    return numbers


print("Unique Random Numbers:", unique_random_numbers())
