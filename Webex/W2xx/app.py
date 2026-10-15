from utils import get, post, delete
import json

def list_rooms():
    res = get("rooms", params={"max": 50})
    for room in res.get("items", []):
        print(f"{room['id']} - {room['title']}")
    return res

def create_room(title):
    data = {"title": title}
    res = post("rooms", data)
    print("Room created:", res)
    return res.get("id")

def delete_room(room_id):
    status = delete(f"rooms/{room_id}")
    print(f"Room {room_id} deletion status: {status}")

def list_members(room_id):
    res = get("memberships", params={"roomId": room_id})
    for m in res.get("items", []):
        print(f"{m['personEmail']} ({m['id']})")
    return res

def add_member(room_id, email):
    data = {"roomId": room_id, "personEmail": email}
    res = post("memberships", data)
    print("Member added:", res)

def send_message(room_id, text):
    data = {"roomId": room_id, "markdown": text}
    res = post("messages", data)
    print("Message sent:", res)

if __name__ == "__main__":
    print("===== W2 Webex Experiment =====")
    print("1. List Rooms")
    print("2. Create Room")
    print("3. Delete Room")
    print("4. List Members")
    print("5. Add Member")
    print("6. Send Message")
    choice = input("Choose action: ")

    if choice == "1":
        list_rooms()
    elif choice == "2":
        title = input("Room title: ")
        create_room(title)
    elif choice == "3":
        room_id = input("Room ID to delete: ")
        delete_room(room_id)
    elif choice == "4":
        room_id = input("Room ID: ")
        list_members(room_id)
    elif choice == "5":
        room_id = input("Room ID: ")
        email = input("Member email: ")
        add_member(room_id, email)
    elif choice == "6":
        room_id = input("Room ID: ")
        message = input("Message to send: ")
