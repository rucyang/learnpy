from lxml.html import parse
from urllib.request import urlopen
from pandas.io.parsers import TextParser

parsed = parse(urlopen('https://www.google.com.hk/finance'))
doc = parsed.getroot()
links = doc.findall(".//a")
tables = doc.findall(".//table")
my_table = tables[1]
rows = my_table.findall(".//tr")


def _unpack(row, kind="td"):
    elts = row.findall(".//%s" % kind)
    return [val.text_content() for val in elts]


def parse_options_data(table):
    rows = table.findall('.//tr')
    header = [val.get('class') for val in rows[0].findall(".//td")]
    data = [_unpack(r) for r in rows]
    return TextParser(data, names=header).get_chunk()


my_data = parse_options_data(my_table)
my_data = my_data.apply(lambda s: s.str.strip())
print(my_data)
