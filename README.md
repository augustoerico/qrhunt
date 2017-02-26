# QR-Hunt
A treasure-hunt-style using QR Code, using [Django](https://www.djangoproject.com/) backend.

# Setup
Before running the application, you have to run `python manage.py makemigrations`, then `python manage.py migrate`. Once is done, you may run `python manage.py runserver`. This last one starts the server on `http://localhost:8000`.

# Create your account
Visit `http://localhost:8000/qrmaster` to land in the `Create account` page. Once you create your account and log in, you can start creating your Quests (a set of hints that leads to an objective) and the Hints that belong to it.

# The QR codes
After you create a Hint to a given Quest, you will notice that an `url` appears. Let's say it is `/qrmaster/hints/abcdef`. If you put this path in your browser, adding the host and the port, so it's `http://localhost:8000/qrmaster/hints/abcdef`, you will get a page with your Hint displayed. The idea is to generate QR codes based on these URLs and then print them and put in strategic places. Once the code is scanned, it will get the hint page. 

# The project
The idea behind this project is to get familiar with REST concepts, including authentication. This was a fun project to make!
