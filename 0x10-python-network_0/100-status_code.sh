#!/bin/bash
# Script that sends a reques to a URL passed as an argument, and displays only the status code of the response.
curl -s -w -o /dev/null '%{http_code}' "$1"
