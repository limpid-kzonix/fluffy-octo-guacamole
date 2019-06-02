#!/usr/bin/env bash

env SANIC_ACCESS_LOG="True" \
gunicorn main:app --bind 0.0.0.0:1337 \
--config ./settings.py \
--worker-class sanic.worker.GunicornWorker \
--log-level debug \
--reload
