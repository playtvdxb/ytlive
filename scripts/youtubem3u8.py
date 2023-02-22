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
    return link[start : end]


# Define an empty list to hold the channels data
channels = []

# Load the youtube channel list
with open('../youtube_channel_list.json') as youtube_channel_list:
    youtube_channel_data = json.load(youtube_channel_list)
    for channel in youtube_channel_data:
        grp_title = channel['group-title']
        tvg_logo = channel['tvg-logo']
        tvg_id = channel['tvg-id']
        ch_name = channel['ch_name']

        url = channel['url']
        m3u8_url = grab(url)

        # Append the channel data to the list
        channels.append({
            "group-title": grp_title,
            "tvg-logo": tvg_logo,
            "tvg-id": tvg_id,
            "ch_name": ch_name,
            "m3u8_url": m3u8_url
        })


# Load the m3u8 channel list
with open('../m3u8_channel_list.json') as m3u8_channel_list:
    m3u8_channel_data = json.load(m3u8_channel_list)
    for channel in m3u8_channel_data:
        grp_title = channel['group-title']
        tvg_logo = channel['tvg-logo']
        tvg_id = channel['tvg-id']
        ch_name = channel['ch_name']

        m3u8_url = channel['url']

        # Append the channel data to the list
        channels.append({
            "group-title": grp_title,
            "tvg-logo": tvg_logo,
            "tvg-id": tvg_id,
            "ch_name": ch_name,
            "m3u8_url": m3u8_url
        })


# Write the channels data to a JSON file
with open('playlist.json', 'w') as f:
    json.dump(channels, f)
