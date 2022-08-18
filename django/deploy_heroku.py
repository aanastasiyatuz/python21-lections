"====================Deploy on heroku===================="

# для начала в requirements.txt добавьте библеотеки
'gunicorn'
'whitenoise'
'dj-database-url'


"-----------settings.py-----------"
# в INSTALLED_APPS добавьте 'whitenoise.runserver_nostatic'

# в MIDDLEWARE первым добавьте 'whitenoise.middleware.WhiteNoiseMiddleware'

# добавьте STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# если вы используете postgresql, настройки бд:
"""
import dj_database_url
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql'
    }
} 
db = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db)
"""

# настройки static и media:
"""
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
"""


"------------Procfile------------"
# web: gunicorn config.wsgi --log-file -

"---------runtime.txt---------"
# python-3.8.10



"---------------terminal---------------"
# heroku login

# после этого на сайте heroku создайте app

# heroku git:remote -a название_app

# зайдите в settings вашего app на сайте heroku, в config vars укажите все переменные вашего .env

# heroku config:set DISABLE_COLLECTSTATIC=1

# после этого чтобы задеплоить или обновить сервер:
# git add .
# git commit -m 'message'
# git push heroku main (если ветка не main -> git checkout -b main)
