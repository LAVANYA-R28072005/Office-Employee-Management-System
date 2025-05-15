# Office-Employee-Management-System
This is a web-based Office Employee Management System built using Python and Django framework. It allows administrators to manage employee records efficiently via a simple and user-friendly interface.

🔧 Features:
* 1.Add, update, Filter and delete employee records
* 2.Interactive admin panel for easy management
* 3.Responsive frontend with support for custom background images
* 4.Powered by Django’s ORM and templating system

## 🛠 Tech Stack
- **Frontend**: HTML, CSS (Django Templates)
- **Backend**: Python, Django
- **Database**: SQLite (default Django DB)

## How to Run the Project:
1. clone the project from GitHub.
2.create a virtual environment in your project folder using cmd or PyCharm terminal:
command: python -m venv myenv(to create virtual env, create only once)
activate env : myenv\Scripts\activate ( run this command every time while running the project) 
3.install Django using command 'pip install django'
4. change the project directory using this command: cd office_emp_proj
5. change the background image path in html file according to your system location
6. type this commands in cmd/ PyCharm terminal for creating models in your system:
* python manage.py makemigrations
* python manage.py migrate
7. Run the project using this command: python manage.py runserver
8. you will login to the webpage of office employee management system. If you need to go for Admin panel, go to the url bar type this:
<port number>/admin (eg.http://127.0.0.1:8000/admin)
* Username: Admin
*Password: 12345678

Note: Refer the Requirement file and Arrange the project folder in this order:
<img width="757" alt="image" src="https://github.com/user-attachments/assets/877678d0-2993-45b6-a672-87ef0c893736" />

----
# Screenshots:
* complete Dashboard
<img width="959" alt="image" src="https://github.com/user-attachments/assets/70e8f7d1-76ae-4589-bb26-f2f034e2a2b0" />

* View all Employees
<img width="959" alt="image" src="https://github.com/user-attachments/assets/0afafca1-3a73-47d3-b0e9-a42eb2c9e798" />

* Add an Employee
<img width="959" alt="image" src="https://github.com/user-attachments/assets/5e242695-52d9-4874-b13c-ff066e36294a" />

*Remove an Employee
<img width="959" alt="image" src="https://github.com/user-attachments/assets/ce46fde3-5ef9-439f-8f29-c0755731db6d" />

*Filter An Employee
<img width="959" alt="image" src="https://github.com/user-attachments/assets/76c9ff34-7ab8-45c7-aaa9-273501595826" />

*Admin Dashboard
<img width="959" alt="image" src="https://github.com/user-attachments/assets/8da476ca-22b1-4ecf-bae2-f9d85c08d0fd" />







