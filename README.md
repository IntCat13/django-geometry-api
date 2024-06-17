# Django Geometry API

![Django](https://img.shields.io/badge/Django-3.2-green)
![Docker](https://img.shields.io/badge/Docker-20.10-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13-yellow)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## Overview

The **Django Geometry API** project is a REST API built with Django Rest Framework to manipulate geospatial data. The API supports CRUD operations for three types of geometries:
- **Point**
- **LineString**
- **Polygon**

The API also includes endpoints to join LineStrings and check intersections between Points and Polygons.

## Installation
Clone the repository:

```bash
git clone https://github.com/IntCat13/django-geometry-api.git
cd django-geometry-api
```
Build and start the Docker containers:

```bash
make init
```

> [!WARNING]  
> Change "docker-compose" to "docker compose" in Makefile if you have an error:
> ```DOCKER_COMPOSE := docker-compose ```

## Usage

To start the development environment with live reloading, use:
```bash
make dev
```

To run tests, use:
```bash
make test
```

To deploy the application, use:
```bash
make deploy
```

## API Documentation
All available endpoints can be explored using Swagger. Once the application is running, you can access the Swagger documentation at:
```bash
http://localhost:8000/docs/
```

## Project Requirements
Docker, docker-compose, Makefile

## Testing Environment
This project has been tested on:
- WSL2 with Ubuntu
- Using Docker Engine instead of Docker Desktop

## License
This project is licensed under the MIT License - see the LICENSE file for details.
