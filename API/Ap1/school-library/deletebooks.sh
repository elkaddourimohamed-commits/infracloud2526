!/usr/bin/env bash

APIKEY="cisco|0X4Vg_8Ofy52Be2vBRK0cc7JHESVdyGYnjYFS1skZLM"

for BOOK in {0..100}
do
  echo $BOOK
  DELETE_URL="http://library.demo.local/api/v1/books/$BOOK"
  echo $DELETE_URL
  curl -X DELETE $DELETE_URL \
    -H "accept: application/json" \
    -H "X-API-Key: $APIKEY" \
    -H "Content-Type: application/json"
done