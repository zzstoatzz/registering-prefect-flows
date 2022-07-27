#!/usr/bin/env bash

if [ pyproject.toml -nt requirements.txt ]
then
    poetry export -f requirements.txt --output requirements.txt --without-hashes
	git add requirements.txt
	echo "Updated requirements.txt because it was older than pyproject.toml"
fi