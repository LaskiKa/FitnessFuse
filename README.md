# FitnessFuse
Django REST framework application to create/update/delete for body measurement, tracking and analysis

### Requirements:
```
asgiref==3.7.2
Django==5.0.2
djangorestframework==3.14.0
psycopg2-binary==2.9.9
pytz==2024.1
sqlparse==0.4.4
tzdata==2024.1
```
## Instalation & configuration:

### Step 1: Install PostgresSQL locally.
```
sudo apt-get install postgresql 
```

### Step 2: Clone repository.
```
path/to/folder
git clone git@github.com:LaskiKa/FitnessFuse.git
```
### Step 3: Create virtual enviroment & install requirements.txt
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 4: Setup database.
```
create database 'Database Name'

set postgresql database in settings.py or loccaly
DATABASES = {
    'default': {
        'HOST': '127.0.0.1',
        'NAME': '[db_name]',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': '[user]',  
        'PASSWORD': '[password]',
    }
}
```