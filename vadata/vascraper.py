import re, urllib2, json
from BeautifulSoup import BeautifulSoup

def _build_json(text):
    metadata = {}
    soup = BeautifulSoup(text)

    ########## COMPLETE METADATA ITEMS ##########

    metadata['name'] = soup.find('b').text
    metadata['number'] = soup.find('a').text
    metadata['date_published'] = re.findall('.*(\d+\/\d+\/\d+).*', text)[0]
    metadata['is_published'] = True
    metadata['court'] = 'Court of Appeals of Virginia'

    parties = re.split('\s+v\.*\s+', soup.find('b').text)
    metadata['parties'] = {'plaintiff': parties[0] if len(parties) > 0 else None,
                           'defendant': parties[1] if len(parties) > 1 else None}

    metadata['text'] = {'pdf': 'http://www.courts.state.va.us/%s' % soup.find('a')['href'],
                        'text': 'rulings/%s.txt' % soup.find('a').text }


    ########## INCOMPLETE METADATA ITEMS ##########

    metadata['judges'] = []
    metadata['attorneys'] = []
    metadata['type'] = None
    metadata['cited_laws'] = None
    metadata['cited_cases'] = None
    metadata['author'] = None
    metadata['outcome'] = None

    return metadata


if __name__ == '__main__':
    # CHALLENGE: Write a one-line web scraper
    # STATUS: ACCEPTED.
    open('json/data.json', 'w').write(
        json.dumps(map(
            _build_json, [str(p) for p in BeautifulSoup(
                urllib2.urlopen('http://www.courts.state.va.us/wpcap.htm').read()).findAll('p') if bool(re.match(
                    '.*opncavwp', str(p)))]
            )
        )
    )