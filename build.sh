#!/bin/bash

cd base
python3 base_cr.py
cd .
docker-compose build
docker-compose up