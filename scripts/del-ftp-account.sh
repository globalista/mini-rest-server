#!/bin/bash

delete_item() {
if ls ./data/$1 ; then 
    rm ./data/$1
    else
    exit 8
    fi
}

delete_item $1
