import requests
from config import TOKEN, FILEPATH


class YaUploader:
    def __init__(self, disk_token: str):
        self.token = disk_token

    def upload(self, file_path: str):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        URL = f"https://cloud-api.yandex.net/v1/disk/resources/upload?path={FILEPATH}&overwrite={False}/files"
        response = requests.get(URL, headers=headers).json()

        if 'href' not in response.keys():
            print(f"Got an error:\n{response}")
        else:
            with open(file_path, 'r') as file:
                requests.put(response['href'], files={'file': file})
            print(f"Data uploaded")


if __name__ == '__main__':
    yandex_loader = YaUploader(TOKEN)
    yandex_loader.upload(FILEPATH)
