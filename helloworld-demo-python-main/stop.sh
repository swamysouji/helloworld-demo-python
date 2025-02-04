#!/bin/bash

#https://www.geeksforgeeks.org/docker-container-id-from-name/
containId=$(docker ps --filter "name= helloworld-demo-python-main-app-1" --format "{{.ID}}")
docker rm -f "$containId"
