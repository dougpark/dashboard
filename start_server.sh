#!/bin/bash
echo 'source .venv/bin/activate'
source .venv/bin/activate
echo Dashboard server started
cd ./dash_app
python3 app.py