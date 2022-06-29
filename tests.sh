#!/bin/bash

declare -a dirs=(front_end monster_species monster_type monster_class)

for dir in ${dirs[@]}; do
    cd ${dir}
    pip3 install -r requirements.txt
    python3 -m pytest --cov=application --cov-report=html --cov-report term-missing
    cd ..
done
