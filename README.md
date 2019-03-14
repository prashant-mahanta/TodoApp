
How to run this TODO APP? 

First download it to your local machine
```sh
$ git clone https://github.com/prashant-mahanta/TodoApp.git
```
```sh
$ cd TodoApp
```
activate virtual environment
```sh
$ source ./env/bin/activate 
```

If you already have PostgreSQL (else visit [here](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04) )
Create PostgreSQL Database for the project:
```sh
$ sudo su - postgres
$ psql

Create a database and user
$ CREATE DATABASE todo;
$ CREATE USER todouser WITH PASSWORD 'pass';

All we need to do is give our database user access rights to the database we created:
$ GRANT ALL PRIVILEGES ON DATABASE todo TO todouser;
$ \q
$ exit
```

```sh
$ cd todoapp
$ python3 manage.py runserver
```

Rest API to add, delete and update the TODO List.
```python
url(r'^api-auth/$', TodoAppView.as_view(), name="TodoAppView")
```

If we visit the http://localhost:8000/api-auth/

We can see the following :
![Rest API](https://user-images.githubusercontent.com/25399528/54344004-12f27980-4666-11e9-9a19-ab14f831ece8.png)


# Demo (User Interface)
![TODO API INTERFACE](https://user-images.githubusercontent.com/25399528/54344287-84cac300-4666-11e9-98b6-65aa247e0b76.gif)

## Work FLow in the demo
1. User Login/Register
2. Add or Delete or Update TODO LIST (through API, api developed using django restframework)

Task Remaining:

3. Mail the user as soon as it is time for his schedule (working.. getting some error, using django celery)

4. Mark complete or incomplete schedules and show them to the user every 10 hr.
