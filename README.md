# Instrucciones para Docker Compose

## Subir el entorno con Docker Compose

Para iniciar los servicios definidos en tu archivo `docker-compose.yml`, utiliza el siguiente comando:

```sh
docker compose up -d
```

El flag `-d` ejecuta los contenedores en segundo plano.

## Bajar el entorno con Docker Compose

Para detener y eliminar los contenedores, redes y volúmenes definidos en tu archivo `docker-compose.yml`, utiliza el siguiente comando:

```sh
docker compose down
```

## Compilar las imágenes de Docker

Si necesitas compilar las imágenes de Docker definidas en tu archivo `docker-compose.yml`, utiliza el siguiente comando:

```sh
docker compose build
```

Este comando compilará las imágenes sin iniciar los contenedores.

## Ver los logs de los servicios

Para ver los logs de los servicios en tiempo real, utiliza el siguiente comando:

```sh
docker compose logs -f
```

El flag `-f` sigue los logs en tiempo real.

## Reiniciar los servicios

Para reiniciar los servicios, puedes utilizar el siguiente comando:

```sh
docker compose restart
```

Este comando reiniciará todos los servicios definidos en tu archivo `docker-compose.yml`.

## Listar los servicios en ejecución

Para listar los servicios que están actualmente en ejecución, utiliza el siguiente comando:

```sh
docker compose ps
```

Este comando mostrará el estado de los contenedores.
