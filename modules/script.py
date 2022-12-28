import re, requests, bs4, wikipediaapi
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob

def summarize(text):
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)

    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    sentences = sent_tokenize(text)
    sentenceValue = dict()
    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq

    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]

    if len(sentenceValue) == 0:
        return ""
    average = int(sumValues / len(sentenceValue))

    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            summary += " " + sentence
    summary = re.sub(r'==.*?==+', '', summary)
    summary = re.sub(r"\[[0-9]*\]", '', summary)
    summary
    return summary


# Just a helper function to check if a string is present in an array
def contains(el, array):
    arr = list(map(lambda x: x.lower(), array))
    el = el.lower()
    return el in arr


# A function which corrects spellings in case web-scrapping fails
def correct(i, ask):
    blob = TextBlob(i)
    ok = ""
    if str(blob.correct()) == i:
        return i
    if ask:
        ok = input('Do you want to search for ' + str(blob.correct()) + ' instead ? (y/n) ')
    else:
        ok = 'y'
    if ok == 'y':
        return str(blob.correct())
    else:
        return i


# Function which scraps data from wikipedia
def get(tosearch):
    url = 'https://en.wikipedia.org/wiki/' + tosearch
    r = requests.get(url)
    return r


# Function which transforms text according to wikipedia url protocol
def reform(text):
    text = text.title()
    text = text.lstrip()
    text = text.rstrip()
    text = re.sub(' ', '_', text)
    return text


# Extracts data from html
def extractData(soup):
    paragraphs = soup.find_all('p')
    article_text = ""
    for para in paragraphs:
        article_text += para.text
    return article_text


# Main binding function for web scraping
def publish(value):
    r = get(reform(value))

    soup = bs4.BeautifulSoup(r.text, 'lxml')
    res = extractData(soup)
    corrected = value
    if r.status_code != 200 or summarize(res) == '':
        corrected = correct(value, True)
        r = get(reform(corrected))

    soup = bs4.BeautifulSoup(r.text, 'lxml')
    res = extractData(soup)

    summary = ''
    try:
        summary = summarize(res)
    except:
        summary = ''
    if summary != '':
        return [summary,corrected]
    else:
        fromwiki = getFromWiki(corrected)
        if fromwiki:
            return [fromwiki,corrected]
        else:
            return "I cannot find anything for you"


def getFromWiki(tosearch):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page(tosearch.title())
    content = page.text
    if content:
        content = content[0:content.index('See also')]
    else:
        content = False
    return content