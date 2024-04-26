#!/bin/bash
if [ $# == 1 ]; then
    curl -sI $1 | grep Body-Size | awk -F" " '{print $2}' 
fi
