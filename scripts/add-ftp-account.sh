#!/bin/bash

add_item() {
    username=$1
    dpath=$2
    
    mkdir $dpath -p
    if [ -f $dpath$username ]; then
    exit 8
    else
    touch $dpath$username
    fi
    }

add_item $1 $2
