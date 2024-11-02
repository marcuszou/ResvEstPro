# ResvEst

by Marcus Zou

## Setup 
1. Install virtualenv tool, create project folder and Virtual Environment `.venv` by:
    ```shell
    # Install python3-virtualenv in Linux
    sudo apt install python3-virtualenv
    # Install py311-virtualenv in macOS using port - sorry I am not a fan of brew
    ## sudo port install py311-virtualenv
    ## sudo port select --set virtualenv virtualenv311

    # Create project folder
    mkdir ResvEstPro
    cd ResvEstPro
    
    # create .venv
    virutalenv .venv
    # activate venv
    source .venv/bin/activate
    ## you shoubd be in the `(.venv)` env now.
    ```
2. Create a Django project: `ResvEst` and the first app: `simulation`:
    ```shell
    # Make requirements.txt file and install packages
    (.venv) echo django >> requirements.txt
    (.venv) echo numpy >> requirements.txt
    (.venv) pip install -r requirements.txt

    # Create Django project in current folder
    (.venv) django-admin startproject ResvEst .
    (.venv) python3 manage.py startapp simulation
    ```
3. Start coding with:
    ```shell
    (.venv) code .
    ```
4. From the VS Code, add the new app `simulation` to the ResvEst/settings.py file at __INSTALLED_APPS__ section
   ```
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'simulation',
       ]
    ```
6. Then run the Djano server:
   ```shell
   (.venv) python3 manage.py runserver
   ## Click the hyperlink https://127.0.0.1:8000/ to launch the default site.
   ```

## Coding
1. to be continued...

## License
MIT
