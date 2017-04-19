# coding: utf-8

from __future__ import print_function, unicode_literals
import os
from boxsdk import Client
from boxsdk.exception import BoxAPIException
from boxsdk.object.collaboration import CollaborationRole
from auth import authenticate


def upload_file(client):
    root_folder = client.folder(folder_id='0')
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'file.txt')
    a_file = root_folder.upload(file_path, file_name='i-am-a-file.txt')
    try:
        print('{0} uploaded: '.format(a_file.get()['name']))
    finally:
        print('Delete i-am-a-file.txt succeeded: {0}'.format(a_file.delete()))


def run_examples(oauth):

    client = Client(oauth)
    upload_file(client)

def main():

    # Please notice that you need to put in your client id and client secret in demo/auth.py in order to make this work.
    oauth, _, _ = authenticate()
    run_examples(oauth)
    os._exit(0)

if __name__ == '__main__':
    main()
