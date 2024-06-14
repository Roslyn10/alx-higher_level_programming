#!/bin/bash
#Takes a URl and displays all HTTP methods the server will accept
curl -sX OPTIONS "$1"
