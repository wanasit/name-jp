import tempfile

from name.named_entity import NamedEntity


def test_basic():
    name = NamedEntity('https://en.wikipedia.org/wiki/Yoshisuke_Aikawa', 'Yoshisuke Aikawa', '鮎川 義介')
    assert name.japanese_name == '鮎川 義介'
    assert name.english_name == 'Yoshisuke Aikawa'


def test_read_write_csv():
    names = [
        NamedEntity('https://en.wikipedia.org/wiki/Yoshisuke_Aikawa', 'Yoshisuke Aikawa', '鮎川 義介'),
        NamedEntity('https://en.wikipedia.org/wiki/Kakuei_Tanaka', 'Kakuei Tanaka', ['田中 角栄', '田中 角榮'])
    ]

    with tempfile.TemporaryFile('r+') as fp:
        NamedEntity.to_csv(names, fp)

        fp.seek(0)
        read_names = NamedEntity.from_csv(fp)

    assert read_names == names
    assert read_names[1].src_url == 'https://en.wikipedia.org/wiki/Kakuei_Tanaka'
    assert read_names[1].japanese_names == ['田中 角栄', '田中 角榮']
