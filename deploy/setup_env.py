import secrets
import os

project_dir = '/var/www/beauty'
secret = secrets.token_urlsafe(50)

env_content = f"""DJANGO_SECRET_KEY={secret}
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=beauty.kislyakov.pro,localhost
"""

with open(os.path.join(project_dir, '.env'), 'w') as f:
    f.write(env_content)

print('.env created with secret key')
