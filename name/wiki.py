import requests
import csv
import re

from name import NamedEntity
from bs4 import BeautifulSoup


def extract_name_from_wiki_page(page_url):
    res = requests.get(page_url)
    page = BeautifulSoup(res.text, features="html.parser")

    empty_elems = page.select('.mw-empty-elt')
    for e in empty_elems:
        e.extract()

    first_paragraph = page.select_one('#mw-content-text p:first-of-type')
    name_pair = extract_name_from_paragraph_text(first_paragraph.text)

    if name_pair:
        return NamedEntity(page_url, name_pair[0], name_pair[1])

    elem_name = page.select_one('#mw-content-text p:first-of-type>b')
    if not elem_name:
        return None

    elem_name_jp = page.select_one('#mw-content-text p:first-of-type span[lang=ja]')
    if not elem_name_jp:

        elem_name_jp = page.select_one('.infobox [lang=ja].nickname')
        if not elem_name_jp:
            return None

    name_en = elem_name.get_text()
    name_jp = elem_name_jp.get_text()
    name_en = re.sub(r'\s*\(.*\)', '', name_en)
    return name_en, name_jp


def extract_name_from_paragraph_text(text: str):
    """
    Extracting names from "Name (名前, ..." pattern
    """
    pattern = re.compile(r'([\w\s.,]+)\s\(([\w\s]+)[).,;]')
    match = pattern.match(text)
    if not match:
        return None

    primary_name = match[1]
    alt_names = match[2]
    if ' or ' in alt_names:
        alt_names = alt_names.split(' or ')

    return primary_name, alt_names
