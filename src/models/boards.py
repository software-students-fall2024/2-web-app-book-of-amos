
from src.app import get_db
from bson.objectid import ObjectId

class Board():
    def __init__(self, user, pedals: list[list], name) -> None:
        self.user = user
        self.pedals = pedals
        self.name = name

def get_boards_by_user(email:str):
    boards = get_db().boards
    return boards.find({"user":email})

def create_board(user:str, name:str):
    new_board = Board()
    new_board.user = user
    new_board.name = name
    boards = get_db().boards
    return boards.insert_one({"user": user, "name": name})

def delete_board(id: str):
    boards = get_db().boards
    return boards.delete_one( {"_id": ObjectId(id)})

def duplicate_board(id: str):
    boards = get_db().boards
    original_board = boards.find_one({"_id": ObjectId(id)})
    return boards.insert_one({"user": original_board['user'] , "name": original_board['name'] + " - Copy", "pedals": original_board['pedals']})
