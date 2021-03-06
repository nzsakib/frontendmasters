import os
import os.path
import string
import requests
from urllib.request import urlopen

def format_filename(filename_str):
    s = filename_str
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ', '_')
    return filename

def get_file_path_from_url(url):
    return url.split("?")[0].split(".")[-1]

def download_file(url, path, self):
    # FIXME(Xinyang): Better exception handling for empty url
    if url is None:
        return
    if len(url) <= 1:
        return

    if not os.path.isfile(path) or os.path.getsize(path) == 0:
        self.browser.get(url)
        temporaryURL = self.browser.current_url
        self.browser.back()
        download_file_mine(temporaryURL, path)
        # buff = urlopen(temporaryURL)
        # print("Downloading: %s" % (path))
        #
        # with open(path, 'wb') as local_file:
        #     local_file.write(buff.read())


def create_path(path):
    if not os.path.exists(path):
        os.makedirs(path)

def download_file_mine(url, save_path):
    r = requests.get(url, stream=True)
    url = r.url
    # parsed = urlparse.urlparse(url)
    # local_filename = urlparse.parse_qs(parsed.query)['filename'][0]
    # index = 1
    # save_path = os.path.join(folder, local_filename)

    # while os.path.isfile(save_path):
    #     base_filename, file_extension = os.path.splitext(save_path)
    #     base_filename += str(index)
    #     save_path = base_filename + file_extension
    #     index += 1

    print(("Downloading ...: " + save_path))

    with open(save_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

    # return local_filename
