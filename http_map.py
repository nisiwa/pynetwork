#!/usr/bin/env python
# encoding: utf-8
import http.client
import urllib

def geocode(address, ak='ZIhr931pcZwO3sDhCPkAvnUUvrIMXUIn'):
    address_toutf = address.encode('utf-8')
    new_ad = urllib.parse.quote(address_toutf)
    param = "/geocoder/v2/?address={}&output=json&ak={}".format(new_ad, ak)
    connection = http.client.HTTPConnection("api.map.baidu.com")
    connection.request('GET', param)
    rawreplay = connection.getresponse().read()
    rawreplay_dict = eval(rawreplay)
    #replay = json.loads(rawreplay.encode('utf-8'))
    print('response:{}'.format(rawreplay_dict))
    print('lat:{}, lng:{}'.format(rawreplay_dict['result']['location']['lat'], rawreplay_dict['result']['location']['lng']))

if __name__ == "__main__":
    #geocode(address=b'\xe5\x8c\x97\xe4\xba\xac')
    geocode(address='北京')
