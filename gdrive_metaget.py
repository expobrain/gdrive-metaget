#!/usr/bin/env python3

import json
import sys

from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# Setup the Drive v3 API
SCOPES = "https://www.googleapis.com/auth/drive.metadata.readonly"
store = file.Storage("credentials.json")
creds = store.get()

if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets("client_secret.json", SCOPES)
    creds = tools.run_flow(flow, store)

service = build("drive", "v3", http=creds.authorize(Http()))

# Call the Drive v3 API
drive = service.files()
nextPageToken = None

while True:
    results = drive.list(
        pageSize=100,
        pageToken=nextPageToken,
        spaces="drive",
        fields="nextPageToken, files(id, name, permissions)",
    ).execute()

    nextPageToken = results.get("nextPageToken")
    files = results.get("files", [])

    for item in files:
        sys.stdout.write(json.dumps(item))

    if nextPageToken is None:
        break
