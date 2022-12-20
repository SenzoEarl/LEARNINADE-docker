web: docker run -it --rm --name redis -p 6379:6379 redis
&& python manage.py migrate && gunicorn LEARNIFY.wsgi
