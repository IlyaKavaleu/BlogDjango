<h1>Learning Log</h1>
<h3>How started my project on your local server?</h3>
The project for study Django.

<h3>Stack:</h3>
- Python - SqLite - Redis - Local Developing All actions should be executed from the source directory of the project and only after installing all requirements.
Firstly, create and activate a new virtual environment:
python3.9 -m venv ../venv source ../venv/bin/activate

<h3>Install packages:</h3>
pip install --upgrade pip

pip install -r requirements.txt

<h3>Run project dependencies, migrations.

<h3>Run Redis Server:</h3>
redis-server

<h3>Run Celery:</h3>
celery -A store worker --loglevel=INFO

<h3>After completing the steps follow the link -- http://127.0.0.1:8000</h3>

  
Learning Log for tasks.
The “learning log” program is designed to create information about cars. The program helps to add various cars to the site. The user has the ability to create a list of machines, in the process of their execution can change, delete, supplement. The program is implemented in the Python programming language using:
Django;
Redis;
HTML;
CSS;


1. - First of all, we are greeted by the main page of the site.
     ![mainpage_1](https://github.com/IlyaKavaleu/BlogDjango/assets/97099564/61705f82-dcc8-4383-8e9c-bd1059db04b0)

2. - Click to "Log In" or "Register" go to the authentication page.
     ![pushtoauth_2](https://github.com/IlyaKavaleu/BlogDjango/assets/97099564/ed151b3f-6dc1-4825-a678-ac1d8bcd8280)

3. - Enter the data for authorization or if you do not have an account, click on the register button.
     ![autorithation3](https://github.com/IlyaKavaleu/BlogDjango/assets/97099564/1c491478-4595-4137-9e7d-d74a8c5de71b)

4. - If everything went well, whether it's authorization or registration, we get to the main page of the site with a personal greeting.
     ![mainpage_4](https://github.com/IlyaKavaleu/BlogDjango/assets/97099564/7ced486b-2ae6-4793-9db3-62b0c7c7ed06)

5. - If we click to "Auto Sections" we get to the car categories page. Here I already have added cars.
     ![sections_5](https://github.com/IlyaKavaleu/BlogDjango/assets/97099564/d3afd303-d91e-488c-8136-c32d1be9275c)

6. - By clicking on the model of interest to us on the previous page, we go to the page of this model where we can view it, edit it or delete it.
     ![model_6](https://github.com/IlyaKavaleu/BlogDjango/assets/97099564/d54f6df9-92ab-4ecf-bb1c-4f5e230e39e3)

7. - Сlick to go to the model of interest to us. Example Bugatti Chiron.
     ![gotomodel_7](https://github.com/IlyaKavaleu/BlogDjango/assets/97099564/ebefbf75-ebd1-4501-9dd7-62799596c1c5)

8. - Our model.
     ![ourmodel_8](https://github.com/IlyaKavaleu/BlogDjango/assets/97099564/1ccf8d87-5bb2-46c1-9281-1d7be1ae8ce8)

9. - Also we can edit model.
![editmodel_9](https://github.com/IlyaKavaleu/BlogDjango/assets/97099564/0ce62519-be39-4e32-affc-67216a9ce452)

10. - Or section.
    ![editsection_10](https://github.com/IlyaKavaleu/BlogDjango/assets/97099564/1cd9076e-3341-41c2-8e9a-8a89526df285)

11. - After we can click "Logout" and go to the logout page.
    ![logged_out_11](https://github.com/IlyaKavaleu/BlogDjango/assets/97099564/02024e87-45f3-4fb0-aa30-54e9ebd3ee2c)
