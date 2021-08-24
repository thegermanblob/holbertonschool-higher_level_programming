#!/bin/bash
# displays all methos webserver will accept 
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
