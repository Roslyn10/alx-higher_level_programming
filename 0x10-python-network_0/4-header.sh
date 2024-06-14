#/bin/bash
#Takes in a URL as an arguemnet, sends a GET request to the URl, and displays the body of the response.
curl -s "$1" -H X-School-User-Id 98
