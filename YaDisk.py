import requests
from settings import TOKEN


class YaUploader:
    HOST = 'https://cloud-api.yandex.net'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, path):
        uri = '/v1/disk/resources/upload/'
        request_url = self.HOST + uri
        params = {'path': path, 'overwrite': True}
        response = requests.get(request_url, headers=self.get_headers(), params=params)
        return response.json()['href']

    def upload(self):
        with open('List of files.txt', 'r') as f:
            for file_name in f:
                upload_url = self._get_upload_link(file_name)
                print(f'Загружаем {file_name}')
                response = requests.put(upload_url, data=open(file_name.strip(), 'rb'), headers=self.get_headers())
                if response.status_code == 201:
                    print('Загружено')


if __name__ == '__main__':
    YaUploader(TOKEN).upload()
