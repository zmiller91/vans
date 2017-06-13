import xml.etree.ElementTree as ET
import mysql.connector
import conf
import urllib2
import re
import json


def get_child_like_tag(node, tag):
    for c in node:
        if tag in c.tag:
            return c
    return None


def text(node):
    if node != None:
        return node.text
    return None


def resource(node):
    if node != None:
        return node.attrib['resource']
    return None


def parse_item(node):
    link = text(get_child_like_tag(node, 'link'))
    desc = {
        'title': re.escape(text(get_child_like_tag(node, 'title'))),
        'link': text(get_child_like_tag(node, 'link')),
        'description': re.escape(text(get_child_like_tag(node, 'description'))),
        'date': text(get_child_like_tag(node, 'date')),
        'enclosure': resource(get_child_like_tag(node, 'enclosure'))
    }

    return desc

def insert_listing(listing, connection):

    img = listing['enclosure']
    listing['enclosure'] = "'" + img + "'" if img is not None else '\N'
    sql = '''
            REPLACE INTO listings
            (city, title, link, description, image, date)
            VALUES
            ('%(city)s', '%(title)s', '%(link)s', '%(description)s', %(enclosure)s, '%(date)s');
        ''' % listing

    listing['enclosure'] = img
    connection.cursor().execute(sql)
    connection.commit()


def save_item(item):
    print item


def get_configuration(connection):

    configuration = {}
    cursor = connection.cursor()
    query = ("SELECT * FROM configuration;")
    cursor.execute(query)

    for (name, jsn) in cursor:
        configuration[name] = json.loads(jsn.decode("utf-8") )

    return configuration


def GET(url):
    response = urllib2.urlopen(url)
    return response.read()


conn = mysql.connector.connect(user=conf.dbuser, password=conf.dbpasswd, host=conf.dbhost, database=conf.db)

clconfig = get_configuration(conn)
for city in clconfig['cities']:
    url = "https://" + city + "." + conf.baseurl + clconfig['search']
    tree = ET.ElementTree(ET.fromstring(GET(url)))
    root = tree.getroot()
    for node in root:
        if "item" in node.tag:
            item = parse_item(node)
            item['city'] = city
            insert_listing(item, conn)

