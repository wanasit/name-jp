import csv
from typing import List


class NamedEntity:
    def __init__(self, src_url, english_names=None, japanese_names=None):
        self.src_url = src_url
        self.english_names = _str_list(english_names)
        self.japanese_names = _str_list(japanese_names)

    @property
    def english_name(self):
        return self.english_names[0] if self.english_names else None

    @property
    def japanese_name(self):
        return self.japanese_names[0] if self.japanese_names else None

    def __repr__(self):
        return '<Entity src_url=%s (%s, %s)>' % (self.src_url, self.english_name, self.japanese_name)

    def __eq__(self, other):
        if isinstance(other, NamedEntity):
            return self.src_url == other.src_url and \
                   self.english_names == other.english_names and \
                   self.japanese_names == other.japanese_names
        return False

    @staticmethod
    def from_csv(fp):
        names = []
        reader = csv.reader(fp)
        next(reader)  # Expect header
        for row in reader:
            src_url = row[0]
            english_names = row[1].split('; ')
            japanese_names = row[2].split('; ')
            names.append(NamedEntity(src_url, english_names, japanese_names))
        return names

    @staticmethod
    def to_csv(entities, fp):
        # sort entities by src_url
        # header: src_url, english_names, japanese_names
        # serialize
        writer = csv.writer(fp)
        writer.writerow(['src_url', 'english_names', 'japanese_names'])
        for e in entities:
            writer.writerow([
                e.src_url,
                '; '.join(e.english_names),
                '; '.join(e.japanese_names),
            ])

def _str_list(str_or_list):
    if not str_or_list:
        return []

    if isinstance(str_or_list, str):
        return [str_or_list]

    return [n for n in str_or_list]
