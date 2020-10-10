from name import wiki

import pytest


def test_extract_name_from_paragraph():
    assert ('Kakuei Tanaka', ['田中 角栄', '田中 角榮']) == wiki.extract_name_from_paragraph_text(
        'Kakuei Tanaka (田中 角栄 or 田中 角榮, Tanaka Kakuei,')

    assert ('Toyohashi University of Technology', '豊橋技術科学大学') == wiki.extract_name_from_paragraph_text(
        'Toyohashi University of Technology (豊橋技術科学大学; Toyohashi Gijutsu Kagaku Daigaku), often abb')


@pytest.mark.webtest
def test_extract_wiki_page_1():
    entity = wiki.extract_name_from_wiki_page('https://en.wikipedia.org/wiki/Kakuei_Tanaka')
    assert entity
    assert entity.english_names == ['Kakuei Tanaka']
    assert entity.japanese_names == ['田中 角栄', '田中 角榮']
