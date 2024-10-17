# miio_test
Technical Challenge - Backend in Django and PostgreSQL

## APPLICATION URL

```sh
https://
```

## Swagger Documentation

```sh
https://
```


## This project was made with:

- Python 3.10.10
- Django 5.1.1
- Django REST Framework 3.15.2
- PostgreSQL
- Docker
- Docker Compose
- Redis
- Celery

# REST API Endpoints:

1. GET `/movie/popular`: details in [Get the most popular movies](https://github.com/ianAraujj/miio_test)

2. GET `/movie/{id}/`: details in [Get details of a specific movie](https://github.com/ianAraujj/miio_test)

3. POST `/movie/`: details in [Create a new movie based on the defined parameters](https://github.com/ianAraujj/miio_test)

4. PUT `/movie/{id}/`: details in [Update a movie](https://github.com/ianAraujj/miio_test)

## Usage Settings

You will need to copy the file in the root of the project called `.env.sample` to a file called `.env`

```sh
cp .env.sample .env
```

The `.env` file must contain the project credentials. To generate the `SECRET_KEY`, run the following command in your terminal:

```sh
python -c "import secrets; print(secrets.token_urlsafe())"
```

The result of this command must be inserted into the `.env` file in the `SECRET_KEY` variable.

### Docker Settings

Você precisa ter o `docker` e o `docker-compose` instalado em sua máquina.
A configuração mais curta, basta executar o comando:
`docker-compose up -d`

### Tests

To run the tests, use the commands:

`docker-compose up -d`

&&

`docker-compose exec web python manage.py test`
