#/bin/bash
#Takes in a URl, sends a POST request to the passed URL, and diplays the body of the response
curl -s "$1" -X POST -d  "email=test@gmail.com&subject=I will always be here for PLD" 
