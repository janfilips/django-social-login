from .base import *  # noqa
import os

# Database settings

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "ioi_devel",
        "USER": "root",
        "PASSWORD": "",
        "HOST": "127.0.0.1",
    }
}

# Social Keys

SOCIAL_AUTH_FACEBOOK_KEY = os.getenv("SOCIAL_AUTH_FACEBOOK_KEY")  # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = os.getenv(
    "SOCIAL_AUTH_FACEBOOK_SECRET"
)  # Facebook App Secret

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv(
    "SOCIAL_AUTH_GOOGLE_OAUTH2_KEY"
)  # Google+ App Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv(
    "SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET"
)  # Google+ App Secret
