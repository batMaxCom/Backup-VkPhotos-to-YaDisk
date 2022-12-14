import requests
from models.log import logger
from tqdm import tqdm



class Ya_API:
    host = 'https://cloud-api.yandex.net'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'content-type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def get_status(self, path=''):
        url = f'{self.host}/v1/disk/resources'
        params = {'path': '/vk_backup/'+path}
        response = requests.get(url, headers=self.get_headers(), params=params)
        return response.json()

    def file_list_for_disk(self, path=''):
        file_list = self.get_status(path)['_embedded']['items']
        file_names = ','.join([str(file['name']) for file in file_list])
        return file_names


    def folder(self, path=''):
        url = f'{self.host}/v1/disk/resources'
        params = {'path':'/vk_backup/'+path}
        response = requests.get(url, headers=self.get_headers(), params=params)
        if response.status_code == 200:
            return True
        else:
            response = requests.put(url, headers=self.get_headers(), params=params)
            if response.status_code == 201:
                return True
            else:
                return f'Системная или ресурсная ошибка'

    @logger
    def vk_backup(self, img_list: list, path='', count_img=5):
        data_list = []
        if self.folder(path) == True:
            url = f'{self.host}/v1/disk/resources/upload'
            for count, img in tqdm(enumerate(img_list), total=count_img):
                if count > count_img-1:
                    break
                name = str(img['likes'])
                file_name = self.file_list_for_disk(path)
                if f'{name}.jpg' in file_name:
                    name = name + str(img['date'])
                params = {'path': f'/vk_backup/{path}{name}.jpg', 'overwrite': 'True'}
                _href = requests.get(url, headers=self.get_headers(), params=params).json().get('href')
                path_img = img['sizes']['url']
                r = requests.get(path_img, allow_redirects=True)
                response = requests.put(_href, data=r, headers=self.get_headers())
                response.raise_for_status()
                if response.status_code == 201:
                    data_list.append({'file_name': name + '.jpg', 'sized': img['sizes']['type']})
            print(f'Загрузка завершена {count_img} фотографий')
        return data_list



