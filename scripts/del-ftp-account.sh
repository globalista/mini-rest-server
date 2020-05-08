#!/bin/bash

delete_item() {
username=$1
dpath=$2

echo $dpath$username
if [ -f $dpath$username ]; then 
    rm $dpath$username
    else
    exit 8
    fi
}

delete_item $1 $2
