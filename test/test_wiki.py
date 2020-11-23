from name import wiki

import pytest


def test_extract_name_from_paragraph():
    assert ('Kakuei Tanaka', ['田中 角栄', '田中 角榮']) == wiki.extract_name_from_paragraph_text(
        'Kakuei Tanaka (田中 角栄 or 田中 角榮, Tanaka Kakuei,')

    assert ('Toyohashi University of Technology', ['豊橋技術科学大学']) == wiki.extract_name_from_paragraph_text(
        'Toyohashi University of Technology (豊橋技術科学大学; Toyohashi Gijutsu Kagaku Daigaku), often abb')

    assert ('Ijuin Tada\'aki', ['伊集院忠朗']) == wiki.extract_name_from_paragraph_text(
        'Ijuin Tada\'aki(伊集院忠朗; 1520–1561)')

    assert ('Yasuke', ['弥助', '弥介']) == wiki.extract_name_from_paragraph_text(
        'Yasuke (variously rendered as 弥助 or 弥介, 彌助 or 彌介 in different sources)')


def test_extract_name_from_paragraph_negative_cases():
    assert None == wiki.extract_name_from_paragraph_text(
        'Yui (born March 26, 1987), stylized as')



@pytest.mark.webtest
def test_extract_wiki_page_1():
    entity = wiki.extract_name_from_wiki_page('https://en.wikipedia.org/wiki/Kakuei_Tanaka')
    assert entity
    assert entity.english_names == ['Kakuei Tanaka']
    assert entity.japanese_names == ['田中 角栄', '田中 角榮']

@pytest.mark.webtest
def test_extract_wiki_page_2():
    entity = wiki.extract_name_from_wiki_page('https://en.wikipedia.org/wiki/Ijuin_Tadaaki')
    assert entity
    assert entity.english_names == ['Ijuin Tada\'aki']
    assert entity.japanese_names == ['伊集院忠朗']


@pytest.mark.webtest
def test_extract_wiki_page_3():
    entity = wiki.extract_name_from_wiki_page('https://en.wikipedia.org/wiki/Susumu_Tonegawa')
    assert entity
    assert entity.english_names == ['Susumu Tonegawa']
    assert entity.japanese_names == ['利根川 進']




