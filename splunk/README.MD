# Splunk as a webhook receiver

In this folder is a docker-compose.yml that leverages splunk as the webhook receiver.

### Additional Required Environment Variables
Note: NGrok authenticated is required for this setup.


    export NGROK_AUTH=
    export SPLUNK_TOKEN=
    export SPLUNK_PASSWORD=
    export MIST_API=
    export MIST_ORG=
    export MIST_SITE=
    
#### Details:
1. NGROK_AUTH is your personal NGROK auth token
2. SPLUNK_TOKEN is just a unique identifier format XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX  Where X is a hexidecimal character (0-9 and a-z)
3. SPLUNK_PASSWORD is what your desired password for the splunk instance is

4. MIST_API is your mist API key

5. MIST_ORG is the org that contains the site you are configuring a webhook for

6. MIST_SITE is the site you are configuring the webhook on.

### Additional configuration step: Edit inputs.conf for Search
You also need to replace the placeholder for the token in the

    ./Search_config/local/inputs.conf

file with the same value you put in the environment variable.

I'm working on a better way to do this, but it's coming in a future release.

### Storage Persistence.
Storage is **NOT PERSISTENT** on the splunk container.  Meaning if you do a docker-compose down, all that data dies.
Currently fighting an issue with splunk and mac os x where i need to push some additional configs.  Storage persistence will hopefully be coming in a future release.

