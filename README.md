# hello-django-docker
Hello world in Django with Docker

## Requirements

You need will need Docker installed and running and an internet connexion.

## Usage

Clone this repository, then build the Docker image with
```
docker build -t hellodjango .
```

Then launch a container with
```
docker run -p80:8000 -v /data/hellodjango:/data hellodjango
```

You should now be able to browse the (empty) index page on [http://localhost/](http://localhost/).

To create new database objects, you will need an access to the web admin. To
create your superuser account, get the id of your Docker container with
`docker ps`, then run
```
docker exec -ti $CONTAINER_ID /opt/venv-hellodjango/bin/python manage.py createsuperuser
```

You should now be able to create new database objects with [http://localhost/admin/helloworld/databaseobject/add/](http://localhost/admin/helloworld/databaseobject/add/).

You should now see the objects you have created listed on [localhost/hello-world/](http://localhost/hello-world/) and see a
greeting for the first object on [localhost:8000/hello-world/1](http://localhost:8000/hello-world/1)

Finally, you can configure your local DNS configuration to access this a greeting
from other devices with an URL like [http://some-django-box.dev/hello-world/&lt;id&gt;](http://some-django-box.dev/hello-world/1).
