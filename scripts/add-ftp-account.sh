#!/bin/bash

add_item() {
    #echo $1
    if ls ./data/$1 ; then 
    exit 8
    else
    touch ./data/$1
    fi
    }

add_item $1
