import django
from django.conf import settings

settings.configure(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'tcp',
            'USER': 'secert',
            'PASSWORD': 'secert',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    },
    TIME_ZONE='Asia/Shanghai',
    INSTALLED_APPS=[
        'tcp.apps.TcpConfig',
    ]
)
django.setup()
