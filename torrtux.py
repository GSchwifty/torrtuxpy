#!/usr/bin/env python

import urllib.request
from bs4 import BeautifulSoup
from colorama import Fore
from subprocess import call

userInput = input(Fore.BLUE + "PIRATE SEARCH : " + Fore.RESET)
#userInput="castle s01e02"
userInput.replace(" ", "%20")
page = 'https://thepiratebay.org/search/' + userInput + '/0/7/0ls'
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
req = urllib.request.Request(page, headers=hdr)
pageContent = urllib.request.urlopen(req)

soup = BeautifulSoup(pageContent, "lxml")

def torrTitle(i): return(tdList[i][1].contents[1].text.strip())
def torrMagnetLink(i): return(tdList[i][1].contents[3].get('href'))
def torrDate(i): return(tdList[i][1].contents[7].text.split(', ')[0])
def torrSize(i): return(tdList[i][1].contents[7].text.split(', ')[1])
def torrUploader(i): return(tdList[i][1].contents[7].text.split(', ')[2])
def torrSE(i): return(tdList[i][2].contents[0])
def torrLE(i): return(tdList[i][3].contents[0])
def torrCategory(i): return(tdList[i][0].contents[1].find_all('a')[0].text)
def torrCategory2(i): return(tdList[i][0].contents[1].find_all('a')[1].text)

trList = soup.find_all('tr')
trList.pop(0)
tdList = [i.find_all('td') for i in trList]
print(Fore.YELLOW + "Num|", Fore.GREEN + "SE|", Fore.RED + "LE|", Fore.RESET + "Genre|", Fore.BLUE + "Name|", Fore.GREEN + "Author" + Fore.RESET, sep="")
for i in range(len(tdList)):
    print(Fore.YELLOW + str(i), Fore.GREEN + torrSE(i), Fore.RED + torrLE(i), Fore.RESET + torrCategory(i), Fore.BLUE + torrTitle(i) + Fore.RESET)
#    print(Fore.YELLOW + str(i), Fore.GREEN + torrSE(i), Fore.RED + torrLE(i), Fore.RESET + torrCategory(i), Fore.BLUE + torrTitle(i), Fore.GREEN + torrUploader(i), torrSize(i) + Fore.RESET)
print(Fore.YELLOW + "==>", Fore.BLUE + "Copy the magnet link?" + Fore.RESET)
torrentSelected = input(Fore.YELLOW + "==> " + Fore.RESET)
print(torrMagnetLink(int(torrentSelected)))
call(["transmission-remote", "-a", torrMagnetLink(int(torrentSelected))])
