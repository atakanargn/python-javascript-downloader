import os, requests, argparse
from bs4 import BeautifulSoup

def download_file(url, folder):
    os.makedirs(folder, exist_ok=True)
    try:
        with open(os.path.join(folder, os.path.basename(url)), 'wb') as file:
            file.write(requests.get(url).content)
        print(f"Downloaded: {url}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

parser = argparse.ArgumentParser(description='Download script files from an HTML file.')
parser.add_argument('file_path', type=str, help='Path to the HTML file.')
args = parser.parse_args()

with open(args.file_path, 'r') as file:
    for script in BeautifulSoup(file.read(), 'html.parser').find_all('script', src=True):
        download_file(script['src'], 'downloaded_scripts')
