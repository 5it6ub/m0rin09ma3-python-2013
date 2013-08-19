#!/bin/bash
count=0; while [ "$count" -lt "$2" ]; do uptime | awk '{print $8 $9 $10}'; sleep $1; ((count += 1)); done
