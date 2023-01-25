# # coding: utf-8
#!/usr/bin/env python

from datetime import datetime, timedelta

dt = datetime(2018, 3, 26, 17, 48, 59)
aa = 365 * 24 * 60 * 60
for i in range(aa):
    dt += timedelta(seconds=1)
    m = dt.strftime('%m%d%H%M%S')
    # print(m)
    if len(set(list(m))) == 10:
        print(m)
        # b = datetime.strptime(m, '%m%d%H%M%S')
        # print(b.strftime('%m%d%H%M%S'))

# (例)
# [1, 2, 3, 4] -> (1 + 2) * 3 * 4 = 36
# [2, 3, 4] -> 2 * 3 * 4 = 24

# print((5 + 3) * 4)

# import itertools

# def func(x):
#     shiki = ['+', '-', '*', '/']
#     for i in itertools.product(shiki, repeat=3):
#         # print(i[0], i[1], i[2])
#         val = str(x)[1] + i[0] + str(x)[4] + i[1] + str(x)[7] + i[2] + str(x)[10]
#         try:
#             if eval(val) == 10:
#                 return True
#         except ZeroDivisionError:
#             pass
#         else:
#             continue
#     return False

# print(func([5, 2, 0, 0])) # True
# print(func([6, 4, 0, 0])) # True
# print(func([2, 0, 0, 5])) # False
# print(func([2, 0, 5, 0])) # False
# print(func([2, 5, 0, 0])) # True
# print(func([1, 1, 5, 0])) # False

    #             # print(val)
    #             # while True:
    #             try:
    #                 # print(eval(val))
    #                 if eval(val) == 10:
    #                 	return True
    #             except ZeroDivisionError:
    #             	# print('aiueo')
    #                 pass
    #             else:
    #                 continue
    #                 return False


                # xlist.append(val)
    # print(xlist)
    # while True:
        # for i in xlist:
            # try:
                # if eval(i) == 10:
                	# print(i)
                    # return True
                # else:
                    # continue
            # except ZeroDivisionError:
            	# continue
                # print("ZeroDivisionError")
            # else:
                # return False
    # finally:
    #     print(eval(i))



                # try:
                #     print(eval(val))
                #     if eval(val) == 10:
                #         return True
                #     else:
                #         return False	
                # except ZeroDivisionError:
                #     print("ZeroDivisionError")
                # print(val_list)
                # if eval(val) == 10:
                    # return True
                # elif eval(val) != 10:
                    # continue
                # else:
                    # return False


# print(func([2, 0, 0, 5]))
# print(func([2, 0, 5, 0]))
# print(func([2, 5, 0, 0]))
# print(func([1, 1, 5, 0]))



# 1~4のうちの整数が一つ与えられた時、その整数が左上になるような数独を完成させてください。
# ただし、数独は 1 ~ 4 の数字を用いて、4 x 4 のサイズとします。
# (各行、列では、1~4の数字が一回ずつ使用され、全体を4分割した 2 x 2 のブロック内でも1~4の数字が一回ずつ使用されているものとします)

# (例)
# 1 ->
# [[1, 2, 3, 4],
# [3, 4, 1, 2],
# [2, 3, 4, 1],
# [4, 1, 2, 3]]


# import itertools

# x_list = [p for p in range(1, 5)]

# print(x_list)

# print(list(itertools.permutations(x_list)))

# narabikae_list = list(itertools.permutations(x_list))
# print(narabikae_list)

# for i in narabikae_list:
#     print(i)
#     # print(i, i[0], i[1], i[-2], i[-1])
#     if i[0] == 1:
#         print('1', i)
#     if i[1] == 2:
#         print('2', i)
#     # elif i[2] == 3:
        # print('3', i)
    # elif i[3] == 4:
        # print('4', i)
    # else:
        # print('p')

# for i in itertools.permutations(x_list):
#     print(i)
#     if i[0] == 1:
#         print('1', i)
#     elif i[1] == 2:
#         print('2', i)
#     elif i[2] == 3:
#         print('3', i)
#     elif i[3] == 4:
#         print('4', i)














# str型、list型の引数をもち、str型引数をしりとりの開始文字とし、
# それに続く文字をlist型引数から取得しlistで返却する関数を作成せよ。
# 例）
# s = りんご, 
# l = ['だるま','らくだ','まり','ごりら'] => ['りんご','ごりら','らくだ','だるま','まり']

# upper_words = [v.upper() for v in words]
# for word in upper_words:
#     pos = upper_words.index(word)
#     arg_words = upper_words[:]
#     arg_words.pop(pos)
# 下記のしりとり開始文字とリスト型のデータを引数にもった関数でしりとりを行いlist型で返却する関数
# 解答パターンは一通りとする
# 例) 開始文字:こおり
# リスト:['ラッパ', [['ゴリラ', 'ルビー']], ['パイナップル', [['りんご']]]] => ['こおり', 'りんご'', 'ゴリラ', 'ラッパ', 'パイナップル', 'ルビー']


# # s = 'りんご'
# s = 'こおり'
# l = ['ラッパ', [['ゴリラ', 'ルビー']], ['パイナップル', [['りんご']]]]
# # l = ['だるま','らくだ','まり','ごりら']

# def func(s, l):
#     xlist = []
#     while len(l) > 0:
#         for i in l:
#             if i[0] == s[-1]:
#                 xlist.append(i)
#                 l.remove(i)
#                 s = i
#                 break
#     return xlist

# print(func(s, l))

# import jaconv

# def siri(s, l):
#     res=[]
#     while len(l) > 0:
#         for i in l:
#             if jaconv.hira2kata(i[0]) == jaconv.hira2kata(s[-1:]):
#                 # print(s[-1:])
#                 res.append(i)
#                 l.remove(i)
#                 s = i
#                 break
#     return res

# s = "りんご"
# l = ['だるま','らくだ','まり','ごりら']
# a = siri(s, l)
# print(a)
# upper_words = [v.upper() for v in l]

# print(upper_words)

# Q14 W杯出場国しりとり
# サッカーファンにとって、FIFAワールドカップは4年に一度の大イベントです。
# ここでは、2014年の大会の出場国でしりとりをしてみましょう。
# ただし、使うのは日本語ではなく、アルファベットです
# (大文字と小文字は同じものとして扱うこととします)。

# words = ['Brazil', 'Cameroon', 'Chile', 'Greece', 'Uruguay', 'Italy', 'France', 
# 'Bosnia and Herzegovina', 'Germany', 'USA', 'Russia', 'Croatia', 'Spain', 'Australia', 
# 'Cote d’lvoire', 'Costa Rica', 'Switzerland', 'Honduras', 'Iran', 'Portugal', 'Belgium', 
# 'Korea Republic', 'Mexico', 'Netherlands', 'Colombia', 
# 'Japan', 'Englan', 'Ecuador', 'Argentina', 'Nigeria', 'Ghana', 'Algeria']

# longst_chain = []

# # def chain(word: str, current_chain: list, usables: list):
# def chain(word, current_chain, usables):
#     global longst_chain
#     current_chain.append(word)
#     print(f'Start: {current_chain[0]}, List: {current_chain}')
#     #print(f'  Usables: {usables}')
#     #input()

#     if len(current_chain) > len(longst_chain):
#         longst_chain = current_chain[:]

#     for next_word in usables:
#         if word[-1] == next_word[0]:
#             pos = usables.index(next_word)
#             # すべての要素を指定
#             arg_words = usables[:]
#             # 除外
#             arg_words.pop(pos)
#             print(pos)
#             chain(next_word, current_chain[:], arg_words)

# lower_words = [v.lower() for v in words]
# for word in lower_words:
#     pos = lower_words.index(word)
#     arg_words = lower_words[:]
#     arg_words.pop(pos)
#     chain(word, [], arg_words)
# print(f'Length: {len(longst_chain)}, List: {longst_chain}')







# xlist = []
# for i in country:
#     # zenbu saisyo saigo
#     print(i.lower()), print(i.lower()[0]), print(i.lower()[-1])
#     if i.lower()[0] == i.lower()[-1]:
#         print(i)
#         xlist.append(i)
# print(xlist)


# Chile
# Greece
# Uruguay
# Italy
# France
# Bosnia and Herzegovina
# Germany
# USA
# Russia
# Croatia
# Spain
# Australia
# Cote d’lvoire
# Costa Rica
# Switzerland
# Honduras
# Iran
# Portugal
# Belgium
# Korea Republic
# Mexico
# Netherlands
# Colombia
# Japan
# Englan
# Ecuador
# Argentina
# Nigeria
# Ghana
# Algeria



# 美しい？IPアドレス
# 上記のようなIPアドレスを2進数で表現したとき、
# 左右対称になるものがいくつあるかをしらべ、その個数を答えてください。
# つまり、「192.168.001.002」のように表現するのではなく、
# 「192.168.1.2」のように表現する。）
# 上記のようなIPアドレスを2進数で表現したとき、左右対称になるものがいくつあるかをしらべ、その個数を答えてください。
# 2進数で表現するときは先頭の0は除かないもの年、32文字で表現するものとします。

# ip = 1XX.2XX.XXX.XXX

# "*"と""のみを挿入するようにした（op = ['*','']）。
# これで組み合わせの数としては53通りから23通りに減るので処理速度は圧倒的に向上する。
# 0絡みの除外をうまくやる方法が思いつかなかったので、
# いっそのこと0を含む数字は全てスキップするようなプログラムにした（if "0" in str(num): continue）。
# 少なくとも一つは"*"が入るようにした（if len(val) > 4:）。
# 気づき・反省点
# Q01もそうだったが、くそまじめに全ての条件を検討するのではなく、
# 除外可能な条件は最初から除外することで実行速度が上がる。
# 0絡みの除外については、今後の学習課題としたい。

# 四則演算
# 出来上がった式を計算した結果、「元の数の桁を逆から並べた数字」と同じになるものを考える。
# 100から999の場合、以下の３つがあります。
# 351 → 3×51=153
# 621 → 6×21=126
# 886 → 8×86=688

# 1000～9999のうち、上記の条件を満たす数を求めてください。

# Q36「0」と「7」の回文数
# 任意の正の整数nについて、「0と7の数字のみ」で構成されるnの正の倍数が存在 することが知られています。
# 例)
# n=2のとき 2×35 = 70
# n=3のとき 3×2359 = 7077
# n=4のとき 4×175=700
# n=5のとき 5×14=70
# n=6のとき 6×1295 = 7770

# さて，問題自体は簡単だが，問題文の文意を読み取るのが難しい（ちょいちょいよく分からない）
# この場合，「0と7の数字のみ」というのは，「0と7」が含まれている事がマスト（and）なのか，
# それともいずれか（or）なのかよく分からない．また，探索範囲の決定条件がよく分からない．
# 等式n x m = 回文数を満たさないと考えられるmの探索範囲の打ち切り条件ってなんだろう．
# 取り敢えず，適当な範囲で探索し（10桁まで），「0と7を含む場合」と「いずれかを含む場合」で考えてみる．

# 問題
# Q36「0」と「7」の回文数
# 1~50までのnについて上記の条件を満たすものを、例に挙げた「13」以外ですべて求めてください。

# 例に挙げられている数字を7で割ると，
# 「10, 1011, 100, 10, 1110,…」となる
# つまり，バイナリから0/7の回文数のリストを作っておいて
# それを正の整数nで割って割り切れれば良い．
# n = []
# for i in range(1, 51):
#     if i % 2 > 0 or i % 5 > 0:
#         n.append(i)

# ans = []
# k = 1

# while len(n) > 0:
#     x = int(str(format(k, 'b'))) * 7
#     if '0' in str(x):
#         for i in n:
#             if x % i == 0:
#                 if str(x) == str(x)[::-1] and i != 13:
#                     ans.append(i)
#                 n.remove(i)
#     k +=1

# print(ans)


# def func():
#     xlist = []
#     # 奇数
#     for i in range(1, 1000, 2):
#         if i % 5 == 0:
#             continue
#         xlist.append(7*int(bin(i)[2:]))

#     result1, result2 = [], []
#     for i in range(1, 51, 2):
#         if i % 5 and i == 13:
#             continue
#         for x in xlist:
#             if x % i == 0:
#                 s = str(x)
#                 # 77707 70777
#                 if s == s[::-1]:
#                     result2.append(i)
#                 if '0' in s:
#                     result1.append(i)
#             break
   
#     return result1, result2
 
 
# print(func())
# 0と7が両方ある場合 result1
# ０を含まない可能性も考える場合 result2


# パーフェクトシャッフル


# def func():
#   cnt = 1 # n=1
#   for i in range(2, 101):
#     if 2**(2*(i-1)) % (2*i - 1) == 1:
#       cnt += 1
#   return cnt
 
 
# print(func())

# def func(x, y):
#         return str(x) == str(y)[::-1]

# op = ['*','']
# for num in range(1000,9999):
#     if "0" in str(num):
#         continue
#     for i in op:
#         for j in op:
#             for k in op:
#                 val = str(num)[0] + i + str(num)[1] + j +str(num)[2] + k + str(num)[3]
#                 if len(val) > 4:
#                     if func(num, eval(val)):
#                         print (val + "=" + str(eval(val)))




# IPアドレス
# 10進数で0~9の10個の数字を1度ずつ使って表現されるIPアドレスを考える。
# （一般的に用いられるように、先頭の0は省略する。
# つまり、「192.168.001.002」のように表現するのではなく、「192.168.1.2」のように表現する。）
# 上記のようなIPアドレスを2進数で表現したとき、左右対称になるものがいくつあるかをしらべ、その個数を答えてください。
# 2進数で表現するときは先頭の0は除かないもの年、32文字で表現するものとします。

# ip = 


# 1つの数字で作る1234
# 1234を1つの数字だけでできるだけ少ない個数で表現するとき、
# 最も少ない個数で表現できる数字を求め、その式をすべて答えてください。

# N = [True]*100
# for i in range(1, 101):
#     j = i - 1
#     while j < 100:
#         N[j] = not N[j]
#         j += i

# print([k + 1 for k in range(100) if N[k] == False])

# op = ['+', '-', '*', '/', '']
# found = False
# leng = 1
# while(True):
# 	permutations(leng):








# 絡まない糸電話

# 16人の子供達がいた場合、作ることができるペアが何通りあるかを求めてください。

# # 

# n = 16
# pair = [0] * (n//2 + 1)
# pair[0] = 1

# for i in range(1, n//2+1):
#     pair[i] = 0
#     for j in range(i):
#         pair[i] += pair[j] * pair[i-j-1]

# print(pair[n//2])

# 男子が来るのは、最後が男子でも女子でもよい。
# 女子がくるのは、最後が男子の場合
# 男子が最後になるのは、一つ前の数と等しい。
# 女子が最後になるのは、一つ前が男子の場合。（２つ前の数と等しい。）
# 求める数＝1つ前の数+2つ前の数

# まずは男性20名、女性10名の並び替えの組み合わせを全て吐きだす。
# 最初の2名のところで区切るところから初めて、28名で区切るところまで全ての場合を検証して、
# 男女の数が等しくならない組み合わせを数えあげて行く。
# # わたしのオリジナル解答
# import itertools

# p = ['M','M','M','M','M','M','M','M','M','M','M','M','M','M','M','M','M','M','M','M',
# 'F','F','F','F','F','F','F','F','F','F']

# r = 7
# cnt = 0
# for q in set(itertools.permutations(p,r)):
#     print(q)
#     for n in range (2, 28):
#         f = q[:n]
#         l = q[n:]
#         if f.count('M') != f.count('F') or l.count('M') != l.count('F'):
#             cnt += 1
# print(cnt)


# def fib(value):
#     f0 = 0
#     f1 = 1
#     while value > f1:
# 	    f2 = f0 + f1
# 	    f0 = f1
# 	    f1 = f2
#     return (f0, f1)

# print(fib(5))
# print(fib(100))

# European = [0,32,15,19,4,21,2,25,17,34,6,27,13,36,11,30,8,23,10,5,24,16,33,1,20,14,31,9,22,18,29,7,28,12,35,3,26]
# American = [0,28,9,26,30,11,7,20,32,17,5,22,34,15,3,24,36,13,1,00,27,10,25,29,12,8,19,31,18,6,21,33,16,4,23,35,14,2]

# def Sum_Max(roulette, n):
#     Max_sum = 0
#     for i in range(0,len(roulette)):
#         Sum = 0
#         for s in range(i, i + n):
#             if s >= len(roulette):
#                 s -= len(roulette)
#             Sum += roulette[s]
#         if Max_sum < Sum:
#             Max_sum = Sum
#     return Max_sum

# cnt = 0
# for n in range(2,36):
#     if Sum_Max(European, n) < Sum_Max(American, n):
#         cnt += 1
# print cnt


# European_lists = [0,32,15,19,4,21,2,25,17,34,6,27,13,
# 36,11,30,8,23,10,5,24,16,33,1,20,14,31,9,22,18,29,7,28,12,35,3,26]

# American_lists = [0,28,9,26,30,11,7,20,32,17,5,22,34,15,3,24,36,13,
# 1,00,27,10,25,29,12,8,19,31,18,6,21,33,16,4,23,35,14,2]

# def sum_max(lists, n):
#     max_sum = 0
#     for i in range(len(lists)):
#         SUM = 0
#         for p in range(i, i+n):
#             if p >= len(lists):
#                 p -= len(lists)
#             SUM += lists[p]
#         if max_sum < SUM:
#             max_sum = SUM
#     return max_sum

# cnt = 0
# for n in range(2,36):
#     if sum_max(European_lists, n) < sum_max(American_lists, n):
#         cnt += 1
# print(cnt)

# print(sum_max(American_lists, 3))



# N = [True]*100
# for i in range(1, 101):
#     j = i - 1
#     while j < 100:
#         N[j] = not N[j]
#         j += i

# print([k + 1 for k in range(100) if N[k] == False])





# def fib(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     return fib(n-1) + fib(n-2)

# def func(m):
#     s = 0
#     m = str(m)
#     for x in m[0:]:
#         s += int(x)
#     return s

# cnt = 0
# n = 13
# while cnt < 5:
#     if fib(n) % func(fib(n)) == 0:
#         print(fib(n))
#         cnt += 1
#     n += 1

# def fibonacci(n):
#     if n == 0: return 1
#     if n == 1: return 1
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(10))
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

#排他的論理和で作る三角形
# 上から順番に配置していったとき、2014番目に「0」が出力されるのは何段目になるかを求めてください。
# ※一番目の「0」は３段目、２・３・４・番目の「0」は5段目出力される。

# cnt = 0
# line = 1
# row = [1]

# while cnt < 2014:
#     next_row = [1]
#     for i in range(len(row)-1):
#         cell = row[i] ^ row[i+1]
#         next_row.append(cell)
#         if cell == 0:
#             cnt += 1
            
#     next_row.append(1)
#     line += 1
#     row = next_row

# print(line)

# cnt = 0  # 0が出現した回数
# line = 1  # 現在の行数 
# row = [1] # 現在の行の値

# while cnt < 2014:
#     next_row = [1]
#     print(len(row))
#     # for i in range(len(row)):
#         # print(i)       


# クラブ活動への最適な配分
# 「学生にとっては勉強以上に大事なクラブ活動。
# あなたは新しく設置される学校の 校長に就任することが決まりました。
# スポーツをしたい150人の学生に、どんなクラ ブ活動を準備するか考えています。
# 各クラブに必要なグラウンドの 表7 各クラブに必要な土地と想定部員数 広さを調べてみたところ、[表1]の ようになりました
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

# 150人を超えないようにクラブ活動を選び、必要な土地の面積を最大にします。その 面積の最大値を求めてください。


# club = [[11000, 40], [8000, 30], [400, 24], [800, 20], [900, 14],
#         [1800, 16], [1000, 15], [7000, 40], [100, 10], [300, 12]]

# N = 150

# from ortoolpy import knapsack

# buin = [40, 30, 24, 20, 14, 16, 15, 40, 10, 12]
# menseki = [11000, 8000, 400, 800, 900, 1800, 1000, 7000, 100, 300]
# ninzu = 150
# print(knapsack(buin, menseki, ninzu))

# # for i in club:
    # print(i)

# from pulp import *

# # 重さ

# w = [40, 30, 24, 20, 14, 16, 15, 40, 10, 12]
# v = [11000, 8000, 400, 800, 900, 1800, 1000, 7000, 100, 300]
# W = 150

# r = range(len(w))

# # 数理モデル
# m = LpProblem(sense=LpMaximize)

# # 変数
# x = [LpVariable('x%d'%i, cat=LpBinary) for i in r]
# print(x)







# def func(m, n):
#     cnt = 0
#     le = 1
#     while le < n:
#         if le < m:
#             le = le + le
#         else:
#             le = le + m
#         cnt += 1
#     return cnt

# print(func(3, 20))
# print(func(5, 100))


# def sol_q04_02(n, m):
#   return 3 + (n- 4) // m if (n - 4) % m else 2 + (n- 4) // m
# # return 2 + (1 + (n- 4) // m if (n - 4) % m else (n- 4) // m)
 
 
# sol_q04_02(20, 3)



# def Cut_Tree(m, n):
#     stick = 1
#     t = 0
#     while stick < n:
#         if stick < m:
#             stick = stick + stick
#         else:
#             stick = stick + m
#         t += 1
#     return t

# print(Cut_Tree(3, 20))
# print(Cut_Tree(5, 100))



# 1~50までのnについて、上記の条件を満たすものを、例に挙げた「13」以外ですべ て求めてください。
# 例に挙げられている数字を7で割ると，「10, 1011, 100, 10, 1110,…」となる．
# つまり，バイナリから0/7の回文数のリストを作っておいて，それを正の整数nで割って割り切れれば良い．
# さて，問題自体は簡単だが，問題文の文意を読み取るのが難しい（ちょいちょいよく分からない）．
# この場合，「0と7の数字のみ」というのは，「0と7」が含まれている事がマスト（and）なのか，
# それともいずれか（or）なのかよく分からない．また，探索範囲の決定条件がよく分からない．
# 等式n x m = 回文数を満たさないと考えられるmの探索範囲の打ち切り条件ってなんだろう．
# 取り敢えず，適当な範囲で探索し（10桁まで），「0と7を含む場合」と「いずれかを含む場合」で考えてみる．


# 10個の数字をすべて表示する際、 点灯・消灯の切り替え回数が
# 最も少なくなる表示順を求め、その切り替え回数を答えてください。

# 0~9をあらわすビットを定義



# def func():
#   xlist = []
#   for i in range(1, 1000, 2):
#       p = 7*int(bin(i)[2:])
#       # print(p)
#       xlist.append(p)
  
#   # print(xlist) 
#   ans1, ans2 = [], []
#   for i in range(1, 51, 2):
#     for x in xlist:
#       if x % i == 0:
#         s = str(x)
#         # print(s)
#         if s == s[::-1]:
#           ans2.append(i)
#           if '0' in s:
#             ans2.append(i)
#         break
   
#   return ans1, ans2
 
 
# print(func())

# def sol_q32():
#   palindromic = []
#   for i in range(1, 1000, 2):
#     if i % 5 == 0:    continue
#     palindromic.append(7*int(bin(i)[2:]))
   
#   res1, res2 = [], []
#   for i in range(1, 51, 2):
#     if i % 5 and i == 13:    continue
#     for x in palindromic:
#       if x % i == 0:
#         s = str(x)
#         if s == s[::-1]:
#           res2.append(i)
#           if '0' in s:
#             res1.append(i)
#         break
   
#   return res1, res2
 











# 1
# 2
# 3
# 4
# 5
# 6
# def sol_q04_02(n=20, m=3):
#   return 3 + (n- 4) // m if (n - 4) % m else 2 + (n- 4) // m
# return 2 + (1 + (n- 4) // m if (n - 4) % m else (n- 4) // m)
 
 
# sol_q04_02(), sol_q04_02(100, 5)
# (8, 22)

# %timeit sol_q04_02()
# %timeit sol_q04_02(100, 5)



# def func():
#     result = {'number': 1, 'number_digits': 100}
#     for n in range(1, 100):
#         sq = math.sqrt(n) 
#         l = [v for v in range(1, 10)]
#         if result['number_digits'] <= len(str(sq).replace('.', '')):
#             continue
#         for i, s in enumerate(str(sq).replace('.', '')):
#             l = [v for v in l if v != int(s)]
#             if len(l) == 0 and result['number_digits'] > int(i + 1):
#                 result.update({'number': n, 'number_digits': i + 1})
#     return result

# r = func()
# print('最小整数:{}, 桁数:{}'.format(r['number'], r['number_digits']))


# # def sol_q12():
#   f1 = 0
#   f2 = 0
#   for x in range(2, 10000):
#     s = str(x**(1/2))
#     if not f1:
#       if len(set(s.replace('.', '')[:10])) == 10:
#         f1 = x
#     if not f2:
#       if len(set(s[s.index('.')+1:s.index('.')+11])) == 10:
#         f2 = x
#     if f1 and f2:
#       return f1, f2
#   return 'Failed'
 
 
# print(sol_q12())














# コラッツの予想
# 自然数nについて
# nが偶数の場合、nを2で割る。
# nが奇数の場合、nに３をかけて１を足す
# という操作を繰り返すとき、初期値がどんな数であっても必ず１に到達する。

# 2で始めた場合（2には戻る）
# 2⇒7⇒22⇒11⇒34⇒17⇒52⇒26⇒13⇒40⇒20⇒10⇒5⇒16⇒8⇒4⇒2
# 4で始めた場合（4には戻らない）
# 4⇒13⇒40⇒20⇒10⇒5⇒16⇒8⇒4
# 6で始めた場合
# 6⇒19⇒58⇒29⇒88⇒44⇒22⇒11⇒34⇒17⇒52・・・・（6には戻る）

# 10000以下の偶数のうち、 
# 上記の2や4のような「最初の数に戻る数」がいくつあるか、その個数を求めてください。

# 解き方☆
# 数字が1になるか元の数になったら、ループを終了させる。
# 1になるまで操作を繰り返して数字を変化させ、最初の数に、戻るかチェックする!!

# def siri(s, l):
#     res=[]
#     while len(l) > 0:
#         for i in l:
#             if i[0] == s[-1:]:
#                 print(s[0])
#                 print(s[-1:])
#                 res.append(i)
#                 l.remove(i)
#                 s = i
#                 break
#     return res

# s = "りんご"
# l = ['だるま','らくだ','まり','ごりら']
# a = siri(s, l)
# print(a)

# def if_even(x):
#     return x / 2

# def if_odd(x):
#     return x * 3 + 1

# def func(x):
#     m = if_odd(x)  # 初回
#     while True:    
#         if m == 1:
#             return False
#         elif m == x:
#             return True
#         elif m % 2 == 0:
#             m = if_even(m)
#         else:
#             m = if_odd(m)

# xlist = []
# for n in range(1, 10001):
#     if func(n):
#         xlist.append(n)
# print(xlist)
# print(len(xlist))


# import jaconv

# def siri(s, l):
#     res=[]
#     while len(l) > 0:
#         for i in l:
#             if jaconv.hira2kata(i[0]) == jaconv.hira2kata(s[-1:]):
#                 print(jaconv.hira2kata(i[0]))    
#             # if i[0] == s[-1:]:
#                 print(s[-1:])
#                 res.append(i)
#                 l.remove(i)
#                 s = i
#                 break
#     return res

# s = "りんご"
# l = ['だるま','らくだ','まり','ごりら']
# a = siri(s, l)
# print(a)




# def if_even(x):
#     return x / 2

# def if_odd(x):
#     return x * 3 + 1

# def func(x):
#     m = if_odd(x)  # 初回
#     while True:    
#         if m == 1:
#             return False
#         elif m == x:
#             return True
#         elif m % 2 == 0:
#             m = if_even(m)
#         else:
#             m = if_odd(m)

# xlist = []
# for n in range(1, 10001):
#     if func(n):
#         xlist.append(n)
# print(xlist)
# print(len(xlist))























# 覆面算
# 以下の式を満たすような数字のあてはめ方は何通りあるか求めてください。
# READ + WRITE + TALK = SKILL

# import string
# import itertools

# def func(word1, word2, word3, word4):
#     word_list = ''.join([word1,word2,word3,word4])
#     word_set = set(word_list)
#     length = len(word_set)
#     if length > 10 :
#         print('too many characters!!')

#     count = 0
#     for num in itertools.permutations('0123456789',length):
#         num_str = ''.join(num)
#         fig1 = word1.translate(str.maketrans(''.join(word_set),num_str))
#         print(fig1)
#         fig2 = word2.translate(str.maketrans(''.join(word_set),num_str))
#         fig3 = word3.translate(str.maketrans(''.join(word_set),num_str))
#         fig4 = word4.translate(str.maketrans(''.join(word_set),num_str))

#         if fig1[0] == '0' or fig2[0] == '0' or fig3[0] == '0' or fig4[0] == '0':
#             continue
#         if int(fig1) + int(fig2) + int(fig3) == int(fig4):
#             print (fig1, '+', fig2, '+', fig3, '==', fig4)
#             count += 1
#     print(count)
  

    # print(number_strings)
    # print(number_strings)
    # print(type(number_strings))
    
    # print(fig1)
    # fig2 = word2.translate(string.maketrans(''.join(char_set),number_strings))
    # fig3 = word3.translate(string.maketrans(''.join(char_set),number_strings))
    # fig4 = word4.translate(string.maketrans(''.join(char_set),number_strings))

    # if fig1[0] == '0' or fig2[0] == '0' or fig3[0] == '0' or fig4[0] == '0' :
        # continue

    # if int(fig1) + int(fig2) + int(fig3) == int(fig4) :
        # print fig1, '+', fig2, '+', fig3, '==', fig4
        # count += 1

# print count

# print(count)
# func('READ', 'WRITE', 'TALK', 'SKILL')






# # 日付の2進数変換

# 年月日をYYYYMMDDの8桁の整数で表したとき、これを2進数に変換してから逆に並べ、
# さらに10進数にもどしたとき、元の日付と同じ日付になるものを探してください。
# 期間は、前回の東京オリンピック(1964年10月10日)から、次回の東京オリンピック（2020年7月24予定）とします。


# print(bin(19660713)[2:])

# print(bin(20200724)[2:])

# ni_start = bin(19660713)[2:]
# ni_end = bin(20200724)[2:]

# rev_start = ni_start[::-1]
# rev_end = ni_end[::-1]

# # print(rev_start)
# # print(rev_end)


# print(int(rev_start, 2))
# print(int(rev_end, 2))

# import pandas as pd

# def func(start_date, end_date):
#     daterange = pd.date_range(start_date, end_date)
#     for single_date in daterange:
#         hi = single_date.strftime("%Y%m%d")
#         s = bin(int(hi))[2:]
#         res = int(s[::-1], 2)
#         if int(hi) == res:
#             print(res)

# func('19641010', '20200724')







# start_date = '20090530'
# end_date = '20110530'

# import pandas as pd

# daterange = pd.date_range(start_date, end_date)

# for single_date in daterange:
#     print (single_date.strftime("%Y-%m-%d"))







# from datetime import datetime, timedelta

# start = datetime.strptime('20120101', '%Y%m%d')
# end = datetime.strptime('20120201', '%Y%m%d')

# def kikan(start_date, end_date):
#     for n in range((end_date - start_date).days):
#         yield start_date + timedelta(n)

# for i in kikan(start, end):
#     print(i)







# id,userでユーザーを定義した文字列（idはユーザーID,userはユーザー名とする）と、
# ユーザーアクティビティを定義した文字列(idはアクティビティID、dateは日付、user-idはユーザーID、actionはアクティビティ名)が与えられた時に、
# 月ごとのアクティビティの種類をkeyと数をvalueとして集計し返す関数"get_activity_per_month"と
# 月ごとのユーザーのアクティビティ数を、ユーザー名をkey、数をvalueとして集計しかえす関数"get_user_activity"の２つの関数を作成せよ。

# バスに設置されている両替機を考えます。
# この機械では、10円玉、50円玉、100円玉、500円玉の組み合わせに両替することができ、
# いずれの硬貨も十分な枚数がセットされています。
# （バスの運賃の場合は10円単位になるため、1円玉と5円玉は取り扱っていません。）
# 両替する際に使わない硬貨はあっても構いませんが、バスの中でたくさん小銭が出ると困るため、最大で15枚になるように両替します。
# 例えば、1000円を両替するときに「10円玉100枚という両替はできません。」
# 1000円札を入れたときに出てくる硬貨の組み合わせは何通りあるか求めてください。
# なお、硬貨の順番は区別しないものしないものとします。

# coins = [10, 50, 100, 500]
# cnt = 0
# (2..15).each do |i|
#  doins.repeated_combination(i).each{[coin_set\
#     cnt += 1 if coin_set.inject(:+) == 1000
# }
# end
# puts cnt


# coins = [10, 50, 100, 500]

# aa = 0
# for i in coins:
#     aa += i;
#     print(aa)
#     print(i)


# import math
# import datetime

# def baisu(a, b):
#     return a * b / math.gcd(a, b)

# # michikake = 29 / 2 
# # michikake = 14.75 # 14 * 3/4  =  59/4
# sen = baisu(int(59 * 4), 183 * 4) / 4

# d1 = datetime.datetime(2018, 1, 1, 0, 0)
# print(d1 + datetime.timedelta(days=sen))













