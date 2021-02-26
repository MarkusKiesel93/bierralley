#! /usr/bin/env bash

set -e

pytest -s ./app

if [[ ${DEPLOY_MODE} -eq "production" ]]; then
    uvicorn app.main:app --reload --host 0.0.0.0 --port ${BACKEND_PORT}
else
    gunicorn -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --workers 4 app.main:app
fi