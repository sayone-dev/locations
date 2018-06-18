# locations
A web service where employees have an ability to log their locations (Lat Long).

System Requirements
------------

-  Python (3.5)

Set proejct for development
------------

- clone the project.
- Create virtualenv and activate.
- cd path-to-project/
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver


End points available
------------

- To get the JWT token: http://localhost:8000/api-token-auth/
	- METHOD: POST
	- PARAMS: username, password
	- example request: curl -X POST -d "username=admin&password=asdf1234" http://localhost:8000/api-token-auth/
	- example response:    {"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MjkzMzE2NTEsImVtYWlsIjoic2FuZGVlcC5zYXlvbmVAZ21haWwuY29tIiwidXNlcm5hbWUiOiJhZG1pbiIsInVzZXJfaWQiOjF9.Zs1WqNdPYyCruXKlRbgmwOMWt-t3Qo6nZG8kPShlxxw"}

- To Add a location: http://localhost:8000/locations/
	- METHOD: POST
	- PARAMS: name, latitude, longitude
	- HEADER: Authorization: JWT <token>
	- example request: curl --header "Authorization:JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MjkzMzE2NTEsImVtYWlsIjoic2FuZGVlcC5zYXlvbmVAZ21haWwuY29tIiwidXNlcm5hbWUiOiJhZG1pbiIsInVzZXJfaWQiOjF9.Zs1WqNdPYyCruXKlRbgmwOMWt-t3Qo6nZG8kPShlxxw" -X POST -d "name=California&latitude=32.44432&longitude=76.343434" http://localhost:8000/locations
	- example response:{"user":1,"name":"California","latitude":"32.444320000000000","longitude":"76.343434000000000"}

- To list locations: http://localhost:8000/locations/
	- METHOD: GET
	- PARAMS (OPTIONAL): created_0, created_1
	- HEADER: Authorization: JWT <token>
	- example request: curl --header "Authorization:JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE1MjkzMzI3MjEsImVtYWlsIjoic2FuZGVlcC5zYXlvbmVAZ21haWwuY29tIiwidXNlcm5hbWUiOiJhZG1pbiJ9.kk35ffheUXor2nVVheCrZ6qeDyKfHnLTiaceLCCXivs" -X GET http://127.0.0.1:8000/locations/?created_0=06/17/2018&created_1=06/20/2018
	- example response: [{"user":1,"name":"California","latitude":"32.444320000000000","longitude":"76.343434000000000"},]

