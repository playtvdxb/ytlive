#! /usr/bin/python3
import os
import json
import requests


def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        #response = requests.get(url).text
        if '.m3u8' not in response:
            os.system(f'curl "{url}" > temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print(
                    'https://raw.githubusercontent.com/firofame/Malayalam-IPTV/main/assets/moose_na.m3u')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner: end]:
            link = response[end-tuner: end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")


print('#EXTM3U')

youtube_channel_list = open('../youtube_channel_list.json')
youtube_channel_data = json.load(youtube_channel_list)
for channel in youtube_channel_data:
    grp_title = channel['group-title']
    tvg_logo = channel['tvg-logo']
    tvg_id = channel['tvg-id']
    ch_name = channel['ch_name']
    print(
        f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')

    url = channel['url']
    grab(url)

m3u8_channel_list = open('../m3u8_channel_list.json')
m3u8_channel_data = json.load(m3u8_channel_list)
for channel in m3u8_channel_data:
    grp_title = channel['group-title']
    tvg_logo = channel['tvg-logo']
    tvg_id = channel['tvg-id']
    ch_name = channel['ch_name']
    print(
        f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')

    url = channel['url']
    print(url)

if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
