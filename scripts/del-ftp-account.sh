#!/bin/bash

delete_item() {
url="./data/"
echo "${url}${1}"
if [ -f "${url}${1}" ]; then 
    rm "${url}${1}"
    else
    exit 8
    fi
}

delete_item $1
