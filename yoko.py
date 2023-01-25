# coding: utf-8
#!/usr/bin/env python

# 以下の文字列を変換して、htmlフォーマットを生成する関数「convert2html」を作成せよ。
# 引数は文字列１個とする。

# input : '''# hello
# This is a example sentence.
# next sentence
# # title2
# mark down
# '''
# output: '''<h1>hello</h1>
# <p>This is a example sentence.</p>
# <p>next sentence</p>
# <h1>title2</h1>
# <p>mark down</p>
# '''






# 所持金：3000円
# 商品値段： 120円, 300円, 440円

# それぞれの商品を１つ以上買い、
# お釣りが最小になるパターンを求めよ。
# ただし、消費税やチップは考えない。
# （返却タイプはリストでも辞書でも構わない）

# 回答例
# {120: 4, 300: 4, 440: 3}
# お釣り：0

# import itertools

# def func(x):
#     s = x // 120
#     a = list(range(1, s))
#     xlist = []
#     for i in itertools.permutations(a, 3):
#         p = 120 * i[0] + 300 * i[1] + 440 * i[2]
#         pp = p, i[0], i[1], i[2]
#         xlist.append(pp)
#         if p == x:
#             return list(i), '0'
#     ylist = []
#     for p in xlist:
#         if p[0] <= x:
#             print(p)
#             ylist.append(p)
#     if max(ylist[0]):
#     	print('a', p)

# print(func(3000))
# print(func(3110))
















# (1, 1)〜(N, N)の大きさNxNの格子を考える。この格子を以下の様な順序でアクセスした時に、アクセスする順に座標列を返す関数を作成せよ
# 引数は整数型N（> 1）とする。

# - N = 2（下記の数字は格子点へのアクセス順）
# 3 4
# 1 2
# 答え: [(1, 1), (2, 1), (1, 2), (2, 2)]

# - N = 3
# 4 8 9
# 3 5 7
# 1 2 6
# 答え: [(1, 1), (2, 1), (1, 2), (1, 3), (2, 2), (3, 1), (3, 2), (2, 3), (3, 3)]

# - N = 4
# 10 11 15 16
# 4 9 12 14
# 3 5 8 13
# 1 2 6 7
# 答え：略


# def func(scale):
#     lst = []
#     flag = True
#     x = y = 1
#     for n in range(2, 2*scale+1):
#         print(n)
#         if flag:
#             x, y = (1, n-1) if n <= scale else (n - scale, scale)
#             while y > 0 and x < scale+1:
#                 lst.append((x,y))
#                 x, y = (x+1, y-1)
#         else:
#             x, y = (n-1, 1) if n <= scale else (scale, n - scale)
#             while x > 0 and y < scale+1:
#                 lst.append((x,y))
#                 x, y = (x-1, y+1)
#         flag ^= True
#     return lst


# print(func(2))

# print(func(3))

# print(func(4))

# print(func(5))



















# デジタル数字で時刻を表す時計(OO:OOのようなフォーマット)があります。
# この時計を上下反転した場合でも、意味のある時刻(00:00 ~ 23:59)を表すような時刻をすべて出力してください。
# ただし、時刻は常に二桁で表されます(例えば、1時1分の場合 "01:01" と表示される)。

# 上下反転した時の対応リスト
# 1 <=> 1
# 2 <=> 5
# 3 <=> 3
# 8 <=> 8

# (例)
# 12:11 -> 15:11 はok
# 21:08 -> 51:08 はダメ

# xlist = []
# for h in range(0, 24):
#     for m in range(0, 60):
#         a = "{}{}".format(h, m)
#         s = "{:02d}{}{:02d}".format(h, ':', m)
#         # print(s)
#         xlist.append(s)
# # print(xlist)

# def henkan(x):
#     # 3, 4, 7はNG 1, 8, 0はOK
#     if '3' in x or '4' in x or '7' in x:
#         return 'NG'
#     # 5と2
#     m = x.replace('5', 'X').replace('2', '5').replace('X', '2')
#     # 6と9
#     n = m.replace('6', 'X').replace('9', '6').replace('X', '9')
#     if n[:2] > '23':
#         return 'NG'
#     if n[-2:] > '59':
#         return 'NG'
#     return n

# xlist = []
# for h in range(0, 24):
#     for m in range(0, 60):
#         a = "{:02}{:02}".format(h, m)
#         if henkan(a) != 'NG':
#             l = "{0}:{1}".format(a[:2], a[-2:])
#             xlist.append(l)
# print(xlist)





# 所持金：3000円
# 商品値段： 120円, 300円, 440円

# それぞれの商品を１つ以上買い、
# お釣りが最小になるパターンを求めよ。
# ただし、消費税やチップは考えない。
# （返却タイプはリストでも辞書でも構わない）

# 回答例
# {120: 4, 300: 4, 440: 3}
# お釣り：0

# Type "help", "copyright", "credits" or "license" for more information.
# >>> print(120*4+300*4+440*3)
# 3000

# import itertools

# def func(x):
#     s = x // 120
#     a = list(range(1, s))
#     xlist = []
#     for i in itertools.permutations(a, 3):
#         p = 120 * i[0] + 300 * i[1] + 440 * i[2]
#         pp = p, i[0], i[1], i[2]
#         xlist.append(pp)
#         if p == x:
#             return list(i), '0'
#     ylist = []
#     for p in xlist:
#         if p[0] <= x:
#             print(p)
#             ylist.append(p)
#     if max(ylist[0]):
#     	print('a', p)

# print(func(3000))
# print(func(3110))







# 同じ長さの3本の紐を折り曲げて 3 つの四角形を作ることを考えます。そのうち、2本でそれぞれ長方形を作り、残りの一本は正方形をつくります。
# このとき、作った 2 つの長方形の面積の和が、正方形の面積と同じになることがあります。(ただし、長方形、正方形のいずれの辺の長さも整数になるとします。)
# (例) ひもの長さが 20 のとき、 (縦 x 横) = (1 x 9), (2 x 8), (5 x 5) とすると、この条件を満たします。

# ひもの長さを1から500まで変化させるとき、2つの長方形の面積の和と、正方形の面積が同じになる組が何通りあるかを求めてください。

# ただし、同じ比で長さが整数倍になっているものは 1 つとしてカウントします。
# (例)
# ひもの長さが 20 のとき、(縦 x 横) = (1 x 9), (2 x 8), (5 x 5)
# ひもの長さが 40 のとき、(縦 x 横) = (2 x 18), (4 x 16), (10 x 10)
# ひもの長さが 60 のとき、(縦 x 横) = (3 x 27), (6 x 24), (15 x 15)
# この3つは長方形の辺の比が同じで、長さが整数倍になっているので、まとめて一つとしてカウントします。

# 2014年のワールドカップ出場国の国名を使ってしりとりをしてみましょう。ただし、使うのはアルファベットです。(大文字と小文字は区別しません)
# どの国名も一度しか使うことができない時、最も長く続けられる順を求め、使用した国名の数を答えてください。

# c_list = ['Brazil', 'Cameroon', 'Chile', 'Greece', 'Uruguay',
#  'Italy', 'France', 'Bosnia and Heregovina', 'Gernany', 'USA',
#  'Russia', 'Croatia', 'Spain', 'Australia', "Cote d'lvoire",
#  'Costa Rica', 'Switzerland', 'Honduras', 'Iran', 'Portugal',
#  'Belgium', 'Korea Republic', 'Mexico', 'Netherlands', 'Colombia',
#  'Japan', 'England', 'Ecuador', 'Agentina', 'Nigeria', 'Ghana', 'Algeria']

# xlist = [ i.lower() for i in c_list ]

# # もっとも長いしりとり記録変数
# longest = []


# for m in longest:
# 	print(m)
#     for p in xlist:
# 	    # print(p, p[0], m[-1])
# 	    if p[0] == m[-1]:



# 3 本の同じ長さの紐があるとき、
# 1 本を正方形にして、２本を長方形とし、長方形二つの面積 = 正方形の面積 となる組み合わせはいくつある？
# ただし、一度出た正方形と長方形の長さの比は同一のものとしてカウントします

# x^2 = (x - n)(x + n) + (x - m)(x + m) の等式が成り立つ m, n の組み合わせなので
#     = x^2 - n^2 + x^2 - m^2
#     = 2x^2 - (n^2 + m^2)
# となるので、x^2 = n^2 + m^2 となる n, m の組み合わせを探す
# なおかつ、一度出た m : n 比はカウントしない

# import itertools

# max_length = 500      # ひもの最長
# result_patterns = {}  # 比率 -> 組み合わせ でハッシュ

# for x in range(1, int(max_length / 4) + 1):  # 正方形の一辺
#     combination = itertools.combinations(range(1, x), 2)
#     valid_patterns = [n for n in combination if n[0] * n[0] + n[1] * n[1] == x * x]
#     for pat in valid_patterns:
#         result_patterns[pat[1] / pat[0]] = pat

# print(len(result_patterns))

# 同じ長さの3本の紐を折り曲げて
# 3 つの四角形を作ることを考えます。
# そのうち、2本でそれぞれ長方形を作り、残りの一本は正方形をつくります。
# このとき、作った 2 つの長方形の面積の和が、
# 正方形の面積と同じになることがあります。
# (ただし、長方形、正方形のいずれの辺の長さも整数になるとします。)
# (例) ひもの長さが 20 のとき、 
# (縦 x 横) = (1 x 9), (2 x 8), (5 x 5) とすると、この条件を満たします。

# ひもの長さを1から500まで変化させるとき、
# 2つの長方形の面積の和と、正方形の面積が同じになる組が何通りあるかを求めてください。

# ただし、同じ比で長さが整数倍になっているものは 1 つとしてカウントします。
# (例)
# ひもの長さが 20 のとき、(縦 x 横) = (1 x 9), (2 x 8), (5 x 5)
# ひもの長さが 40 のとき、(縦 x 横) = (2 x 18), (4 x 16), (10 x 10)
# ひもの長さが 60 のとき、(縦 x 横) = (3 x 27), (6 x 24), (15 x 15)
# この3つは長方形の辺の比が同じで、長さが整数倍になっているので、まとめて一つとしてカウントします。

















# 所持金：3000円
# 商品値段： 120円, 300円, 440円

# それぞれの商品を１つ以上買い、
# お釣りが最小になるパターンを求めよ。
# ただし、消費税やチップは考えない。
# （返却タイプはリストでも辞書でも構わない）

# 回答例
# {120: 4, 300: 4, 440: 3}
# お釣り：0

# import itertools

# def func(x):
#     s = x // 120
#     a = list(range(1, s))
#     xlist = []
#     for i in itertools.permutations(a, 3):
#         p = 120 * i[0] + 300 * i[1] + 440 * i[2]
#         pp = p, i[0], i[1], i[2]
#         xlist.append(pp)
#         if p == x:
#             return list(i), '0'
#     ylist = []
#     for p in xlist:
#         if p[0] <= x:
#             print(p)
#             ylist.append(p)
#     if max(ylist[0]):
#     	print('a', p)

# print(func(3000))
# print(func(3110))


# 日時をOO月OO日OO時OO分OO秒の形式の10個の数字で表す時、
# 0~9の数字が一回ずつ使われている日時をすべて出力してください。

# ただし、日付は1月1日から12月31日までで、
# 時刻は0時0分0秒から23時59分59秒まで(分と秒はそれぞれ0から59までの数字で表される)とします。
# 例)
# 07月29日18時57分46秒

# xlist = list(range(0, 10))
# print(xlist)

# import datetime as dt
# from datetime import datetime, date, timedelta

# date = dt.datetime(2018, 3, 26, 0, 0)
# m = []
# for i in range(365):
#     mm = datetime.strftime(date, '%m%d')
#     m.append(mm)
#     date += dt.timedelta(days=1)

# y = []
# # 24 * 60 * 60 = 86400
# for i in range(86400):
#     yy = datetime.strftime(date, '%H%M%S')
#     y.append(yy)
#     date += dt.timedelta(seconds=1)

# for mm in m:
#     for yy in y:
#         a = '{}{}'.format(mm, yy)
#         if len(set(list(a))) == 10:
#             print(a)


# from datetime import datetime, timedelta

# dt = datetime(2018, 3, 26, 0, 0, 0, 0)
# while True:
#     dt += timedelta(seconds=1)
#     a = dt.strftime('%m%d%H%M%S')
#     if len(list(set(a))) == 10:
#         b = datetime.strptime(a, '%m%d%H%M%S')
#         print(b.strftime('%m%d%H%M%S'))




        # if len(list(a)) == 10:
            # print(a)

# today = datetime.today()
# print(datetime.strftime(today, '%Y-%m-%d'))
# tomorrow = today + timedelta(days=1)
# print(datetime.strftime(tomorrow, '%Y-%m-%d'))
# yesterday = today - timedelta(days=1)

# aida = tomorrow - today
# print(datetime.strftime(date, '%m,%d'))
# 01、
# from datetime import datetime
# from datetime import timedelta

# start = datetime.strptime('2018-09-01, 00:00:00', '%Y-%m-%d, %H:%M:%S')
# end = datetime.strptime('2018-09-05, 23:59:59', '%Y-%m-%d, %H:%M:%S')

# def daterange(_start, _end):
#     for n in range((_end - _start).days):
#         yield _start + timedelta(n)


# for i in daterange(start, end):
#     print (i)

# import datetime

# start = str(2018010100)
# end = str(201812312359)

# start_dt = datetime.datetime.strptime(start, "%Y%m%d%H")
# end_dt = datetime.datetime.strptime(end, "%Y%m%d%H")

# lst = []
# t = start_dt
# while t <= end_dt:
#     lst.append(t)
#     t += datetime.timedelta(hours=1)

# print([int(x.strftime("%Y%m%d%H")) for x in lst])

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
#         # print(time.strftime('%m%d%H%M%S'))
#     return result

# print(func())


# 整数 x, y, z は次の式を満たしているとします。
# 6x + 4y + z = 50
# 2x + 3y + z = 30

# この時、 4x + 3y の最大値を求めてください。




# 正の整数のリストの要素と＋、✕をもちいて計算できる最大値を出力して下さい。
# (例)
# [1, 2, 3, 4] -> (1 + 2) * 3 * 4 = 36
# [2, 3, 4] -> 2 * 3 * 4 = 24

# import itertools
# from itertools import *
# from itertools import zip_longest

# def func(x):
#     a = len(x) - 1

#     shiki = ['+', '*']
#     for i in itertools.product(shiki, repeat=a):
#         a = list(chain(*zip_longest(x, i, fillvalue='')))
#         print(x, a)
#         a = map(str, a)
#         print(' '.join(a))


# print(func([1, 2, 3, 4]))
# print(func([2, 3, 4]))


# print(2+3+4)
# print(sum(2+3)+4)
# print(2+3+4)
# print(2+3+4)

# lower = [1, 2, 3]
# upper = ['+', '*']


# list1 = [1, 2, 3]
# list2 = ['+', '*']

# print(sum([[list1[i], list2[i]] for i in range(len(list1))], []))
# # print(list(chain.from_iterable([[list1[i], list2[i]] for i in range(len(list1))])))
# # print(list(chain.from_iterable(zip(list1, list2))))
# print([item for pair in zip(list1, list2) for item in pair])
# # print(list(chain(*zip(list1, list2))))

# list3 = [0] * (len(list1) + len(list2))
# list3[::2] = list1
# list3[1::2] = list2
# print(list3)

# for i in range(len(list1)):
#     list1.insert(i * 2 + 1, list2[i])
# print(list1)