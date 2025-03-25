# Django Project Setup Guide

python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate


## 🔥 Clone the Repository
```bash
# Replace <repo-url> with your GitHub repository URL
git clone <repo-url>
cd tiket
##

## 📦 Install Dependencies
``` bash
pip install -r requirements.txt

## Apply migrations
python manage.py migrate


##Create Superuser
python manage.py createsuperuser

## 🏃 Run the Server
python manage.py runserver

##API Endpoints

1.POST Method with all fields data inside the body
id, description, users, status, task_type 
``` http://127.0.0.1:8000/api/tasks

For . API to create a task
Response: got 201 and the created task object detials

2. PATCH method to  assign the task to  a user - API to assign a task to a user
- Enables assigning a task to one.
```bash
http://127.0.0.1:8000/api/tasks/id/

for this you  need to pass the task id which you  wanted to  assign the user and users email  address and inside postmen or any other assign them like this
{
    users:["example1@gmail.com" , "example2@gmail.com"]
}
Response: got 202 and with updated task object details.

3. GET method to  - Fetches all tasks assigned to a particular user

```bash
http://127.0.0.1:8000/api/tasks?user_email=example1@gmail.com

here you  need to pass and url parameter user_email  to  find related all task.
Response: got 200 with all the task object related to  it.

## credentials
Superuser

email: hiwhystudio.dev@gmail.com
password: admin

second user email:
mofafu@gmail.com

Note:
I have added my postmen test and response export with this repo  you  can use that  one for testing all the api endpoint just import this into your postmen setup  and test it.