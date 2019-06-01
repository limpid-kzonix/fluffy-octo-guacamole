#!/usr/bin/env bash

env SANIC_ACCESS_LOG="True" \
gunicorn main:app \
--config ./settings.py \
--worker-class sanic.worker.GunicornWorker \
--log-level info \
