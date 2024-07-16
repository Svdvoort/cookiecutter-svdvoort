#!/bin/bash

if [[ $PWD == /tmp* ]]; then
    echo "This is copier update. Exiting"
    exit 0
fi

if [ -d .git/ ]; then
  echo "This project is already initialized. Exiting"
  exit 0
fi

lice $1 -o $2 -p $3 > $3/LICENSE

eval "$(pyenv init --path)"
eval "$(pyenv init -)"
pyenv install -s $5
pyenv local $5
pyenv shell $5
pyenv exec pip install poetry
poetry env use $5
poetry install --with dev,docs,cruft

git init --initial-branch="main"
git add .
git commit -m "Initial commit"
git remote add origin $4
git push --set-upstream origin main

poetry run pre-commit install
