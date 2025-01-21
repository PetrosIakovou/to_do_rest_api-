1. Create the file structure of the project
    - create .venv
    - template folder for .html files
    - static folder for .js, .css, .jpn 
    - models folders where the classes of database tables
    - instance folder created by flask by initialize the app 
    - api folder to put all the routes for the rest api
    - site folder to put all theroutes for the site
    - create the files -> Dockerfile, docker-compose.ymal, requirements.txt, app.py, extensions.py, error_handlers.py, .gitignore, .flaskenv
2. Write a basic code in the app.py to initialize server
    - make the initialazation using function -> create_app(db_url=None)
3. Write basic routes in the api 
    - use for the begining a built in data structure (dictionary) for the data
    - connect the app and the api routes using blueprints (https://www.youtube.com/watch?v=WhwU1-DLeVw&list=LL)
4. Create the docker file
    - make the binding to the local folder so to monitor real time changes without restart the server
5. Create the database
    - insert the libraries to extensions.py
    - connect (import) the libraries in extensions.py in the app.py and in the database clasees
    - create the classes in the models file better use flask-sqlalchemy v2 approach with mapped data types
    - create the databse and the tables when tha app initialize 
        with app.app_context():
            db.create_all() 
    - change the code in api routes so the data to be stored in the database instead of the dictionary
    - delete the dictionary
6. Insert abort and try except control where it needs
7. Start build the JWT token authedication for users  (https://www.youtube.com/watch?v=aX-ayOb_Aho)