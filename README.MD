# Mist Flask Receiver
This project is a sample project leveraging docker to easily spin up a webhook receiver for use with the mist_webhook.

### Flask : mist_flask
mist_flask.py is a simple flask application.  You should modify this in order to handle what you want with the inbound webhook.  This is set to run on port 5000.

### Inbound Proxy: ngrok
This leverages ngrok to spin up an inbound proxy.
There is an authenticated version docker-compose-authenticated.yml that will leverage the ngrok auth token

### receiver_configurator
It also spins up an instance of the receiver_configurator.  This container runs once to identify the ngrok public URL and uses your mist credentials to create a webhook receiver pointed at your ngrok instance

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
 
    docker-compose down

