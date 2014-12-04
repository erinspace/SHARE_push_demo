# Demonstration of the SHARE Push API
===============

This code is an example of how a provider for content for the SHARE notification service would push content to be included in the notification stream. 

Right now, the data is accepted in the same schema output by the SHARE otification system, specified on the [main page's github wiki](https://github.com/CenterForOpenScience/SHARE/wiki/SHARE-schema). 


# Running the demonstration

- Fork this project and clone your own local repo
- Register an API key on the [share-dev site](ttps://share-dev.osf.io)
    + [Create an account](https://share-dev.osf.io/) and sign in
    + In the upper right hand corner, click the gear labeled "settings"
    + On the left hand menu, click "Configure API Keys"
    + Give your new key a name, and create a new API key by clicking "Create New Key"
- In your example pusher repository, create a file in the settings directory named local.py
- in the file local.py, add a line with your OSF API Key credientials like so: 
```OSF_API_AUTH = ('my_label', 'my_long_api_key')```
- From within a [virtual enviornment](http://virtualenv.readthedocs.org/en/latest/), run ```pip install -r requirements.txt```
- Run the example pusher with ```python example_pusher.py```
- Check out the [share notification stream](https://share-dev.osf.io/api/v1/app/6qajn/) to see your pushed content
