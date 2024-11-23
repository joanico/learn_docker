DEBUG = True
ALLOWED_HOSTS = ['*']

# Local database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'learndocker_db',  
        'USER': 'niko',  
        'PASSWORD': 'nikopython1',  
        'HOST': '127.0.0.1', 
        'PORT': 5432, 
    }
}
