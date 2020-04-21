
import lxml
from lxml import etree
from urllib.request import urlopen


def getVideoTitle(_url):
    youtube = etree.HTML(urlopen(_url).read())
    return str(youtube.xpath("//span[@id='eow-title']/@title"))
