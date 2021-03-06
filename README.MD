# Mist Flask Receiver
This project is a sample project leveraging docker to easily spin up a webhook receiver for use with the mist_webhook.
This project is not intended to be a production application.  Simply an simplified example for people trying to work with Mist webhooks.

THIS IS A WORK IN PROGRESS


### Flask : mist_flask
mist_flask.py is a simple flask application.  You should modify this in order to handle what you want with the inbound webhook.  This is set to run on port 5000.
During the build of this container, it copies the mist_flask.py file to the container and sets it to run on start.

### Inbound Proxy: ngrok
This leverages ngrok to spin up an inbound proxy.
There is an authenticated version docker-compose-authenticated.yml that will leverage the ngrok auth token

### receiver_configurator
It also spins up an instance of the receiver_configurator.  This container identifies the ngrok public URL and uses your mist credentials to create a webhook receiver pointed at your ngrok instance.
It watches for the SIGTERM and deletes the webhook created during the startup.

### Requirements
This leverages docker and docker-compose.  You should be working on 3.0+ of docker compose.
You also need to define your environmental variables.  In the receiver_configurator, the .env file specifies your mist org, site and api key.  You can hard-code these here, or you can export them as a local environmental variable.

Tested with
Docker Desktop 2.1.5 (on Mac)
docker-compose 1.24.1

### Environment Variables

    export MIST_API=Your-Mist-API-Key
    export MIST_ORG=Your-Mist-Org-ID
    export MIST_SITE=Your-Mist-Site-ID
 
 ### Optional Authenticated NGROK
 
    NGROK_AUTH=Your-NGROK-Auth-Token

### Getting Started
You can start the project
    docker-compose up -d --build

You can check the status of your ngrok tunnel by hitting 

    http://< IP of Docker Host >:4040

or with curl:

    curl http://127.0.0.1:4040/api/tunnels
    
 ### Stopping the Webhook
 
    docker-compose stop


### Authenticating with NGROK
Ngrok.com has some restrictive limits on unauthenticated processes.  I HIGHLY recommend signing up for a free account and using the `docker-compose-authenticated.yml` file to pass in your authtoken.

    docker-compose -f ./docker-compose-authenticated.yml up -d --build
