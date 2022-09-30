import requests
import time




class VK_API:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, user_id, version='5.194'):
        self.token = token
        self.id = user_id
        self.version = version

    def get_photos(self):
        method = 'photos.get'
        params = {'album_id':'profile',
                  'extended': 'likes',
                  'photo_sizes': '0',
                  'access_token': self.token,
                  'v': self.version}
        response = requests.get(VK_API.url + method, params=params).json()
        response = response['response']['items']
        sorted_list = []
        for resp in response:
            sort = {'date': resp['date'], 'likes': resp['likes']['count'], 'sizes': resp['sizes'][-1]}
            sorted_list.append(sort)
            # time.sleep(0.33)
        return sorted_list










