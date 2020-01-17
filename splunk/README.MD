# Splunk as a webhook receiver

In this folder is a docker-compose.yml that leverages splunk as the webhook receiver.

###Required Environment Variables
Note: NGrok authenticated is required for this setup.


    export NGROK_AUTH=
    export SPLUNK_TOKEN=
    export SPLUNK_PASSWORD=
    export MIST_API=
    export MIST_ORG=
    export MIST_SITE=
    
#### Details:
1. NGROK_AUTH is your personal NGROK auth token
2. SPLUNK_PASSWORD is what your desired password for the splunk instance is

3. MIST_API is your mist API key

4. MIST_ORG is the org that contains the site you are configuring a webhook for

5. MIST_SITE is the site you are configuring the webhook on.



I'm working on a better way to do this, but it's coming in a future release.

### Storage Persistence.
Storage is **NOT PERSISTENT** on the splunk container.  Meaning if you do a docker-compose down, all that data dies.
Currently fighting an issue with splunk and mac os x where i need to push some additional configs.  Storage persistence will hopefully be coming in a future release.

### Security Warning
To make things easier, i've hardcoded a splunk token in the docker-compose.yml and the Search_config/local/inputs.conf
If you are using this on a regular basis, you may want to change this to a unique OID.
