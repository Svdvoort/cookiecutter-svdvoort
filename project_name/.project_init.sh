#!/bin/bash

if [[ $PWD == /tmp* ]]; then
    echo "This is copier update. Exiting"
    exit 0
fi

if [ -d .git/ ]; then
  echo "This project is already initialized. Exiting"
  exit 0
fi

lice {{ license.lower() }} -o {{ organization }} -p {{ project_name }} > {{ project_name }}/LICENSE
poetry install --with dev,docs
git init
git add .
git checkout -b main
git commit -m "Initial commit"
git remote add origin {{ git_url }}
