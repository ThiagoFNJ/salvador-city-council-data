import requests
from bs4 import BeautifulSoup

cms_website_request = requests.get("https://www.cms.ba.gov.br/transparencia/recursos-humanos")
cms_website_parser = BeautifulSoup(cms_website_request.text, "html.parser")