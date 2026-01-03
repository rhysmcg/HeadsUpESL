import os
import json
import requests

# The JSON data mapped to your specific list
animal_data = [
    {"id": 1, "name": "cat", "emoji_hex": "1f408"},
    {"id": 2, "name": "frog", "emoji_hex": "1f438"},
    {"id": 3, "name": "chicken", "emoji_hex": "1f414"},
    {"id": 4, "name": "turtle", "emoji_hex": "1f422"},
    {"id": 5, "name": "crab", "emoji_hex": "1f980"},
    {"id": 6, "name": "rabbit", "emoji_hex": "1f407"},
    {"id": 7, "name": "shark", "emoji_hex": "1f988"},
    {"id": 8, "name": "crocodile", "emoji_hex": "1f40a"},
    {"id": 9, "name": "giraffe", "emoji_hex": "1f992"},
    {"id": 10, "name": "cow", "emoji_hex": "1f404"},
    {"id": 11, "name": "horse", "emoji_hex": "1f40e"},
    {"id": 12, "name": "butterfly", "emoji_hex": "1f98b"},
    {"id": 13, "name": "bull", "emoji_hex": "1f402"},
    {"id": 14, "name": "pig", "emoji_hex": "1f416"},
    {"id": 15, "name": "rhino", "emoji_hex": "1f98f"},
    {"id": 16, "name": "sheep", "emoji_hex": "1f411"},
    {"id": 17, "name": "snake", "emoji_hex": "1f40d"},
    {"id": 18, "name": "panda", "emoji_hex": "1f43c"},
    {"id": 19, "name": "fish", "emoji_hex": "1f41f"},
    {"id": 20, "name": "penguin", "emoji_hex": "1f427"},
    {"id": 21, "name": "tiger", "emoji_hex": "1f405"},
    {"id": 22, "name": "duck", "emoji_hex": "1f986"},
    {"id": 23, "name": "bat", "emoji_hex": "1f987"},
    {"id": 24, "name": "dragon", "emoji_hex": "1f409"},
    {"id": 25, "name": "fox", "emoji_hex": "1f98a"},
    {"id": 26, "name": "elephant", "emoji_hex": "1f418"},
    {"id": 27, "name": "spider", "emoji_hex": "1f577"},
    {"id": 28, "name": "fly", "emoji_hex": "1fab0"},
    {"id": 29, "name": "mouse", "emoji_hex": "1f401"},
    {"id": 30, "name": "monkey", "emoji_hex": "1f412"},
    {"id": 31, "name": "bird", "emoji_hex": "1f426"},
    {"id": 32, "name": "dog", "emoji_hex": "1f415"},
    {"id": 33, "name": "skunk", "emoji_hex": "1f9a8"},
    {"id": 34, "name": "eagle", "emoji_hex": "1f985"},
    {"id": 35, "name": "swan", "emoji_hex": "1f9a2"},
    {"id": 36, "name": "bee", "emoji_hex": "1f41d"},
    {"id": 37, "name": "tortoise", "emoji_hex": "1f422"},
    {"id": 38, "name": "wolf", "emoji_hex": "1f43a"},
    {"id": 39, "name": "lion", "emoji_hex": "1f981"},
    {"id": 40, "name": "owl", "emoji_hex": "1f989"},
    {"id": 41, "name": "caterpillar", "emoji_hex": "1f41b"},
    {"id": 42, "name": "gorilla", "emoji_hex": "1f98d"},
    {"id": 43, "name": "hippo", "emoji_hex": "1f99b"},
    {"id": 44, "name": "goat", "emoji_hex": "1f410"},
    {"id": 45, "name": "snail", "emoji_hex": "1f40c"},
    {"id": 46, "name": "beetle", "emoji_hex": "1fab2"},
    {"id": 47, "name": "kangaroo", "emoji_hex": "1f998"},
    {"id": 48, "name": "parrot", "emoji_hex": "1f99c"},
    {"id": 49, "name": "whale", "emoji_hex": "1f40b"},
    {"id": 50, "name": "grasshopper", "emoji_hex": "1f997"},
    {"id": 51, "name": "ant", "emoji_hex": "1f41c"},
    {"id": 52, "name": "camel", "emoji_hex": "1f42a"},
    {"id": 13, "name": "lizard", "emoji_hex": "1f98e"},
    {"id": 54, "name": "rat", "emoji_hex": "1f400"},
    {"id": 55, "name": "zebra", "emoji_hex": "1f993"},
    {"id": 56, "name": "donkey", "emoji_hex": "1facf"},
    {"id": 57, "name": "scorpion", "emoji_hex": "1f982"},
    {"id": 58, "name": "squirrel", "emoji_hex": "1f43f"},
    {"id": 59, "name": "bear", "emoji_hex": "1f43b"},
    {"id": 60, "name": "dolphin", "emoji_hex": "1f42c"},
    {"id": 61, "name": "octopus", "emoji_hex": "1f419"},
    {"id": 62, "name": "deer", "emoji_hex": "1f98c"},
    {"id": 63, "name": "peacock", "emoji_hex": "1f99a"}
]

# Create directory
folder = "images"
if not os.path.exists(folder):
    os.makedirs(folder)

print(f"Starting download of {len(animal_data)} images...")

for animal in animal_data:
    hex_code = animal["emoji_hex"]
    name = animal["name"].replace(" ", "_")
    url = f"https://fonts.gstatic.com/s/e/notoemoji/latest/{hex_code}/512.png"
    
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            filename = f"{folder}/{hex_code}.png"
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to find image for {name} (Hex: {hex_code})")
    except Exception as e:
        print(f"Error downloading {name}: {e}")

print("Done!")
