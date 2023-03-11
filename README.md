# Flask

# crear entorno

```py
python -m venv venv
```

# activar entorno

```py
pip install Flask
```

# instalar flask

```py
source venv/scripts/activate
```

# instalar dotenv

```py
 pip install python-dotenv
```

# guardar dependencias, ejecutar cada que se instalen complementos

```py
pip freeze > requirements.txt
```

# iniciar Flask

```py
Flask run
```

### Migraciones

- iniciar migraciones(se ejecuta una sola vez)

```sh
flask db init
```

- crear una migracion(cuando se crea o modifica un modelo)

```sh
flask db migrate -m "comentario"
```

- subir los cambios a nuestra bd

```sh
flask db upgrade
```
