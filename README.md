# schoolweb
School Web with Many to Many Relations with the use of Generic Views

Which will allow you to CREATE Many-to-Many Relation in POST from DRF's Browsable api

How to setup project

1. Extract the zip schoolweb.zip
2. cd schoolweb
3. Install the requirements
pip install -r requirements.txt
4. To run the project
python manage.py runserver

For Documentation :
http://127.0.0.1:8000/docs/

Admin URL: http://127.0.0.1:8000/admin/
create a super user for you
python manage.py createsuperuser

Api Root URL: http://127.0.0.1:8000/api/

List all Students: 
Allow: GET, POST, HEAD, OPTIONS
URL: http://127.0.0.1:8000/api/students/

Student Resource: 
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
URL: http://127.0.0.1:8000/api/students/<pk>/ 

List all Schools: 
Allow: GET, POST, HEAD, OPTIONS
URL: http://127.0.0.1:8000/api/schools/

School Resource: 
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
URL: http://127.0.0.1:8000/api/schools/<pk>/
