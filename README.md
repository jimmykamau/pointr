# Pointr

This Django application allows you to find the closest points on a grid given a set of input points.

## Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Installation and Setup

1. Clone the repository:

   ```shell
   git clone https://github.com/jimmykamau/pointr.git
   cd pointr
   ```

3. Build and start the Docker containers using Docker Compose:

   ```shell
   docker compose up --build
   ```

   Docker Compose will build the images and start the Django application and PostgreSQL database containers.

4. Run migrations

    ```shell
    docker compose exec web python manage.py migrate
    ```

5. Access the app in your browser at `http://localhost:8000/`.

## Running Tests

To run the unit tests for the app, use the following command:

```shell
docker compose exec web python manage.py test
```

## Admin Interface

The app includes an admin interface for managing the stored points. To access the admin interface:

1. Create a superuser account:

   ```shell
   docker compose exec web python manage.py createsuperuser
   ```

2. Access the admin interface in your browser at `http://localhost:8000/admin/`. Log in with your superuser credentials.

## Stopping the App

To stop the running Docker containers, use the following command:

```shell
docker compose down
```

This will stop and remove the containers, but will preserve the database data.
