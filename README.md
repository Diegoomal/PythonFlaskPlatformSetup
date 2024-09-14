# Github AI Models

## '.env' file

```
SECRET_KEY="super-secret-key"
SQLALCHEMY_DATABASE_URI="sqlite:///db.sqlite"
```

## Manage Conda ENV

### Create
```
conda env create -n python-platform-setup-env -f ./env.yml
```

### Update
```
conda env update -n python-platform-setup-env -f ./env.yml
```

### Remove
```
conda env remove --n python-platform-setup-env
```

### List
```
conda env list
```

### Activate
```
conda activate python-platform-setup-env
```

## To Execute

### Config the DB
```
flask db init
flask db migrate -m "initial migration"
flask db upgrade
flask db downgrade
```

<!-- 
flask db upgrade OR downgrade
path -> migrations/script.py.mako
-->

### Run Flask server
```
flask run
```

### Run uvicorn server (prod)
```
uvicorn src.main:asgi_app --host 0.0.0.0 --port 8000 --workers 4 --reload
```

## Links

[github_author](https://github.com/Diegoomal)

[generate-token](https://github.com/settings/tokens)
[freecodecamp-tutorial](https://www.freecodecamp.org/news/how-to-authenticate-users-in-flask/)
[digitalocean-migration-tutorial](https://www.digitalocean.com/community/tutorials/how-to-perform-flask-sqlalchemy-migrations-using-flask-migrate)