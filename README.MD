# Django Firebase


## Install

```bash
pip3 install django_firebase
```

## Usage

settings.py

```python
# Add application
INSTALLED_APPS = [
    <...>
    'django.contrib.staticfiles',
    'django_firebase',
]

# Set Default media storage
DEFAULT_FILE_STORAGE = 'django_firebase.storage.FirebaseStorage'

# Set Bucket name
FIREBASE_STORAGE_BUCKET = 'example.appspot.com'

# Set Firebase cert data
# Note: it can be dict or json file
# You can get credentials in firebase console
FIREBASE_CERT_DATA = os.path.join(BASE_DIR, './firebase-cert.json')
```

## Feature

- Firebase storage support

## Requirements

Python >= 3

- Django >= 2.0
- firebase-admin >= 5.0.0
