#!/bin/bash
# gets the size of the http response
curl -s "$1" |wc -c
