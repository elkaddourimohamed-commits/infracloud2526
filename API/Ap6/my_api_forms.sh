#!/usr/bin/env bash
set -euo pipefail

# Basis-URL van de demo API
BASE_URL="https://httpbin.org"

# Hulpfuncties
line() { echo "--------------------------------------------"; }
pause() { read -r -p "Druk op Enter om verder te gaan..."; }
clear_screen() { printf "\033c"; }

# Statuscode extraheren uit response
extract_status() {
  sed -n '1{s/.* \([0-9][0-9][0-9]\).*/\1/p; q;}'
}

# Controleer of curl geïnstalleerd is
require_tools() {
  command -v curl >/dev/null 2>&1 || { echo "Fout: curl is niet geïnstalleerd."; exit 1; }
}

# Menu tonen
menu() {
  clear_screen
  echo "============================================"
  echo " EIGEN REST API EXPERIMENT - CURL FORMS "
  echo "============================================"
  echo "1) POST formulier sturen"
  echo "2) GET request testen"
  echo "q) Stoppen"
  line
}

# GET request uitvoeren
get_ping() {
  echo "GET: $BASE_URL/get"
  line
  resp="$(curl -sS -i "$BASE_URL/get")"
  status="$(printf "%s" "$resp" | extract_status)"
  printf "%s\n" "$resp"
  line
  echo "HTTP status: $status"
}

# POST form sturen
post_form() {
  read -r -p "Voornaam: " first_name
  read -r -p "Achternaam: " last_name
  read -r -p "Email: " email
  read -r -p "Bericht: " msg

  # Validatie
  if [[ -z "$first_name" || -z "$last_name" || -z "$email" || -z "$msg" ]]; then
    echo "Vul alle velden in!"
    return
  fi

  echo "POST multipart/form-data naar: $BASE_URL/post"
  line

  resp="$(curl -sS -i -X POST "$BASE_URL/post" \
    -F "first_name=$first_name" \
    -F "last_name=$last_name" \
    -F "email=$email" \
    -F "message=$msg")"

  status="$(printf "%s" "$resp" | extract_status)"
  printf "%s\n" "$resp"
  line
  echo "HTTP status: $status"
  echo "Controle: je formvelden staan in de JSON response onder \"form\"."
}

# Hoofdprogramma
main() {
  require_tools

  while true; do
    menu
    read -r -p "Kies een optie: " choice
    case "$choice" in
      1) post_form; pause ;;
      2) get_ping; pause ;;
      q|Q) echo "Programma afgesloten."; exit 0 ;;
      *) echo "Ongeldige keuze."; pause ;;
    esac
  done
}

main
