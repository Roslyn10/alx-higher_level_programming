0x11-python-network_1

0. What's my status?#0

	A Python script that fetches https://alx-intranet.hbtn.io/status
		* You must use the package urllib
		*Not allowed to import any packages other than urllib
		* The body of the response must be displayed with the tabulation before -
		* Must use a with statement

1. Response header value #0

	A Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found i the header of the response.
		* Must use the packages urllib and sys
		* Not allowed to import packages other than sys and urllib
		* The value of this variable is different for eacrequest
		* Don't need to check arguments passed to the script (number type)
		* Must use a with statement


2. POST an email #0

	A python script that taes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
		* The email must be sent in the email variable
		* Must use packages urllib and sys
		* Not allowed to import packages other than urllib and sys
		* Don't need t check arguments passed to the script (number or type)
		* Must use the with statement


3. Error code #0

	A Python script that takes in  a URL, send a request to the URl and displays the body of the response (decoded in utf-8)
		* Have to manage urllib.error.HTTPError exceptions and print Error code: followed by the HTTP status code
		* Must use the packages urllib and sys
		* Not allowed to import other packages than urllib and sys
		* Don't need to check arguments passed to the script (number or type)
		* Must use the with statement

4. What's my status? #1

	A Python scipt that fetches https://alx-intranet.hbtn.io/status
		* Must use the package requests
		* Not allowed to import packages other than requests
		* The body of the response must be displayed with tabulation before -

5. Response header value #1

	A Python script that takes in a URl, sends a request to the URL and displays the value of the variable  X-Request-Id in the response header
		* Must use the packages requests and sys
		* Not allowed to import other packages other than requests and sys
		* The value of this variable is different for each request
		* Don't need to check script arguments (number and type)

6. POST an eamil #1

	A Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
		* The email must be sent in the variable email			* Must use the packages requests and sys
		* Not allowed to import packages other than requests and sys
		* Don't need to error check arguments passed to the script (number or type)


7. Error code #1

	A Python script that takes in a URL, send a request to the URl and displays the body of the response	
		* If the HTTP status code is greater than or equal to 400, print Error code: followed by the value of the HTTP status code
		* Must use the packages requests and sys
		* Not allowed to import packages other than requests and sys
		* Don't need to check arguments passed to the script (number or type)

8. Search API

	A Python script that takes in a letter and sends a PST request to http://0.0.0.0:5000/search_user with the letter as a parameter
		* The letter must be sent variable q
		* If no argument is given, set q=""
		* If the response body is properly JSON formatted and not empty, display the id and name like this  [<id>] <name>
		* Otherwise:
			* Display Not a valid JSON if the JSON is invalid
			* Display No result if the JSON is empty
		* Must use the package requests and sys
		* NOt allowed to import packages other than requests and sys

9. My Github!

	A Python script that takes your GitHub credentials (username and password) and uses the Github API to display your id
		* Must use Basic Authentication with a personal acess token as password to acess to your information (only read:user permission is needed)
		* The first argument will be your username
		* The secind argument will be your password (in case, a personal access token as password)
		* Must use the package requests and sys
		* Not allowed to import packages other than requests and sys
		* Don't need to check arguments passed to thescript 
