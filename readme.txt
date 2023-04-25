# Railway configuration file

[uwsgi]
module = my_app.wsgi:application

chdir = /var/www/my_app
home = /var/www/my_app/venv

master = true
processes = 5
socket = :8001
vacuum = true