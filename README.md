# FastAPI APP


## Validations
The first one is validate that python is installed on your PC

```
python3 --version
```

So should validate that you manager of virtual env

```
sudo apt install python3.12-env
```

## Run server

### Run in local Mode

1. Activate virtual env
```
python3 -m venv venv
```

2. Dependecies installation
```
pip install requirements.txt
```


3. Run server in local mode
```
fastapi dev main.py
```

### Run in Docker mode

1. Build docker image
```
docker build -t nombre_imagen . 
```

2. Run images
```
docker run -p 8000:8000 nombre_imagen 
```

# IMAGES

# 1. Build Image

![Crear Imagen](images/make_images.png)

# 2. Run Image

![Ejecutar un contenedor](images/run_images.png)

# 3. Upload images

![Cargar imagen a Docker Hub](images/push_images.png)

# 4. Validate imagen is running

![Publicar el puerto 8000](images/validate_run.png)

# 5. Local Access 

![Publicar el puerto 8000](images/access_local.png)

# 6. Docker with username

![Contenedor con mi usuario](images/docker_with_name.png)

# 7. Clean All 

![Borrar contenedor e imagen](images/delete_container_images.png)