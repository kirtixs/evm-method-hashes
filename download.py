#!/usr/bin/python

import requests
import json

directory = "https://www.4byte.directory/api/v1/signatures/?ordering=created_at&format=json"
destination = './method-hashes.json'

if __name__ == '__main__':

    hashes = {}
    downloading = True
    session = requests.Session()

    while downloading:

        print(directory)
        response = session.get(directory).json()

        for known_hash in response['results']:
            hashes[known_hash['hex_signature']] = known_hash['text_signature']
        directory = response['next']

        if directory is None:
            downloading = False

    f = open(destination, 'w')
    f.write(json.dumps(hashes, sort_keys=True, indent=4))
    f.close()


