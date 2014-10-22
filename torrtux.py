#!/usr/bin/env python

import urllib.request
from bs4 import BeautifulSoup
from colorama import Fore
from subprocess import call

userInput = input(Fore.BLUE + "PIRATE SEARCH : " + Fore.RESET)
#userInput="castle s01e02"
userInput.replace(" ", "%20")
page = 'https://thepiratebay.se/search/' + userInput + '/0/7/0ls'

pageContent = urllib.request.urlopen(page)

soup = BeautifulSoup(pageContent)

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
