# Splunk as a webhook receiver

In this folder is a docker-compose.yml that leverages splunk as the webhook receiver.

### Additional Required Environment Variables
Where X is a hexidecimal character (0-9 and a-z)
Note: NGrok authenticated is required for this setup.


    export NGROK_AUTH=*INSERT NGROK AUTH TOKEN

    export SPLUNK_TOKEN=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX

    export SPLUNK_PASSWORD= *Insert desired password here*
    
This uses a slightly different setup on the MIST API, because of the need to set a splunk token.

### Additional configuration step: Edit inputs.conf for Search
You also need to replace the placeholder for the token in the

    ./Search_config/local/inputs.conf

file with the same value you put in the environment variable.

I'm working on a better way to do this, but it's coming in a future release.

### Storage Persistence.
Storage is **NOT PERSISTENT** on the splunk container.  Meaning if you do a docker-compose down, all that data dies.
Currently fighting an issue with splunk and mac os x where i need to push some additional configs.  Storage persistence will hopefully be coming in a future release.

