# coding: utf-8
#!/usr/bin/env python



from itertools import zip_longest

def func(x):
    if len(x) % 2:
        s = len(x)//2 + 1
    else:
        s = len(x)//2
    keys = x[:s]
    values = x[s:][::-1]
    return {k: v for k, v in zip_longest(keys, values)}

print(func('abcde'))
print(func('abcdef'))
print(func('abcdefg'))

# 一つの文字xが与えられた時、一文字ずつスライスして下記の形式で返す関数を作成せよ
# 例：’abcde’=> {a:e, b:d, c:None}
# [a, b, c]  [d, e]

# from itertools import zip_longest

# def func(x):
#     if len(x) % 2:
#         s = len(x)//2 + 1
#     else:
#         s = len(x)//2
#     keys = x[:s]
#     values = x[s:][::-1]
#     return {k: v for k, v in zip_longest(keys, values)}

# print(func('abcde'))
# print(func('abcdef'))
# print(func('abcdefg'))



# names = ['Rao', 'Toki', 'Jagi', 'Ken']
# numbers = [1, 5]

# for name, number in zip_longest(names, numbers):
#     print(name, number)


# def func(x):
#     print(len(x))
#     # ['a', 'b', 'c', 'd', 'e', '']









# def func(x):
#     xlist = []
#     for i in x:
#         if i % 2 == 0:
#         	xlist.append(i)
#             # s += i
#             # s = s + i
#         else:
#         	xlist.append(-i)
#     return sum(xlist)

# print(func([1, 3, 5, 0, 9, 7, 6]))

# # data = [1, 2, 3, 4, 5]

# def func(x):
#     return sum(i if i % 2 == 0 else -i for i in x)

# print(func([1, 3, 5, 0, 9, 7, 6]))

# print(func([1, 3, 5, 0, 9, 7, 6]))

# even_list = [i if i % 2 == 0 else "odd" for i in range(10)]

# even_list = []
# for i in range(10):
#     if i % 2 == 0:
#         even_list.append(i)
#     else:
#         even_list.append("odd")


"""
https://sonogym.sizebook.jp/program/42/create/
- ２つのリストを連結させ、重複したキーは値の合計をいれよ
例
list1 = {'sonoki': 25, 'anzu': 28, 'yun': 32, 'shogo': 30, 'kenta': 31}
list2 = {'youko': 100, 'anzu': 40, 'yun': 50, 'sawai': 20, 'kenta': 60}
結果
{'sonoki': 25, 'anzu': 68, 'yun': 82, 'shogo': 30, 'kenta': 91, 'youko': 100, 'sawai': 20}
"""

# list1 = {'sonoki': 25, 'anzu': 28, 'yun': 32, 'shogo': 30, 'kenta': 31}
# list2 = {'youko': 100, 'anzu': 40, 'yun': 50, 'sawai': 20, 'kenta': 60}

# print(list1)
# print(list2)
# print(list1['sonoki'])


# for i in list1:
#     for p in list2:
#         print(i, p)
#         if i == p:
#             print(i, list1[i], list2[i])
#     print(i, p)


# https://sonogym.sizebook.jp/program/86/create/
# で作った100個の数字の標準偏差を求めよ
# ただしstatistics とnumpyは使用禁止



# import random
# import math

# rlist = [random.randint(0, 99) for i in range(100)]

# # 平均値
# average = sum(rlist)/len(rlist)

# # 偏差(各データの値から平均値を引いた値)を求めて、2乗
# hensa = []
# for i in rlist:
#     s = (i - average) ** 2
#     hensa.append(s)

# # 偏差の2乗の合計をデータの総数で割る
# bunsan = sum(hensa)/len(rlist)

# # 分散の正の平方根が標準偏差
# print(math.sqrt(bunsan))








# def func(x):
#     s = 0
#     for i in x :
#         if i % 2 == 0:
#             s += i
#         else:
#             s -= i
#     return s

# # print(func([1, 3, 5, 0, 9, 7, 6]))

# [s += i if a % 2 == 0 else print('odd')]



# Q1.
# 0~99までの乱数を100個生成し
# 以下のように分類せよ
# 0~9は0代とする
# 0代:10
# 10代:5
# 20代:14
# 30代:17
# 40代:13
# 50代:14
# 60代:19
# 70代:14
# 80代:13
# 90代:26

# import random

# rlist = [random.randint(0, 99) for i in range(100)]
# print(rlist)

# for i in range(0, 10):
#     print(i*10, (i*10+10)) # 0<= <10, 10<= <20
#     print([i*10<=x<(i*10+10) for x in rlist])
#     a = sum(i*10<=x<(i*10+10) for x in rlist)
#     print('{}代:{}'.format(i*10, a))



# def func(x):
#     l = [chr(i) for i in range(ord('a'), ord('z')+1)] + ['a']
#     print(l)
#     s = ''
#     for i in x:
#         if i == ' ':
#             s += ' '
#         else:
#             s += l[l.index(i) + 1]
#     print(s)

# func('abc z')














# もとの問題：
# https://sonogym.sizebook.jp/program/34/create/

# 一つのリストxが与えられた時、偶数の場合加算して、奇数の場合減算する、関数を作成せよ
# 例：[1, 3, 5, 0, 9, 7, 6] == -19


# def func(x):
#     s = 0
#     for i in x:
#         if i % 2 == 0:
#             s += i
#         else:
#             s -= i
#     return s

# print(func([1, 3, 5, 0, 9, 7, 6]))



# https://sonogym.sizebook.jp/program/40/create/
# のアレンジ版

# 与えられた文字列の文字を１つずつ後ろにずらした文字列を作成せよ
# ただし、
# ・英小文字と半角スペースのみ使用
# ・ｚの次はaになる
# ・スペースはそのまま
# とする。
# def func(x):
#     l = [chr(i) for i in range(ord('a'), ord('z')+1)] + ['a']
#     s = ''
#     for i in x:
#         if i == ' ':
#             s += ' '
#         else:
#             s += l[l.index(i) + 1]
#     print(s)

# func('abc z')


# def func(x):
#     l = [chr(i) for i in range(ord('a'), ord('z')+1)]
#     s = ''
#     for i in x:
#         if i == ' ':
#             s += ' '
#         else:
#             s += l[l.index(i) + 1]
#     print(s)

# func('mo ji')

# 文字列の中で~が出るたびに小文字と大文字を切り替えて文字列をコピーする関数作ってみな。
# ただし
# 　大文字モードのときに大文字が来ても変化なし。
# 　小文字モードのときに小文字が来ても変化なし。

# s = "saikin ~usuge~ ga kininaru kanojo ha ~SVENSON~ wo hajime ~masita."
# 出力：
# saikin USUGE ga kininaru kanojo ha SVENSON wo hajime MASITA.
# x = [1, 3, 5, 8, 9, 7, 6]
# y = [1, 5, 8, 7]
# def multiple_3_judgement(l):
#     return [a % 3 == 0 for a in l]

# print(multiple_3_judgement(x))
# print(multiple_3_judgement(y))

# もとの問題：
# https://sonogym.sizebook.jp/program/37/create/

# 次の文字列を解析し、指定した単語がいくつ出てきたか辞書で返す関数を作成せよ

# st = "ノッキいえい！むうむう。むう？いえい！キィィ！むう…。むあむあ？くぅぁくぅぁ。ミー。むう。"
# words = ['ノッキ', 'むう', 'iPhone', 'カヌー']

# 実行結果
# {'ノッキ': 1, 'むう': 5, 'iPhone': 0, 'カヌー': 0}


# def func(x, y):
#     d = dict()
#     for i in y:
#         d[i] = x.count(i)
#     return d

# st = "ノッキいえい！むうむう。むう？いえい！キィィ！むう…。むあむあ？くぅぁくぅぁ。ミー。むう。"
# words = ['ノッキ', 'むう', 'iPhone', 'カヌー']

# print(func(st, words))

# ある数字xが与えられた場合、0からxまでの整数をフィボナッチ数列の長さでsliceしたlistを返す関数slice_fib(x)を作成する。
# （例：x＝１０） [ [0], [1], [2, 3], [4, 5, 6], [7, 8, 9] ]
# （例：x＝１００） [[0], [1], [2, 3], [4, 5, 6], [7, 8, 9, 10, 11], 
# [12, 13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32], 
# [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], 
# [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 
# 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], 
# [88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]]





# 下記の関数にデコレータを使って”Hello wold!!”と返す

# 下記の関数にデコレータを使って”Hello wold!!”と返す
# def world():
# return ‘world’

# def is_world(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#     return wrapper



# @is_world
# def world():
#     return 'world'

# is_world()


# class myDecorator(object):
#     def my_decorator(self, my_func):
#         def decorator_wrapper(*args, **kwargs):
#             print('--- decorator before my_func ---')
#             my_func(*args, **kwargs)
#             print('--- decorator after my_func ---\n')

#         return decorator_wrapper

# decorator = myDecorator()

# @decorator.my_decorator
# def print_hello():
#     print('hello world')

# print_hello()

# def hoehoe(func):
#     def wrapper(*args, **kwargs):
#         if args[0] % 3 == 0:
#             return "ほえほえ"
#         else:
#             return func(*args, **kwargs)
#     return wrapper

# @hoehoe
# def is_even(n):
#     if n % 2 == 0:
#         return "偶数"
#     else:
#         return "奇数"

# print(is_even(1))
# print(is_even(2))
# print(is_even(3))



# a = "abc def ghi jkl mno pqr stu V"
# print(a.split())
        # (p.split('/'))
#     a = ''
#     a += x
#     print(list(a))


# print(func("abcdefghijklmnopqrstuV", 3))


# もとの問題：
# https://sonogym.sizebook.jp/program/34/create/
# 文字列の中で~が出るたびに小文字と大文字を切り替えて文字列をコピーする関数作ってみな。
# ただし
# 　大文字モードのときに大文字が来ても変化なし。
# 　小文字モードのときに小文字が来ても変化なし。

# s = "saikin ~usuge~ ga kininaru kanojo ha ~SVENSON~ wo hajime ~masita."
# 出力：
# saikin USUGE ga kininaru kanojo ha SVENSON wo hajime MASITA.

"""
https://sonogym.sizebook.jp/program/26/create/

- for loop 1つとformat関数を使って下記の様に1から15までを出力させる。
- ただし、bin()関数は使用禁止
'''
0001
0010
0011
0100
0101
0110
0111
1000
1001
1010
1011
1100
1101
1110
1111
:
'''
"""

# def func(x):
#     s = ''
#     for i in range(1, x+1):
#         print('{0:04b}'.format(i))
# func(15)






# 一つのリストxが与えられた時、偶数の場合加算して、奇数の場合減算する、関数を作成せよ
# 例：[1, 3, 5, 0, 9, 7, 6] == -19

# def func(x):
#     m = ''
#     for i in x:
#         if x % 2 == 0:
#             m += str(x)
#         else:
#             m -= str(x)
#         return m
# print(func([1, 3, 5, 0, 9, 7, 6]))
		



# Q1.
# 0~99までの乱数を100個生成し
# 以下のように分類せよ
# 1~9は0代とする

# 0代:10   0~9
# 10代:5   10~19
# 20代:14  20~29 
# 30代:17  30~39
# 40代:13  40~49
# 50代:14  50~59
# 60代:19  60~69
# 70代:14  70~79
# 80代:13  80~89
# 90代:26  90~99

# import random

# r = []
# for p in range(10):
#     r.append(random.randint(0, 99))
# print(r)

# m = ''
# for s in r:
#     if s in range(0, 10):
#     	m += str(s)
#     	print(m)
    	# print('0代:{}'.format(s))



# 百人一首のかるたでは、特に「決まり文字」を知っているかが勝負を分けるポイントになります。
# 決まり文字とは、「ここまで読まれれば、札がわかる（何の句か判断できる）」という部分のことです。
# 決まり字を覚えることで、上の句の最初の数文字で札を取ることが出きます。

# 今回は、上の句で決まり字を求めるだけでなく、下の句についても札に記載する文字数を最小限にすることを考えてください。
# 例えば、

# 村雨の　露もまだひぬ　まきの葉に　霧たちのぼる　秋の夕ぐれ

# という句では、上の句は最初の「む」一文字で判別できます。また、下の句も最初の「き」一文字で判別できます。
# つまり、この句では、読み札は一文字、取り札も一文字の合計二文字で表現できることになります。

# すべての句（100句）を一意に識別するのに必要な最小の文字数を求めてください。

# 百人一首のデータは下記の csv ファイルを使用することにします。
# https://www.shoeisha.co.jp/book/download/1761/read
# （圧縮フォルダ内の q33.csv を開き、「上の句かな」と「下の句かな」の列を使ってください）









# 一つの日時リストを引数にとり、年の昇順、月の降順、日の昇順のリストを返却する関数を作成せよ
# 例)
# x = ['2017/01/02', '2001/01/01', '2017/01/01', '2018/01/01', '2017/02/01'] 
# => ['2001/01/01', '2017/02/01', '2017/01/01', '2017/01/02', '2018/01/01']


# ２つの引数を持ち、その和を返す関数「add_value」を作成し、以下のプログラムが走るようにしなさい




 # 1, 3, 5が順に出力される
# x = ['2017/01/02', '2001/01/01', '2017/01/01', '2018/01/01', '2017/02/01']


# from datetime import datetime

# x.sort(key=lambda date: datetime.strptime(date, "%Y/%m/%d"))
# print(x)

# a = []
# for m in x:
#     a.append(m[0:4])
# b = list(set(a))
# print(list(set(a) - set(b)))





# ソートの交換回数の最小化
# n = 3
# 枚数：2n枚
# 3, 1, 2, 1, 3, 2
# 2, 3, 1, 2, 1, 3
# 2通り


# def func(n):
#     m = list(range(1, n+1)) * 2
#     print(m)

# func(3)

# ・ある数字xが与えられた場合、0からxまでの整数をフィボナッチ数列の長さでsliceしたlistを返す関数slice_fib(x)を作成する。
# （例：x＝１０） [ [0], [1], [2, 3], [4, 5, 6], [7, 8, 9] ]
# （例：x＝１００） [[0], [1], [2, 3], [4, 5, 6], [7, 8, 9, 10, 11], 
# [12, 13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32], 
# [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], 
# [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], 
# [88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]]






# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89・・・

# m = ''
# for i in range(0, 10):
#     m += str(i)
# print(m[1])

# xlist = []
# for i in range(0, 10):
#     xlist.append(i)
# print(xlist)

# p = []
# for m in xlist:
#     p.extend(m)
# print(p)








# 整数xが与えられた時に、エクセルの行の名前を返す関数をかけ

# 例: x=1 -> A, x=2 -> B, x=27 -> AA, x=54 -> BA


# def func(x):
#     alist = [chr(i) for i in range(65, 65+26)]
#     q = x // len(alist)
#     r = x % len(alist)
#     print(q, r)
#     if x <= 26:
#         return alist[x-1]
#     else:
#         return alist[q-1] + alist[r-1]

# print(func(1))
# print(func(2))
# print(func(27))
# print(func(54))



# def func(x):
#     for i in range(x):
#         xlist = []
#         for p in reversed(range(x)):
#             print(p, i)
#             if p > i:
#                 xlist.append(' ')
#             else:
#                 xlist.append('X')
#         ylist = []
#         for y in range(x-1):
#             # print(y, i)
#             if y >= i:
#                 ylist.append(' ')
#             else:
#                 ylist.append('X')
#         print(xlist)

# func(5)



# ２つのvalueがリストである辞書の引数を取り、
# ２つの辞書のkeyが同じものはvalueをつなげた、辞書を合体させる関数を作成せよ
# 例) x={'a': [3], 'b': [9]}, 
# y={'a': [5, 4], 'b': []} => {'a': [3, 5, 4], 'b': [9]}

# dic = {'a': [3], 'b': [9]}
# # dic1 = {'a': [5, 4], 'b': []}

# dic  = {'a':'3', 'b':'9'}
# dic1 = {'a':'5, 4', 'b':''}
# dic_rev = {}
# print(set(dic))
# for k in set(dic) | set(dic1):
#     print(dic)
#     vl = []
#     if k in dic:
#         vl.append(dic[k])
#     if k in dic1 and dic1[k] not in vl:
#         vl.append(dic1[k])
#     dic_rev[k] = ', '.join(vl)

# print(dic_rev)

# print(dict(d1.items() + d2.items()))

# ・年利5%で増えると100万円は毎年いくらになるかを出力
# ・2倍になるのはいつかを出力

# def n5(i):
#     return i * 1.05

# # 年利5%で増えると100万円は毎年いくらになるかを出力
# def ikura(x):
#     for i in range(1, 21):
#         print('{}年目：{:,.0f}円'.format(i, n5(x)))
#         x = n5(x)

# # 2倍になるのはいつかを出力
# def nibai(x):
#     ni = x*2
#     for i in range(1, 1000):
#         x = n5(x)
#         if x >= ni:
#             print('{}年目に{:,.0f}円'.format(i, x))
#             break

# ikura(1000000)
# nibai(1000000)



# answer1
# 1年後 1,050,000円
# 2年後 1,102,500円
# 3年後 1,157,625円
# 4年後 1,215,506円
# 5年後 1,276,281円
# 6年後 1,340,095円
# 7年後 1,407,099円
# 8年後 1,477,453円
# 9年後 1,551,325円
# answer2
# 15年後に2,078,921円


# def mue(n, p):
#     return int(n * (p/100)) + n

# print("answer1")
# mymoney = 1000000
# for i in range(1,10):
#     mymoney = mue(mymoney, 5)
#     print("{}年後 {:,}円".format(i, mymoney))

# print("answer2")
# y = 0
# mymoney1 = 1000000
# mymoney2 = 1000000
# while True:
#     y += 1
#     mymoney2 = mue(mymoney2, 5)
#     if mymoney2 > mymoney1 *2:
#         break
# print("{}年後に{:,}円".format(y, mymoney2))









# 野球の試合を見ようとたくさんの人が並んでいます。みんなホームチームのファンで、チームの帽子をかぶっていますが、帽子のかぶり方がバラバラです。
# 普通にひさし（つば/バイザー）を前にかぶっている人と、反対にひさし（つば/バイザー）を後ろにかぶっている人とがいます。
# あなたが入り口の入場係で、並んでいるファンの帽子がみんな揃っている場合に、つまり、みんなが普通かぶりか逆かぶりかのどちらかの場合にだけ入場させるのだとします。
# 向きの定義（帽子のどっちが前か後ろか）はバラバラの可能性があるので、かぶり方を命令するわけには行きません。
# 向きを変えろとだけ命令できます。ありがたいことに、列に並んでいる人は、自分が列の何番目にいるのかはわかっています。
# 一番前の人の位置は０、最後の人の位置はｎ-1です。次の２つのように命令できます。
# ＜命令＞
# ①i番目の人は、帽子の向きを変えてください
# ②i番目からj番目の人は帽子の向きを変えてください

# この２つの命令を使い、命令回数の最小値を答えるプログラムを記述してください。
# ※なお、帽子を前向きにかぶっている人を'F'、後ろ向きにかぶっている人を'B'と表記する。

# 例：cap1 = ['F','F','B','B','B','F','B','B','B','F','F','B','F']
# 　＜命令＞
# ≪パターン１≫
# １回目：0番目から1番目の人は、帽子の向きを変えてください。
# ２回目：5番目の人は、帽子の向きを変えてください。
# ３回目：9番目から10 番目の人は、帽子の向きを変えてください。
# ４回目：12番めの人は帽子の向きを変えてください。
# →合計４回

# ≪パターン２≫
# １回目：2番目から4番目の人は、帽子の向きを変えてください。
# ２回目：6番目から8番目の人は帽子の向きを変えてください。
# ３回目：11番目の人は、帽子の向きを変えてください。
# →合計３回

# ≪パターン１≫より≪パターン２≫のほうが命令回数が「４回＞３回」と少ない。
# よって答え、３回


# caps1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
# caps2 = ['F', 'B', 'F', 'B', 'B', 'B', 'F', 'B', 'F', 'B', 'B', 'F', 'F']
# case3 = []
# case4 = ['F']


# def please_conform_one_pass(caps):
#     if 0 <= len(caps) <= 1:
#         return
#     caps = caps + [caps[0]]
#     start_i = 0
#     for i in range(1, len(caps)):
#         if caps[i] != caps[i - 1]:
#             if caps[i] != caps[0]:
#                 start_i = i
#             elif start_i == i - 1:
#                 print(f'Person at position {i - 1} flip your cap!')
#             else:
#                 print(f'People in positions {start_i}'
#                       f' through {i - 1} flip your caps!')


# for caps in [caps1, caps2, case3, case4]:
#     print(caps)
    # please_conform_one_pass(caps)
    # print()


# def multiple_of_3(x):
#     i = 0
#     multiple_three_list = []
#     while i < x:
#         if i % 3 == 0:
#             # print(i)
#             multiple_three_list.append(i)
#         i += 1
#     return multiple_three_list

# print(multiple_of_3(25))

# def mul(x):
#     xlist = []
#     for i in range(0, x+1):
#         if i % 3 == 0:
#             xlist.append(i)
#     return xlist

# print(mul(25))

# 高橋君は無限に広い掛け算表の上にいます。
# 掛け算表のマス (i,j)には整数i×jが書かれており、高橋君は最初 (1,1)にいます。
# 高橋君は 1回の移動で (i,j)から (i+1,j)か (i,j+1)のどちらかにのみ移ることができます。
# 整数 Nが与えられるので、Nが書かれているマスに到達するまでに必要な移動回数の最小値を求めてください。
# ≪制約≫
# 2≤N≤10^12
# 計算時間が2s以下であること（N^12のforループを２回繰り返し使うとタイムオーバーする）

# 例) N = 19237596204
# 移動回数の最小値： 398769


# 「1234」を1つの数字だけで、できるだけ少ない個数で表現するとき、
# 最も少ない個数で表現できる数字を求め、その式をすべて答えてください。

# N = 19237596204
# 入力して計算させる用
# N = int(input())
# s = N-1
# a = N
# b = 1
# for i in range(int(N**0.5)+1, 1, -1):
#         if N%i == 0:
#             a = i
#             b = N//i
#             s = a + b -2
#             break

# print(s)



# n=int(input())
# i=1
# ans=10**13
# while(i*i<=n):
#     if(n%i==0):
#         ans=min(ans,n/i+i-2)
#     i+=1
# print(int(ans))


# 時間、cpu使用率、memory使用率が順に並んだ以下のような文字列がある。
# この文字列をパースして、分単位の平均cpu使用率、memory使用率を辞書形式で返す関数を作成せよ
# from decimal import Decimal

# s = """2018-03-02 02:25:52+00:00,0.101,649494528.0
# 2018-03-02 02:25:42+00:00,0.101,649494528.0
# 2018-03-02 02:25:32+00:00,0.504,649441280.0
# 2018-03-02 02:25:22+00:00,0.101,649498624.0
# 2018-03-02 02:25:12+00:00,1.31,649498624.0
# 2018-03-02 02:25:02+00:00,6.539,649109504.0
# 2018-03-02 02:24:52+00:00,1.308,647024640.0
# 2018-03-02 02:24:42+00:00,0.202,647028736.0
# 2018-03-02 02:24:32+00:00,0.403,647032832.0
# 2018-03-02 02:24:22+00:00,0.201,647036928.0"""

# jikan, cpu, mem = [], [], []
# for p in s.splitlines():
#     jikan += [p.split(',')[0]]
#     cpu += [p.split(',')[1]]
#     mem += [p.split(',')[2]]

# m, n = [], []
# for i, j in enumerate(jikan):
#     if j[0:16] not in m:
#         n.append(i)
#         m.append(j[0:16])

# mae = cpu[:n[-1]]
# ato = cpu[n[-1]:]
# cpu_1 = sum([Decimal(i) for i in mae])/len(mae)
# cpu_2 = sum([Decimal(i) for i in ato])/len(ato)
# cpu1 = round(cpu_1, 3)
# cpu2 = round(cpu_2, 3)
# cc = [cpu1, cpu2]

# ma = mem[:n[-1]]
# at = mem[n[-1]:]
# mem_1 = sum([Decimal(i) for i in ma])/len(ma)
# mem_2 = sum([Decimal(i) for i in at])/len(at)
# mem1 = round(mem_1, 1)
# mem2 = round(mem_2, 1)
# mm = [mem1, mem2]

# print('cpu　平均使用率', dict(zip(m, cc)))
# print('memory平均使用率', dict(zip(m, mm)))

# s = 0
# for i, c in enumerate(cpu):
#     print(i, c)
#     s += Decimal(c)
# print(s)


# kotae {"2018-03-02 02:24":"cpu平均, memory平均", "2018-03-02 02:25":"cpu平均, memory平均"}

# 時間が同じだったら、
# shiki = ['*', '/', '+', '-', '']


# import itertools

# for i in itertools.permutations(shiki, 5):
# 	print(i)


# 1,2,3,...,nというラベルが付いたn枚のカードがあります。
# 1枚目のカードのラベルがkのとき、最初のk枚のカードを逆順にする、
# という操作を繰り返すことを考えます。
# 例えば、n＝6で「362154」という並びから始めたとき、
# カードは次のように変化します。
# n＝9のとき、カードが変化しなくなるまでの回数が最も多くなるような9枚の並びを求めてください。

# 623154
# 451326
# reversed

# import itertools

# card = [i for i in range(1, 10)]
# cnt = 0
# # print(card)

# # def s(xlist):
#     # l = i[0]
#     # return l, i[:l][::-1]+i[l:]

# for i in itertools.permutations(card, 9):
#     while True:
#         if i[0] != 1:
#             l = i[0]
#             print(l, i[:l][::-1]+i[l:])
#             a = i[:l][::-1]+i[l:][:]
#             print(a)
#         elif i[0] == 1:
#             break

        # xlist.append(m)
# print(xlist)



#         # print(cnt)
# MAX_CNT = 0
# MAX_CARD = [i for i in range(1, 10)]

# for i in itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 9):
#     card = list(i)
#     pre_card = card[:]
#     cnt = 0

#     while True:
#         if card[0] == 1:
#             break
#         card[:card[0]] = card[card[0]-1::-1]
#         print(card[:card[0]], card[card[0]-1::-1])
#         cnt += 1

#     if cnt > MAX_CNT:
#         MAX_CNT = cnt
#         MAX_CARD = pre_card[:]

# print(MAX_CNT, MAX_CARD)

# def henkan(x):
#     # 4, 6, 7, 9はNG, 1, 3, 8, 0はOK
#     if '4' in x or '6' in x or '7' in x or '9' in x:
#         return 'NG'
#     # 5と2
#     m = x.replace('5', 'X').replace('2', '5').replace('X', '2')
#     if m[:2] > '23':
#         return 'NG'
#     if m[-2:] > '59':
#         return 'NG'
#     return m

# xlist = []
# for h in range(0, 24):
#     for m in range(0, 60):
#         a = "{:02}{:02}".format(h, m)
#         if henkan(a) != 'NG':
#             l = "{0}:{1}".format(a[:2], a[-2:])
#             xlist.append(l)
# print(xlist)


# import itertools

# BOARD = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# MEMO = {}


# def strike(board):
#     """
#     ストラックアウト
#     """
#     if tuple(board) in MEMO:
#         return MEMO[tuple(board)]

#     if not board:
#         return 1

#     ptn = []
#     for i in board:  # 1枚抜き
#         ptn += [(i, 0)]

#     for i in itertools.combinations(board, 2):  # 2枚抜き
#         if i[0] == 5 or i[1] == 5:
#             continue

#         elif i[0] % 3 != 0 and i[0] + 1 == i[1] or i[0] + 3 == i[1]:
#             ptn += [(i[0], i[1])]

#     cnt = 0
#     for i in ptn:  # ボールを投げる
#         next_board = board[:]

#         if i[0] in next_board:
#             next_board.remove(i[0])

#         if i[1] in next_board:
#             next_board.remove(i[1])

#         cnt += strike(next_board)

#     MEMO[tuple(board)] = cnt

#     return cnt


# if __name__ == "__main__":
#     print(strike(BOARD))

# 異なる 2 つの自然数 n, m があるとき、
# 自分自身を除いた約数の和が、もう一方の数と等しくなるような数を友愛数といいます。
# n = (m を除いた m の約数の和)
# m = (n を除いた n の約数の和)
# (例)
# (220, 284) 
# -> 220 の自分自身を除いた約数は
 # 1, 2, 4, 5, 10, 11, 22, 44, 55, 110 で和は 284、
# 284 の自分自身を除いた約数は 
# 1, 2, 4, 71, 142 で和は 220 なので、(220, 284) は友愛数である。

# 友愛数を小さい順に 5 組求めてください。

# def yakusu(p):
#     div = []
#     for i in range(1, p+1):
#         if p % i == 0:
#             div.append(i)
#     return sum(div[:-1])

# rslt = []
# max_val = 15000
# s = 0
# for m in range(1, max_val+1):
#     n = yakusu(m)
#     if n >= m:
#         continue
#     if yakusu(n) == m:
#         rslt.append((n, m))     
#         s += 1
#         if s == 5:
#             break
# print(rslt)


# 自然数 N 以下の素数 p, q, r を考えます。

# p + q = r^2

# を満たす (p, q, r) の組をすべて求めてください。
# ただし、p, q, r は同じ数字が入っても良いとして、p <= q とします。

# (例) 
# N = 5 -> (p, q, r) = (2, 2, 2)

# import itertools

# def func(x):
#     sosu_l = []
#     for i in range(1, x+1):
#         if x % i != 0:
#             sosu_l.append(i)
#     print(sosu_l)
#     for i in itertools.product(sosu_l, repeat=3):
#         if (i[0] + i[1] == i[2] * i[2]):
#             return (i[0], i[1], i[2])

# print(func(5))

# def func(x):
#     sosu_l = []
#     for i in range(1, x+1):
#         if x % i == 0:
#             print(i)
#             # sosu_l.append(i)
#         else:
#             sosu_l.append(i)
#     print(sosu_l)

# print(func(5))

# def func(x):
#     primes = [2, 3]
#     for n in range(5, x+1, 2):
#         isprime = True
#         for i in range(1, len(primes)):
#             if n % primes[i] == 0:
#                 isprime = False
#                 break
#         if isprime:
#             primes.append(n)
#     print primes

# func(x)

# def isPrime(n):
#     xlist = []
#     if n == 2:
#         xlist.append(2)
#         return True
#     for p in range(2, n):
#        if n % p == 0:
#         # nまでの数で割り切れたら素数ではない
#            return False
#   # nまでの数で割り切れなかったら素数
#     # xlist.append(n)
#     print(n)
#     return True
#     print(n)
# # print(xlist)


# print(isPrime(1))
# print(isPrime(2))
# print(isPrime(3))
# print(isPrime(4))
# print(isPrime(5))


# def primes(n):
#     is_prime = [True] * (n + 1)
#     is_prime[0] = False
#     is_prime[1] = False
#     for i in range(2, n + 1):
#         for j in range(i * 2, n + 1, i):
#             is_prime[j] = False
#     return [i for i in range(n + 1) if is_prime[i]]
# print(primes(5))
# 一つのリストxが与えられた時、0の要素ごとにくぎって総和を返す関数を作成せよ
# 例1:[1, 0, 2, 3, 0, 4, 8] => [1, 5, 12] # (1, 2 + 3, 4 + 8)
# 例2:[0, 9, 10, 0, 3, 0, 4, 8] => [0, 19, 3, 12]

# def func(x):
#     xlist = []
#     ylist = []
#     for i in x:
#         if i == 0:
#             xlist.append(sum(ylist))
#             ylist = []
#         else:
#             ylist.append(i)
#     if i != 0:
#         xlist.append(sum(ylist))
#     print(ylist)
    # return xlist

# 一つのリストxが与えられた時、0の要素ごとにくぎって総和を返す関数を作成せよ
# 例1:[1, 0, 2, 3, 0, 4, 8] => [1, 5, 12] # (1, 2 + 3, 4 + 8)
# 例2:[0, 9, 10, 0, 3, 0, 4, 8] => [0, 19, 3, 12]

# alist = [1, 0, 2, 3, 0, 4, 8]

# print([i for i, x in enumerate(alist) if x == 0])

# total = 0
# for i in alist:# i は 1 から 10未満（つまり9）を動く
#     total += i
#     print(i, total)

# print(total)
# def func(x):
#     xlist = []
#     # while x:
#     print(sum(x[0:x.index(0)]))
#         # i, x = (sum(x[0:x.index(0)]), x[x.index(0)+1:]) if 0 in x else (sum(x), None)
#         # xlist.append(i)
#     # return xlist

# print(func([1, 0, 2, 3, 0, 4, 8]))

# print(func([0, 9, 10, 0, 3, 0, 4, 8]))

# def func(x):
#     xlist = []
#     while x:
#         i, x = (sum(x[0:x.index(0)]), x[x.index(0)+1:]) if 0 in x else (sum(x), None)
#         xlist.append(i)
#     return xlist


# [1, 0, 2, 3, 0, 4, 8]

# xlist = [[1], [2, 3], [4, 8]]

# plist = []
# for i in xlist:
#     plist.append(sum(i))
# print(plist)    


# def func(x):
#     xlist = []
#     ylist = []
#     for i in x:
#         if i == 0:
#             xlist.append(sum(ylist)-i)
#             # ylist = []
#         else:
#             ylist.append(i)
#     if i != 0:
#         xlist.append(sum(ylist))
#     return xlist

# print(func([1, 0, 2, 3, 0, 4, 8]))
# 例1:[1, 0, 2, 3, 0, 4, 8] => [1], [2, 3], [4, 8]
#        0  1  2  3  4  5  6  
# alist = [1, 0, 2, 3, 0, 4, 8]

# xlist = []
# for i, p in enumerate(alist):
#     # print(i, p)
#     if p == 0:
#         xlist.append(i)
# print(xlist[0], xlist[1])

# 一つのリストxが与えられた時、0の要素ごとにくぎって総和を返す関数を作成せよ
# 例1:[1, 0, 2, 3, 0, 4, 8] => [1, 5, 12] # (1, 2 + 3, 4 + 8)
# 例2:[0, 9, 10, 0, 3, 0, 4, 8] => [0, 19, 3, 12]
# def func(x):
#     xlist = []
#     cnt = 0
#     for i in x:
#         if len(xlist) != cnt + 1:
#             xlist.append(0)
#         print(xlist)    
#         xlist[cnt] += i
#         if i == 0:
#             cnt = cnt + 1
#     return xlist

# print(func([1, 0, 2, 3, 0, 4, 8]))
# print(func([0, 9, 10, 0, 3, 0, 4, 8]))

# def func(x):
#     shiki = ','.join(map(str,x))
#     print(shiki)
#     l = shiki.split(0)
#     print(l)
#     # for i in x:
#         # print(i)    
# #     xlist = []
# #     cnt = 0
# #     for i in x:
# #         if len(xlist) != cnt + 1:
# #             xlist.append(0)
# #         print(cnt)
# #         print(xlist[cnt])
# #         if i == 0:
# #             cnt += 1
# #     print(cnt)



# print(alist[0:1], alist[2:4], alist[5:7])

# print([i for i, x in enumerate(alist) if x != 0])

# print(alist[1:4])


# 正の整数のリストの要素と＋、✕をもちいて計算できる最大値を出力して下さい。
# (例)
# [1, 2, 3, 4] -> (1 + 2) * 3 * 4 = 36
# [2, 3, 4] -> 2 * 3 * 4 = 24





# a = [i for i, x in enumerate(alist) if x != 0]

# b = [i for i, x in enumerate(alist) if x == 0]

# print([i for i in range(0, len(alist))])
# c = [i for i in range(0, len(alist))]

# print(set(c))
# print(list([set(c) - set(b)]))

    # return alist[]

# def func(x):
#     xlist = []
#     ylist = []
#     t = 0
#     while t < len(x):
#         t += 1
#         for s, i  in enumerate(x):
#         # print(s, i)
#             if i != 0:
#                 xlist.extend([i])
#                 # ylist = []
#             else:
#                 continue
#     print(xlist)
#     # print(ylist + xlist)

# print(func([1, 0, 2, 3, 0, 4, 8]))

# data = [1, 3, 5]
# new_data = [2, 4, 6]
# data.append(new_data)
# print(data)
# 例1:[1, 0, 2, 3, 0, 4, 8] => [1, 5, 12] # (1, 2 + 3, 4 + 8)
# print(func([1, 0, 2, 3, 0, 4, 8]))
# print(func([0, 9, 10, 0, 3, 0, 4, 8]))
# print(func([0, 9, 10, 0, 3, 0, 4, 8, 0, 3]))

# def fun(l):
#     s = []
#     p = []
#     for i in l:
#         if i == 0:
#             p.append(sum(s))
#             # s = []
#         else:
#             s.append(i)
#     if i != 0:
#         p.append(sum(s))

#     return p

# print(fun([1,2,3,0,4,5,0,6,1,0]))


# def func(x):
#     xlist = []
#     cnt = 0
#     for num in x:
#         if len(xlist) != cnt + 1:
#             xlist.append(0)
#         xlist[cnt] += num
#         if num == 0:
#             cnt += 1
#     return xlist
# print(func([1, 0, 2, 3, 0, 4, 8]))


# def flatten(l):
#     rslt = []
#     for p in l:
#         if isinstance(p, list):
#             # print('p', p)
#             rslt.extend(flatten(p))
#             # print('rslt', rslt)
#         else:
#             # rslt.append(p)
#             print('rsltt', rslt)
#             print(p)
#     return rslt

# l = ['ラッパ', [['ゴリラ', 'ルビー']], ['パイナップル', [['りんご']]]]

# print(flatten(l))

    # print(ylist.sort(reverse=True))
    # print(zlist.sort())
    # print(sort(xlist), sorted(ylist), sort(zlist))
        # print(i.year, i.month, i.day)


# from datetime import datetime

# def func(x):
#     l = [ datetime.strptime(d, '%Y/%m/%d') for d in x ]
#     return sorted(l, key=lambda d: (d.year, -d.month, d.day))

# x = ['2017/01/02', '2001/01/01', '2017/01/01', '2018/01/01', '2017/02/01']
# func(x)


# (例)
# 1 ->
# [[1, 2, 15, 16],
# [13, 14, 3, 4],
# [12, 7, 10, 5],
# [8, 11, 6, 9]]

# pythonの予め登録されている関数rangeと同じ挙動を行う関数"my_range"を実装せよ。
# 以下を満たすこと
# - 関数内でrangeの利用は禁止
# - [x for x in my_range(3)] => [0, 1, 2]
# - [x for x in my_range(1, 4)] = > [1, 2, 3]
# - [x for x in my_range(8, 3, -2)] => [8, 6, 4]
# - for x in my_range(1<<60): print(x); break; が動くこと

# print(range(3))
# for i in range(3):
#     print(i)

# 正の整数のリストの要素と＋、✕をもちいて計算できる最大値を出力して下さい。
# (例)
# [1, 2, 3, 4] -> (1 + 2) * 3 * 4 = 36
# [2, 3, 4] -> 2 * 3 * 4 = 24

# def func(x):
#     shiki = ['+', '*']
#     kakko = ['(', ')']
#     n = len(x)
#     # print(x, x[n-4], x[n-3], x[n-2], x[n-1])
#     for i in x:
#         print(i)

# func([1, 2, 3, 4])
# func([2, 3, 4])



# def func(lst):
#     ppp = itertools.permutations(lst)
#     xlist = []
#     for c in ppp:
#         print(c)
#         value = "".join([str(n) for n in c])
#         p = abs(int(value[0:3]) - int(value[3:6]))
#         xlist.append(p)
#     return min(xlist)
# print(func([1, 2, 3, 4, 5, 6]))
# # print(func([1, 2, 3, 4, 5, 1]))
# COUNTRIES = [
# 'Brazil', 'Croatia', 'Mexico',
# 'Cameroon', 'Spain', 'Netherlands',
# 'Chile', 'Australia', 'Colombia',
# 'Greece', 'Cort d\'Ivoire', 'Japan',
# 'Uruguay', 'Costa Rica', 'England',
# 'Italy', 'Switzerland', 'Equador',
# 'France', 'Honduras', 'Argentina',
# 'Bosnia and Harzegovina', 'Iran', 'Nigeria',
# 'Germany', 'Portugal', 'Ghana',
# 'USA', 'Belgium', 'Algeria',
# 'Russia', 'Korea Republic'
# ]

# MAX_CNT = 0
# MAX_SHIRITORI = []

# def shiritori(depth, key, chain):
#     global MAX_CNT
#     global MAX_SHIRITORI
#     total_cnt = 0
#     # キーワードで始まる国を探す
#     next_countries = []
#     for i in COUNTRIES:
#         if i[0].upper() == key[0].upper():
#             next_countries += [i]

#     for i in next_countries:
#         if i not in chain:
#             chain.append(i)

#             total_cnt = shiritori(depth + 1, i[-1].upper(), chain)
#             print(total_cnt)
#             if total_cnt > MAX_CNT:
#                 MAX_CNT = total_cnt
#                 MAX_SHIRITORI = chain[:]
#             chain.pop()

#     return depth

# for country in COUNTRIES:
#     shiritori(0, country, [])

# print(MAX_CNT, " : ", MAX_SHIRITORI)



# 1~4のうちの整数が一つ与えられた時、その整数が左上になるような数独を完成させてください。
# ただし、数独は 1 ~ 4 の数字を用いて、4 x 4 のサイズとします。
# (各行、列では、1~4の数字が一回ずつ使用され、
# 全体を4分割した 2 x 2 のブロック内でも1~4の数字が一回ずつ使用されているものとします)

# (例)
# 1 ->
# [[1, 2, 3, 4],
# [3, 4, 1, 2],
# [2, 3, 4, 1],
# [4, 1, 2, 3]]

# def func(x):
#     xlist = []
#     for i in range(1, x+1):
#         xlist.append(i)
#     print(xlist)

# print(func(4))


# 正の整数のリストが与えられた時に、+、×、＝ を間に入れて等式が作れる場合はtrue、
# そうでない場合はfalseを返す関数を作成してください。
# ただし、＝が使えるのは一箇所のみとします。

# 整数 x, y, z は次の式を満たしているとします。
# 6x + 4y + z = 50
# 2x + 3y + z = 30

# この時、 4x + 3y の最大値を求めてください。

# (例)
# [1, 4, 5, 6, 7, 8] -> 1 + 4 * 5 = 6 + 7 + 8 -> true
# [1, 4, 2, 1] -> false

# shiki = ['+', '×', '=']
# import itertools

# def func(lst):
#     xlist = []
#     for c in itertools.permutations(lst):
#         value = "".join([str(n) for n in c])
#         p = abs(int(value[0:3]) - int(value[3:6]))
#         xlist.append(p)
#     return min(xlist)

# print(func([1, 2, 3, 4, 5, 6]))
# print(func([1, 2, 3, 4, 5, 1]))



# def func(x):
#     mo = ""
#     for i in x:
#         mo += i
#     print(mo)
#     # kaburi = set(list(mo))
#     # print(list(kaburi))

# def funca(l):
#     st = ''.join([''.join(set(v)) for v in l])
#     print(st)
#     return [s for s in set(st) if st.count(s) == len(l)]

# print(funca(['apple', 'appple', 'apppple']))
# print(funca(['post', 'stop', 'tops', 'pot']))

# def func(x):
#     xlist = []
#     for i in x:
#         xlist.append(''.join(i))
#     p = ''.join(xlist)
#     ylist = []
#     for i in set(p):
#         if p.count(i) == len(x):
#             ylist.append(i)
#     return ylist

# print(func(['apple', 'appple', 'apppple']))
# print(func(['stop', 'tops', 'pot']))



# def funca(l):
#     st = ''.join([''.join(set(v)) for v in l])
#     print(st)
#     # return [s for s in set(st) if st.count(s) == len(l)]

# print(funca(['apple', 'appple', 'apppple']))
# print(funca(['post', 'stop', 'tops', 'pot']))


# lists = [["a", "b", "c"], ["b", "d"], ["a", "b", "e"], ["f", "f", "a"]]
# list = [e for list in lists for e in list]            # 2重リストを1重リストに
# print(list)
# res = set([e for e in list if list.count(e) > 1])     # 重複要素の取り出し
# print(res)
# def func(x):
#     xlist = []
#     for i in x:
#         xlist.append((''.join([p for p in set(i)])))
#     print(xlist)
#     for p in xlist:
#         print(p)
#         print(len(p))

    # print(len(xlist))
    # xlist = []
    # for i in x:
        # xlist.append([p for p in set(i)])
    # print(xlist)
    # print(xlist.count())
    # print(len(xlist))
    # for i in xlist:
        # print(i)
#     print(xlist)
#     # p = xlist[0]
#     # for i in xlist:
#         # print(i)
#         # print(set(p) & set([p+1]))
#         # print(i)
#         # for i in aiueo_list:
#         #     print(i)
#             # print(i)


# lists = [["a", "b", "c"], ["b", "d"], ["a", "b", "e"], ["f", "f", "a"]]
# list = [e for list in lists for e in list]            # 2重リストを1重リストに
# print(list)
# res = set([e for e in list if list.count(e) > 1])     # 重複要素の取り出し
# print(res)

# def fncs(a):
#     b = []
#     for x in a:
#         b.append([x for x in set(x)])
#     bb = b[0]
#     print(range(len(b)-1))
#     for i in range(len(b)-1):
#         print(i)
#         bb = list(set(bb) & set(b[i+1]))
#     return bb

# print(fncs(['post', 'stop', 'tops', 'pot']))
# print(fncs(['apple', 'appple', 'apppple']))

# l1 = ['a', 'b', 'c']
# l2 = ['b', 'c', 'd']
# l3 = ['c', 'd', 'e']

# l1_l2_l3_and = set(l1) & set(l2) & set(l3)
# print(l1_l2_l3_and)


# def func(l):
#     st = ''.join([''.join(set(v)) for v in l])
#     print(st)
# #     return [s for s in set(st) if st.count(s) == len(l)]

# print(func(['apple', 'appple', 'apppple']))
# print(func(['post', 'stop', 'tops', 'pot']))

# 長さが6で要素が1~9の間の整数であるようなリストの数字を一回ずつ使って
# 3桁の整数を2つ作るとき、その2つの整数の差の絶対値が最小になるときの値を求めてください。
# ただし、リストの要素は同じ数字を含んでいても良いとします。

# (例)
# [1, 2, 3, 4, 5, 6] -> 412 - 365 = 47
# [1, 2, 3, 4, 5, 1] -> 142 - 135 = 7


# import itertools
# import re

# def func(l):
#     result = {'diff': 1000, 'comb': [0, 0]}
#     for v in list(itertools.permutations(l, 3)):
#         exc_l = []
#         s = ''.join([str(i) for i in l])
#         for i in v:
#             r = re.search(r'[%s]{1}' % str(i), s)
#             exc_l.append(r.span()[0])
#             s_l = list(s)
#             s_l[r.span()[0]] = 'd'
#             s = ''.join(s_l)

#         l2 = list({index: value for index, value in enumerate(l) if index not in exc_l}.values())

#         if len([i for i in l2 if i <= v[0]]) == 0:
#             continue

#         for v2 in list(itertools.permutations(l2, 3)):
#             r1 = int(''.join([str(i) for i in v]))
#             r2 = int(''.join([str(i) for i in v2]))
#             diff = r1 - r2

#             if diff < result['diff'] and diff >= 0:
#                 result.update(diff=diff, comb=[r1, r2])
#     return result

# print(func([1, 2, 3, 4, 5, 1]))
# print(func([1, 2, 3, 4, 5, 6]))


# cnt = 0

# for i in range(65536):
#     ip_bin = "{0:016b}".format(i) + "{0:016b}".format(i)[::-1]
#     ip_dec = str(int(ip_bin[0:8], 2))
#     ip_dec += str(int(ip_bin[8:16], 2))
#     ip_dec += str(int(ip_bin[16:24], 2))
#     ip_dec += str(int(ip_bin[24:32], 2))
#     print(ip_dec)

#     if len(set(ip_dec)) == 10:
#         # 10進数と2進数の左右対称になるもの一覧
#         print(ip_dec, ip_bin)
#         cnt += 1

# print(cnt)

# 絡まない糸電話
# 同一円周上に等間隔に並んだこどもたちが、ペアを組んで糸電話で会話しようとしています。
# このとき、交差してしまうと、糸が絡まってしまいますので、交差しないような相手とペアを組む必要がある。
# 例えば、こどもが6人いた場合、ペアを作ると、うまく会話ができる。
# つまり、6人では5通りのペアができる。
# 交差しないということを考えて、
# 任意の位置で区切り、分けられた領域の中で糸電話をすればよいと考えられる。
# それぞれのエリアでは人数が偶数である必要がある。
# 2人の場合は組み合わせが一通りであることは明らか
# 両側のメンバーの組み合わせを計算して、両側の数をかければOK

# 交差の判定を簡単にする場合に領域を分けて考える。

# 問
# 16人の子供たちがいた場合、作ることができるペアが何通りあるか求めてください。
# def func(x):
#     pair = [0] * (x//2 + 1)
#     pair[0] = 1
 
#     for i in range(1, x//2+1):
#         pair[i] = 0
#         for j in range(i):
#             pair[i] += pair[j] * pair[i-j-1]
#     return pair[x//2]

# print(func(6))
# print(func(16))

# import math 
 
# q = 0
# cnt1 = 0
# for p in range(2, 13):
#   a, b, c = 2*p*q, p**2-q**2, p**2+q**2
#   if c <= 125 and math.gcd(a, b):
#     cnt1 += 1
# p = 1
# cnt2 = 0
# for q in range(2, 13):
#   a, b, c = 2*p*q, p**2-q**2, p**2+q**2
#   if c <= 125 and math.gcd(a, b):
#     cnt2 += 1

# print(cnt1 + cnt2)

# 月食または日食は太陽と地球と月が一直線に並んだ時に起こります。
# この三者が一直線に並ぶのは、月が満月or新月の時かつ、月の公転軌道と太陽と地球の位置関係がある条件を満たす時です。
# 月の満ち欠けの周期を29.5日とし、月の公転軌道に関する条件が183日周期で満たされるとします。
# 2018年1月1日0時0分に太陽と地球と月が一直線に並んだとすると、次にこの三者が一直線に並ぶのはいつか計算してください。

# 以下の文字列を変換して、htmlフォーマットを生成する関数「convert2html」を作成せよ。
# 引数は文字列１個とする。
# txt = '''# hello
# This is a example sentence.
# next sentence
# # title2
# mark down
# '''
# # output: '''<h1>hello</h1>
# # <p>This is a example sentence.
# # next sentence</p>
# # <h1>title2</h1>
# # <p>mark down</p>
# # '''

# print(txt)


# id,userでユーザーを定義した文字列（idはユーザーID,userはユーザー名とする）と、
# ユーザーアクティビティを定義した文字列(idはアクティビティID、dateは日付、user-idはユーザーID、actionはアクティビティ名)が与えられた時に、
# 月ごとのアクティビティの種類をkeyと数をvalueとして集計し返す関数"get_activity_per_month"と
# 月ごとのユーザーのアクティビティ数、ユーザー名をkey、数をvalueとして集計しかえす関数"get_user_activity"の２つの関数を作成せよ。


# 月ごとのアクティビティの種類をkeyと数をvalueとして集計し返す関数"get_activity_per_month"と
# {"commit":10, "pull":2, "push":3}
# 月ごとのユーザーのアクティビティ数、ユーザー名をkey、数をvalueとして集計しかえす関数"get_user_activity"
# {"hoge":10, "foo":2, "bar":5}

# # ------ ユーザー --------------
# users = """id,user
# 1,hoge
# 2,foo
# 3,bar"""

# # ------ ユーザーアクティビティ --------------
# activities = """id,date,user-id,action
# 1,2017-12-26,1,commit
# 2,2018-01-06,3,pull
# 3,2018-01-11,1,push
# 4,2018-02-06,2,commit
# 5,2018-02-10,2,pull
# 6,2018-02-20,3,push"""

# from collections import Counter

# def get_activity_per_month(x):
#     m = x.replace('\n',',')
#     active_list = m.split(",")
#     xlist = []
#     for i, p in enumerate(active_list):
#         if (i+1) % 4 == 0 and (i+1 > 4):
#             xlist.append(p)
#     return Counter(xlist)

# print(get_activity_per_month(activities))

# def get_user_activity(x):
#     m = x.replace('\n',',')
#     active_list = m.split(",")
#     u = users.replace('\n',',')
#     u_list = u.split(",")
#     u_dict = dict(zip(u_list[0::2], u_list[1::2]))
#     xlist = []
#     for i, p in enumerate(active_list):
#         if (i+2) % 4 == 0 and (i+2 > 4):
#             for k in u_dict.keys():
#                 if p == k:
#                     xlist.append(u_dict[k])
#     return Counter(xlist)

# print(get_user_activity(activities))






        # print(type(i))
#     l = x.splitlines()
#     print(l)

#     count = {}
#     for i in active_list:
#         count.setdefault(i, 0)
#         count[i] +=1
#     for key, value in count.items():
#             print('{}: {}'.format(key, value))

    # d = {}
    # for i in m:
    #     # print(i[10])
    #     d[i] = i
    # print(d)
        # print(dict(i))

 # dic = {}
 #    for elem in x:
 #        en, jp, num, d = elem
 #        dic[en] = num

    # print([i.split() for i in x])
   # m = x.replace('\n','')
   # m = [i.strip() for i in x]
   # print(m)





 # dic = {}
 #    for elem in x:
 #        en, jp, num, d = elem
 #        dic[en] = num

# def get_activity_per_month(x):



# get_activity_per_month(activities)




# print(get_activity_per_month(x))

# def func(x):
#     with open(x) as f:
#         l = f.readlines()
#         l_rep = [s.strip() for s in l]
#         print(l_rep)
#         return l_rep

# def file_list(a, b):
#     a_list = func(a)
#     b_list = func(b)
#     return list(set(a_list) - set(b_list))

# print(file_list('1.txt', '2.txt'))


# URLが与えられたとき、URLが存在するかチェックする関数を作成してください

# 例) 
# x="http://aaa"
# Not found
# x="https://sonogym.sizebook.jp/"
# OK


# 以下のように１行ごとに１個のファイル名が書かれているファイル２つある。
# ファイル１に存在して、ファイル２に存在しないファイル名を
# pythonのリストにして返却する関数を作成せよ。

# 1.txt
# 00e7a4f3b01c479584a9cf821108680e.xlsx
# 00f06a5d6a0645b99350118ce44c9f02.xlsx
# 00fcfbbbf48944fcad96c754b92cc442.xlsx
# 010101.xlsx
# 010101_Baq9phb.xlsx
# 010101_Baq9phb_lecktlR.xlsx
# (略)

# 2.txt
# 000eccf95e27464fbe6b2866a7d074ba.xlsx
# 000ef14d5b854cb2baf4b7cd82301143.xlsx
# 00118901db8749e29ec09e12c2262a06.xlsx
# 001f64f96d894550810591e580e8ce4c.xlsx
# 00261a27e37b4958a30c7a049149c582.xlsx
# 002c378ae19d4fe7a1bbf60d38b89168.xlsx
# 002e4a6aeacc424da944d7545951ff7a.xlsx
# 00301d04bb264078b63f8afc90df8bda.xlsx
# (略)
# d = dict((['k1', 1], ['k2', 2], ['k3', 4]))
# print(d)
# # {'k1': 1, 'k2': 2, 'k3': 4}

# d = dict([{'k1', 1}, {'k2', 2}, {'k3', 4}])
# print(d)
# # {1: 'k1', 2: 'k2', 'k3': 4}

# import pandas as pd


# https://dev.sizebook.jp/gitbucket/anzu/workmemo/blob/master/1.txt
# https://dev.sizebook.jp/gitbucket/anzu/workmemo/blob/master/2.txt


# def func(x):
#     with open(x) as f:
#         s = f.read()
#         print(s)

# print(func('1.txt'))
# print(func('2.txt'))

# ファイル１　abcde
# ファイル２　efg

# result  abcd

# ファイル１に存在して、ファイル２に存在しないファイル名を
# def func(x):
#     with open(x) as f:
#         s = f.read()
#         print(s)
#         return s

    # with open(x) as f:
    # 	l = f.readlines()
    #     for line in f:
    #         line = line.rstrip('\r\n')
    #     return line
# def func(x):
#     with open(x) as f:
#         l = f.readlines()
#         l_rep = [s.replace('\n', '') for s in l]
#         return l_rep

# def file(a, b):
#     a_list = func(a)
#     b_list = func(b)
#     return list(set(a_list) - set(b_list))

# print(file('1.txt', '2.txt'))


# file('1.txt')
    # 1_list = func('1.txt')
    # 2_list = func('2.txt')
    # xlist = []
    # for i in 1_list:
    #     for p in 2_list:
    #         if i == p:
    #             xlist.append(x):
    # return xlist

# def main():
#     a = fnc1('1.txt')
#     print(a)
#     b = fnc1('2.txt')
#     print(b)
#     c = []
#     for x in a:
#         if x not in b:
#             c.append(x)
#     return c

# print(main())


# def func(b):


# matched_list = []
# for tag in tag_list:
#     for src in src_list:
#         if tag == src:
#             matched_list.append(tag)

# 1_text_list = list(func('1.txt'))
# print(list(func('1.txt')))

# for i in 



# # -*- coding: utf-8 -*-
# from __future__ import print_function

# def func(x):
#     with open('1.txt') as f:
#         print(f.read(), end='')

# with open('2.txt') as f:
#     print(f.readlines())













# input_url = "http://aa"
# check_result = checkURL(input_url)

# if check_result == "OK":
#     print u"アクセスOK"
# else:
#     print check_result





# 月食または日食は太陽と地球と月が一直線に並んだ時に起こります。この三者が一直線に並ぶのは、月が満月or新月の時かつ、月の公転軌道と太陽と地球の位置関係がある条件を満たす時です。
# 月の満ち欠けの周期を29.5日とし、月の公転軌道に関する条件が183日周期で満たされるとします。
# 2018年1月1日0時0分に太陽と地球と月が一直線に並んだとすると、次にこの三者が一直線に並ぶのはいつか計算してください。

# 目的地までの距離が2000mで、出発地と目的地の間には200m間隔に9つの信号があり、すべての信号は同じタイミングで変化しています。
# 信号は30秒青、30秒赤を繰り返しており、すべての信号がちょうど青になったタイミングで時速18km/hの車が目的地に向かって出発しました。
# 車が目的地に到着するまでにかかる時間を計算してください。


# 18000m /60m
# 300m / 分
# 5m /秒







# 月の満ち欠けの周期は29.5日です。
# 2018年8月1日の0時0分(UT)にちょうど月が満月になったとすると、
# 次に8月1日の日本の夜間(18:00~6:00JST)に月が満月になるのは何年か計算して下さい。
# (例えば次に満月になるのは2018年8月1日0時0分(UT) + 29.5日=2018年8月30日12時0分(UT)です。）










# 月の満ち欠けの周期は29.5日です。2018年8月1日の0時0分(UT)にちょうど月が満月になったとすると、
# 次に8月1日の日本の夜間(18:00~6:00JST)に月が満月になるのは何年か計算して下さい。
# (例えば次に満月になるのは2018年8月1日0時0分(UT) + 29.5日=2018年8月30日12時0分(UT)です。）
# 日時をOO月OO日OO時OO分OO秒の形式の10個の数字で表す時、0~9の数字が一回ずつ使われている日時をすべて出力してください。
# ただし、日付は1月1日から12月31日までで、時刻は0時0分0秒から23時59分59秒まで(分と秒はそれぞれ0から59までの数字で表される)とします。
# 例)
# 07月29日18時57分46秒

# 月食または日食は太陽と地球と月が一直線に並んだ時に起こります。
# この三者が一直線に並ぶのは、月が満月or新月の時かつ、月の公転軌道と太陽と地球の位置関係がある条件を満たす時です。
# 月の満ち欠けの周期を29.5日とし、月の公転軌道に関する条件が183日周期で満たされるとします。
# 2018年1月1日0時0分に太陽と地球と月が一直線に並んだとすると、次にこの三者が一直線に並ぶのはいつか計算してください。

# def func(x):
#     for i in range(x):
#         print(i)

# print(func(5))

# # モジュールを読み込む
# import math

# # 最小公倍数
# def lcm(a, b):
# 　return a * b // math.gcd(a, b)

# # 1-20の最小公倍数を求める
# result = 1
# for val in range(1, 21):
# 　result = lcm(val, result)

# 問題
# 目的地までの距離が2000mで、出発地と目的地の間には200m間隔に9つの信号があり、すべての信号は同じタイミングで変化しています。
# 信号は30秒青、30秒赤を繰り返しており、すべての信号がちょうど青になったタイミングで時速18km/hの車が目的地に向かって出発しました。
# 車が目的地に到着するまでにかかる時間を計算してください。


# from datetime import datetime, timedelta

# dt = datetime(2018, 1, 1, 0, 0, 0, 0)
# while True:
#     dt += timedelta(seconds=1)
#     a = dt.strftime('%m%d%H%M%S')
#     if len(list(set(a))) == 10:
#         # print(a)
#         b = datetime.strptime(a, '%m%d%H%M%S')
#         print(b.strftime('%m月%d日%H時%M分%S秒'))
#         break

# import math

# # a = 29.5
# # b = 183

# # print(29.5)
# # print(math.gcd(a, b))

# # lcm(a, b) = a * b / gcd(a, b)

# def lcm(x, y):
#     return (x * y) / math.gcd(x, y)

# print(lcm(int(29.5), int(183)))

# 12

# import datetime
# from dateutil.relativedelta import relativedelta

# def func():
#     time = datetime.datetime(2018, 3, 26, 17, 48, 59)
#     result = []
#     while True:
#         if 2019 == int(time.year):
#             break
#         l = list(time.strftime('%m%d%H%M%S'))
#         if len(set(l)) == 10:
#             result.append('{0:02d}月{1:02d}日 {2:02d}時{3:02d}分{4:02d}秒'.format(time.month, time.day, time.hour, time.minute, time.second))
#         time = time + relativedelta(seconds=1)
#         print(time.strftime('%m%d%H%M%S'))
#     return result

# print(func())


# import re

# def parse_mail(x):
#     m = txt.replace('\n','')
#     code = re.match(r'.*商品コード: (.*)商品名:.*', m).group(1)
#     mail = re.match(r'.*To: (.*) 様 <.*', m).group(1)
#     name = re.match(r'.*商品名: (.*)$', m).group(1)
#     listdata = [('code', code), ('name', name), ('mail', mail)]
#     return dict(listdata)
# txt = """
# From: 7+English [mailto:info@7plus-english.com]
# Sent: Thursday, December 21, 2017 6:03 PM
# To: spring_jyucyu@sizebook.co.jp 様 <spring_jyucyu@sizebook.co.jp>
# Subject: 【7+English】 【7+English】注文が入りました。


# spring_jyucyu@sizebook.co.jp 様

# 今回の注文は【7plus-English-***】です。

# ************************************************
# 　ご注文商品明細
# ************************************************

# 商品コード: 7plus-english-gad1b
# 商品名: 【七田式英語教材】「7+English(セブンプラス・イングリッシュ)」
# """
# print(parse_mail(txt))




# 月の満ち欠けの周期は29.5日です。
# 2018年8月1日の0時0分(UT)にちょうど月が満月になったとすると、
# 次に8月1日の日本の夜間(18:00~6:00JST)に月が満月になるのは何年か計算して下さい。
# (例えば次に満月になるのは2018年8月1日0時0分(UT) + 29.5日=2018年8月30日12時0分(UT)です。）

# def func(x):
# 	for i in range(x):
# 		print(i)

# func(6)





# 時間、cpu使用率、memory使用率が順に並んだ以下のような文字列がある。
# この文字列をパースして、分単位の平均cpu使用率、memory使用率を辞書形式で返す関数を作成せよ

# 2018-03-02 02:25:52+00:00,0.101,649494528.0
# 2018-03-02 02:25:42+00:00,0.101,649494528.0
# 2018-03-02 02:25:32+00:00,0.504,649441280.0
# 2018-03-02 02:25:22+00:00,0.101,649498624.0
# 2018-03-02 02:25:12+00:00,1.31,649498624.0
# 2018-03-02 02:25:02+00:00,6.539,649109504.0
# 2018-03-02 02:24:52+00:00,1.308,647024640.0
# 2018-03-02 02:24:42+00:00,0.202,647028736.0
# 2018-03-02 02:24:32+00:00,0.403,647032832.0
# 2018-03-02 02:24:22+00:00,0.201,647036928.0


# def func(x):
#     for i in range(x):
#         print(i)

# func(6)





# 目的地までの距離が2000mで、出発地と目的地の間には200m間隔に9つの信号があり、すべての信号は同じタイミングで変化しています。
# 信号は30秒青、30秒赤を繰り返しており、すべての信号がちょうど青になったタイミングで時速18km/hの車が目的地に向かって出発しました。
# 車が目的地に到着するまでにかかる時間を計算してください。

# 日時をOO月OO日OO時OO分OO秒の形式の10個の数字で表す時、
# 0~9の数字が一回ずつ使われている日時をすべて出力してください。
# ただし、日付は1月1日から12月31日までで、
# 時刻は0時0分0秒から23時59分59秒まで(分と秒はそれぞれ0から59までの数字で表される)とします。
# 例) 07月29日18時57分46秒

# import random
# l = list(range(10))
# print(range(10))

# # print(random.randrange(0, 13, 1))
# m = random.randrange(0, 13, 1)
# # x以上、y未満の間で、z間隔でランダムな整数を返す。

# b = 1
# c = 3
# d = 2
# e = 7
# print(l.pop(m))
# print(l)
# print("{}月{}日{}時{}分{}秒".format(m, b, c, d, e))

# print(random.sample(l, 1))
# print(random.sample(l, 2))
# print(random.sample(l, 2))
# print(random.sample(l, 2))
# print(random.sample(l, 2))
# a = random.sample(l, 2)
# print(l - a)



# a =     # 01 ~ 12
# b =     # 10 ~ 31
# c =     # 00 ~ 23
# d =     # 00 ~ 59
# e =     # 00 ~ 59

# print("{}月{}日{}時{}分{}秒".format(a, b, c, d, e))





# 月の満ち欠けの周期は29.5日です。2018年8月1日の0時0分にちょうど月が満月になったとすると、
# 次に8月1日に月が満月になるのは何年か計算して下さい。
# (例えば次に満月になるのは2018年8月1日0時0分 + 29.5日=2018年8月30日12時0分です。）
# from datetime import datetime, timedelta
# d1 = datetime(2018, 8, 1, 0, 0, 0, 0)
# print(d1)

# print(365 * 2 % 29.5)


# from datetime import datetime, timedelta

# d1 = datetime(2018, 8, 1, 0, 0, 0, 0)

# while True:
# # for i in 
#     d1 += timedelta(days=29, hours=12)
#     if d1.month == 8 and d1.day == 1:
#         print("{}/{}/{}".format(d1.year, d1.month, d1.day))
#         break

# func(x):
   # for i in 365

# import datetime

# tstr = '2018-08-01 00:00:00'
# tdatetime = datetime.datetime.strptime(tstr, '%Y-%m-%d %H:%M:%S')
# # tdate = datetime.date(tdatetime.year, tdatetime.month, tdatetime.day)

# print(tdatetime)
# dt = datetime.datetime(2018, 8, 1, 12, 30, 0, 0)

# if (dt.month == 8 and dt.day == 1):

# dt.day == 29 and dt.hour == 12







# print(dt.microsecond)
# # 2000

# dt = datetime.datetime(2018, 2, 1)
# print(dt)
# # 2018-02-01 00:00:00

# print(dt.minute)
# 0











# while True:
#     d1 += timedelta(days=29, hours=12)
#     # print(d1)
#     if d1.month == 8 and d1.day == 1:
#         print("{}/{}/{}".format(d1.year, d1.month, d1.day))
#         break



# 日時をOO月OO日OO時OO分OO秒の形式の10個の数字で表す時、
# 0~9の数字が一回ずつ使われている日時をすべて出力してください。
# ただし、日付は1月1日から12月31日までで、
# 時刻は0時0分0秒から23時59分59秒まで(分と秒はそれぞれ0から59までの数字で表される)とします。
# 例)
# 07月29日18時57分46秒
# 0か1
# # 

# def func(x):
#     for i in x:
#         print(i)

# func(5)
# ・100名の企業で、起算日までに年間10名が退職。在籍者数が90名となった場合（その間に新たに採用した人数は除く）
# ⇒10名÷90名×100＝離職率約11％

# ケースB

# 「新卒社員が3年以内に離職した割合」

# ・100名の企業で、10名の新卒社員を採用。3年以内に5名が退職した場合
# ⇒5名÷10名＝離職率50％

# ケースC

# 「過去5年をさかのぼり、中途社員が1年以内に離職した割合」

# ・100名の企業で、2009年から2014年まで毎年2名ずつ計10名を採用。そのうち5名が1年以内に離職した場合
# ⇒5名÷10名＝離職率50％



# 初乗り1000mまでは400円で、その後は100mごとにそれまでの走行距離(メートル)が加算運賃として加算されるタクシーで、
# 2000m利用した場合の運賃を求めてください。

# 円周率の整数部分と小数点以下第20桁までの数値を合算し返却する関数を作成せよ。
# また、ループ中の該当桁の数値と合算途中経過を表示すること。

# 任意の数の整数を与えられたときに、その値の最高値と最低値を覗いた数値から平均を求める関数を作成しよう。
# 例）1,2,3,4,5,5,1 →　2,3,4 = 3.0

# print(1,2,3,4,5,5,1)
# l = [1,2,3,4,5,5,1]
# print(max(l)) # 最高値
# print(min(l)) # 最低値





