#!/bin/bash

# This script builds a specified docker container from a local directory and logs it with the date appended.

# Add and echo back args
BUILD_NAME=$1
BUILD_DIR=$2
LOG_DIR=$3

echo "Building $BUILD_NAME in $BUILD_DIR. Logging results in $LOG_DIR."

docker build -t $BUILD_NAME $BUILD_DIR --network=host > $LOG_DIR/`date -Iseconds`-$BUILD_NAME                                       