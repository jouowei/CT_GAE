# GAE-Backend
## simple CRUD API to connect to MySQL db on Google App Engine with Cloud SQL

Install the MySQLdb library
sudo apt-get install python-mysqldb

* Create isolated Python environments

    `pip install virtualenv`

    `cd my_project_folder`

    `virtualenv my_project`

    begin by `source my_project/bin/activate` for linx or `.my_project/Scripts/activate`


* clone the repository `git clone https://github.com/cbchien/GAE-backend.git`

* `cd` to directory

* `sudo pip install -t lib -r requirements.txt`

* `pip install flask flask_sqlalchemy flask_migrate`

* `sudo pip install mysql-python==1.2.5 --upgrade -t lib` 
  
* Database Setup if not through Google Cloud SQL panel
    Flask has support for several relational database management systems, including SQLite, MySQL, and PostgreSQL. MySQL is used for this exercise.
    Along with `Flask-SQLAlchemy` (Python-SQL Object Relational Mapper) and `mysqlclient` (Python 3 interface to MySQL. It will help us connect the MySQL database to the app.)
    
    `mysql -u root`
    
    Once in mysql CLI:
    
      `CREATE USER '{username}'@'localhost or {server IP}' IDENTIFIED BY '{password}';
      
      `CREATE DATABASE somedatabasename;`
      
      `GRANT ALL PRIVILEGES ON somedatabasename . * TO '{username}'@'localhost or {server IP}';`
      
      `ALTER USER '{username}'@'localhost or {server IP}' IDENTIFIED WITH mysql_native_password BY 'youpassword';

   
* Migrations allow us to manage changes we make to the models, and propagate these changes in the database. Python package `flask-migrate`

    temparory change app.config['SQLALCHEMY_DATABASE_URI'] to `mysql://[username]:[password]@[instanceIP]/[databaseName]`

    inside terminal, run `export FLASK_APP=main.py`
    
    `flask db init` creates a migrations directory in the project directory
    
    `flask db migrate` creates migration
    
    `flask db upgrade` apply migration

    change app.config['SQLALCHEMY_DATABASE_URI'] to back to `= os.environ['SQLALCHEMY_DATABASE_URI']`


* For running locally,

    set FLASK_APP variable

        For WindowsOS: `set FLASK_APP=basicapi.py`
    
        For MacOS: `export FLASK_APP=basicapi.py`

    run `flask run` in terminal at the directory

* For deploying to Google App Engine,

    update `env_variables` and `beta_settings` in app.yaml

    in Google Cloud cmd

    `gcloud app deploy app.yaml`

    `gcloud app browse`
    

* Update API url in index.html form post

* List of APIs:

      [GET] /delivery                                retrun JSON of all delivery enteries 
      
      [POST] /delivery                               create a delivery entery (fields: businesstype, clientname, order_ID, comment)
      
      [GET] /delivery/<order_id>                     retrun JSON of delivery entry matching `order_id`
      
      [PUT] /delivery/<order_id>                     update delivery entry matching `order_id`
      
      [DELETE] /delivery/<order_id>                  delete delivery entry matching `order_id`
      
      [GET] /shippment                               retrun JSON of all delivery enteries 
      
      [POST] /shippment                              create a delivery entery (fields: ship_ID, contact_info, ship_area, ship_district, driver, car_type, car_ID, is_elevator, floors_byhand, amount_collect, comment)
      
      [GET] /shippment/<ship_id>                     retrun JSON of delivery entry matching `ship_id`
      
      [PUT] /shippment/<ship_id>                     update delivery entry matching `ship_id`
      
      [DELETE] /shippment/<ship_id>                  delete delivery entry matching `ship_id`

References:

* [mbithenzomo](https://github.com/mbithenzomo/project-dream-team-one)

* [MySQLdb User’s Guide](https://mysqlclient.readthedocs.io/user_guide.html#installation)

* [Flask + marshmallow for beautiful APIs](https://flask-marshmallow.readthedocs.io/en/latest/)

* [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/quickstart/)

* [app.yaml Reference](https://cloud.google.com/appengine/docs/standard/python/config/appref)
