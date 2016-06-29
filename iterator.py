import requests
import time
import itertools

SLEEP = 0.5
saved = []

def get(url):
  response = requests.get(url, timeout = 5)
  #print(response, url.split('/')[-1].split('.')[0])
  time.sleep(SLEEP)
  return response.status_code != 404

def trial(url, ans):
  while True:
    try:
      if get(url+ans):
        return url+ans
      return
    except Exception:
      print('failed to connect on '+str(ans))

def normalize(x):
  return x.replace(" ","").lower()

def nopunct(x):
  return x.replace(",","").replace(";","").replace("'","").replace(":","").replace(".","").replace('-','')

def concat(x):
  s = ''
  for i in x:
    s += i
  return s

def load_dict(x):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  num = "0123456789"
  f = None
  if x == 'enable': # ~174000 words
    f = open('enable2k.txt')
  if x == 'ukacd': # ? words
    f = open('UKACD17.txt')
  if x == '2a': # ? words
    f = open('web2a.txt')
  if x == 'countries':
    f = open('countries.txt')
  if x == 'cities':
    f = open('cities.txt')
  if x == 'names': # 1325 names
    f = open('propernames.txt')
  if x == 'popular':
    f = open('popular.txt')
  if x == 'phrase':
    f = open('phrases-wiki.txt')
  if x == 'newnoun':
    f = open('base_forms_en_nouns.txt')
  if x == 'numbers':
    return [str(k) for k in range(100000)]
  if x == 'negative':
    return [str(-k) for k in range(1000)]
  if x == 'deci1':
    return [str(k/10) for k in range(10000)]
  if x == 'deci2':
    return [str(k/100) for k in range(10000)]
  if x == 'deci3':
    return [str(k/1000) for k in range(10000)]
  if x == 'letters':
    return [chr(i) for i in range(97,123)]
  if x == 'bin':
    return ['{0:b}'.format(i) for i in range(10000)]
  if x == 'two':
    return itertools.product(alphabet, repeat=2)
  if x == 'tla':
    return itertools.product(alphabet, repeat=3)
  if x == 'fla':
    return itertools.product(alphabet, repeat=4)
  if x == 'musical':
    return itertools.product('abcdefg', repeat=7)
  if x == 'vowels':
    return itertools.product('aeiouy', repeat=5)
  if x == 'alphanum2':
    return itertools.product(alphabet+num, repeat=2)
  if x == 'alphanum3':
    return itertools.product(alphabet+num, repeat=3)
  return f.read().split("\n")

def d2b(i):
  return '{0:b}'.format(i)

def main(url):
  root = "http://bit.ly/"
  let = load_dict('letters')
  l = ['ois'+x+'ash'+y+'n' for x in let for y in let]
  print(len(l))
  st = 0
  begin = '' # first string to start at.
  for i in l:
    if i > begin:
      q = i
      if trial(root+url, str(q)): saved.append(url+str(q))
      if st%25 == 0: print(st, saved, url+str(q))
    st += 1
  print(saved)

main("")
