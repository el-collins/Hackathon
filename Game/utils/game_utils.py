player_inventory = []

game_locations = {
    "forest": {
        "description": "A dense forest with tall trees and a hidden path.",
        "items": ["sword", "shield"]
    },
    "castle": {
        "description": "An ancient castle standing tall amidst the mountains.",
        "items": ["crown", "robe"]
    },
}

def add_item_to_inventory(item_name: str):
    if item_name in player_inventory:
        raise ValueError("Item already in inventory.")
    player_inventory.append(item_name)

def remove_item_from_inventory(item_name: str):
    if item_name not in player_inventory:
        raise ValueError("Item not in inventory.")
    player_inventory.remove(item_name)