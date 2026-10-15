import requests

base_url = "https://jsonplaceholder.typicode.com"

def get_all_posts():
    """Haalt alle posts op via de REST API"""
    url = f"{base_url}/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Fout bij ophalen van posts.")
        print("Statuscode:", response.status_code)
        return None

def get_post_by_id(post_id):
    """Haalt één specifieke post op via ID"""
    url = f"{base_url}/posts/{post_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Post niet gevonden.")
        return None

def main():
    # 1. Alle posts ophalen
    posts = get_all_posts()
    
    if posts is None:
        return

    print("Lijst van posts:\n")
    for post in posts[:5]:  # toon slechts 5 voor overzicht
        print("ID   :", post["id"])
        print("Titel:", post["title"])
        print("Body :", post["body"][:50] + "...")  # eerste 50 tekens
        print("-" * 30)

    # 2. Specifieke post opvragen
    while True:
        user_input = input("\nVoer een post-ID in (of druk op 'q' om te stoppen): ")
        if user_input.lower() == "q":
            print("\nProgramma gedaan")
            break

        if not user_input.isdigit():
            print("Voer een geldig nummer in.")
            continue

        post_id = int(user_input)
        post = get_post_by_id(post_id)

        if post:
            print("\nGevonden post:")
            print("Titel:", post["title"])
            print("Body :", post["body"])

if __name__ == "__main__":
    main()
