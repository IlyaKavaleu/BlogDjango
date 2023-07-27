To Do Woo
How started my project on your local server?
The project for study Django.<

Stack:
- Python - SqLite - Redis - Local Developing All actions should be executed from the source directory of the project and only after installing all requirements.
Firstly, create and activate a new virtual environment:
python3.9 -m venv ../venv source ../venv/bin/activate

Install packages:
pip install --upgrade pip

pip install -r requirements.txt

Run project dependencies, migrations, fill the database with the fixture data etc.:
./manage.py migrate ./manage.py loaddata <path_to_fixture_files>

Run Redis Server:
redis-server
Run Celery:
celery -A store worker --loglevel=INFO
After completing the steps follow the link -- http://127.0.0.1:8000/
ToDoWoo for tasks.
The “to do woo” program is designed to create a list of tasks. The program helps to manage to-do lists, implement planned tasks and not forget anything. The user has the ability to create a list of tasks, in the process of their execution, can change, delete, complete. The program is implemented in the Python programming language using:
Django;
Redis;
HTML;
CSS;
Description of the program interface: When the “New todo” button is clicked, the createtodo event handler invokes a modal window to create a task. The window contains fields for title, description, priority selection, saving and returning to the main menu. There is a limit on the number of characters on the field for entering the name, if the number of characters entered matches the maximum number, are checked using the max_length attribute. In the modal window, the user has a warning label for the maximum number of input characters. The project was implemented using caching, in my case "Redis", also for convenience, the tool "Django-Toolbar" was used, object-oriented programming, framework Django, HTML, CSS, Python, SqLite(default), TestCase.

Modal window for creating a task. The “Save” button, if all fields are filled, calls the createtodo () function in which the markup of the task is generated with all the entered values and by choosing to change the state of the task. createtodo_1
Ability to change the importance of the task. createtodo_2
A generated block with a task. Working with the task block. The block of each task contains information: Name; Description; A priority; Task state change menu.
Menu for working with the task. Option "Done" - completes work on the task, makes its menu inactive. Option "Edit" - causes the generation of a modal window for editing. The user can change: title, description, priority, keep or refuse changes. Option “Delete“ - deletes the task. crearedtodo_3

Task editing window. Also in the task name input field, we can change it, as well as descriptions. You can also change the task status from “Important” to “Minor”. Also, when choosing to change the importance of a task, the color of the task changes - from white to red! edittodo_4
List of current tasks, which is formed using the "currenttodos" method. currenttodos_5
List of completed tasks, which is formed using the “completetodos“ method. completetodos_6
Registration. By clicking on the “Sign Up“ button, we will go to the user registration window with the following fields: -username -password 1 -password 2 The password will need to be repeated. After filling in the fields and upon successful registration, we are redirected to the main page with current tasks.
Authorization By clicking on the “Login“ button, we will go to the user logging window with the following fields: -username -password After filling in the fields and upon successful authorization, we are also redirected to the main page with current tasks. authorization_8
Exit the session using the “Logout“ button. logout_9
Library tests were imposed on the project “UnitTest“. For example, a test for successful user registration is taken: Have a check:
page status
redirect url
absence of a user
user presence
check by message(fail) for an error tests_10 png
