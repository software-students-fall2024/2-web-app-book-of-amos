from src.app import get_db
from bson.objectid import ObjectId

def get_boards_by_user(email: str):
    boards = get_db().boards
    return boards.find({"user": email})

def create_board(user: str, name: str):
    boards = get_db().boards
    return boards.insert_one({"user": user, "name": name, "pedals": []})

def delete_board(id: str):
    boards = get_db().boards
    return boards.delete_one({"_id": ObjectId(id)})

def duplicate_board(id: str):
    boards = get_db().boards
    original_board = boards.find_one({"_id": ObjectId(id)})
    if original_board:
        new_board = original_board.copy()
        new_board.pop('_id')
        new_board['name'] = f"{new_board['name']} - Copy"
        return boards.insert_one(new_board)
    return None

def get_board(id: str):
    boards = get_db().boards
    return boards.find_one({"_id": ObjectId(id)})

def update_board(id: str, name: str, pedals: list):
    boards = get_db().boards
    return boards.update_one(
        {"_id": ObjectId(id)},
        {"$set": {"name": name, "pedals": pedals}}
    )










