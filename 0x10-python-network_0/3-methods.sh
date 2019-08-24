#!/bin/bash
# Request to that URL, and displays the size of the body of the response
curl -sI $1 | grep 'Allow' | cut -f 2- -d ' '
