# ResvEstPro

by Marcus Zou

## Introduction

In decades of Oil and Gas industry, the reserve estimation is a complex process, engaging a lot of domain-specific knowledge and best practices. But all in all, the principle of calculation is still as simple as a multipication with a lot of involement of statistics though. 

## Domain Knowledge Base

Please refer to the following notes:

- AAPG Wiki - **Reservers Estimation**: [Note](notes/AAPG-Reserves-Estimation.md) or [External Link](https://wiki.aapg.org/Reserves_estimation)

- AAPG Wiki - **Drive Mechanism and Recovery**: [Note](notes/AAPG-Drive-Mechanism-and-Recovery.md) or [External Link](https://wiki.aapg.org/Drive_mechanisms_and_recovery)
* AAPG Wiki - **Enhanced Oil Recovery**: Note or [External Link](https://wiki.aapg.org/Enhanced_oil_recovery)

* AAPG Wiki - **Reservoir Simulation Study**: Note or [External Link](https://wiki.aapg.org/Reservoir_simulation_study)

* AAPG Wiki - **Petroleum Reservoir Fluid Properties**: Note or [External Link](https://wiki.aapg.org/Petroleum_reservoir_fluid_properties)

## Setup

1. Install virtualenv tool, create project folder and Virtual Environment `.venv` by:
   
   ```shell
   # Install python3-virtualenv in Ubuntu 24.04
   sudo apt install python3-virtualenv
   # Install py312-virtualenv in macOS using port or brew
   ## sudo port install py312-virtualenv
   ## sudo port select --set virtualenv virtualenv312
   ##
   ## brew install python@3.12
   
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

5. Then run the Djano server:
   
   ```shell
   (.venv) python3 manage.py runserver
   ## Click the hyperlink https://127.0.0.1:8000/ to launch the default site.
   ```

## Coding

1. to be continued...

## License

MIT
