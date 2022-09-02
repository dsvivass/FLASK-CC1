# Steps

- Create virtual environment

    ```
        mkdir venv
        cd venv
        virtualenv .
        source bin/activate
    ```

- Create flask folder 

    ```
        mkdir flaskr
        cd flaskr
    ```

`Note: I did not use * flask init *`

- Create **__ init __.py** and **app.py**, write the code.

- Run flask app

    ```
        flask run
    ```

-------------------------

# Celery and Redis

- Install redis

    ```
        pip install redis
    ```

- Install redis server

    ```
        brew install redis
    ```

- Install celery

    ```
        pip install celery
    ```

- If we develop the code in the same flask folder, we can run the celery worker with the following command

    ```
        celery -A flaskr.tareas.tareas worker -l info
    ```

`Note: we must use the decorator @celery.task without parenthesis`

- If we develop the code outside the flask folder, we must run the celery worker with the following command

    ```
        celery -A tareas worker -l info -Q logs
    ```