#!/bin/bash

echo $(dirname $0)

python3 -m pip install requests

cd $(dirname $0)/scripts/

python3 youtube_m3ugrabber.py > ../iptv.m3u

echo m3u grabbed

python3 youtubem3u8.py > ../playlist.json

echo json grabbed
