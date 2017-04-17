#!/usr/bin/env python

from __future__ import print_function
import os
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


def upload_download():
    for filename, mimeType in FILES:
        body = {'name': filename}
        if mimeType:
            body['mimeType'] = mimeType
        res = DRIVE.files().create(body=body,
            media_body=filename,).execute()
        filename = res['name']
        mimeType = res['mimeType']
        fileId = res['id']
        print('Uploaded "%s" (%s)' % (filename, mimeType))

        if res:
            MIMETYPE = 'application/pdf'
            data = DRIVE.files().export(fileId=fileId,mimeType=MIMETYPE).execute()
            if data:
                fn = '%s.pdf' % os.path.splitext(filename)[0]
                with open(fn, 'wb') as fh:
                    fh.write(data)
                print('Downloaded "%s" (%s)' % (fn, MIMETYPE))



try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/drive.file'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store, flags) \
            if flags else tools.run(flow, store)
DRIVE = build('drive', 'v3', http=creds.authorize(Http()))

FILES = (
    ('hello.txt', 'application/vnd.google-apps.document'),
    ('sample.txt', 'application/vnd.google-apps.document'),
    ('SunriseoverLake_2560x1600.jpg', 'application/vnd.google-apps.document'), 
)

upload_download()
