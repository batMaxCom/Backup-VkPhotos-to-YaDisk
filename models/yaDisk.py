import requests
from pprint import pprint
import os

from urllib.request import urlopen

class Ya_API:
    host = 'https://cloud-api.yandex.net'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'content-type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def vk_backup(self, img_list:list):
        url = f'{self.host}/v1/disk/resources/upload'
        headers = self.get_headers()
        for count, img in enumerate(img_list):
            if count > 4:
                break
            name = img['likes']
            params = {'path': f'/vk_backup/{name}.jpg', 'overwrite': 'True'}
            _href = requests.get(url, headers=headers, params=params).json().get('href')
            path_img = img['sizes']['url']
            r = requests.get(path_img, allow_redirects=True)
            response = requests.put(_href, data=r, headers=headers)
            response.raise_for_status()
            if response.status_code == 201:
                print('Success')




