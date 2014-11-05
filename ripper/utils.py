import re

def image_name(url):
	pattern = re.compile('.+\/(.+)')
	match = re.match(pattern, url)
	return(match.group(1))
