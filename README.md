# GDrive-Metaget

## Introduction

This project is a little CLI tool to extract all the permissions metadata of your files on your Google Drive.

## Prerequisites

Before running the code you need a secret token to access the Google Drive API.

To do that just follow the [Step 1: Turn on the Drive API](https://developers.google.com/drive/v3/web/quickstart/python#step_1_turn_on_the_api_name) to create a new set of credentials and save the downloaded JSON file in the same directory of `gdrive_metaget.py` as `client_secret.json`.

The just install the dependancies:

```bash
pip install -r requirements.txt
```

## Execution

Just execute:

```bash
gdrive_metaget.py
```

to fetch all the file's metadata in a list of JSON object one line per file.

The output can be post-processed with [jq](https://stedolan.github.io/jq/), for example if you want to get a list of unique email addresses of users whom have access to your files:

```bash
./gdrive_metaget.py | jq '.permissions[]?.emailAddress' | sort | uniq
```
