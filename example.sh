#!/bin/bash

curl -X POST -H 'Content-Type: application/json' -H 'Accept: application/json' -d '{"repo": "https://github.com/dnck/logline"}' http://0.0.0.0:8000/generate_llms_txt | jq .
