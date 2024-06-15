import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

apps = [
    'posts',
    'ckeditor'
]

# Run Django commands to create new migrations
os.system('pip install -r requirements.txt')
os.system('py manage.py runserver')
 