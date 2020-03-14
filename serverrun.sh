# for local development

brew services start redis
source venv/bin/activate
python ./roverbyopenstax/manage.py runserver

