#!/bin/bash

echo "BUILD START"
pip install --upgrade pip
pip install -q -r requirements.txt
python3.9 manage.py migrate
echo "BUILD END"
