#!/bin/sh

set -e
influx apply -o ${DOCKER_INFLUXDB_INIT_ORG} -f ../templates/template.yml --force yes