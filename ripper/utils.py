import re

def image_name(url):
    pattern = re.compile(r'.+\/(.+)')
    match = re.match(pattern, url)
    return match.group(1)
