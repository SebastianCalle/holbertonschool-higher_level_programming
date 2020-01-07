#!/bin/bash
# Script that takes in a URL, sends a request to that URL, and dislplay size
curl -w '%{size_download}\n' -so /dev/null "$1"
