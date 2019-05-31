import urllib.request
import json


def getJson(request_url):
    url = str(request_url)
    req = urllib.request.Request(url, headers={'User-Agent': "Magic Browser"})
    r = urllib.request.urlopen(req).read()
    json_data = json.loads(r.decode('utf-8'))

    return json_data


def get_format(format):
    if format == "image/jpeg":
        return ".jpg"
    elif format == "image/png":
        return ".png"
    else:
        return ".png"


def saveImage(url, path, filename):
    url_address = url

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}
    request_ = urllib.request.Request(
        url_address, None, headers)  # The assembled request
    response = urllib.request.urlopen(request_)  # store the response
    # create a new file and write the image
    f = open(path+"/"+filename, 'wb')
    f.write(response.read())
    f.close()


# info = getJson(
#     "https://wallhaven.cc/api/v1/search?categories=010&purity=100&resolutions=1920x1080&sorting=random&order=asc")

# # print(len(info['data']))

# for x in range(len(info['data'])):
#     img_id = info['data'][x]['id']
#     img_format = info['data'][x]['file_type']
#     img_url = info['data'][x]['path']

#     print(img_url)
#     image_location = "images/"+img_id+""+get_format(img_format)
#     print(image_location)

#     saveImage(img_url, img_id+""+get_format(img_format))
