import random
import urllib
from hello.domains import myRandom, memberlist
from quiz00 import Quiz00
import random

from bs4 import BeautifulSoup
from urllib.request import urlopen
import  pandas as pd


class Quiz20:

    def quiz20list(self) -> str: return None

    def quiz21tuple(self) -> str: return None

    def quiz22dict(self) -> str: return None

    def quiz23listcom(self) -> str:
        print('---legacy---')
        a=[]
        for i in range(5):
            a.append(i)
        print(a)

        print('---comprehension---')
        a2=[i for i in range(5)]
        print(a2)
        return None

    def quiz24bugs_zip(self) -> {}:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml')  # html.parser vs lxml

        # self.print_music_list(soup) # 아티스트와 타이틀을 분리해서 출력하기
        # self.find_rank(soup) # 랭킹보기
        # a = [i for i in cls_names]
        # print(soup.prettify())
        ls1 = self.find_bugs_music(soup, 'title')
        ls2 = self.find_bugs_music(soup, 'artist')
        a = [i if i == 0 or i == 0 else i for i in range(1)]
        b = [i for i in []]
        c = [(i, j) for i, j in enumerate([])]
        d = {i: j for i, j in zip(ls1, ls2)}
        dict = {i:j for i, j in zip(ls1,ls2)}
        l = [ i + j for i, j in zip(ls1,ls2)]
        l2 = list(zip(ls1,ls2))
        #d1 = dict(zip(ls1,ls2))
        # self.dict1(ls1, ls2)
        # self.dict2(ls1, ls2)
        # self.dict3(ls1, ls2)
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
            print(dict)
        return dict

    def print_bugs_list(self, soup) -> None:
        artists = soup.find_all('p', {'class': 'artist'})
        # print(type(artists)) # <class 'bs4.element.ResultSet'>
        artists = [i.get_text() for i in artists]
        # print(type(artists))
        print(''.join(i for i in artists))
        titles = soup.find_all('p', {'class': 'title'})
        titles = [i.get_text() for i in titles]
        print(''.join(i for i in titles))

    def find_bugs_rank(self, soup):
        for i, j in enumerate(['artist', 'title']):
            for i, j in enumerate(self.find_bugs_music(soup, j)):
                print(f'{i}위 : {j}')
                print('#' * 100)

    @staticmethod
    def find_bugs_music(soup, cls_nm) -> []:
        ls = soup.find_all('p', {'class': cls_nm})
        return [i.get_text() for i in ls]


    @staticmethod
    def dict3(ls1,ls2):
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
            print(dict)
        return dict


    @staticmethod
    def dict2(ls1,ls2):
        dict = {}
        for i, j in enumerate(ls1):
            dict[j] = ls2[i]
        print(dict)

    @staticmethod
    def dict1(ls1,ls2) -> None:
        dict = {}
        for i in range(len(ls1)):
            dict[ls1[i]] = ls2[i]
        print(dict)

    @staticmethod
    def quiz25dictcom()-> str:
        a = Quiz00
        #1명인데 5명 추출 0~100사이 랜덤
        b = set([a.quiz06memberChoice() for i in range(5)])
        print(b)
        while len(b) !=5:
            b.add(a.quiz06memberChoice())

        scores = [myRandom(0,101)for i in range(5)]
        students = list(b)
        aa={i : j for i , j in zip (students,scores)}

        print(aa)

    def quiz26map(self) -> str: return None

    def quiz27melon_zip(self) -> {}:

        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        ls1 = self.find_melon_music(soup,'ellipsis rank01')
        ls2 = self.find_melon_artist(soup, 'checkEllipsis')
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
        print(dict)
        return dict

        # artists = soup.find_all('span',{'class' : 'checkEllipsis'})
        # artists = [i.get_text() for i in artists]
        # print('\n'.join(i for i in artists))
        #title = soup.find_all('div', {'class': 'ellipsis rank01'})
        #title = [i.get_text() for i in title]
        #print(''.join(i for i in title))
        # print(soup)

    def print_melon_list(self, soup) -> None:
        for i, j in enumerate(['ellipsis rank01', 'checkEllipsis']):
            print(''.join(i for i in [i for i in self.find_melon(soup, j)]))
            print('*' * 100)

    def find_melon_rank(self, soup) -> None:
        for i, j in enumerate(['ellipsis rank01', 'checkEllipsis']):
            for i, j in enumerate(self.find_melon(soup, j)):
                print(f'{i}위 : {j}')
            print('*' * 100)

    @staticmethod
    def find_melon_music(soup, music) -> []:
        ls = soup.find_all('div', {'class':  music})
        return [i.get_text() for i in ls]

    @staticmethod
    def find_melon_artist(soup, artist) -> []:
        ls = soup.find_all('span', {'class': artist})
        return [i.get_text() for i in ls]

    def quiz28dataframe(self) -> None:
        dict = self.quiz24bugs_zip()
        df = pd.DataFrame.from_dict(dict, orient='index')
        soup = BeautifulSoup()
        print(df)
        df.to_csv('./save/bugs.csv', sep=',', na_rep='NaN')

        dict1 = self.quiz27melon_zip()
        ds = pd.DataFrame.from_dict(dict1, orient= 'index')
        soup = BeautifulSoup()
        print(ds)
        ds.to_csv('./save/melon.csv', sep=',', na_rep='NaN')
    '''
    다음 결과 출력
        a   b   c
     1  1   3   5
     2  2   4   6
     
    '''
    def quiz29_pandas_(self) -> object:
        d2 = {"1": [1, 3, 5], "2": [2, 4, 6]}
        d3 = {"1": [1, 3, 5]}
        d4 = {"2": [2, 4, 6]}
        '''
        *방법1
        df2 = pd.DataFrame.from_dict(d2, orient='index', columns=['a', 'b', 'c'])
        print(df2)
        ---------------------------------------
        *방법2
        d = {'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}
        df1 = pd.DataFrame(d, index=[1, 2])
        print(df1)
        '''
        evens = []
        odds = []
        [evens.append(i) if i % 2 == 0 else odds.append(i) for i in range(1,7)]
        #print(j)
        #print(h)

        jh = [odds,evens]
        #print(jh)
        ind = ['1','2']
        c_zip = {i:j for i, j in zip(ind, jh)}
        #print(c_zip)
        c = [chr(i) for i in range(97, 100)]
        df3 = pd.DataFrame.from_dict(c_zip, orient='index', columns=c)
        print(df3)
        '''   
           0  1  2
        1  1  3  5
        2  2  4  6
        '''
        df4 = pd.DataFrame.from_dict(c_zip, orient='index')
        #print(df4)

        #frame = pd.DataFrame(d1, index=[1,2])
        #print(frame)

        return None

