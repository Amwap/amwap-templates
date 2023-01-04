https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

```
Ubuntu version: 22.04 (WSL also)
python version: 3.12
postgresql version: 14
```

## Base usage

build this container
> docker-compose build

run container
> docker-compose up -d

stop container
> docker-compose down -v

rebuild and run container
> docker-compose up -d --build

exec commands to dajngo (web volume)
> docker-compose exec web python manage.py migrate --noinput

go to psql (db volume)
> docker-compose exec db psql --username=ur_best_project_name --dbname=ur_best_project_name_dev


## Specific docker-compose

### Develop
> docker-compose -f docker-compose.dev.yml down -v
> docker-compose -f docker-compose.dev.yml up -d --build
> docker-compose -f docker-compose.dev.yml exec web python manage.py migrate --noinput

> docker-compose -f docker-compose.dev.yml logs -f

### Production
> docker-compose -f docker-compose.prod.yml down -v
> docker-compose -f docker-compose.prod.yml up -d --build
> docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput

> docker-compose -f docker-compose.prod.yml logs -f

