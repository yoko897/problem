# coding: utf-8
# #!/usr/bin/env python


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


# import itertools
# import math

# # 正方形の1辺の長さ
# # c = himo//4
# # 正方形の面積
# # print(c*c)
# # ((c-x)*(c+x)) + M == c*c
# # (c^2 - x^2) - c^2 == M
# # x^2 == M
# # a^2 + b^2 == c^2
# # 面積は全部平方数になる。

# xlist = []
# for p in range(1, 501):
#     i = p//4
#     for m in itertools.combinations(range(1, i+1), 3):
#         if (m[0] * m[0]) + (m[1] * m[1]) == (m[2] * m[2]):
#             if math.gcd(m[0], m[1]) == 1:
#                 xlist.append(m)
# print(set(xlist))
# print(len(set(xlist)))

# import itertools

# def func(x):
#     a = []
#     b = []
#     l = range(1, x//120+1)
#     for m in itertools.permutations(l, 3):
#         if 120 * m[0] + 300 * m[1] + 440 * m[2] == x:
#             return 'お釣り:0, 120*{}, 300*{}, 440*{}'.format(m[0], m[1], m[2])
#         else:
#             i = x - (120 * m[0] + 300 * m[1] + 440 * m[2])
#             if i > 0:
#                 a.append(m)
#                 b.append(i)
#     t = b.index(min(b))
#     return 'お釣り:{}, 120*{}, 300*{}, 440*{}'.format(min(b), a[t][0], a[t][1], a[t][2])

# print(func(3000))
# print(func(3001))
# print(func(3200))



# 次のXMLを読み、以下の関数を作成せよ
# http://sizebook.co.jp/test/anzu/180226.xml
# ただし、このxmlは既に xml　という変数にSTRで入っているのでcurlとかしなくて良い
# ・価格(price)が1500円以上のアイテムの名前(name)とpriceを表示する関数
# ・購入したproduct_idが入っているリストを渡すと、nameとpriceとpriceの合計を表示する関数


# <products>
# <product id="10">
# <name>ブルーライセンス３０日</name>
# <price>500</price>
# </product>
# <product id="20">
# <name>プラチナガチャチケ</name>
# <price>1000</price>
# </product>
# <product id="30">
# <name>backdoor入学</name>
# <price>500000</price>
# </product>
# <product id="40">
# <name>初めてのdocker</name>
# <price>1500</price>
# </product>
# <product id="50">
# <name>三江線　三次→江津</name>
# <price>1800</price>
# </product>
# </products>

# import xml.etree.ElementTree as ET
# 
# root = ET.fromstring(XmlData)

# 以下の関数は偶数を与えると”偶数”
# 奇数を与えると”奇数”と返ってくる。

# def is_even(n):
# if n % 2 == 0:
# return "偶数"
# else:
# return "奇数"

# これに３の倍数を与えると”ほえほえ”と返却するデコレータを追加し
# 1=奇数
# 2=偶数
# 3=ほえほえ
# となるようなプログラムを作ってください。


# def muemue(func):
#     import functools
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         if args[0] % 3 == 0:
#             return "ほえほえ"
#         else:
#             return func(args[0])
#     return wrapper


# @muemue
# def is_even(n):
#     if n % 2 == 0:
#         return "偶数"
#     else:
#         return "奇数"

# print(is_even(1))
# print(is_even(2))
# print(is_even(3))

# def hoe(n):
#     if n % 3 == 0:
#         return "ほえほえ"

# def is_even(n):
#     if n % 2 == 0:
#         return "偶数"
#     else:
#         return "奇数"

# from functools import wraps

# def hoehoe(f):
#     @wraps(f)
#     def wrapper():
#         if n % 3 == 0:
#             return "ほえほえ"
#         else:
#             return f()
#     return wrapper

# @hoehoe
# def is_even(n):
#     if n % 2 == 0:
#         return "偶数"
#     else:
#         return "奇数"

# print(is_even(1))

# import itertools

# def sa(l1, l2):
#     return list(set(l1) - set(l2))

# sudoku = [[5, 8, None, 3, None, None, None, None, 1],
# [None, None, 2, None, None, None, 8, 6, None],
# [None, None, 9, None, None, 2, 7, None, 4],
# [6, None, None, 2, 3, None, 4, 1, None],
# [8, None, None, 5, 1, None, None, 7, None],
# [9, 1, 4, None, 7, None, None, 3, None],
# [3, 9, None, 7, 2, None, None, None, None],
# [None, 6, 5, 4, None, None, 1, None, None],
# [4, None, None, 9, None, 6, None, 8, None]]

# def func(xlist, ylist):
#     zlist = []
#     cnt = 0 
#     for x in xlist:
#         if x != None:
#             zlist.append(x)
#         elif x == None:
#             zlist.append(ylist[cnt])
#             cnt += 1
#     return zlist

# print(func([5, 8, None, 3, None, None, None, None, 1], [2, 4, 6, 7, 9]))


# a = list(range(1, 10))
# # print(a)

# # tate = []
# cnt = 0
# b = []
# for i in sudoku:
#     # print(i, i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
#     # b += str(i[0])
# # print(b)
#     # tate.append(i[0])

# # print(sum(tate))
#     for m in itertools.permutations(sa(a, i)):
#         print(cnt, func(i, m), func(i, m)[0])
#     cnt += 1

    	# if len(set(m)) == 9:
        # tate.append(func(i, m)[0])
# print(sum(tate))

# [5, 8, None, 3, None, None, None, None, 1] [2, 4, 6, 7, 9]


        # if x == 'N':
        	# print(x, y)
            # m = x.replace('N', str(y))
            # print(y)
            # zlist.append(m)
# print(zlist)


# ->
# [[5, 8, 6, 3, 4, 7, 9, 2, 1],
# [7, 4, 2, 1, 9, 5, 8, 6, 3],
# [1, 3, 9, 8, 6, 2, 7, 5, 4],
# [6, 5, 7, 2, 3, 9, 4, 1, 8],
# [8, 2, 3, 5, 1, 4, 6, 7, 9],
# [9, 1, 4, 6, 7, 8, 2, 3, 5],
# [3, 9, 8, 7, 2, 1, 5, 4, 6],
# [2, 6, 5, 4, 8, 3, 1, 9, 7],
# [4, 7, 1, 9, 5, 6, 3, 8, 2]]

# import itertools

# def s(x)
#     return 7 - x


# for i in itertools.permutations(range(1, 7), 6):
# 	print(i)


# n = i




# カジノの定番ブラックジャックではゲームを一回行うには、最低一枚コインが必要です。
# 勝てば二枚のコインを得られますが、負けると賭けたコインが没収されます。
# 最初に一枚だけコインを持っており、一枚ずつかけて行った時、
# ゲームを四回行って手元にコインが残るような枚数の変化は6通り考えられます。
# 最初に10 枚コインを持っていた時、
# ゲームを24 回行って手元にコインが残るような枚数の変化が何通りあるかを求めてください。

# def func(coin, game):
#     cnt = 0
#     if coin <= 0:
#         return 0
#     if coin >= 1 and game >= 24:
#         return 1
#     cnt += func(coin+1, game+1)
#     cnt += func(coin-1, game+1)

#     return cnt

# print(func(10, 0))

# ホールケーキを切り分けるとき、
# ケーキに乗っているいちごの数がすべて異なるような切り方を考える。
# ここでは、N 個に切り分けるときには
 # 「1 ~ N 個のいちご (合計 N (N + 1) / 2 個)」 がそれぞれに乗っているようにする。
# ただし、隣り合う２つのケーキに乗っているいちごの数の和が、
# いずれも平方数になるように切らなければならないという条件を追加する。
# このような条件を満たすような切り方ができる最小の N (> 1) を求めてください。
# import itertools


# def is_heiho(x):
#     heiho =	[ i * i for i in range(1, 100000)]
#     if x in heiho:
#         return True
#     else:
#         return False

# # # 切り分ける数 x
# def ichigo_sum(x):
#     return x * (x + 1) // 2

# ichigo = []
# for n, i in enumerate(range(1, 10)):
#     # 切り分ける数、イチゴの合計
#     # print(n+1, ichigo_sum(i))
#     ichigo.append(ichigo_sum(i))
# print(ichigo)

# for n, i_sum in enumerate(ichigo):
#     for m in itertools.permutations(range(1, i_sum+1), n+1):
#         if sum(m) == i_sum:
#             if is_heiho(sum(m[0:2])) and is_heiho(sum(m[2:4])):
#             	print(m)

    # print(['i' for v in range(1, i+1)])
    # print(list(range(1, i+1)))



# for m in itertools.permutations(range(1, 6+1), 3):
#     if sum(m) == 6:
#         print(m)

# 正の整数のリストの要素と＋、✕をもちいて計算できる最大値を出力して下さい。
# (例)
# [1, 2, 3, 4] -> (1 + 2) * 3 * 4 = 36
# [2, 3, 4] -> 2 * 3 * 4 = 24

# import itertools

# l = ['*', '+']
# k =  ['(', ')']

# for m in itertools.permutations(l, 2):
#     print(m)


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
#     a = []
#     b = []
#     l = range(1, x//120+1)
#     for m in itertools.permutations(l, 3):
#         if 120 * m[0] + 300 * m[1] + 440 * m[2] == x:
#             return 'お釣り:0, 120*{}, 300*{}, 440*{}'.format(m[0], m[1], m[2])
#         else:
#             i = x - (120 * m[0] + 300 * m[1] + 440 * m[2])
#             if i > 0:
#                 a.append(m)
#                 b.append(i)
#     t = b.index(min(b))
#     return 'お釣り:{}, 120*{}, 300*{}, 440*{}'.format(min(b), a[t][0], a[t][1], a[t][2])

# print(func(3000))
# print(func(3010))
# print(func(3200))


# 時間、cpu使用率、memory使用率が順に並んだ以下のような文字列がある。
# この文字列をパースして、分単位の平均cpu使用率、memory使用率を辞書形式で返す関数を作成せよ

# str = """2018-03-02 02:25:52+00:00,0.101,649494528.0
# 2018-03-02 02:25:42+00:00,0.101,649494528.0
# 2018-03-02 02:25:32+00:00,0.504,649441280.0
# 2018-03-02 02:25:22+00:00,0.101,649498624.0
# 2018-03-02 02:25:12+00:00,1.31,649498624.0
# 2018-03-02 02:25:02+00:00,6.539,649109504.0
# 2018-03-02 02:24:52+00:00,1.308,647024640.0
# 2018-03-02 02:24:42+00:00,0.202,647028736.0
# 2018-03-02 02:24:32+00:00,0.403,647032832.0
# 2018-03-02 02:24:22+00:00,0.201,647036928.0
# """
# # print(str.splitlines())

# zikan = []
# cpu = []
# memory = []
# for i in str.splitlines():
#     zikan += [i.split(',')[0]]
#     cpu += [i.split(',')[1]]
#     memory += [i.split(',')[2]]
# print(zikan)
# # print(cpu)
# # print(memory)

# # for p in zikan:
# # 	print(p[0:4], p[5:7], p[8:10], p[11:13], p[14:16])
# # 	nen = p[0:4]
# # 	mon = p[5:7]
# # 	day = p[8:10]
# # 	hour = p[11:13]
# # 	mini = p[14:16]

# from datetime import datetime as dt

# tstr = '2012-12-29 13:49:37'
# tdatetime = dt.strptime(tstr, '%Y-%m-%d %H:%M:%S')




# proc = subprocess.run(["ls"],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
# print(proc.stdout.decode("cp932"))

# 同じ長さの3本のひもを折り曲げて3つの四角形を作ることを考えます。そのうち 2本でそれぞれ長方形を作り、残りの1本は正方形を作ります。
# このとき、作った2つ の長方形の面積の和が、正方形の面積と同じになることがあります(ただし、いずれ の長方形、正方形も辺の長さは整数になるものとします)。
# 例) ひもの長さが20のとき、以下のような長方形と正方形を作ることができます。
# 1本目 縦1×横9の長方形 → 面積 = 9
# 2本目 縦2×横8の長方形 → 面積 = 16
# 3本目 縦5×横5の正方形 → 面積 = 25

# さらに、ひもの長さを変えてできる長方形と正方形の組をカウントすることを考えます。ただし、同じ比で整数倍のものは1つとしてカウントするものとします。

# 問題

# ひもの長さを1から500まで変化させるとき、2つの長方形の面積の和と、正方形の 面積が同じになる組が何通りあるかを求めてください。

# import itertools
# import math

# # 正方形の1辺の長さ
# # c = himo//4
# # 正方形の面積
# # print(c*c)
# # ((c-x)*(c+x)) + M == c*c
# # (c^2 - x^2) - c^2 == M
# # x^2 == M
# # a^2 + b^2 == c^2
# # 面積は全部平方数になる。

# xlist = []
# for p in range(1, 501):
#     i = p//4
#     for m in itertools.combinations(range(1, i+1), 3):
#         if (m[0] * m[0]) + (m[1] * m[1]) == (m[2] * m[2]):
#             if math.gcd(m[0], m[1]) == 1:
#                 xlist.append(m)
# print(set(xlist))
# print(len(set(xlist)))


# cnt = 0
# for himo in range(1, 501):
#     se = himo//4
#     se_men = se * se
#     # 縦+横
#     # print(himo//2)
#     m = himo//2
#     # 足して10になる組み合わせ
#     # [1, 9], [2, 8], [3, 7], [4, 5]
    
#     xlist = []
#     for i in itertools.combinations(range(1, m), 2):
#         if sum(i) == m:
#             ii = i[0] * i[1]
#             xlist.append(ii)
#     for i in itertools.combinations(xlist, 2):
#         if se_men == i[0] + i[1]:
#             print(i)
#             cnt += 1
# print(cnt)








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
# 4  9  12 14
# 3  5  8  13
# 1  2  6  7
# 答え：略


# def func(x):
#     zahyo = []
#     for i in range(1, x+1):
#         for p in range(1, x+1):
#             m = '({}, {})'.format(i, p)
#             zahyo.append(m)
#     print(zahyo)

# print(func(2))











# 9x9 の大きさのリストが与えられた時に、数独を完成させてください。
# ただし、リストの数字は各マスの数字を表し、 値がすでに決まっている場合にはその数字が、そうでない場合には None が入っている。

# def sabun(l1, l2):
# 	return list(set(l1) - set(l2))

# import itertools

# # (例)
# sudoku = [[ 5, 8, None, 3, None, None, None, None, 1],
# [None, None, 2, None, None, None, 8, 6, None],
# [None, None, 9, None, None, 2, 7, None, 4],
# [ 6, None, None, 2, 3, None, 4, 1, None],
# [ 8, None, None, 5, 1, None, None, 7, None],
# [ 9, 1, 4, None, 7, None, None, 3, None],
# [ 3, 9, None, 7, 2, None, None, None, None],
# [None, 6, 5, 4, None, None, 1, None, None],
# [ 4, None, None, 9, None, 6, None, 8, None]]

# for i in sudoku:
# 	print(i)

# print(list(range(1, 10)))
# a = list(range(1, 10))

# xlist = []
# for i in [ 5, 8, None, 3, None, None, None, None, 1]:
#     if i != None:
#         xlist.append(i)
# print(xlist)

# sa = sabun(a, xlist)

# for i in itertools.permutations(sa):
#     print(i)


# ->
# [[5, 8, 6, 3, 4, 7, 9, 2, 1],
# [7, 4, 2, 1, 9, 5, 8, 6, 3],
# [1, 3, 9, 8, 6, 2, 7, 5, 4],
# [6, 5, 7, 2, 3, 9, 4, 1, 8],
# [8, 2, 3, 5, 1, 4, 6, 7, 9],
# [9, 1, 4, 6, 7, 8, 2, 3, 5],
# [3, 9, 8, 7, 2, 1, 5, 4, 6],
# [2, 6, 5, 4, 8, 3, 1, 9, 7],
# [4, 7, 1, 9, 5, 6, 3, 8, 2]]

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


# import csv

# kaminoku = []
# simonoku = []
# with open('./q33.csv') as f:
#     reader = csv.reader(f)
#     # ヘッダーを読み飛ばしたい時
#     header = next(reader)
#     for row in reader:
#         kaminoku += [row[3]]
#         simonoku += [row[4]]

# a_list = []
# cnt = 0
# for m, i in enumerate(kaminoku):
# 	# 文字数
# 	# for m in range(0, 20):
#     a_list.append(i[0])
# print(a_list)

# for index, i in enumerate(a_list):
#     if a_list.count(i) == 1:
#         print(index, i)
#         cnt += 1

# for m, i in enumerate(kaminoku):
#     b_list.append(i[1])
# print(b_list)

# for index, i in enumerate(b_list):
#     if b_list.count(i) == 1:
#         print(index, i)
#         cnt += 1



# # 重複した要素
# # print(list(set(a_list)))
# # m = list(set(a_list))


# # print(sabun(a_list, m))


# # new_list = []
# # for i in ue_list:
# # 	# print(i[0])
# # 	if i[0] 







# new_list.append(i[0])
# 	# else:
# 		# new_list.append('aa')
# print(new_list)

























# import itertools
# import re
# from itertools import zip_longest


# def func():
#     shiki = ["*", "/", "+", "-", ""]
#     plist = []
#     for i in range(1, 10):
#         for p in range(1, 10):
#             plist.append([i] * p)

#     kotae_list = []
#     for a in plist:
#         m = len(a) - 1
#         for i in itertools.product(shiki, repeat=m):
#             moji = list(zip_longest(a, list(i), fillvalue=""))
#             s = sum(moji, ())
#             keisan = ''.join(list(map(str, s)))
#             if int(eval(keisan)) == 1234:
#                 # b = '[{}], [{}]'.format(len(a), keisan)
#                 # print(len(a), keisan, b)
#                 kotae_list.append(keisan)
#     print(kotae_list)
#     for i in kotae_list:
#         a = re.findall(r'[0-9]+', i)
#         b = ''.join(a)
#         print(b, len(b))



# print(func())

# xml = """
# <products>
#   <product id="10">
#     <name>ブルーライセンス３０日</name>
#     <price>500</price>
#   </product>
#   <product id="20">
#     <name>プラチナガチャチケ</name>
#     <price>1000</price>
#   </product>
#   <product id="30">
#     <name>backdoor入学</name>
#     <price>500000</price>
#   </product>
#   <product id="40">
#     <name>初めてのdocker</name>
#     <price>1500</price>
#   </product>
#   <product id="50">
#     <name>三江線　三次→江津</name>
#     <price>1800</price>
#   </product>
# </products>
# """
	
# # XMLパース
# # 次のXMLを読み、以下の関数を作成せよ
# # http://sizebook.co.jp/test/anzu/180226.xml
# # ただし、このxmlは既に xml　という変数にSTRで入っているのでcurlとかしなくて良い
# # ・価格(price)が1500円以上のアイテムの名前(name)とpriceを表示する関数
# # ・購入したproduct_idが入っているリストを渡すと、nameとpriceとpriceの合計を表示する関数

# from xml.etree import ElementTree

# def mondai1(x):
#     for element in ElementTree.fromstring(x):
#         if 1500 <= int(element.find('price').text):
#             print(element.find('name').text, element.find('price').text)

# def mondai2(x, l):
#     p_sum = 0
#     for element in ElementTree.fromstring(x):
#         for i in l:
#             if int(element.get('id')) == i:
#                 print(element.find('name').text, element.find('price').text)
#                 p_sum += int(element.find('price').text)
#     print(p_sum)


# mondai1(xml)
# mondai2(xml, [20, 30])










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
#     # 個数の最大値
#     a = x//120
#     for i in itertools.permutations(range(1, a), 3):
#         if 120 * i[0] + 300 * i[1] + 440 * i[2] == x:
#             print('お釣り：0, 120円：{}, 300円：{}, 440円：{}'.format(i[0], i[1], i[2]))

# print(func(3000))
# print(func(3001))












# Q43
# ここでは、2n枚のカードがあったとき、そのうちn枚のカードをまとめて抜き出し、その他のカードの上に重ねる動作を繰り返します
# （バラバラに抜き出すのではなく、1つの塊で抜き出すことにします）。イメージとしては図13のようになります。
# これを繰り返して、最初の並びの逆順になるまで
# まで繰り返すことにします。例えば、n＝2のとき、4枚のカードを逆順にするには次のように4回の操作で実現できます
# ます（開始時のカードを上から順に1,2,3,4とします）。
# mondai
# n＝5のとき、10枚のカードを逆順にするために必要な最少の回数を答えてください。

# result = list(set(l1) - set(l2))
# print(result)

# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# xlist = list(range(1, 11))
# # print(list(xlist)[0:5])
# # print(list(xlist)[1:6])
# # print(list(xlist)[2:7])
# # print(list(xlist)[3:8])
# # print(list(xlist)[4:9])
# # print(list(xlist)[5:10])
# xlist = []
# for i, n in enumerate(range(5, 11)):
#     print(xlist[i:n] +  (list(set(xlist) - set(xlist[i:n]))))

# n = 5
# print(2*n)

# print(xlist)
# print([i for i in reversed(xlist)])


# n＝5のとき、10枚のカードを逆順にするために必要な最少の回数を答えてください。

# 2n


# 一つの日時リストを引数にとり、年の昇順、月の降順、日の昇順のリストを返却する関数を作成せよ
# 例)
# x = ['2017/01/02', '2001/01/01', '2017/01/01', '2018/01/01', '2017/02/01']
# => ['2001/01/01', '2017/02/01', '2017/01/01', '2017/01/02', '2018/01/01']

# import datetime

# def func(x):
#     dlist = [datetime.datetime.strptime(i, '%Y/%m/%d') for i in x]
#     y = [i.year for i in dlist]
#     yy = sorted(y)
#     print(yy)


#     # m = [i.month for i in dlist]
#     # mm = sorted(m, reverse=True)
#     # d = [i.day for i in dlist]
#     # dd = sorted(d)
#     # xlist = []
#     # for a, b, c in zip(yy, mm, dd):
#         # xlist.append('{}/{}/{}'.format(a, b, c))
#     # return xlist    
# print(func(['2017/01/02', '2001/01/01', '2017/01/01', '2018/01/01', '2017/02/01']))



# def func(x):    
#     shiki = ['+', '-', '*', '/']
#     for p in shiki:
#         for q in shiki:
#             for r in shiki:
#                 val = x[1] + p + x[4] + q + x[7] + r + x[10]
#                 # val = str(x)[1] + p + str(x)[4] + q + str(x)[7] + r + str(x)[10]
#                 if eval(val) == 10:
#                     return True
#                 else:
#                     return False
                    
# print(func([6, 4, 0, 0]))
# print(func([2, 0, 0, 5]))
# print(func([1, 1, 5, 0]))

# print(range(w_list[i], w_list[-1]))
# print([w_list[i] for i in range(i, -1)])
# a = [w_list[i] for i in range(i, 3+3)]
# print([w_list[i] for i in range(0, 3-1)])
# b = [w_list[i] for i in range(0, 3-1)]
# print(a+b)


# print(w_list[0], w_list[1])


# import time

# for _ in range(5):
#     print("Hello")
#         time.sleep(5)

# for i in ['hogehoge', 'hogehoge_campaign', 'hoge_campaign', 'aiueo']:
#     time.sleep(10)
# import csv
# import re

# def dup(key, pattern):
#     """
#     重複チェック
#     """
#     count = 0

#     for i in pattern:
#         if re.match(key, i):
#             count += 1

#             if count > 1:
#                 return True

#     return False


# def countlen(array):
#     """
#     最小文字数のカウント
#     """
#     cnt = 0

#     for i in array:
#         index = 0
#         check = i[index]

#         while dup(check, array):
#             index += 1
#             check += i[index]

#         print(check, " : ", i)
#         cnt += len(check)

#     return cnt

# # # def main():
# #     """
# #     CSV読み込み
# #     """
# csvfile = open('./q33.csv', 'r', encoding='utf-8')
# reader = csv.reader(csvfile)
# # print(reader)
# header = next(reader)  # ヘッダーを捨てる

# kaminoku, simonoku = [], []

# for row in reader:
#     kaminoku += [row[3]]
#     simonoku += [row[4]]

# print((kaminoku), (simonoku))
# print(countlen(kaminoku) + countlen(simonoku))

# 美しい？IPアドレス
# IPアドレスを2進数で表現したとき、「左右対称」になるものがいくるあるか調べ、
# その個数を答えてください。
# （2進数で表現するときは、先頭の0は除かないものとし、32文字で表現するものとする。）

"""
Q23
"""

# C = 10
# G = 24


# def blackjack(coin, game):
#     """
#     ブラックジャック
#     """
#     if coin <= 0:
#         return 0

#     if coin >= 1 and game >= 24:
#         return 1

#     cnt = 0
#     cnt += blackjack(coin + 1, game + 1)
#     cnt += blackjack(coin - 1, game + 1)

#     return cnt

# print(blackjack(10, 0))

# if __name__ == "__main__":
#     print("cnt =", blackjack(10, 0))

# def func(N):
#     # N = 100  # カード枚数
#     C = [False for i in range(N)]
#     # print(C)

#     # カードを裏返す
#     for i in range(1, N):
#         for j in range(i, N, i+1):
#             C[j] = not C[j]

#     # 結果表示
#     for i in range(0, N):
#         # 成立しなければ
#         if not C[i]:
#             print(str(i+1))

# func(100)

# IPV4の場合、IPアドレスは2進数で32bitの数値です。
# しかし、人間にはわかりにくいので、8bitずつ区切って「192.168.1.2」のように10進数で表現するのが一般的です。
# https://dev.sizebook.jp/gitbucket/ysonoki/blog/issues/6

# 10進数で0～9の10個の数字を「一度ずつ」使って表現されるIPアドレスを考える。
# （一般的に用いられるように、先頭の0は省略するものとする。
# つまり、「192.168.001.002」のように表現するのではなく、
# 「192.168.1.2」のように表現する。）

# 問
# IPアドレスを2進数で表現したとき、「左右対称」になるものがいくつあるか調べ、
# その個数を答えてください。
# （2進数で表現するときは先頭の0は除かないものとし、32文字で表現するものとする）
# 0~255で256通り

# p = pow(2, 16)
# cnt = 0
# for i in range(p):
#     # 2進数
#     bin_ip = "{0:016b}".format(i) + "{0:016b}".format(i)[::-1]
#     # 10進数
#     dec_ip = str(int(bin_ip[0:8], 2))
#     dec_ip += str(int(bin_ip[8:16], 2))
#     dec_ip += str(int(bin_ip[16:24], 2))
#     dec_ip += str(int(bin_ip[24:32], 2))

#     #10個の数字を一度ずつ 
#     if len(set(dec_ip)) == 10:
#         print(dec_ip, bin_ip)
#         cnt += 1

# print(cnt)

# def func(x, y):
#         return str(x) == str(y)[::-1]

# shiki = ['+', '-', '*', '/','']
# for num in range(1000,9999):
#     if "0" in str(num):
#         continue
#     for p in shiki:
#         for q in shiki:
#             for r in shiki:
#                 val = str(num)[0] + p + str(num)[1] + q + str(num)[2] + r + str(num)[3]
#                 # 必ず一つは演算子を入れる。
#                 if len(val) > 4:
#                     if func(num, eval(val)):
#                         print (val + "=" + str(eval(val)))



# num = 11

# while True:
#     if str(num) == str(num)[::-1] and
#      str(format(num, 'b')) == str(format(num, 'b'))[::-1] and
#      str(format(num, 'o')) == str(format(num, 'o'))[::-1]:
#         print(num)
#         break
#     num += 2

# def func(x):
#     return str(x) == str(x)[::-1]

# n = 11

# while True:
#     if func(n) and func(format(n, 'b')) and func(format(n, 'o')):
#         print(n)
#         break
#     n += 2

# def fib(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a + b
#     return b

# print(fib(30 + 1))
# i = 0
# while(True):
#     i += 1
#     if i == 31:
#         print(fib(i))
#         break


# from collections import Counter
# import itertools as it

# # 魔法陣を配列にセット
# magic = [1,14,14,4,11,7,6,9,8,10,10,5,13,2,3,15]
# xlist = []

# for i in range(len(magic)):
#     # 長さiのタプル列、ソートされた順で重複なし
#     for d in it.combinations(magic,i):
#         xlist.append(sum(d))
# counter = Counter(xlist)
# for num, cnt in counter.most_common():
#     print(num, cnt)
#     break
# print(count)

# magic_square = [1, 14, 14, 4, 11, 7, 6, 9, 8, 10, 10, 5, 13, 2, 3, 15]

# dic = {}
# dic[0] = 1

# for x in magic_square :
#     for i in sorted(dic,reverse=True) :
#         if ( i + x ) in dic :
#             dic[ i + x ] += dic [i]
#         else :
#             dic[ i + x ]  = dic [i]

# max_value = max(dic.values())
# keys = [ x[0] for x in dic.iteritems() if x[1] == max_value ]

# print('sum:'),
# for x in sorted(keys) :
#     print(x),
# print('count:',max_value)
