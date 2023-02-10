images from https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

```
Ubuntu version: 22.04 (WSL also)
python version: 3.12
postgresql version: 14
```

# postgres deploy

### psql 

> CREATE ROLE hadiku WITH LOGIN ENCRYPTED PASSWORD 'pwd here';
> CREATE DATABASE hadiku_db WITH OWNER hadiku;

# Docker

## Develop
> docker-compose -f docker-compose.dev.yml down -v

> docker-compose -f docker-compose.dev.yml up -d --build

> docker-compose -f docker-compose.dev.yml exec web python manage.py migrate --noinput

> docker-compose -f docker-compose.dev.yml exec web python manage.py collectstatic --noinput

> docker-compose -f docker-compose.dev.yml logs -f

## Production
> docker-compose -f docker-compose.prod.yml down -v 

> docker-compose -f docker-compose.prod.yml up -d --build

> docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput

> docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --noinput

> docker-compose -f docker-compose.prod.yml logs -f




GIT_SSH_COMMAND="ssh -i ~/.ssh/hadiku" git push