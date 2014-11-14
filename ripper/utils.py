import re

def image_name(url):
    pattern = re.compile(r'.+\/(.+)')
    match = re.match(pattern, url)
    return match.group(1)

def vertical_to_comma(string):
	string = re.split(r'(,|\s)',string)
	string = '|'.join(string)
	return string
