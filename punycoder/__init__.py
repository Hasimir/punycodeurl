# -*- coding:utf-8 -*-

from encodings.punycode import punycode_encode
from encodings import idna
from urllib.parse import urlparse 

def get(url):
    if type(url) == str:
        if url.startswith('http://') == False and \
           url.startswith('https://'):
            url = "http://{0}".format(url)
    elif type(url) == unicode:
        if url.startswith(u'http://') == False and \
           url.startswith(u'https://'):
            url = u"http://{0}".format(url)

    def need_punycode(string):
        for ch in string:
            if ord(ch) > 127:
                return True

        return False

    if need_punycode(url) == False:
        return url

    o = urlparse(url)
    ret_parts = []
    parts = idna.dots.split(o.netloc)

    for part in parts:
        if need_punycode(part) == True:
            code = part
            try:
                code = part.decode('utf8')
            except UnicodeEncodeError as e:
                pass

            part = "xn--{0}".format(punycode_encode(code))

        ret_parts.append(part)

    if o.query == "":
        target_url = "{0}://{1}{2}".format(o.scheme, '.'.join(ret_parts), o.path)
    else:
        target_url = "{0}://{1}{2}?{3}".format(o.scheme, '.'.join(ret_parts), o.path, o.query)

    return target_url
