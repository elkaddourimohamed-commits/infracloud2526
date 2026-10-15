#!/usr/bin/env bash
set -euo pipefail

BASE_URL="https://jsonplaceholder.typicode.com"

# Functie: Alle users ophalen
get_all_users() {
    echo "GET: $BASE_URL/users"
    curl -sS -i "$BASE_URL/users"
}

# Functie: Specifieke user ophalen
get_user_by_id() {
    read -r -p "Geef user ID: " id
    curl -sS -i "$BASE_URL/users/$id"
}

# Functie: Nieuwe post maken
create_post() {
    read -r -p "Titel: " title
    read -r -p "Body: " body
    read -r -p "UserId: " userId

    payload=$(cat <<EOF
{
  "title": "$title",
  "body": "$body",
  "userId": $userId
}
EOF
)
    curl -sS -i -X POST "$BASE_URL/posts" \
        -H "Content-Type: application/json; charset=UTF-8" \
        -d "$payload"
}

# Functie: Post verwijderen
delete_post() {
    read -r -p "Geef post ID om te verwijderen: " id
    curl -sS -i -X DELETE "$BASE_URL/posts/$id"
}

# Main menu
while true; do
    echo "1) GET alle users"
    echo "2) GET user op ID"
    echo "3) POST nieuwe post"
    echo "4) DELETE post"
    echo "q) Stoppen"
    read -r -p "Kies optie: " choice
    case "$choice" in
        1) get_all_users ;;
        2) get_user_by_id ;;
        3) create_post ;;
        4) delete_post ;;
        q|Q) exit 0 ;;
        *) echo "Ongeldige keuze" ;;
    esac
done