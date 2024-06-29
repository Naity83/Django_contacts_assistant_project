#!/bin/bash

cd contacts_assistant
gunicorn contacts_assistant.wsgi
