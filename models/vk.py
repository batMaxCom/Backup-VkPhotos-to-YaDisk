import requests
import time

class VK_API:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version='5.194'):
        self.token = token
        self.version = version

    def get_photos(self, album_id='profile'):
        time.sleep(0.33)
        method = 'photos.get'
        params = {'album_id':album_id,
                  'extended': 'likes',
                  'photo_sizes': '0',
                  'access_token': self.token,
                  'v': self.version,
                  'count':1000,
                  'user_ids':'1'}
        response = requests.get(VK_API.url + method, params=params).json()
        response = response['response']['items']
        sorted_list = []
        count_img = ''
        for count, resp in enumerate(response):
            sort = {'date': resp['date'], 'likes': resp['likes']['count'], 'sizes': resp['sizes'][-1]}
            sorted_list.append(sort)
            count_img = count+1
        return sorted_list, count_img

    def get_album_photo(self):
        time.sleep(0.33)
        method = 'photos.getAlbums'
        params = {'access_token': self.token,
                  'v': self.version,
                  'user_ids':'1'}
        response = requests.get(VK_API.url + method, params=params).json()
        response = response['response']['items']
        sorted_list = []
        for resp in response:
            sort = {'id': resp['id'], 'name': resp['title']}
            sorted_list.append(sort)
            time.sleep(0.33)
        return sorted_list











