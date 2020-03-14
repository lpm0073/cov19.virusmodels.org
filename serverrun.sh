# for local development

brew services start redis
source venv/bin/activate
python ./cov19/manage.py runserver

