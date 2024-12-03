## Documentasaun setup django iha docker

### Setup Simple Django Project iha local environment
    1. Kria folder ida ba projetu foun hanesan (e.z. learn_docker) 
    2. Setup python environment usa poetry
    3. Install poetry
    4. Install Django uza poetry
    5. Kria projetu naran (e.z. learn_docker)
    6. cd learn_docker
    7. Run python manage.py migrate
    8. Run python manage.py createsuperuser
        - Hatama user, no password
    9. Run python manage.py runserver
    Ka bele uza Poetry
    - poetry run ./manage.py migrate
    - poetry run ./manage.py runserver

### Install docker
Download docker app ba desktop (macOs, Linux)
- Install Docker iha laptop
- Loke ita django project nebe ita foin kria iha VS code karik ita install ona vs code
- Install docker extension in VS code
- Kria Docker file uza VS code
    - cmd+shift+p in vs code
    - Ketik no klik iha >Add Docker Files to Workspace
    - Hili Python:Django
    - Hili manage.py ka iha root directory
    - Hili port 8000 ka port seluk

### Setup docker compose
- Loke ita nia Dockerfile no hare prosesu setup sira nebe existe ona iha file nia laran bele halo mudansa tuir ita nia environment
- Loke docker compose file setup postgresql 
### Kria ka Build image
- Depois de ita setup hotu docker file no docker compose tuir mai bele run:
    - `docker-compose build learndocker` # kria spesific image 
    - `docker-compose up` # run ita nia docker koko test nia docker 
- Se iha Erru ruma ka atu hamos cache bele run ida nee
    - `docker-compose build –no-cache learn_docker`
    - `docker-compose up learn_docker`
- Se ita uza gunicorn bele run command ida ne'e:
    `docker-compose up -d learn_docker`  
- Se ita misconfiguration ka conflit ruma bele hamos fali docker container no image nebe ita kria antes nee bele uza: 
    - `docker-compose down` # hamoos container   
    - `docker-compose up -b --build `
- Koko run migrate no kria super user manual:
    - `docker-compose up -d` # Start containers in detached mode
    - `docker-compose exec learndocker python manage.py migrate`
    - `docker-compose exec learndocker python manage.py createsuperuser`
- Koko run server iha container laran bele kria entrypoint hanesan
    - Kria file `entrypoint.sh`
    - Update Dockerfile run ho entrypoint
    - Depois kria entrypoin bele koko build fila fali
    - `docker-compose build learn_docker`
    - `docker-compose up -d learn_docker`

- Halo jestaun ka kontrola Docker bele uza command sira nee:
    - `docker-compose stop`
    - `docker-compose start`
    - `docker-compose restart`
    - `docker-compose down`

