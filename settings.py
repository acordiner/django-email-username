SECRET_KEY = 'uak)i#z(gsj(89z#_^9pk*@3evxtbxsccx1$u#50de3n7thuqm'

MIDDLEWARE_CLASSES = ()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'emailusername',
)

AUTH_USER_MODEL = 'emailusername.User'