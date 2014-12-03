# This is code to simulate someome pushing to SHARE!

import json
from datetime import datetime

import requests

import settings


def get_time_now():
    return datetime.now().isoformat()


def generate_events():
    '''
    returns a dictionary list of dicts with all of 
    the information needed to push to the SHARE
    notification service 
    '''
    payload = {
        'source': settings.LONG_NAME,
        'events': [
            {
                'title': 'An Example Title to Demonstrate the SHARE Push API',
                'contributors': [
                    {
                        'prefix': '',
                        'given': 'Example',
                        'middle': '',
                        'family': 'Exampleson',
                        'suffix': '',
                        'email': 'this@email.test',
                        'ORCID': 'anORCid'
                    }
                ],
                'id': {
                    'url': 'http://www.anexample.org/article',
                    'doi': 'an_official_doi/doi.DOI!',
                    'serviceID': 'some_unique_id'
                },
                'properties': {
                    'figures': ['http://www.anexample.org/article/image.png'],
                    'type': 'text',
                    'another_property':'An interesting property'
                },
                'description': 'This is a test article that is meant to\
                demonstrate the PUSH API aspect of the SHARE notification\
                service. ',
                'tags': [
                    'testing',
                    'the',
                    'push'
                ],
                'source': settings.SHORT_NAME,
                'dateCreated': get_time_now(),
                'dateUpdated': get_time_now(),
            }
        ]
    }

    return payload


def send_post_to_scrapi(events):

    url_for_post = settings.SHARE_PUSH_URL
    headers = {'Content-Type': 'application/json'}
    auth = settings.OSF_API_AUTH

    posted = requests.post(
        url_for_post, headers=headers, data=json.dumps(events), auth=auth, verify=False)
    import pdb; pdb.set_trace()
    return posted


if __name__ == '__main__':
    send_post_to_scrapi(generate_events())
