#!/bin/bash

declare -a dirs=(front_end monster_species monster_type monster_class)

for dir in ${dirs[@]}; do
    cd ${dir}
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    python3 -m pytest --cov=application --cov-report=html
    cd ..
done
