import requests
from urllib.parse import urlparse, urlsplit
import argparse
from dotenv import load_dotenv
import os


def shorten_link(token, url):
    url_api_vk = 'https://api.vk.com/method/utils.getShortLink'

    headers = {'Authorization': f'Bearer {token}'}
    params = {'url': url, 'v': '5.199', 'private': '0'}

    response = requests.post(url_api_vk, headers=headers, params=params)
    response.raise_for_status()
    return response.json()['response']['short_url']


def count_clicks(token, short_link):
    url_api_vk = 'https://api.vk.com/method/utils.getLinkStats'

    headers = {'Authorization': f'Bearer {token}'}
    params = {
        'key': short_link,
        'v': '5.199',
        'interval': 'forever',
        'extendet': '0'
    }

    response = requests.post(url_api_vk, headers=headers, params=params)
    response.raise_for_status()
    return response.json()['response']['stats'][0]['views']


def is_shorten_link(url):
    parsed_url = urlsplit(url)
    return parsed_url.scheme == 'https' and parsed_url.netloc == 'vk.cc'


def main():
    load_dotenv()

    token = os.environ['VK_API_KEY']

    parser = argparse.ArgumentParser()
    parser.add_argument('link')
    args = parser.parse_args()

    if is_shorten_link(args.link):
        try:
            parsed_short_link = urlparse(args.link)
            short_link_path = parsed_short_link.path.split('/')[1]
            clicks = count_clicks(token, short_link_path)
            print(f'По вашей ссылке перешли {clicks} раз')
        except requests.exceptions.HTTPError as error:
            print('Неправильно введена ссылка')

    else:
        try:
            short_link = shorten_link(token, args.link)
            print(short_link)

        except requests.exceptions.HTTPError as error:
            print('Неправильно введена ссылка')


if __name__ == '__main__':
    main()
