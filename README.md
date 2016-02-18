# CaesarCipher
The task was to build single-page application which allows users 
to encode/decode some message with Caesar cipher.

The App must have frontend and backend parts and must use AJAX.
Encoding/decoding must run on server-side.
Programming language on server can be:  php, python, ruby, etc.
		( I used python3 )
Data exchange between web-page and server must use JSON format.

-------------------------------------------------------------------
To run this App on your local PC you must:
1)Unpack folder on PC with installed Python3.
	Go into the folder.
2)Run local web-server: there is one in folder
	IN WINDOWS:
		Run 'webserver.py' - a black console window must appear.
	IN LINUX:
		Allow executing rights for:
			webserver.py
			cgi-bin/index.py
		Then run 'webserver.py' in console:
			python3 startserver.py

3) Work with the App:
Run browser and go to this page: http://localhost:8000/
