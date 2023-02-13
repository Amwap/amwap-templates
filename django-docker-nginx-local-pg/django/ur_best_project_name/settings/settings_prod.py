from ur_best_project_name.settings.settings_base import *

CSRF_TRUSTED_ORIGINS = [
    "http://localhost", 
    "http://localhost:3000",
    "http://localhost:1337"
    ]

CORS_ORIGIN_WHITELIST = CSRF_TRUSTED_ORIGINS
CORS_ALLOWED_ORIGINS = CSRF_TRUSTED_ORIGINS