# coding: utf-8
#!/usr/bin/env python

l = ['[9], [1+1+11*111+11]', '[9], [1+1+11+11*111]', 
 '[9], [1+1+11+111*11]', '[9], [1+1+111*11+11]', 
 '[9], [1+11*111+1+11]', '[9], [1+11*111+11+1]', 
 '[9], [1+11+1+11*111]', '[9], [1+11+1+111*11]', 
 '[9], [1+11+11*111+1]', '[9], [1+11+111*11+1]', 
 '[9], [1+111*11+1+11]', '[9], [1+111*11+11+1]', 
 '[9], [11*111+1+1+11]', '[9], [11*111+1+11+1]', 
 '[9], [11*111+11+1+1]', '[9], [11+1+1+11*111]', 
 '[9], [11+1+1+111*11]', '[9], [11+1+11*111+1]', 
 '[9], [11+1+111*11+1]', '[9], [11+11*111+1+1]', 
 '[9], [11+111*11+1+1]', '[9], [111*11+1+1+11]', 
 '[9], [111*11+1+11+1]', '[9], [111*11+11+1+1]', 
 '[8], [33333/3/3/3]', 
 '[9], [9*99999/9/9/9]', '[9], [9/9*99999/9/9]', 
 '[9], [9/9/9*99999/9]', '[9], [9/9/9/9*99999]', 
 '[9], [9+99999/9/9-9]', '[9], [9-9+99999/9/9]', 
 '[9], [99999*9/9/9/9]', '[9], [99999/9*9/9/9]', 
 '[9], [99999/9/9*9/9]', '[9], [99999/9/9/9*9]', 
 '[9], [99999/9/9+9-9]', '[9], [99999/9/9-9+9]']


print(l.index(min(l)), min(l))









# 点(x, y) と距離 d が与えられた時に、
# 点(x, y) から距離 d 以下にある格子点の数を求めてください。
# ただし、x, y, d はすべて整数とする。

# (例)
# (x, y) = (1, 1) , d = 1 => 5




# サイコロは 1 から6 までの整数がそれぞれの面に書かれており、
# 向かい合う面に書かれた数の和はどれも 7 です。
# サイコロを使って次のようなゲームを行います。

# まず、サイコロを好きな面が上向きになるように置きます。
# その後、得点が x 点を超えるまで以下の操作を繰り返します。
# サイコロを手前、奥、左、右のどれかの方向に 90° だけ回転させ、
# 上を向いている面に書かれた数を得点として得る。

# x が与えられた時、
# 上のゲームで x 点以上獲得するために
# 必要な最小の操作の回数を求めてください。

# (例)
# x = 7 -> 2 回
# x = 149696127901 -> 27217477801 回

# def func(x):
#     amari = x % 11
#     sho  = x // 11
#     print(amari, sho)
#     if amari == 0:
#         print( sho*2 )
#     elif amari <= 6:
#         print( sho*2 + 1 )
#     else:
#         print( sho*2 + 2)

# print(func(1496))

# def func(x):
#     sho = x // 11
#     amari = x % 11
#     n = sho * 2
#     print(sho, amari)
#     if amari == 0:
#         return n
#     elif amari <= 6:
#         return n + 1
#     else:
#         return n + 2

# print(func(7))
# print(func(149696127901))

#     total = 0
#     # count = 0
#     # while total < tensu:
#     for i in range(0, 10000):
#         print(total, tensu)
#         if total < tensu:
#             if m == 1 or m == 6:
#                 total += 5
#                 m = 5
#             else:
#                 total += 6
#                 m = 6  
#             i += 1
#         else:
#             break    
#         return i

# # 149696127901
# print(func(3, 7))
# print(func(5, 149696))

# for i in range(10):
#     print(i)

# elapsed_time = time.time() - start
# print("elapsed_time:{0}".format(elapsed_time))

# def func(m, tensu):
#     total = 0
#     count = 0
#     while total < tensu:
#         print(total, tensu)
#         if m == 1 or m == 6:
#             total += 5
#             m = 5
#         else:
#             total += 6
#             m = 6
#         print(count)    
#         count += 1
#     return count

# print(func(3, 7))
# print(func(5, 100))






# 始まりの数, x 点
# print(func(6, 7))
# print(func(6, 1496))

# a = [False for i in range(100)]
# for m in range(2, 101):
#     p = m - 1
#     while p < 100:
#         # print(a, p)
#         # 反転
#         a[p] = not a[p]
#         p += m

# for i, x in enumerate(a):
#     if x == False:
#         print(i+1)
# def func(a, b, c, x):
#     for p in list(range(0, a+1)):
#         for q in list(range(0, b+1)):
#             for r in list(range(0, c+1)):
#                 print(p, q, r)
#                 if 100 * p + 50 * q + 10 * r == x:
#                     return True
#     return False

# print(func(5, 3, 1, 560))
# print(func(2, 3, 2, 130))
# print(func(3, 4, 4, 540))

# ある正方形があり、一辺の長さが 1cm の正方形のマス目で区切られています。この境界上を通って左上から右下まで最短距離で往復することを考えます。
# このとき、往路で通った道は、復路では通ることができないものとします。（ただし、交差点が重なること、クロスすることは ok とします。）
# 例えば、正方形の一辺の長さが 2cm の場合、 10 通りの経路があります。

# https://dev.sizebook.jp/gitbucket/kitamura/sonogym/blob/master/img/q31_figure.png

# 一辺が 6 cm の正方形の場合、最短経路がいくつあるか求めてください。




# 同じ場所を通らない掃除ロボットを考えます。このロボットは前後左右の4方向にのみ移動することができます。
# 例えば、3回移動する場合、最初に後ろに移動する経路は 9 パターンあります 。

# (https://dev.sizebook.jp/gitbucket/kitamura/sonogym/blob/master/img/q8_figure.png)
# 最初の移動方向は前後左右があるので、考えられる移動経路は全部で 9 x 4 = 36 通りあります。
# このロボットが12回移動するとき、考えられる移動経路のパターンが何通りあるかを求めてください。

# N = 12
# # 前後左右に移動
# ugoku = [[0,1],[0,-1],[1,0],[-1,0]]

# def move(x):

#     # 最初の位置を含んで、N+1個調べれば終了
#     if len(x) == N+1:
#         return 1
        
#     cnt = 0    
#     for d in ugoku:
#         # print(d)
#         next_pos = [x[-1][0] + d[0], x[-1][1] + d[1]]
#         # 探索済みでなければ移動させる
#         if not next_pos in x:
#             cnt += move(x + [next_pos])
#     return cnt

# print(move([[0,0]]))


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

# import csv
# import re

# # csvインポート & 出力
# # def main():
# csvfile = open('./q33.csv', 'r', encoding='utf-8')
# reader = csv.reader(csvfile)
# _ = next(reader)  # ヘッダーを捨てる

# kami = []
# shimo = []

# for row in reader:
#     # print(row)
#     kami += [row[3]]
#     shimo += [row[4]]
# print(kami)

# # 重複チェック
# count = 0
# xlist = []
# print(len(kami))
# for i in kami:
#     xlist.append(i[0])
# #　重複無しの単語
# print(set(xlist))


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
# print(dup(kami))

# print(countlen(kaminoku) + countlen(simonoku))

# サイコロは 1 から6 までの整数がそれぞれの面に書かれており、向かい合う面に書かれた数の和はどれも 7 です。
# サイコロを使って次のようなゲームを行います。

# まず、サイコロを好きな面が上向きになるように置きます。
# その後、得点が x 点を超えるまで以下の操作を繰り返します。
# サイコロを手前、奥、左、右のどれかの方向に 90° だけ回転させ、
# 上を向いている面に書かれた数を得点として得る。

# x が与えられた時、
# 上のゲームで x 点以上獲得するために必要な最小の操作の回数を求めてください。

# (例)
# x = 7 -> 2 回
# x = 149696127901 -> 27217477801 回

# def func(m, tensu):
#     s_list = list(range(1, 7))
#     total = 0
#     count = 0
#     while total < tensu:
#         p = 7 - m
#         s_list.remove(m)
#         s_list.remove(p)
#         m = max(s_list)
#         total += m
#         count += 1
#         s_list.append(m)
#         s_list.append(p)
#     return count

# # 始まりの数、最大の点数
# print(func(6, 7))
# print(func(6, 149))
# print(func(6, 149696127901))



# 最初に選ぶ好きな面
# N = 2

# X点以上獲得
# X = 7






# 同じ場所を通らない掃除ロボットを考えます。
# このロボットは前後左右の4方向にのみ移動することができます。
# 例えば、3回移動する場合、最初に後ろに移動する経路は 9 パターンあります 。
# (https://dev.sizebook.jp/gitbucket/kitamura/sonogym/blob/master/img/q8_figure.png)
# 最初の移動方向は前後左右があるので、考えられる移動経路は全部で 9 x 4 = 36 通りあります。
# このロボットが12 回移動するとき、考えられる移動経路のパターンが何通りあるかを求めてください。


# N = 12
# SHIFT = [[0,1],[0,-1],[1,0],[-1,0]]

# def move(log):
    
#     if len(log) == N+1:
#         return 1
        
#     cnt = 0
    
#     for d in SHIFT:
#         next_pos = [log[-1][0]+d[0], log[-1][1]+d[1]]
#         if not next_pos in log:
#             cnt += move(log + [next_pos])
#     return cnt

# print(move([[0,0]]))





# 1～100までのバングが書かれた100枚のカードが順番に並べられています。
# 最初、すべてのカードは裏返しの状態で置かれています。
# ある人が2番のカードから、1枚おきにカードを裏返していきます。
# すると、2,4,6・・・,100番のカードが表を向くようになります。
# 次に、別の人が、3番のカードを2枚おきにカードを裏返していきます。
# （裏向きのカードは表を向き、表を向いているカードは裏返されます。）
# また、別の人が4番のカードから3枚おきにカードを裏返していきます。
# このように、n番目のカードからn-1枚おきにカードを裏返す操作を、
# どのカードの向きも変わらなくなるまで続けたとします。
# カードの向きが変わらなくなったとき、
# 裏向きになっているカードの番号をすべて求めてください。

# a = [False for i in range(100)]
# for m in range(2, 101):
#     p = m - 1
#     while p < 100:
#         # print(a, p)
#         # 反転
#         a[p] = not a[p]
#         p += m

# for i, x in enumerate(a):
#     if x == False:
#         print(i+1)


# 一つのリストxが与えられた時、0の要素ごとにくぎって総和を返す関数を作成せよ
# 例1:[1, 0, 2, 3, 0, 4, 8] => [1, 5, 12] # (1, 2 + 3, 4 + 8)
# 例2:[0, 9, 10, 0, 3, 0, 4, 8] => [0, 19, 3, 12]

# list = [1, 2, 3, 4, 5]
# result = list[0]
# for x in list[1:]:
#     print(x)
#     result = result + x
# print(result)


# def func(x):
#     p = []
#     m = []
#     for i in x:
#         if i != 0:
#             p.append(i)
#         else:
#             m.append(sum(p))
#             p = []
#     m.append(sum(p))
#     return m

# print(func([1, 0, 2, 3, 0, 4, 8]))
# print(func([0, 9, 10, 0, 3, 0, 4, 8]))


# def func(x):
#     xlist = []
#     y = []
#     for i in x:
#         if i == 0:
#             xlist.append(sum(y))
#             y = []
#             print('a')
#         else:
#             y.append(i)
#             print('b')
#     return xlist

# print(func([1, 0, 2, 3, 0, 4, 8]))
# print(func([0, 9, 10, 0, 3, 0, 4, 8]))

# print([1, 0, 2, 3, 0, 4, 8].count(0))

# cnt = 0
# while cnt < [1, 0, 2, 3, 0, 4, 8].count(0):
#     cnt += 1

# def convert(num_list):
#     result = []
#     cont = 0
#     for num in num_list:
#         print(len(result))
#         if len(result) != cont + 1:
#             result.append(0)
#         result[cont] += num
#         if num == 0:
#             cont += 1
#     return result
# print(convert([1, 0, 2, 3, 0, 4, 8]))
# print(convert([0, 9, 10, 0, 3, 0, 4, 8]))

# d = [0, 9, 10, 0, 3, 0, 4, 8]
# print(func(d))



# sum = 0
# xlist = []
# klist = []
# for i, p in enumerate(ylist):
#     if p == 0:
#         pass
#     else:
#         klist.append(p)
#         xlist.append(sum(klist))
#     print(xlist)
# print('a')





# print([i+1 for i, x in enumerate(N) if x == False])

# xlist = []
# for i in range(100):
#     if N[i] == False:
#         xlist.append(i+1)
# print(xlist)


#1, 4, 9, 16, 25, 36, 49, 64, 81, 100

# C = 100
# N = ['ura'] * 100
# for i in range(1, 101):
#     print(i)
#     j = i - 1
#     while j < 100:
#         print(N[j])
#         N[j] = not N[j]
#         print(j)
#         j += i

# print([k + 1 for k in range(100) if N[k] == False])






# print([k + 1 for k in range(100) if xlist == 'ura'])

# カードを裏返す
# for i in range(1, N):
    # for j in range(i, N, i+1):
        # print(j)
#         # print(C[j])
#         C[j] = not C[j]
#         # print(C[j])

# # 結果表示
# for i in range(0, N):
#     if not C[i]:
#         print(str(i+1))

# N = [True]*100
# for i in range(1, 101):
#     j = i - 1
#     while j < 100:
#         N[j] = not N[j]
#         j += i

# print([k + 1 for k in range(100) if N[k] == False])
# #1, 4, 9, 16, 25, 36, 49, 64, 81, 100








# print(count_line(0, 0, 20, 10))
# import itertools

# p = ['B']*20 + ['G']*10

# count = 0
# for i in set(itertools.permutations(p, 30)):
#     # 2人+28人 ~28人+2人で区切る
#     for n in range (2, 29):
#         mae = i[:n]
#         ato = i[n:]
#         if mae.count('B') != mae.count('G') or ato.count('B') != ato.count('G'):
#             count += 1
# print(count)

# 学生にとっては勉強以上に大事なクラブ活動。
# あなたは新しく設置される学校の 校長に就任することが決まりました。
# スポーツをしたい150人の学生に、どんなクラ ブ活動を準備するか考えています。
# 各クラブに必要なグラウンドの 各クラブに必要な土地と想定部員数 広さを調べてみたところ、[表1]の ようになりました
# 各クラブに所属する部員数との関係を考え、土地を確保する必要があります。

# [表1]
# クラブ | 必要な広さ | 想定部員数
# 野球 | 11000m2 | 40人
# サッカー | 8000m2 | 30人
# バレーボール | 400m2 | 24人
# バスケットボール | 800m | 20人
# テニス | 900m2 | 14人
# 陸上 | 1800m2 | 16人
# ハンドボール | 1000m2 | 15人
# ラグビー | 7000m | 40人
# 卓球 | 100m2 | 10人
# バドミントン | 300m2 | 12人

# 問題
# 150人を超えないようにクラブ活動を選び、必要な土地の面積を最大にします。その 面積の最大値を求めてください。

# 男性２０人、女性１０人が到着した場合、
# どこで区切っても２つのグループのいずれも男女の数が異なってしまうような到着順が何通りあるかを求めてください。

# buin = [40, 30, 24, 20, 14, 16, 15, 40, 10, 12]
# menseki = [11000, 8000, 400, 800, 900, 1800, 1000, 7000, 100, 300]
# mb = [i for i in zip(menseki, buin)]

# import itertools

# xlist = []
# for i in range(1, len(mb)+1):
#     for j in itertools.combinations(mb, i):
#         print(list(map(lambda x: x[0], j)))
#         menseki = sum(map(lambda x: x[0], j))
#         print(menseki)
#         ninzu = sum(map(lambda x: x[1], j))

#         if ninzu <= 150:
#             xlist.append(menseki)
# print(max(xlist))

# import itertools

# p = ['B']*4 + ['G']*2

# count = 0
# for i in itertools.permutations(p, 6):
#     # print(i)
# #     # 2人+28人 ~28人+2人で区切る
#     for n in range (2, 5):
#         mae = i[:n]
#         ato = i[n:]
#         if mae.count('B') == mae.count('G') or ato.count('B') == ato.count('G'):
#             print(mae, ato)
#             continue
#         else:
#             count += 1
# print(count)




# class Item:
#     def __init__(self,w=0,p=0):
#         self.weight=w
#         self.price=p

# items = [ Item(40,11000), Item(30,8000), Item(24,400),
#           Item(20,800), Item(14,900), Item(16,1800),
#           Item(15,1000), Item(40,7000), Item(10,100), Item(12,300) ]

# def knapsack(i, w):
#     print(i, w)
#     if i>=len(items):
#         return 0
#     elif  w - items[i].weight < 0.0:
#         return knapsack(i+1, w)
#     else:
#         p1 = knapsack(i+1, w)
#         #                      i番目の重量　　　　　i番目の品の価値
#         p2 = knapsack(i+1, w - items[i].weight) + items[i].price
#         if p1>p2:
#             return p1
#         else:
#             return p2

# p = knapsack(0, 150)
# print("TOTAL PRICE=",p)


# 正の整数のリストの要素と＋、✕をもちいて計算できる最大値を出力して下さい。
# (例)
# [1, 2, 3, 4] -> (1 + 2) * 3 * 4 = 36
# [2, 3, 4] -> 2 * 3 * 4 = 24

# あるイベント会場に入場待ちの列が一列にできています。
# ある位置で区切って２つのグループに分けたいと考えています。
# ２つのグループのいずれかは男女の人数が均等になるように分けたいのですが、
# 到着した順番が悪い場合、どこで区切っても２つのグループで男女の数が異なってしまいます。

# 例えば、男女３人ずつが到着している場合、「男男女男女女」 の順番で
# 到着するとどこで区切っても男女の数が異なってしまいます。
# https://dev.sizebook.jp/gitbucket/kitamura/sonogym/blob/master/img/q9_figure.png

# 男性２０人、女性１０人が到着した場合、
# どこで区切っても２つのグループのいずれも男女の数が異なってしまうような到着順が何通りあるかを求めてください。

# 模範解答では、男女の順列の問題を2次元の表を使って考えている。
# 男性が来たら右へ、女性が来たら上へ移動する経路を考える。
# 男女が同数になる場所をカウントしないように、経路が何通りあるかを算出する。

# ホールケーキを切り分けるとき、ケーキに乗っているいちごの数がすべて異なるような切り方を考える。
# ここでは、N 個に切り分けるときには 「1 ~ N 個のいちご (合計 N (N + 1) / 2 個)」 がそれぞれに乗っているようにする。
# ただし、隣り合う２つのケーキに乗っているいちごの数の和が、いずれも平方数になるように切らなければならないという条件を追加する。
# このような条件を満たすような切り方ができる最小の N (> 1) を求めてください。

# def path(b, g):
#     if b == g:
#         return 0
#     elif b - g == 9:
#         return path(b-1, g)
#     elif b == 0 or g == 0:
#         return 1
#     else:
#         return path(b-1, g) + path(b, g-1)

# print(path(19,10))

# p = ['B']*20 + ['G']*10

# count = 0
# for i in itertools.permutations(p, 30):
#     # 2人+28人 ~28人+2人で区切る
#     for n in range (2, 29):
#         mae = i[:n]
#         ato = i[n:]
#         if mae.count('B') != mae.count('G') and ato.count('B') != ato.count('G'):
#             count += 1
# print(count)

# import itertools

# def func(N, M):
#     for i in itertools.product(range(0, N), repeat=3):
#       print(i)
        # if i[0]*2 + i[1]*3 + i[2]*4 == M and i[0] + i[1] + i[2] == N:
            # return i
    # return (-1, -1, -1)  

# import itertools

# p = ['B']*2 + ['G']*2

# count = 0
# for i in itertools.permutations(p, 4):
#     print(i)
    # 2人+28人 ~28人+2人で区切る
#     for n in range (2, 29):
#         mae = i[:n]
#         ato = i[n:]
#         if mae.count('B') != mae.count('G') and ato.count('B') != ato.count('G'):
#             count += 1
# print(count)
    # 2人+28人 ~28人+2人で区切る
#     for n in range (2, 29):
#         mae = i[:n]
#         ato = i[n:]
#         if mae.count('B') != mae.count('G') and ato.count('B') != ato.count('G'):
#             count += 1
# print(count)
# (例)
# N = 3, M = 9 -> "1, 1, 1"
# N = 10, M = 41 -> "-1, -1, -1"
# N = 1500, M = 5000 -> "200, 600, 700"

# def func(N, M):
#     for i in range(0, N):
#         for j in range(0, N):
#             for k in range(0, N):
#                 print(i, j, k)
#                 if 2 * i + 3 * j + 4 * k == M and i + j + k == N:
#                     print(i, j, k)
#     return -1, -1, -1

# print(func(3, 9))
# print(func(10, 41))
# print(func(1500, 5000))


# import itertools

# p = ['B']*20 + ['G']*10

# count = 0
# for i in itertools.permutations(p, 30):
#     # 2人+28人 ~28人+2人で区切る
#     for n in range (2, 29):
#         mae = i[:n]
#         ato = i[n:]
#         if mae.count('B') != mae.count('G') and ato.count('B') != ato.count('G'):
#             count += 1
# print(count)

# p = ['B']*6 + ['G']*4

# for i in range(2, 29):
#   print(i)
# # print(p[:2])
# # print(p[2:])
# print(p[8:])
# print(p[:8])


# for q in set(itertools.permutations(p,r)):
#     for n in range (2, 28):
#         former = q[:n]
#         latter = q[n:]
#         if former.count('M') != former.count('F') or latter.count('M') != latter.count('F'):
#             cnt += 1
# print cnt


# def path(b, g):
#     if b == g:
#         return 0
#     elif b - g == 9:
#         return path(b-1, g)
#     elif b == 0 or g == 0:
#         return 1
#     else:
#         return path(b-1, g) + path(b, g-1)

# print path(19,10)




# A[0][0] = 1

# for i in range(B):
#     for j in range(G):
#         if (i != j) and (B - i != G - j):
#             if i > 0:
#                 A[i][j] += A[i-1][j]
#             if j > 0:
#                 A[i][j] += A[i][j-1]

# print(A[B - 1][G - 2] + A[B - 2][G - 1])

# import itertools
# from itertools import zip_longest

# def func(x):
#     s = ['+', '*']
#     for i in itertools.product(s, repeat=len(x)-1):
#         xlist = []
#         ylist = []
#         for a, b in zip_longest(x, list(i)):
#             xlist.append('{}, {}'.format(a, b))
#         a = [s.replace('None', '') for s in xlist]
#         b = [s.replace(', ', '') for s in a]
#         c = ylist.append(eval(''.join(b)))
#     print(ylist)    

# # func([1, 2, 3, 4])
# print(func([2, 3, 4]))




# # 国士無双
# # a,b,c,d,e,f,g,h,i,j,k,l,m をそれぞれ0文字以上用いた13文字の文字列が与えられた時に、
# # その文字列に一文字加えると a ~ m のうちどれか一つの文字を2つ、それ以外の文字を1つずつ含むようにできるかどうかを判別し、
# # できる場合にはその文字を全て出力してください

# # (例)
# # abcdfghijklmm -> e
# # abcdefghijklm -> a, b, c, d, e, f, g, h, i, j, k, l, m
# # abbccdefghijk -> false

# xlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
#          'h', 'i', 'j', 'k', 'l', 'm', 'n']

# def func(x):
#   print(set(x))


# # print(func('abcdfghijklmm'))
# # print(func('abcdefghijklm'))
# print(func('abbccdefghijk'))

# ある街には大人、老人、赤ちゃんが合わせて N 人います。
# 大人の足は 2 本、老人の足は 3 本、赤ちゃんの足は 4 本とします。
# この街の足の数の合計が M 本のとき、
# 人数の組み合わせとしてあり得るものを 1 つ、
# "大人の人数、老人の人数、赤ちゃんの人数" の形で出力してください。
# ただし、そのような組み合わせが存在しない場合は "-1 -1 -1" と出力してください。

# (例)
# N = 3, M = 9 -> "1, 1, 1"
# N = 10, M = 41 -> "-1, -1, -1"
# N = 1500, M = 5000 -> "200, 600, 700"

# print(int(700/2))

# def func(N, M):
#     for i in range(0, N):
#         for j in range(0, N):
#             for k in range(0, N):
#                 if 2 * i + 3 * j + 4 * k == M and i + j + k == N:
#                     return i, j, k    
#     return -1, -1, -1

# print(func(3, 9))
# print(func(10, 41))
# print(func(1500, 5000))




# rslt = []
# max_val = 10000
# s = 0
# for m in range(1, max_val+1):
#     n = y(m)
#     if m >= n:
#         continue
#     if y(n) == m:
#         rslt.append((n, m))
#         s += 1
#         if s == 5:
#             break
# print(rslt)


# (例)
# (220, 284) 
# -> 220 の自分自身を除いた約数は 1, 2, 4, 5, 10, 11, 22, 44, 55, 110 で和は 284、
# 284 の自分自身を除いた約数は 1, 2, 4, 71, 142 で和は 220 なので、
# (220, 284) は友愛数である。
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
#         print(n, m)
#         rslt.append((n, m))
#         s += 1
#         if s == 5:
#             break
# print(rslt)