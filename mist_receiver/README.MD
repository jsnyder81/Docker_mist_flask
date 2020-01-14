# Mist Flask Receiver
The goal of this project is to have a simple way to spin up a mist webhook receiver.
### Inbound Proxy
This leverages ngrok to spin up an inbound proxy.
### receiver_configurator
It also spins up an instance of the receiver_configurator.  This container runs once to identify the ngrok public URL and uses your mist credentials to create a webhook receiver pointed at your ngrok instance
### mist_flask
This instance is a simple flask shell.  You should modify this in order to handle what you want with the inbound webhook.

### Requirements
This leverages docker and docker-compose.  You should be working on 3.0+ of docker compose.
You also need to define your environmental variables.  In the receiver_configurator, the .env file specifies your mist org, site and api key.  You can hard-code these here, or you can export them as a local environmental variable.

### Getting Started
You can run the project by running docker-compose up -d --build

You can check the status of your ngrok tunnel by hitting <IP of Docker Host>:4040
