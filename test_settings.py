SECRET_KEY = "secret_key_for_testing"
DEBUG = True

INSTALLED_APPS = (
    'pygments_renderer',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
