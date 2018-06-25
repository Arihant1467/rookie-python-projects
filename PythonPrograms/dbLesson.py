import xml.etree.ElementTree as ET
import sqlite3
connection=sqlite3.connect("Music.sqlite")
cursor=connection.cursor()

# creating the tables
cursor.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Track;
''')
cursor.executescript('''
CREATE TABLE Artist(
id INTEGER NOT NULL AUTOINCREMENT PRIMARY KEY UNIQUE,
name TEXT UNIQUE
);
CREATE TABLE Album(
id INTEGER NOT NULL AUTOINCREMENT PRIMARY KEY UNIQUE,
artist_id INTEGER NOT NULL
name TEXT UNIQUE
);
CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None
fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'
# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
data=ET.parse(fname)
ele=data.findall("dict/dict/dict")
for sElement in ele:

