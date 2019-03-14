
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
```sh
$ cd todoapp
$ python3 manage.py runserver
```

Rest API to add, delete and update the TODO List.
```python
url(r'^api-auth/$', TodoAppView.as_view(), name="TodoAppView")
```

If you visit the http://localhost:8000/api-auth/
We can see the following :
![Rest API](https://user-images.githubusercontent.com/25399528/54344004-12f27980-4666-11e9-9a19-ab14f831ece8.png)
