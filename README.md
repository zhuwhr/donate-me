# donate-me
Online payment system supporting user login and authentication, built in Django and Stripe API.

This project is being deployment, here is instruction for local usage.

- Clone this repo `git clone git@github.com:zhuwhr/donate-me.git`
- Create a virtual environment for this project
  - `virtualenv donate`
  - `source donate/bin/activate`
  - `cd src`
- Install all required packages  `pip install -r requirements.txt`
- Start the server  `python manage.py runserver`

Use Cases:
1. Sign up and log in
2. Send Email via contact form
3. Click check out button and donate. This requires user to signup
4. Process payment. This is implemented with Stripe API 3.x, which is not supported anymore. I will upgrade it to Stripe API 4.x later
5. Display a thanks message after user loggin

