import os
import sys
import urllib.request
import urllib.parse

curDir = os.getcwd()
print(curDir)

os.mkdir('newDir')

os.rename('newDir','newDir2')

os.rmdir('newDir2')


sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')


x = urllib.request.urlopen('https://www.google.com/')
print(x.read())


#url = 'https://www.google.com/search'
#values = {'q' : 'python programming tutorials'}
#data = urllib.parse.urlencode(values)
#data = data.encode('utf-8') # data should be bytes
#req = urllib.request.Request(url, data)
#resp = urllib.request.urlopen(req)
#respData = resp.read()

#print(respData)

try:
    url = 'https://www.google.com/search?q=python'

    # now, with the below headers, we defined ourselves as a simpleton who is
    # still using internet explorer.
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('withHeaders.txt','w')
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    print(str(e))