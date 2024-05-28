#!/bin/bash

set -x
MY_HOME_DIR=/home/pinho/dev/sw-engineering-challenge
APP_DIR=/apps/bloqit/amnesia

cp -r ${MY_HOME_DIR}/system/apps/bloqit/amnesia/* ${APP_DIR}/amnesia/
cp -r ${MY_HOME_DIR}/api/* ${APP_DIR}/api/
