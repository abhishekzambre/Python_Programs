from lxml import html
import requests

page = requests.get('https://graduate.asu.edu/graduate-faculty/degree/G10')
tree = html.fromstring(page.content)

