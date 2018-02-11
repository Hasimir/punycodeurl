# -*- coding:utf-8 -*-

from encodings.punycode import punycode_encode
from encodings import idna
from urllib.parse import urlparse 

def get(url):
    if type(url) == str:
        if url.startswith('http://') is False and \
           url.startswith('https://') is False:
            url = "http://{0}".format(url)
    elif type(url) == unicode:
        # Unlikely to appear in Python 3, but leaving intact for now.
        if url.startswith(u'http://') is False and \
           url.startswith(u'https://') is False:
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
                code = part.encode('utf-8').decode('utf-8')
            except UnicodeEncodeError as e:
                pass

            part = "xn--{0}".format(punycode_encode(code))

        ret_parts.append(part)

    if o.query == "":
        target_url = "{0}://{1}{2}".format(o.scheme, '.'.join(ret_parts), o.path).replace("b'", "").replace("'", "")
    else:
        target_url = "{0}://{1}{2}?{3}".format(o.scheme, '.'.join(ret_parts), o.path, o.query).replace("b'", "").replace("'", "")

    return target_url
