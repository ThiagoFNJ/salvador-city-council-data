from bs4 import BeautifulSoup as soup
import pandas as pd
import requests
import re

cms_website_request = requests.get("https://www.cms.ba.gov.br/transparencia/recursos-humanos")
cms_website_parser = BeautifulSoup(cms_website_request.text, "html.parser")

documents = []

for divTag in cms_website_parser.find_all("div", attrs = {"class" : re.compile("tab-pane fade in")}):
  doc_year = divTag['id']

  for h3Tag in divTag.find_all("h3"):
    doc_list = h3Tag.find_next_sibling("ul")

    for liTag in doc_list.find_all("li"):
      doc_metadata = []

      doc_download_link = liTag.a['href']
      doc_reference_date = re.sub(" ", "", re.sub("\r\n","", liTag.a.em.get_text()))
      doc_type = h3Tag.get_text()
    
      doc_metadata.append(doc_type)
      doc_metadata.append(doc_year)
      doc_metadata.append(doc_reference_date)
      doc_metadata.append("https://www.cms.ba.gov.br" + doc_download_link)

      documents.append(doc_metadata)