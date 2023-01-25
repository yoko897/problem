# coding: utf-8
#!/usr/bin/env python


def func(x, y, z, q):
    print(q[::-1])
    print(z[::-1])
    print(y[::-1])
    print(x[::-1])

a = '....'
b = '.oo.'
c = '.xx.'
d = '....'

func(a, b, c, d)

e = 'o o x x'
f = 'o o x x'
g = 'x x o o'
h = 'x x o o'

func(e, f, g, h)



# N個の整数の列 A1,…,AN が与えられます。
# これらの逆数の総和の逆数を求めてください。

# def func(N, A):
#     s = 0
#     for i in A:
#         s += 1/i
#     print(1/s)

# def func(A):
#     print(1/sum([1/i for i in A]))


# func([10, 30])  #7.5
# func([200, 200, 200])  #66.66666666666667




# ・問題文
# zでない英小文字Cが与えられます。
# アルファベット順でCの次の文字を出力してください。

# ・制約
# Cはzでない英小文字

# def func(x):
#     a = [chr(i) for i in range(97,97+26)]
#     print(a[a.index(x)+1])

# func('a')
# func('k')
# func('y')


# https://sonogym.sizebook.jp/program_answer/911/detail/
# 正整数 A,Bが与えられます。
# AがBの約数ならA+Bを、そうでなければB−Aを出力してください。

# def y(m):
#     ylist = []
#     for i in range(1, m+1):
#         if m % i == 0:
#             ylist.append(i)
#     return ylist

# def func(A, B):
#     return A + B if A in y(B) else B - A



# def func(A, B):
#     cnt = 0
#     for i in range(3):
#         if A[i] == B[i]:
#             cnt += 1
#     print(cnt)

# func('CSS', 'CSR')


# def func(A, B):
#     print(len([i for i in range(3) if A[i] == B[i]]))

# func('CSS', 'RRR')
# func('CSS', 'RSR')
# func('CSS', 'CSR')
# func('CSR', 'CSR')

# def func(A):
#     s = 0
#     for i in A:
#         s += 1/i
#     print(1/s)


# print(func([10, 30]))  #7.5
# print(func([200, 200, 200]))  #66.66666666666667



# def func(S):
#     flag = True
#     for i in range(len(S)):
#         if i % 2 == 0:
#             if S[i] == 'L':
#                 flag = not flag
#                 break
#         else:
#             if S[i] == 'R':
#                 flag = not flag
#                 break

#     print('Yes' if flag == True else 'No')

# func('RUDLUDR')  # Yes
# func('DULL')     # NO

# def func(S):
#     flag = True
#     for i in range(len(S)):
#         if i % 2 == 0:
#             print(i, S[i])
#             if S[i] == 'L':
#                 flag = not flag
#                 break
#         # 奇数
#         else:
#             if S[i] == 'R':
#                 flag = not flag
#                 break

#     print('Yes' if flag == True else 'No')

# func('RUDLUDR')  # Yes
# func('DULL')     # NO


# Attack Survival

# 高橋君は九九を覚えたので、1 以上 9 以下の 2 つの整数の積を計算することができます。
# 整数 N が与えられるので、N を 1 以上 9 以下の 2 つの整数の積として表すことができるか判定し、
# できるなら Yes を、できないなら No を出力して下さい。





# N K Q
# A1
# A2
# .
# .
# .
# AQ

# 出力
# N 行出力してください。
# i 行目には、参加者iが勝ち抜けたなら Yes を、敗退したなら No を出力してください。

# ■入力例 1
# 6 3 4
# 3
# 1
# 3
# 2

# ■出力例 1
# No
# No
# Yes
# No
# No
# No






















# N個の整数の列 A1,…,AN が与えられます。
# これらの逆数の総和の逆数を求めてください。

# def func(N, A):
#     s = 0
#     for i in A:
#         s += 1/i
#     print(1/s)


# print(func(2, [10, 30]))  #7.5
# print(func(3, [200, 200, 200]))  #66.66666666666667


# 正の整数Nが与えられます。
# N以下の正の整数の組 (A,B)であって、次の条件を満たすものの個数を求めてください。
# 
# A,Bを先頭に 0のつかない10進数表記で表したときに、 
# Aの末尾の桁がBの先頭の桁に等しく、 
# Aの先頭の桁がBの末尾の桁に等しい


# def func(x):
#     print(x)

# print(func(25))


# 25
# 17

# (1,1) , (1,11), (2,2), (2,22), (3,3), 
# (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), 
# (11,1), (11,11), (12,21), (21,12), (22,2), (22,22)



# フェネックはN体のモンスターと戦っています。
# i番目のモンスターの体力はHiです。

# フェネックは次の2種類の行動を行うことができます。
# 攻撃：モンスターを1体選んで攻撃することで、そのモンスターの体力を1減らす
# 必殺技：モンスターを1体選んで必殺技を使うことで、そのモンスターの体力を0にする
# 攻撃と必殺技以外の方法でモンスターの体力を減らすことはできません。
# 全てのモンスターの体力を0以下にすればフェネックの勝ちです。
# フェネックがK回まで必殺技を使えるとき、
# モンスターに勝つまでに行う攻撃の回数 (必殺技は数えません) の最小値を求めてください。













# アライグマはモンスターと戦っています。
# 
# モンスターの体力はHです。
# 
# アライグマはN種類の必殺技を使うことができ、
# i番目の必殺技を使うとモンスターの体力を Ai減らすことができます。
# 必殺技を使う以外の方法でモンスターの体力を減らすことはできません。
# 
# モンスターの体力を0以下にすればアライグマの勝ちです。
# 
# アライグマが同じ必殺技を2度以上使うことなくモンスターに勝つことができるならYesを、
# できないならNoを出力してください。


# def func(H, N, A):
#     return 'Yes' if sum(A) >= H else 'No'

# print(func(10, 3, [4, 5, 6])) #Yes
# print(func(20, 3, [4, 5, 6])) #No
# print(func(210, 5, [31, 41, 59, 26, 53])) #Yes
# print(func(211, 5, [31, 41, 59, 26, 53])) #No








# def y(m):
#     ylist = []
#     for i in range(1, m+1):
#         if m % i == 0:
#             ylist.append(i)
#     return ylist

# def func(A, B):
#     return A + B if A in y(B) else B - A



    #     return A + B
    # else:
    #     return B - A

# print(func(4, 12)) #4は12の約数なので4+12=16
# print(func(8, 20)) #8は20の約数じゃないので20-8=12
# print(func(1, 1))  #1は1の約数なので1+1=2






# def func(x):
#     print(chr(x))
#     # print(chr(x))

# print(func(1))
# print(func(1))
# print(func(1))


# # 問題文
# # 高八士君は回文が大好きで、回文でない文字列が許せません。
# # 高八士君は文字列を1回ハグするごとに、
# # 文字列から1文字を選んで任意の文字に変えることができます。

# # 文字列 Sが与えられます。
# # Sを回文にするために必要なハグの最小回数を答えてください。

# def func(S):
#     print(S)

# print(func(10))



# 6
# abcabc Yes
# T= 'abc' とおくと、 
# S=T+Tとなります。
# def func(N, S):
#     a = len(S)//2
#     if S[:a] == S[a:]:
#         return 'Yes'
#     else:
#         return 'No'
# print(func(6, 'abcabc')) # Yes
# print(func(6, 'abcadc')) # No


# 1桁の正整数a,bが与えられます。
# 整数aをb回繰り返してできる文字列と 
# 整数bを回繰り返してできる文字列のうち、
# 辞書順で小さい方を答えてください。
# 43
# 3333
# 77
# 7777777
# a,bが4,3の場合、
# できる2つの文字列は、'444'と'3333'です。このうち辞書順で小さい文字列は '3333' です。

# def func(a, b):
#     print(str(a) * b if a <= b else str(b) * a)

# func(4, 3)
# func(1, 2)
# func(7, 7)

# def prime(p):
#     s = []
#     for i in range(1, p+1):
#         if p % i == 0:
#             s.append(i)
#     if len(s) == 2:
#         return p
#     else:
#         return False
# def func(x):
#     while x:
#         if prime(x) != False:
#             print(x)
#             break
#         x += 1

# func(20) # 23
# func(2) # 2
# func(99992) # 100003





# # input
# X = int(input())
 
# # process
# def is_prime(x):
#     if x < 2:
#         return False
    
#     i = 2
#     while i*i <= x:
#         if x % i == 0:
#             return False
#         i += 1
    
#     return True
    
# x = X
# while not is_prime(x):
#     x += 1
 
# # output
# print(x)




# 一つの辞書xが与えられた時、奇数キーの値と偶数キーの値を結合したリストを返す関数を作成せよ
# 例：x = {1:'hello', 2:'world', 3:'hello', 4:'', 5:'world'} => ['helloworld', 'hello', 'world']





# import re

# def func(s):
#     # 3桁の数字にマッチする。
#     if re.match(r"\d{3}", s):
#         return int(s) * 2
#     else:
#         return 'error' 

# print(func('678')) # 1356
# print(func('abc')) # error
# print(func('0x8')) # error
# print(func('012')) # 24



# import re

# def func(x):
#     return re.match('[0-9a-zA-Z\._+]+@[a-zA-Z]+\.[a-zA-Z]', x) != None

# word.isdecimal()
# print(func('yoko.sonoki@sizebook.co.jp'))
# print(func('yoko.sonoki@sizebookcojp'))


# import re

# # re.sub(正規表現パターン, 置換後文字列, 置換したい文字列)
# # \D : 10進数でない任意の文字。（全角数字等を含む）
# num = re.sub("\\D", "", "77566593４あああ")
# print(num)    # "2019"



# for i in mail.splitlines():
#     a += i
# print(a)




# 例えば、2,3,5は素数ですが、4,6は素数ではありません。

# 制約
# 2≤X≤10^5
# 入力はすべて整数

# def is_prime(p):
#     l = []
#     for i in range(2, p+1):
#         if p % i == 0:
#             l.append(i)
#     print(l, len(l))
#     if len(l) == 2:
#         return p
#     else:
#         return False

# print(is_prime(11))
# def func(x):
#     for i in range(2, x+1+10):
#         if is_prime(i) != False and is_prime(i) > x:
#             print(i)

# print(func(10))





















# import re

# def func(s):
#     if re.match(r"\d{3}", s):
#         return int(s) * 2
#     else:
#         return 'error' 

# print(func('678')) # 1356
# print(func('abc')) # error
# print(func('0x8')) # error
# print(func('012')) # 24


# 引数の2倍を返す関数「double_value」, 
# 引数の6倍を返す関数「six_value」をそれぞれ作成し、six_valueの中でdouble_valueをよびだせ



# def double_value(x):
#     return x * 2

# def six_value(x):
#     return double_value(x * 3)

# print(six_value(8))
# print(six_value(3))

# # ２つの引数を持ち、その和を返す関数「add_value」を作成し、以下のプログラムが走るようにしなさい

# def add_value(a, b):
#     return a+b

# def func(x):
#     for i in range(x):
#         print(add_value(i, i + 1))

# func(3) # 1, 3, 5が順に出力される


















# import re

# # 下記のdict(zip(y[0::2], y[1::2]))をforループを用いて同等の処理を行いなさい

# def func(x):
#     y = re.split(r'[,:]', x)
#     print(y)
#     # z = dict(zip(y[0::2], y[1::2]))
#     d = dict()
#     for i in range(0, len(y), 2):
#         d[y[i]] = y[i + 1]
#     return d

# print(func('hello:world,xxxx:yyyy'))


# 一つのリストxが与えられた時、順番は最初に出現した順で重複を除外したリストを返す関数を作成せよ
# [1, 3, 10, 9, 1, 9, 10, 3, 6] => [1, 3, 10, 9, 6]


# def func(x):
#     return list(set(x))
#     # a = []
#     # for i in x:
#     #     if i not in a:
#     #         a.append(i)
#     # return a




# print(func([1, 3, 10, 9, 1, 9, 10, 3, 6]))











# xに与えた数値をy進数に変換する関数を作成してみれ
# ただしformat使用禁止。
# 例
# conv(100, 2)
# 結果
# "1100100"


# def conv(x, y):
    


# print(conv(100, 2))















# 二つのリストx,yが与えられた時、xの値で割り切れるyの値を下記の形式で返す関数を作成せよ
# 例：[2,5], [2,3,4,5,6,7,8,9,10]=> {2:[2,4,6,8,10], 5:[5,10], ‘Other’:[3,7,9]}


# あるリストLが与えられた場合、Lの全要素が同じであればTrue、
# 違う要素が１つでもあればFalseを返す関数all_same(L)を作成する。


# def all_same(L):
#     return len(list(set(L))) == 1

# print(all_same([2,3,4,5,6,7,8,9,10]))
# print(all_same([2,2]))








# def func(x):
#     d = {}
#     for i in x:
#         for m in i:
#             print(d.get(m))
#             # keyが存在しなければNone
#             if d.get(m) == None:
#                 d[m] = 1
#             else:
#                 d[m] += 1
#     return d

# print(func(['abc', 'ac', 'ddd']))


# 一つのリストxが与えられた時、0の要素ごとにくぎって総和を返す関数を作成せよ
# 例1:[1, 0, 2, 3, 0, 4, 8] => [1, 5, 12] # (1, 2 + 3, 4 + 8)
# 例2:[0, 9, 10, 0, 3, 0, 4, 8] => [0, 19, 3, 12]

# xlist = [1, 0, 2, 3, 0, 4, 8]

# def func(x):
#     xlist, ylist = [], []
#     for i in x:
#         if i == 0:
#             ylist.append(sum(xlist))
#             xlist = []
#         else:
#             xlist.append(i)
#     ylist.append(sum(xlist))
#     return ylist

# print(func([1, 0, 2, 3, 0, 4, 8]))
# print(func([0, 9, 10, 0, 3, 0, 4, 8]))

# 一つのリストxが与えられた時、xの平均値より低いもののリストを返す関数を作成せよ

# [1, 9, 3, 5, 7, 6] => [1, 3, 5]

# def func(x):
#     return [i for i in x if i < sum(x)/len(x)]

# print(func([1, 9, 3, 5, 7, 6]))



# ひとつのの文字列をパースして辞書に変換する関数を作成せよ。フォーマットは以下のようなもの
# 例："hello:world,xxxx:yyyy" 
# => {"hello": "world", "xxxx": "yyyy"}
# def func(x):
#     d = {}
#     for i in x.split(","):
#         a, b = i.split(":")
#         d[a] = b
#     return d

# print(func("hello:world,xxxx:yyyy"))

# 文字列の配列xが与えられた時に、以下のように、
# 最後の代入式のみを辞書形式で返す関数をかけ
# 例1: x=['x=3', 'z=hello world', 'y=4', 'x=10']
 # -> {'x': '10', 'y': '4', 'z': 'hello world'}
# 例2: x=['x=3', 'x=10', 'x=xxx', 'x=yyy']
 # -> {'x': 'yyy'}

# x=['x=3', 'z=hello world', 'y=4', 'x=10']

# def func(x):
#     d = {}
#     for i in x:
#         a, b = i.split('=')
#         print(a, b)
#         # print(dict(zip(a, b)))


# print(func(['x=3', 'z=hello world', 'y=4', 'x=10']))
# print(func(['x=3', 'x=10', 'x=xxx', 'x=yyy']))

# -*- coding: utf-8 -*-

# def func(x):
#     result = {}
#     for v in x:
#         x_list = v.split('=')
#         result = {x_list[0]: x_list[1]}
#     return result
# print(func(['x=3', 'z=hello world', 'y=4', 'x=10']))
# print(func(['x=3', 'x=10', 'x=xxx', 'x=yyy']))












# 以下のような依存関係を示した辞書を引数に取り、
# 依存関係を満たすような順序のkeyのリストを返す関数を作成せよ
# 意味) { キー: 依存するキー }, 
# 依存するキーがNoneの場合は依存するものがないものとする
# 例) x={1: None, 2: 1, 3: 2} => [1, 2, 3]
# x={1: 3, 2: None, 3: 2} => [2, 3, 1]

# # x={1: 3, 2: None, 3: 2} => [2, 3, 1]

# def func(x):
#     print(x)

# print(func({1: 3, 2: None, 3: 2}))




"""
https://sonogym.sizebook.jp/program/42/create/
- ２つのリストを連結させ、重複したキーは値の合計をいれよ
例
list1 = {'sonoki': 25, 'anzu': 28, 'yun': 32, 'shogo': 30, 'kenta': 31}
list2 = {'youko': 100, 'anzu': 40, 'yun': 50, 'sawai': 20, 'kenta': 60}
結果
{'sonoki': 25, 'anzu': 68, 'yun': 82, 'shogo': 30, 'kenta': 91, 'youko': 100, 'sawai': 20}
"""


# def func(list1, list2):
#     for m in list1:
#         for n in list2:
#             if m == n:
#                 list1[m] += list2[n]
#             else:
#                 list1 = dict(list2, **list1)
#     return list1

# print(func({'sonoki': 25, 'anzu': 28, 'yun': 32, 'shogo': 30, 'kenta': 31}, 
#     {'youko': 100, 'anzu': 40, 'yun': 50, 'sawai': 20, 'kenta': 60}))

# xlist1 = {'sonoki': 25, 'anzu': 28, 'yun': 32, 'shogo': 30, 'kenta': 31}, 
# xlist2 = {'youko': 100, 'anzu': 40, 'yun': 50, 'sawai': 20, 'kenta': 60}

# print(dict(xlist2, **xlist1))

# ひとつのの文字列をパースして辞書に変換する関数を作成せよ。フォーマットは以下のようなもの
# 例："c" => {"hello": "world", "xxxx": "yyyy"}

# 文字列の配列xが与えられた時に、配列内の文字のカウントを返す関数をかけ

# # 例: x=['abc', 'ac', 'ddd'] -> {'a': 2, 'b': 1, 'c': 2, 'd': 3}
# 文字列の配列xが与えられた時に、配列内の文字のカウントを返す関数をかけ
# 例: x=['abc', 'ac', 'ddd'] -> {'a': 2, 'b': 1, 'c': 2, 'd': 3}


# def func(x):
#     d = {}
#     for i in x:
#         for m in i:
#             if d.get(m) == None:
#                 d[m] = 1
#             else:
#                 d[m] += 1
#     return d

# print(func(['abc', 'ac', 'ddd']))




# # def fnc(x):
# #     for i in x:
# #         for j in i:
# #             print(d.get(j))
# #             if d.get(j) is None:
# #                 d[j] = 0
# #             d[j] += 1
# #     return d

# x = ['abc', 'ac', 'ddd']

# def func(x):
#     d = {}
#     for i in x:
#         for p in i:
#             print(p)
#             # print(p.count())

# print(func(['abc', 'ac', 'ddd']))

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


# def func(list1, list2):
#     for m in list1:
#         for n in list2:
#             if m == n:
#                 list1[m] += list2[n]
#             else:
#                 list1 = dict(list2, **list1)
#     return list1

# print(func({'sonoki': 25, 'anzu': 28, 'yun': 32, 'shogo': 30, 'kenta': 31}, 
#     {'youko': 100, 'anzu': 40, 'yun': 50, 'sawai': 20, 'kenta': 60}))

        # list1[k] +=  list2[k]
    # else:
        # list1[k] = list2[k]

# print(list1)

# Q1. 以下の２つのリスト同士を四則演算して、その結果をリストにいれよ
# a = [2, 4, 8, 16, 32, 64, 128]
# b = [8, 7, 6, 5, 3, 2, 1]
# result_add = [10, 11, 14, ....]  # 加算
# result_sub = [-6, -3, 2, ...]  # 減算
# result_mul = [16, 28, 48, ...]  # 乗算
# result_div = [0.25, 0.57, 1.33, ...]  # 除算
# 小数点以下桁数は問わない(できたら２桁)

# a = [2, 4, 8, 16, 32, 64, 128]
# b = [8, 7, 6, 5, 3, 2, 1]

# def func(a, b):
#     add = [x + y for (x, y) in zip(a, b)]
#     sub = [x - y for (x, y) in zip(a, b)]
#     mul = [x * y for (x, y) in zip(a, b)]
#     div = ['{:.2f}'.format(x / y) for (x, y) in zip(a, b)]

#     print('result_add = {}'.format(add))
#     print('result_sub = {}'.format(sub))
#     print('result_mul = {}'.format(mul))
#     print('result_div = {}'.format(div))

# print(func([2, 4, 8, 16, 32, 64, 128], [8, 7, 6, 5, 3, 2, 1]))











# list1 = {'sonoki': 25, 'anzu': 28, 'yun': 32, 'shogo': 30, 'kenta': 31}
# list2 = {'youko': 100, 'anzu': 40, 'yun': 50, 'sawai': 20, 'kenta': 60}


# for i in list1:
#     if i in list2:
#         print('chohuku', i[0])
#     else:
#         print('tigau', i)

    # for p in list2.items():
        # print(i[0], i[1], p[0], p[1])
        # if i[0] == p[0]:
            # print(i[1], p[1], i[1]+p[1])

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

# print(list1.values(), list2.values())

# for m in list1:
#     for i in list2:
#         print(m, i)

# ある数字xが与えられた場合、
# 0からxまでの整数をフィボナッチ数列の長さでsliceしたlistを返す関数
# slice_fib(x)を作成する。
# （例：x＝１０）
# [[0], [1], [2, 3], [4, 5, 6], [7, 8, 9]]

# （例：x＝１００）
# [[0], [1], [2, 3], [4, 5, 6], [7, 8, 9, 10, 11], 
# [12, 13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32], 
# [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53


# def fib(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     return fib(n-1) + fib(n-2)

# def slice_fib(x):
#     m = 0
#     xlist = [i for i in range(x)]
#     flist = []
#     for i in range(x):
#         a = m
#         m += fib(i)
#         flist.append(xlist[a:m])
#         if x < m:
#             break
#     return flist

# print(slice_fib(10))
# print(slice_fib(100))
# p = [0,1,2,3,4,5,6,7,8,9]

# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144


# print(p[0:1], p[1:2], p[2:4], p[4:7], p[7:-1])












# def decorator(func):
#     def wrapper():
#         return "Hello " + func() + "!!"
#     return wrapper

# @decorator
# def world():
#     return "world"

# print(world())

# {2: 3, 5: 7, 11: None}

# from itertools import zip_longest

# def is_prime(p):
#     l = []
#     for i in range(1, p+1):
#         if p % i == 0:
#             l.append(i)
#     if len(l) == 2:
#         return True
#     else:
#         return False

# def func(x):
#     xlist = []
#     for i in range(x+1):
#         if is_prime(i):
#             xlist.append(i)
#     return {k: v for k, v in zip_longest(xlist[::2], xlist[1::2])}

# print(func(11))



# 下記の関数にデコレータを使って”Hello wold!!”と返す
# def world():
# return "world"

# def decorator(func):
#     def wrapper():
#         return "Hello " + func() + "!!"
#     return wrapper

# @decorator
# def world():
#     return "world"

# print(world())


# ある数字xが与えられた場合、0からxまでの整数をフィボナッチ数列の長さでsliceしたlistを返す関数slice_fib(x)を作成する。

# （例：x＝１０） [ [0], [1], [2, 3], [4, 5, 6], [7, 8, 9] ]
# （例：x＝１００） [[0], [1], [2, 3], [4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32], [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], [88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]]


# xlist = [i for i in range(10)]
# test = "orange,apple,banana,strawberry"
# test1 = "0, 1, 23, 456, 789"

# print(test.split(","))
# print(test1.split(","))













# 一つの整数xがあたえれた時、次の２つのリストを作成し、それぞれのリストの対応する要素の積が入ったリストを作成せよ。
# リストA[0, 1, 2, ... x]
# リストB[x, x - 1, x - 2, ... 0]
# リストC[0, x, 2*(x-1), ... 0]

# 例：3 ->
# [0, 1, 2, 3]
# [3, 2, 1, 0]
# [0, 2, 2, 0]




# 一つの数字xが与えられた時、xまでの素数を辞書型で返す関数を作成せよ
# 例：x = 11=> {2:3, 5:7, 11:None}

# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47・・・・

# from itertools import zip_longest

# def is_prime(p):
#     l = []
#     for i in range(1, p+1):
#         if p % i == 0:
#             l.append(i)
#     if len(l) == 2:
#         return True
#     else:
#         return False

# def func(x):
#     xlist = []
#     for i in range(x+1):
#         if is_prime(i):
#             xlist.append(i)
#     keys = xlist[::2]
#     values = xlist[1::2]
#     return {k: v for k, v in zip_longest(keys, values)}

# print(func(11))





# 一つの辞書xが与えられた時、
# 奇数キーの値と偶数キーの値を結合したリストを返す関数を作成せよ
# # 例：x = {1:'hello', 2:'world', 3:'hello', 4:'', 5:'world'} 
# => ['helloworld', 'hello', 'world']



# 二つのリストx,yが与えられた時、xの値で割り切れるyの値を下記の形式で返す関数を作成せよ
# 例：[2,5], [2,3,4,5,6,7,8,9,10]=> {2:[2,4,6,8,10], 5:[5,10], ‘Other’:[3,7,9]}

# def func(x, y):
#     for i in x:
#         for p in y:
#             if p % i == 0:
#                 xlist.append(p)
#             else:
#                 ylist.append(p)
#     print(x, y)

# print(func([2,5], [2,3,4,5,6,7,8,9,10]))



# 9x9 の大きさのリストが与えられた時に、数独を完成させてください。
# ただし、リストの数字は各マスの数字を表し、 値がすでに決まっている場合にはその数字が、そうでない場合には None が入っている。

# (例)
# [[ 5, 8, None, 3, None, None, None, None, 1],
# [None, None, 2, None, None, None, 8, 6, None],
# [None, None, 9, None, None, 2, 7, None, 4],
# [ 6, None, None, 2, 3, None, 4, 1, None],
# [ 8, None, None, 5, 1, None, None, 7, None],
# [ 9, 1, 4, None, 7, None, None, 3, None],
# [ 3, 9, None, 7, 2, None, None, None, None],
# [None, 6, 5, 4, None, None, 1, None, None],
# [ 4, None, None, 9, None, 6, None, 8, None]]

# list1 = {'sonoki': 25, 'anzu': 28, 'yun': 32, 'shogo': 30, 'kenta': 31}
# list2 = {'youko': 100, 'anzu': 40, 'yun': 50, 'sawai': 20, 'kenta': 60}

# out = {}
# for k in list2:
#     if k in list1:
#         list1[k] +=  list2[k]
#     else:
#         list1[k] = list2[k]

# print(list1)

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












# 一つの日時リストを引数にとり、年の昇順、月の降順、日の昇順のリストを返却する関数を作成せよ
# 例)
# x = ['2017/01/02', '2001/01/01', '2017/01/01', '2018/01/01', '2017/02/01'] 
# => ['2001/01/01', '2017/02/01', '2017/01/01', '2017/01/02', '2018/01/01']


# def func(x):









# list1 = {'sonoki': 25, 'anzu': 28, 'yun': 32, 'shogo': 30, 'kenta': 31}
# list2 = {'youko': 100, 'anzu': 40, 'yun': 50, 'sawai': 20, 'kenta': 60}

# for i in list1:
#     for n in list2:
#         print(i, list1[i], n, list2[n])
#         if i == n:
#             a = list1[i] + list2[n]
#             print(i, a)

# def sosu(p):
#     l = []
#     for i in range(1, p+1):
#         if p % i == 0:
#             l.append(i)
#     # 約数が2つだったら素数
#     if len(l) == 2:
#         return p
#     else:
#         return False

# m = []

# for i in range(100, 1000):
#     if sosu(i) != False:
#         m.append(sosu(i))
# # 3桁の素数リスト
# print(m)
# cnt = 0
# for a in m:
#     for b in m:
#         for c in m:
#             if a != b and a != c and b != c:
#                 s = '{},{},{}'.format(a, b, c)
#                 if int(s[0]+s[4]+s[8]) in m:
#                     if int(s[1]+s[5]+s[9]) in m:
#                         if int(s[2]+s[6]+s[10]) in m:
#                             if len(set([a, b, c, int(s[0]+s[4]+s[8]), int(s[1]+s[5]+s[9]), int(s[2]+s[6]+s[10])])) == 6:
#                             	cnt += 1
# print(cnt)
# # def sosu(p):
#     l = []
#     for i in range(1, p+1):
#         if p % i == 0:
#             l.append(i)
#     # 約数が2つだったら素数
#     if len(l) == 2:
#         return p
#     else:
#         return False

# m = []

# for i in range(100, 1000):
#     if sosu(i) != False:
#         m.append(sosu(i))
# # 3桁の素数リスト
# print(m)
# cnt = 0
# for a in m:
#     for b in m:
#         for c in m:
#             if a != b and a != c and b != c:
#                 s = '{},{},{}'.format(a, b, c)
#                 if int(s[0]+s[4]+s[8]) in m:
#                     if int(s[1]+s[5]+s[9]) in m:
#                         if int(s[2]+s[6]+s[10]) in m:
#                             if len(set([a, b, c, int(s[0]+s[4]+s[8]), int(s[1]+s[5]+s[9]), int(s[2]+s[6]+s[10])])) == 6:
#                                 cnt += 1
# print(cnt)

    #             if a != b and b != c and a != c:
    #                 s = '{},{},{}'.format(a, b, c)
    #                 if int(s[0]+s[4]+s[8]) in m:
    #                     if int(s[1]+s[5]+s[9]) in m and int(s[2]+s[6]+s[10]) in m:
    #                         if len(set([int(a), int(b), int(c), s[0]+s[4]+s[8], s[1]+s[5]+s[9], s[2]+s[6]+s[10]])) == 6:
    #                             ss = [int(a), int(b), int(c), s[0]+s[4]+s[8], s[1]+s[5]+s[9], s[2]+s[6]+s[10]]
    #                             print(len(set(ss)), ss)
    #                             cnt += 1
    # print(cnt)
                # print(s[0]+s[4]+s[8], m)
                # print(s, s[0]+s[4]+s[8], s[1]+s[5]+s[9], s[2]+s[6]+s[10])
                # if s[0]+s[4]+s[8] in m and s[1]+s[5]+s[9] in m and s[2]+s[6]+s[10] in m:
                # if s[0]+s[4]+s[8] in m:
                	# print(s)

                # if s[0], s[4], s[8] in m

 
                # alist.append(s)
    # print(alist)









# def func(p):
#     l = []
#     for i in range(1, p+1):
#         if p % i == 0:
#             l.append(i)
#     return l

# print(func(10))

# for i in range(2,n):
#     if n%i==0:
#         print('素数でない')
#         break
#     else:
#         print('素数')
#         print(n)


# （例：x＝10） [ [0], [1], [2, 3], [4, 5, 6], [7, 8, 9] ]
# （例：x＝100） [[0], [1], [2, 3], [4, 5, 6], [7, 8, 9, 10, 11], 
# [12, 13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32], 
# [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], 
# [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], 
# [88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

# print(range(0, 9))

# 一つの日時リストを引数にとり、年の昇順、月の降順、日の昇順のリストを返却する関数を作成せよ
# 例)
# x = ['2017/01/02', '2001/01/01', '2017/01/01', '2018/01/01', '2017/02/01'] =>
 # ['2001/01/01', '2017/02/01', '2017/01/01', '2017/01/02', '2018/01/01']

# from datetime import datetime

# def func(x):
#     for i in x:
#         x.sort(key=lambda i: datetime.strptime(i, '%Y/%m/%d'))
#         print(datetime.strptime(i, '%Y/%m/%d'))
    	
# print(func(['2017/01/02', '2001/01/01', '2017/01/01', '2018/01/01', '2017/02/01']))

# 文字列の配列xが与えられた時に、以下のように、最後の代入式のみを辞書形式で返す関数をかけ
# 例1: x=['x=3', 'z=hello world', 'y=4', 'x=10'] 
# -> {'x': '10', 'y': '4', 'z': 'hello world'}
# 例2: x=['x=3', 'x=10', 'x=xxx', 'x=yyy'] 
# -> {'x': 'yyy'}

# x=['x=3', 'z=hello world', 'y=4', 'x=10']

# def func(x):
#     xlist = []
#     for i in x:
#         a = i.split('=')
#         xlist.append(a[0], a[1])
#     print(xlist)

# print(func(['x=3', 'z=hello world', 'y=4', 'x=10']))
# print(func(['x=3', 'x=10', 'x=xxx', 'x=yyy']))

# 整数xが与えられた時に、エクセルの行の名前を返す関数をかけ
# 例: x=1 -> A, x=2 -> B, x=27 -> AA, x=54 -> BA

# def func(x):
#     alist = [chr(i) for i in range(65, 65+26)]
#     q = x // len(alist)
#     r = x % len(alist)
#     if x <= 26:
#         return alist[x-1]
#     else:
#         return alist[q-1] + alist[r-1]

# print(func(1))
# print(func(2))
# print(func(27))
# print(func(54))



# # -*- coding: utf-8 -*-

# def func(num):
#     alha_list = [chr(i) for i in range(65,65+26)]
#     result = []
#     while num > 0:
#         if num < len(alha_list):
#             result.append(alha_list[num - 1])
#             num = 0
#         else:
#             div_num = int(num /  len(alha_list))
#             num = num - div_num * len(alha_list)
#             if div_num < len(alha_list):
#                 result.append(alha_list[div_num - 1])
#             else:
#                result.append('Z')
#     return ''.join(result)

# print(func(1))
# print(func(2))
# print(func(27))
# print(func(54))



# ある数字xが与えられた場合、0からxまでの整数をフィボナッチ数列の長さでsliceしたlistを返す関数slice_fib(x)を作成する。

# （例：x＝１０） [ [0], [1], [2, 3], [4, 5, 6], [7, 8, 9] ]
# （例：x＝１００） [[0], [1], [2, 3], [4, 5, 6], 
# [7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18, 19], 
# [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32], 
# [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], 
# [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], 
# [88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]]

# 1, 2, 3, 4, 5, 6, 7,   8,  9, 10, 11, 12
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
# def fib(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     return fib(n-1) + fib(n-2)

# print(fib(3))

# print([fib(n) for n in range(0,10)])

# a = [fib(n) for n in range(0,10)]
# print([[] for i in range(5)])

# [0], [1], [2, 3], [4, 5, 6], [7, 8, 9]

# def func(x):
#     for i in range(x):
#     	print(i, fib(i))

# print(func(5))



# def func(x):
#     a = []
#     m = 0
#     for i in range(x):
#         a.append([i] * fib(i))
#         m += 1
#     print(a)

# func(5)

# stafflist = [["Yamada", 25], ["Suzuki", 38], ["Tanaka", 28]]

# for p in [0, 1, 2]:
#     for m in [0, 1]:
#         print(p, m)

# def split_list(l, n):
#     for idx in range(0, len(l), n):
#         yield l[idx:idx + n]
 
 
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = list(split_list(l, 3))
# print(result)


# ある数字xが与えられた場合下記のように出力する関数をloopを使って作成する。

# （x＝２の場合）
# [' ', 'X',  ' ']
# ['X', 'X',  'X’]

# （x＝３の場合）
# [' ', ' ', 'X',   ' ', ' ']
# [' ', 'X', 'X',   'X', ' ']
# ['X', 'X', 'X',   'X', 'X’]

# （x＝５の場合）
# [' ', ' ', ' ', ' ', 'X',   ' ', ' ', ' ', ' ']
# [' ', ' ', ' ', 'X', 'X',   'X', ' ', ' ', ' ']
# [' ', ' ', 'X', 'X', 'X',   'X', 'X', ' ', ' ']
# [' ', 'X', 'X', 'X', 'X',   'X', 'X', 'X', ' ']
# ['X', 'X', 'X', 'X', 'X',   'X', 'X', 'X', 'X’]

# def func(x):
#     for i in range(x):
#         xlist = []
#         for p in reversed(range(x)):
#             if p > i:
#                 xlist.append(' ')
#             else:
#                 xlist.append('X')
#         ylist = []
#         for y in range(x-1):
#             if y >= i:
#                 ylist.append(' ')
#             else:
#                 ylist.append('X')
#         print(xlist + ylist)

# func(2)
# func(3)
# func(5)


# リストのソート問題
# 一つの日時リストを引数にとり、年の昇順、月の降順、日の昇順のリストを返却する関数を作成せよ
# 例)
# x = ['2017/01/02', '2001/01/01', '2017/01/01', '2018/01/01', '2017/02/01'] 
# => ['2001/01/01', '2017/02/01', '2017/01/01', '2017/01/02', '2018/01/01']

# from datetime import datetime

# def func(x):
#     for i in x:
#         d = datetime.strptime(i, '%Y/%m/%d')
#         # 日付の古い順で並び替え(datetime型)
#         x.sort(key=lambda d: d)
#     print(x)
#     y, m, d = [], [], []
#     for i, p in enumerate(x):
#         print(i, p, p[0:4], p[5:7], p[8:10])
#         if p[0:4] not in y:
#             y.append(p[0:4])
#     print(y)


# func(['2017/01/02', '2001/01/01', '2017/01/01', '2018/01/01', '2017/02/01'] )
# #     aa = []
#     for a in x:
#         aa += [a[0:4]]
#     print(sorted(aa))

        # for p in x:
            # print(p.year)
    # for a, i in enumerate(x):
    #     ds = datetime.strptime(i, '%Y/%m/%d')
        # print(ds)
        # print(ds.year, ds.month, ds.day)
        # y.append(ds.year)
    # y.sort()
    # print(y)
    # print(sorted(y), a)
    #     print(a)
    #     y.append(dates.year)
    #     m.append(dates.month)
    #     d.append(dates.day)
    # print(sorted(y), sorted(m, reverse=True), sorted(d))
    
# dlist = [datetime.datetime.strptime(i, '%Y/%m/%d') for i in x]
# print(dlist)




# 下記のリストxがあり、ランダムにて要素番号を取得し、
# その要素にて昇順にて並び替えたリストと要素番号を出力する関数を作成せよ
# 例）
# x =[[3, 5, 7], [2, 4, 6], [8, 1, 5]]
# random_index = 2
# 出力:
# 2, [[8, 1, 5], [2, 4, 6], [3, 5, 7]]














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
# print(m, n)

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

# print('cpu平均使用率', dict(zip(m, cc)))
# print('memory平均使用率', dict(zip(m, mm)))

# 指定された年度の期間内の日付を全て返す関数を作成せよ
# yは2017~2019
# m:1~12
# d:1~31 ただし m=4,6,9,11 のときは30まで
# yが4で割り切れるときには m2のdは29までになる
# ただしyが100で割り切れるときにはm2は28まで
# さらに yが４で割りきれて、100で割り切れても、400で割り切れる場合は m2の時 dは29になる
# (答え) ['2017/1/1',.....'2017/1/31', '2017/2/1'....'2019/12/31']

# def func(kikan1, kikan2):
#     xlist = []
#     for y in range(kikan1, kikan2+1):
#         for m in range(1, 13):
#             day = 30
#             if m in [1, 3, 5, 7, 8, 10, 12]:
#                 day = 31
#             elif m == 2:
#                 day = 28
#                 if (y % 4 == 0 and y % 100 != 0) and y % 400 == 0:
#                     day = 29
#             for d in range(1, day+1):
#                 xlist.append('{}/{}/{}'.format(y, m, d))
#     return xlist

# print(func(2017, 2019))





# 高橋君は無限に広い掛け算表の上にいます。
# 掛け算表のマス (i,j)には整数 i×jが書かれており、高橋君は最初 (1,1)にいます。
# 高橋君は 1回の移動で (i,j)から (i+1,j)か (i,j+1)のどちらかにのみ移ることができます。
# 整数 Nが与えられるので、Nが書かれているマスに到達するまでに必要な移動回数の最小値を求めてください。
# ≪制約≫
# 2≤N≤10^12
# 計算時間が2s以下であること（N^12のforループを２回繰り返し使うとタイムオーバーする）




# print(s)
# def func(year_from, year_to):
#     result = []
#     for y in range(year_from,  year_to + 1):
#         for m in range(1, 13):
#            day = 31
#            if m in [4,6,9,11]:
#                day = 30
#            elif m == 2:
#                day = 28
#                if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
#                    day = 29
#            result =  result + ['{}/{}/{}'.format(y, m, d) for d in range(1, day + 1)]
#     return result
# print(func(2017, 2019))



# 以下のような依存関係を示した辞書を引数に取り、依存関係を満たすような順序のkeyのリストを返す関数を作成せよ
# 意味) { キー: 依存するキー }, 依存するキーがNoneの場合は依存するものがないものとする
# 例) x={1: None, 2: 1, 3: 2} => [1, 2, 3]
# x={1: 3, 2: None, 3: 2} => [2, 3, 1]

# 異なる 2 つの自然数 n, m があるとき、自分自身を除いた約数の和が、もう一方の数と等しくなるような数を友愛数といいます。
# n = (m を除いた m の約数の和)
# m = (n を除いた n の約数の和)

# (例)
# (220, 284)
# -> 220 の自分自身を除いた約数は 1, 2, 4, 5, 10, 11, 22, 44, 55, 110 で和は 284、
# 284 の自分自身を除いた約数は 1, 2, 4, 71, 142 で和は 220 なので、(220, 284) は友愛数である。

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

# def yakusu(p):
#     l = []
#     for i in range(1, p+1):
#         if p % i == 0:
#             l.append(i)
#     return l

# def gosei(p):
#     l = []
#     for i in range(1, p+1):
#         if p % i == 0:
#             l.append(i)
#     if len(l) > 2:
#         return True
#     else:
#         return False


# １以外の同じ約数を持つ数字を「友達」とします。
# つまり、2 つの数字の最大公約数が 1 でない場合を友達とします。
# 1 ~ N までの「合成数」からいずれか一つを選び、
# この数から他のすべての数にたどり着くには何段階の友達をたどればよいかを数えます。
#（合成数は「1とその数自身以外の約数を持つ自然数」です。）

# 例えば、N = 10 のとき、 1~ 10 までの合成数は 4, 6, 8, 9, 10 の 5 つです。
# 最初に 10 を選ぶと、 10 の友達は公約数が 2 である 4, 6, 8 です。
# 9 は 6 の友達ですので、9 は 10 から 2 段階たどることで、求められます。
# 最初に 6 を選ぶと、他の 4, 8, 9, 10 はいずれも １段でたどりつけます。
# このように調べてみると、 N=10 のときは最初にどの数を選んでも最大で 2 段階たどれば良いことになります。

# 1~Nまでの合成数から7個の数を選んだ時、最大で6段階たどることになる最小のNを求めてください。

# 共通の公約数がある二つの数を「知り合い」とみなしたとき、
# 1-n の数字の中で、7 つの値直列で 6 次の知り合いとなる最小の n を求めよ。
# 公約数がある ≒ 非素数で、例えば 3 次の知り合いなら
#   A*A → A*B → B*C → C*C で素数が 3 つあればいい。
# 最小を求めるから、2, 3, 5 を割り当てると最小の組み合わせは、
#   4(2x2) → 10(2x5) → 15(5x3) → 9(3x3)
# となり、最小の n は 15 となるわけだ。
# 今回は 6 次の知り合いであればよいので、
#   AA,AB,BC,CD,DE,EF,FF

# def to_pairs(l):
#     pairs = []
#     pre = l[0]
#     for n in l[1:]:
#         pairs.append((pre, n))
#         pre = n
#     return pairs

# def func(N):
#     for i in range(1, N+1):
#         if gosei(i):
#             print(i, yakusu(i))

# func(20)

# 1から１００までのマス目があるすごろくがあります。
# サイコロ１こ振って出た目の分だけ進めますが、１が２回出た場合さらに２つ進むことができます。
# ゴールにはぴったりではなくても和がることができ、２個進むとかもどるというマス目は存在しません。
# スタートからゴールまで
# 1しか出なかったパターンと1,2を繰り返して出したパターンでそれぞれ何回サイコロを振ったか求めるプログラムを作成してください。

# def saikoro(x):
#     # 1, 1+2, 1, 1+2 ・・
#     # amari = 0
#     amari = x % 4
#     n = (x // 4) * 2
#     return n

# print(saikoro(100))

# def saikoro2(x):
#     # 1, 2, 1, 2・・
#     # amari = 1
#     amari = x % 3
#     n = (x // 3) * 2
#     return n + 1

# print(saikoro2(100))



# import subprocess
# import time

# cmd1 = "ls -la"
# cmd2 = "pwd"
# cmd3 = "help"
# p = subprocess.Popen(cmd1, shell=True)
# time.sleep(2)
# p2 = subprocess.Popen(cmd2, shell=True)
# time.sleep(2)
# p3 = subprocess.Popen(cmd3, shell=True)
# time.sleep(2)


# def hoehoe(func):
#     def wrapper(*args, **kwargs):
#         if args[0] % 3 == 0:
#             return "ほえほえ"
#         else:
#             return func(args[0])
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

# 時間、cpu使用率、memory使用率が順に並んだ以下のような文字列がある。
# この文字列をパースして、分単位の平均cpu使用率、memory使用率を辞書形式で返す関数を作成せよ
# def mu(list1, list2):
#     aa = list1[:]
#     a = aa.pop(-1)
#     for i in range(len(aa)):
#         aa.insert(i * 2 + 1, list2[i])
#     return aa+[a]

# import itertools

# def func(x):
#     tmp = ['+', '*']
#     m = len(x) - 1
#     for p in itertools.product(tmp, repeat=m):
#         s_list = [i for i in p]
#         s = mu(x, s_list)
#         if '*' not in s:
#             print(s)
#         # ()付けたい 
#         elif '+' in s:
#             mm = [m for m, l in enumerate(s) if l == '+']
#             moji = map(str, s)
#             a = ''.join(moji)
#             print(a)
#             print(mm)
#         else:
#             print(s)

# print(func([1, 2, 3, 4]))

# カジノの定番ブラックジャックではゲームを一回行うには、
# 最低一枚コインが必要です。勝てば二枚のコインを得られますが、
# 負けると賭けたコインが没収されます。
# 最初に一枚だけコインを持っており、一枚ずつかけて行った時、
# ゲームを四回行って手元にコインが残るような枚数の変化は6通り考えられます。
# https://dev.sizebook.jp/gitbucket/kitamura/sonogym/blob/master/img/q23_figure.png
# 最初に10 枚コインを持っていた時、
# ゲームを24 回行って手元にコインが残るような枚数の変化が何通りあるかを求めてください。

# def blackjack(game, coin):
#     num = 0
#     while num < game:
#         # win
#         coin += 2
#         # lose
#         coin -= 1
#         num += 1
#     print(coin)
# blackjack(4, 1)
# blackjack(24, 10)


# 与えられた３つのコマンドを非同期に実行して、結果を表示するプログラムを作ってください。
# 関数にしなくてもよいです。


# 1から100までのマス目があるすごろくがあります。
# サイコロ１こ振って出た目の分だけ進めますが、１が２回出た場合さらに２つ進むことができます。
# ゴールにはぴったりではなくても和がることができ、２個進むとかもどるというマス目は存在しません。
# スタートからゴールまで
# 1しか出なかったパターンと1,2を繰り返して出したパターンでそれぞれ何回サイコロを振ったか求めるプログラムを作成してください。

# 50と67？
# def func(x):
#     sho = x // 11
#     amari = x % 11
#     n = sho * 2
#     if amari == 0:
#         return n
#     elif amari <= 6:
#         return n + 1
#     else:
#         return n + 2

# def saikoro(x):
#     # 1, 1+2, 1, 1+2 ・・
#     # amari = 0
#     amari = x % 4
#     n = (x // 4) * 2
#     return n

# print(saikoro(100))

# def saikoro2(x):
#     # 1, 2, 1, 2・・
#     # amari = 1
#     amari = x % 3
#     n = (x // 3) * 2
#     return n + 1

# print(saikoro2(100))




# import io
# import pandas as pd

# txt = """
# time,cpu,memory
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
# """
# # データをうけとる　index_colはindexとして使いたい列の列番号を0始まりで指定する。
# df = pd.read_csv(io.StringIO(txt), index_col="time")
# # 2018-03-02 02:24:22みたいに変換してくれる。
# # datetime型への変換処理は、pandasのto_datetimeを使います。
# df.index = pd.to_datetime(df.index)
# # 1分毎のデータを集約
# r = df.resample("1T")
# # 平均値を辞書で返す
# print(r.mean().to_dict())



# 与えられた３つのコマンドを非同期に実行して、結果を表示するプログラムを作ってください。
# 関数にしなくてもよいです。



# requestsを使用して以下の作業を行うコードを作成せよ。

# json_urlからjsonで
# {"ip": "xxx.xxx.xxx.xxx"}
# が返ってくる。

# そのip addressをslackの#randomに飛ばす。
# なお、エンドポイントは以下とする
# slack_url = "https://hooks.slack.com/services/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"
# json_url = "http://sizebook.co.jp/test/anzu/ipaddress.php"

# slack_url = "https://hooks.slack.com/services/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"
# json_url = "http://sizebook.co.jp/test/anzu/ipaddress.php"

# import json
# import requests

# data = requests.get(json_url).json()
# p = {
#     "text": data['ip'],
#     'username': 'sonoki',
#     "icon_emoji": ':dog2:',
# }
# requests.post(slack_url, json.dumps(p))

# import json
# import requests


# def get_json():
#     res = requests.get(json_url)
#     return res.json()

# def send_slack(rjson):
#     requests.post(slack_url, data = json.dumps({
#         'text': rjson['ip'], # 投稿するテキスト
#         'username': 'sonoki', # 投稿のユーザー名
#         'icon_emoji': u':dog2:', # 投稿のプロフィール画像に入れる絵文字
#     }))

# send_slack(get_json())




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

# def hoehoe(func):
#     def wrapper(*args, **kwargs):
#         if args[0] % 3 == 0:
#             return "ほえほえ"
#         else:
#             return args[0]
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











# from subprocess import Popen, PIPE
# import time

# processes = [
#     Popen(['ls', '-l'], stdout=PIPE, stderr=PIPE),
#     Popen(['df', '-h'], stdout=PIPE, stderr=PIPE),
#     Popen(['ls', '-l', '/'], stdout=PIPE, stderr=PIPE),
# ]

# while processes:
#     for proc in processes:
#         retcode = proc.poll()
#         if retcode is not None:
#             processes.remove(proc)
#             break
#     else:
#         time.sleep(.1)
#         continue

#     if retcode != 0:
#         print("error")

#     print(proc.stdout.read())

# 同じ場所を通らない掃除ロボットを考えます。
# このロボットは前後左右の4方向にのみ移動することができます。
# 例えば、3回移動する場合、最初に後ろに移動する経路は 9 パターンあります 。
# (https://dev.sizebook.jp/gitbucket/kitamura/sonogym/blob/master/img/q8_figure.png)
# 最初の移動方向は前後左右があるので、
# 考えられる移動経路は全部で 9 x 4 = 36 通りあります。
# このロボットが12 回移動するとき、
# 考えられる移動経路のパターンが何通りあるかを求めてください。

# ugoki = [[0, 1],[1, 0],[0, -1],[-1, 0]]

# for p in ugoki:
#     print(p)


# 1~16のうちの一つの整数が与えられた時に、
# その数字が左上に来るような4×4の魔方陣を作成してください。
# ただし、魔方陣とは、全ての行と列の和がそれぞれ等しくなるようなもののことを表すとし、
# 1~16の数字を一回ずつ使うものとします。

# from datetime import datetime, timedelta

# dt = datetime(2018, 3, 26, 17, 48, 59)
# aa = 365 * 24 * 60 * 60
# for i in range(aa):
#     dt += timedelta(seconds=1)
#     print('a', dt)
#     m = dt.strftime('%m%d%H%M%S')
#     print('m', m)
#     if len(set(list(m))) == 10:
#         print(m)

# カジノの定番ブラックジャックではゲームを一回行うには、最低一枚コインが必要です。
# 勝てば二枚のコインを得られますが、負けると賭けたコインが没収されます。
# 最初に一枚だけコインを持っており、一枚ずつかけて行った時、
# ゲームを四回行って手元にコインが残るような枚数の変化は6 通り考えられます。
# 最初に10 枚コインを持っていた時、
# ゲームを24 回行って手元にコインが残るような枚数の変化が何通りあるかを求めてください。

# コインが 10 枚あり、勝てば +1 負ければ -1 していきます。
# 24 回ゲームをやったとき、手元にコインが残る経過は何通りある？

# 今のゲームに買った場合と負けた場合でそれぞれカウント。
# コインが 0 でゲームオーバー depth=0 で勝ち抜きで + 1
# ルートによって同じ coins/depth が頻出することは想像できるのでメモ
# …模範解とそんな離れてなかった…
# memo = {}


# def this_game(coins, depth):
#     if (coins, depth) in memo.keys():
#         return memo[(coins, depth)]
    
#     if coins == 0:
#         return 0
#     if depth == 0:
#         return 1

#     won = this_game(coins + 1, depth - 1)
#     lose = this_game(coins - 1, depth - 1)
#     memo[(coins, depth)] = won + lose

#     return memo[(coins, depth)]

# print(this_game(10, 24))

# C = 10
# G = 24

# def blackjack(coin, game):
#     if coin <= 0:
#         return 0

#     if coin >= 1 and game >= G:
#         return 1

#     cnt = 0
#     cnt += blackjack(coin + 1, game + 1)
#     cnt += blackjack(coin - 1, game + 1)

#     return cnt

# print(blackjack(10, 0))


# INIT = 10
# N = 24
# SHIFT = [1,-1]

# def search(current, num):
#     if num == N:
#         return 1
        
#     cnt = 0
    
#     for d in SHIFT:
#         next_pos = current + d
#         if next_pos != 0:
#             cnt += search(next_pos, num +1)
#     return cnt

# print(search(INIT, 0))

# 16051010通り

# a = [[ 5, 8, 0, 3, 0, 0, 0, 0, 1],
# [0, 0, 2, 0, 0, 0, 8, 6, 0],
# [0, 0, 9, 0, 0, 2, 7, 0, 4],
# [6, 0, 0, 2, 3, 0, 4, 1, 0],
# [8, 0, 0, 5, 1, 0, 0, 7, 0],
# [9, 1, 4, 0, 7, 0, 0, 3, 0],
# [3, 9, 0, 7, 2, 0, 0, 0, 0],
# [0, 6, 5, 4, 0, 0, 1, 0, 0],
# [4, 0, 0, 9, 0, 6, 0, 8, 0]]


# for i in a:
#     print(i)
#     for p in i:
#         if p == 0:



# ylist = list(range(1, 5))

# # print(xlist)
# # print(ylist)

# import itertools

# for p in itertools.permutations(xlist, 4):
#     if p[0] == 1:
#         if sum(p) == 34:
#             print(p)
#         # p[0:4] == p[4:5]
#         # print(p[0:4], p[4:8])
#         # print(p)

# print(list(set(xlist) - set(ylist)))


# import itertools

# def sabun(x1, y2):
#     return list(set(x1) - set(y2))

# def func(x):
#     xlist = list(range(1, 17))
#     n = sum(xlist) // 4
#     for p in itertools.permutations(xlist, 4):
#         if p[0] == x:
#             if sum(p) == n:
#                 ylist = sabun(xlist, list(p))
#                 for a in itertools.permutations(ylist, 4):
#                     b = list(p) + list(a)
#                     zlist = sabun(xlist, list(p) + list(a))
#                     for c in itertools.permutations(zlist, 4):
#                         d = b + list(c)
#                         wlist = sabun(xlist, d)
#                         for c in itertools.permutations(wlist, 4):
#                             k = d + list(c)
#                             if sum(k[0:4]) == sum(k[4:8]) == sum(k[8:12]) == sum(k[12:16]):
#                                 if sum(k[0:16:4]) == sum(k[1:16:4]) == sum(k[2:16:4]) == sum(k[3:16:4]):
#                                     return list(zip(*[iter(k)]*4))

# print(func(1))








# import itertools

# def sabun(x1, y2):
#     return list(set(x1) - set(y2))

# def func(x):
#     xlist = list(range(1, 17))
#     n = sum(xlist) // 4
#     for p in itertools.permutations(xlist, 4):
#         if p[0] == x:
#             if sum(p) == n:
#                 ylist = sabun(xlist, list(p))
#                 for a in itertools.permutations(ylist, 12):
#                     k = list(p) + list(a)
#                     if sum(k[0:4]) == sum(k[4:8]) == sum(k[8:12]) == sum(k[12:16]):
#                         if sum(k[0:16:4]) == sum(k[1:16:4]) == sum(k[2:16:4]) == sum(k[3:16:4]):
#                             return list(zip(*[iter(k)]*4))


                #     b = list(p) + list(a)
                #     zlist = sabun(xlist, list(p) + list(a))
                #     for c in itertools.permutations(zlist, 4):
                #         d = b + list(c)
                #         wlist = sabun(xlist, d)
                #         for c in itertools.permutations(wlist, 4):
                #             k = d + list(c)
                #             if sum(k[0:4]) == sum(k[4:8]) == sum(k[8:12]) == sum(k[12:16]):
                #                 if sum(k[0:16:4]) == sum(k[1:16:4]) == sum(k[2:16:4]) == sum(k[3:16:4]):
                #                     return list(zip(*[iter(k)]*4))

# print(func(1))








# a = list(range(10))
# print(a)

# print([iter(a)])

# 同一円周上に等間隔に並んだこどもたちが、ペアを組んで糸電話で会話しようとしています。
# このとき、交差してしまうと、糸が絡まってしまいますので、交差しないような相手とペアを組む必要があります。

# 例えば、並んだ子供が6人いた場合、図のようにペアを作ると、うまく会話ができます。
# つまり、6人では5通りのペアができます。

# https://dev.sizebook.jp/gitbucket/ysonoki/blog/issues/7

# 問
# 16人の子供たちがいた場合、作ることができるペアが何通りあるかを求めてください。
# num = 16
# count_list = [0] * (num + 1)
# count_list[0] = 1
# print(count_list)

# def count(n):
#     if not count_list[n] == 0:
#         return count_list[n]

#     for i in range(1, n, 2):
#         print(i)
#         count_list[n] += count(i - 1) * count(n - i - 1)

#     print(n)
#     return count_list[n]

# print(count(num))

# x = iter([1,2,3,4,5,6,7,8,9])

# print(x)

# xlist = []
# for i in zip(x, x, x):
#     xlist.append(i)
# print(xlist)

# print([i for i in zip(x, x, x)])


# 目的地までの距離が2000mで、
# 出発地と目的地の間には200m間隔に9つの信号があり、すべての信号は同じタイミングで変化しています。
# 信号は30秒青、30秒赤を繰り返しており、
# すべての信号がちょうど青になったタイミングで時速18km/hの車が目的地に向かって出発しました。
# 車が目的地に到着するまでにかかる時間を計算してください。
# 18km/h
# # 18000m /h

# # 1秒5メートル進む
# s1 = 18000/60/60
# print(s1)
 
# # 1つ目の信号まで40秒かかる
# kan = 200 / s1
# print(kan)

# # 青になるまで20秒待つ
# wait = 60 - kan

# kotae = (wait + kan) * 9 + kan
# print('{}秒'.format(kotae))


# 1-9 のストラックアウトがあります
# 1 2 3
# 4 5 6
# 7 8 9
# 真ん中（5）以外は最大まとめて２枚引っこ抜けます。
# 全部落とすパターンは何通り？

# 真ん中は必ず1回はかかるという制約条件…
# 1 回は２枚抜きするパターン
# xlist = [[1, 2], [2, 3], [3, 6], [6, 9], [8, 9], [7, 8], [4, 7], [1, 4]]

# for i in range(1, 10):
#     xlist.append([i])

# def shot(bord):
#     if len(xlist) == 0:
#         return 1
#     # print(xlist)
#     cnt = 0
#     for n in xlist:
#         cp_list = xlist.copy()
#         for s in n:
#             cp_list = [i for i in cp_list if s not in i]
#         cnt += shot(cp_list)
#     return cnt
# print(shot(xlist))


# Q24
# ストラックアウトはホームベースにある９枚の的に対し、
# マウンドからボールを投げて撃ちぬくゲームです。
# 今回は、９枚の的を抜く順番を考えます。
# ただし、周囲にフレームがある５番の的以外では、
# 隣り合う的が存在する場合に二枚抜きすることができます。
# 例えば、１，６，９番がぬかれた状態であれば、
# ２と３、４と７、７と８は二枚抜きが可能です。

# https://dev.sizebook.jp/gitbucket/kitamura/sonogym/blob/master/img/q24_figure.png

# このとき、９枚の的を抜く順番が何通りあるかを求めてください。投げたボールは必ずいずれかの的に当たるものとします。

# 798000通り

# import itertools

# # B = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ni = [[1, 2], [2, 3], [3, 6], [6, 9], 
#          [8, 9], [7, 8], [4, 7], [1, 4]]


# def kaijo(n):
#     if n == 1:
#         return n
#     return n * kaijo(n-1)

# # print(kaijo(4))

# def flatten(nested_list):
#     return [e for inner_list in nested_list for e in inner_list]

# # 全部1枚抜きのときの順序
# # print(len(list(itertools.permutations(B))))

# xlist = []
# for i in range(1, 10):
#     for p in itertools.permutations(ni, i):
#         if len(set(flatten(list(p)))) == len(p) * 2:
#             print(p)
#             # print(list(p))
#             # print(len(list(p)), 9 - len(flatten(list(p))))
#             # print(p, len(list(p)), )
#             # print(len(list(p)), 9 - len(flatten(list(p))))
#             # print(kaijo(len(list(p))), kaijo(9 - len(flatten(list(p)))))
#             # print(kaijo(len(list(p))) + kaijo(9 - len(flatten(list(p)))))
#             # print(kaijo(9 - len(flatten(list(p)))))
#             # a = len(list(p)) + kaijo(9 - len(flatten(list(p))))
#             bb = len(list(p)) * kaijo(9 - len(flatten(list(p))))
#             # print(bb)
#             # a = kaijo(bb)
#             xlist.append(bb)

# # print(xlist)
# # print(sum(xlist))

# # print(kaijo(9))

# print(sum(xlist) + kaijo(9))
# xlist = []
# for i in range(1, 9):
#     xlist.append(len(list(itertools.permutations(ni, i))))
# # print(xlist)

# for i, n in enumerate(xlist):
#     print(i+1, n)


# 1~16のうちの一つの整数が与えられた時に、その数字が左上に来るような4×4の魔方陣を作成してください。
# ただし、魔方陣とは、全ての行と列の和がそれぞれ等しくなるようなもののことを表すとし、
# 1~16の数字を一回ずつ使うものとします。

# (例)
# 1 ->
# [[1, 2, 15, 16],
# [13, 14, 3, 4],
# [12, 7, 10, 5],
# [8, 11, 6, 9]]

# import itertools

# def gokei(x):
#     return sum(x)

# a = reversed(range(1, 9))

# for i in itertools.permutations(a, 8):
#     # if sum(i[0:5])
#     print(i, sum(i[0:4]), sum(i[4:8]))
# p = range(1, 16)
# x = [1]
# print(len(list(itertools.permutations(p, 16))))
# for i in itertools.permutations(p, 8):
    # if sum(i[0:4]) > 20:
    # print(i)


# ある自然数nが与えられた時に、nが左上にきて、
# 全ての行・列で積が等しくなるような、3×3の魔方陣を作成してください。

# (例)
# n = 2 ->
# [[2, 256, 8],
# [64, 16, 4],
# [32, 1, 128]]



# import itertools

# def func(x):
#     p = range(1, 10)
#     for i in itertools.permutations(p, 9):
#         if i[0] == 1:
#             if sum(i[0:3]) == sum(i[3:6]) == sum(i[6:9]):
#                 if i[0] + i[3] + i[6] == i[1] + i[4] + i[7] == i[2] + i[5] + i[8]:
#                     p = [x ** m for m in i]
#                     return list(zip(*[iter(p)]*3))

# print(func(2))

# p = [1, 2, 3, 4, 5, 6, 7, 8]
# print(list([iter(p)]*2))
# print(list(zip(*[iter(p)]*2)))


# 1~16のうちの一つの整数が与えられた時に、その数字が左上に来るような4×4の魔方陣を作成してください。
# ただし、魔方陣とは、全ての行と列の和がそれぞれ等しくなるようなもののことを表すとし、1~16の数字を一回ずつ使うものとします。


# a = list(range(1, 17))
# b = [1, 3, 4]

# print(list(set(a) - set(b)))

# (例)
# 1 ->
# [[1, 2, 15, 16],
# [13, 14, 3, 4],
# [12, 7, 10, 5],
# [8, 11, 6, 9]]


# import itertools


# al = range(1, 17)

# print(sum(al) / 4)


# def func(x):
#     print(i)


# print(func())


# print(list(zip(*[iter(i)]*4)))

# def func(x):
#     for i in itertools.permutations(al, 16):
#         if i[0] == x:
#             a = i[0]+i[4]+i[8]+i[12]
#             b = i[1]+i[5]+i[9]+i[13]
#             c = i[2]+i[6]+i[10]+i[14]
#             d = i[3]+i[7]+i[11]+i[15]
            # if sum(i[0:4]) == sum(i[4:8]) == sum(i[8:12]) == sum(i[12:16]):
#             if a == sum(i[12:16]):
#                 print('1', i)
#                 if a == sum(i[8:12]):
#                     print('2', i)
#                     if a == b == c == d:
#                     # print(a, b, c, d)
#                     # print(sum(i[0:4]), sum(i[4:8]), sum(i[8:12]), sum(i[12:16]))
#                     # if sum(i[0:4]) == sum(i[4:8]) == sum(i[8:12]) == sum(i[12:16]):
#                     # == sum(i[0:4])== sum(i[4:9])== sum(i[8:13]) == sum(i[12:-1]):
#                     # print(sum(i[0:4]), i[0:4])
#                         return list(zip(*[iter(i)]*4))
# print(func(1))

# group_by = 3
# chunks = zip(*[iter(li)]*group_by)
# print(chunks)


# def func(x):
# alist = list(range(1, 17))
# for i in itertools.permutations(alist, 4):
#     if i[0] == 1:
#         # print(list(i), sum(i))
#         gokei = sum(i)
#         blist = list(set(alist) - set(list(i)))
#         print(blist)
#         for j in itertools.permutations(blist, 4):
#             clist = list(set(blist) - set(list(j)))
#             print(clist)

# print(func(1))




# ホールケーキを切り分けるとき、
# ケーキに乗っているいちごの数がすべて異なるような切り方を考える。
# ここでは、N 個に切り分けるときには
# 「1 ~ N 個のいちご (合計 N (N + 1) / 2 個)」 がそれぞれに乗っているようにする。
# ただし、隣り合う２つのケーキに乗っているいちごの数の和が、
# いずれも平方数になるように切らなければならないという条件を追加する。
# このような条件を満たすような切り方ができる最小の N (> 1) を求めてください。

# import itertools

# def func(x):
#     heiho = [i * i for i in range(10)]
#     # print(heiho)
#     ichigo = range(1, x+1)
#     # print(ichigo)
#     xlist = []
#     for i in itertools.combinations(ichigo, 2):
#         if sum(i) in heiho:
#             # print(i, sum(i))
#             xlist.append(i)
#             print(xlist)

# print(func(1000))

# N = 2
# def check(num, ichigo, heiho):
#     if len(ichigo) == num:
#         print(ichigo[-1])
#         if ichigo[-1] + ichigo[0] in heiho:
#             print("N =", num)
#             print(ichigo)
#             return True
#     else:
#         for i in list({j for j in range(1, num + 1)} - set(ichigo)):
#             if ichigo[-1] + i in heiho:
#                 if check(num, ichigo + [i], heiho):
#                     return True
#     return False

# while True:
#     if check(N, [1], [i * i for i in range(10)]):
#         break
#     N += 1

# 1~4のうちの整数が一つ与えられた時、その整数が左上になるような数独を完成させてください。
# ただし、数独は 1 ~ 4 の数字を用いて、4 x 4 のサイズとします。
# (各行、列では、1~4の数字が一回ずつ使用され、
# 全体を4分割した 2 x 2 のブロック内でも1~4の数字が一回ずつ使用されているものとします)
# (例)
# 1 ->
# [[1, 2, 3, 4], i
# [3, 4, 1, 2],  j
# [2, 3, 4, 1],  k
# [4, 1, 2, 3]]  l

# import itertools

# def func(x):
#     a = range(1, 5)
#     for i in itertools.permutations(a, 4):
#         if i[0] == x:
#             for j in itertools.permutations(a, 4):
#                 for k in itertools.permutations(a, 4):
#                     for l in itertools.permutations(a, 4):
#                         if (len(set([i[0], j[0], k[0], l[0]])) == 4 and 
#                             len(set([i[1], j[1], k[1], l[1]])) == 4 and
#                             len(set([i[2], j[2], k[2], l[2]])) == 4 and 
#                             len(set([i[3], j[3], k[3], l[3]])) == 4):
#                             if (len(set([i[0], i[1], j[0], j[1]])) == 4 and 
#                                 len(set([k[0], k[1], l[0], l[1]])) == 4 and
#                                 len(set([i[2], i[3], j[2], j[3]])) == 4 and
#                                 len(set([k[2], k[3], l[2], l[3]])) == 4):
#                                 return [i, j, k, l]

# print(func(1))
# print(func(2))
# print(func(3))
# print(func(4))


# １以外の同じ約数を持つ数字を「友達」とします。つまり、2 つの数字の最大公約数が 1 でない場合を友達とします。
# 1 ~ N までの「合成数」からいずれか一つを選び、この数から他のすべての数にたどり着くには何段階の友達をたどればよいかを数えます。

# 例えば、N = 10 のとき、 1~ 10 までの合成数は 4, 6, 8, 9, 10 の 5 つです。
# 最初に 10 を選ぶと、 10 の友達は公約数が 2 である 4, 6, 8 です。
# 9 は 6 の友達ですので、9 は 10 から 2 段階たどることで、求められます。最初に 6 を選ぶと、他の 4, 8, 9, 10 はいずれも １ 段でたどりつけます。
# このように調べてみると、 N=10 のときは最初にどの数を選んでも最大で 2 段階たどれば良いことになります。

# 1 ~ N までの合成数から 7 個の数を選んだ時、最大で 6 段階たどることになる最小の N を求めてください。



# COUNTRIES = [
#     "Brazil",
#     "Cameroon",
#     "Chile",
#     "Greece",
#     "Uruguay",
#     "Italy",
#     "France",
#     "Bosnia and Heregovina",
#     "Gernany",
#     "USA",
#     "Russia",
#     "Croatia",
#     "Spain",
#     "Australia",
#     "Cote d'lvoire",
#     "Costa Rica",
#     "Switzerland",
#     "Honduras",
#     "Iran",
#     "Portugal",
#     "Belgium",
#     "Korea Republic",
#     "Mexico",
#     "Netherlands",
#     "Colombia",
#     "Japan",
#     "England",
#     "Ecuador",
#     "Agentina",
#     "Nigeria",
#     "Ghana",
#     "Algeria",
#     ]

# MAX_CNT = 0
# MAX_SHIRITORI = []

# def shiritori(depth, key, chain):
#     """
#     しりとり
#     """
#     global MAX_CNT
#     global MAX_SHIRITORI
#     total_cnt = 0

#     # キーワードで始まる国を探す
#     next_countries = []
#     for i in COUNTRIES:
#         if i[0].upper() == key[0].upper():
#             next_countries += [i]

#     if not next_countries:
#         return 0

#     for i in next_countries:
#         if i not in chain:
#             chain.append(i)

#             total_cnt = shiritori(depth + 1, i[-1].upper(), chain)
#             if total_cnt > MAX_CNT:
#                 MAX_CNT = total_cnt
#                 MAX_SHIRITORI = chain[:]

#             chain.pop()

#     return depth


# for country in COUNTRIES:
#     shiritori(0, country, [])

# print(MAX_CNT, " : ", MAX_SHIRITORI)



# # q = 16
# # 同じ長さの3本の紐を折り曲げて
# # 3 つの四角形を作ることを考えます。
# # そのうち、2本でそれぞれ長方形を作り、残りの一本は正方形をつくります。
# # このとき、作った 2 つの長方形の面積の和が、
# # 正方形の面積と同じになることがあります。
# # (ただし、長方形、正方形のいずれの辺の長さも整数になるとします。)
# # (例) ひもの長さが 20 のとき、 
# # (縦 x 横) = (1 x 9), (2 x 8), (5 x 5) とすると、この条件を満たします。

# # ひもの長さを1から500まで変化させるとき、
# # 2つの長方形の面積の和と、正方形の面積が同じになる組が何通りあるかを求めてください。

# # N = 500

# # i = 10
# # print(i / 4)

# # import math
 
 
# # q = 0
# # cnt1 = 0
# # for p in range(2, 13):
# #   a, b, c = 2*p*q, p**2-q**2, p**2+q**2
# #   if c <= 125 and math.gcd(a, b):
# #     cnt1 += 1
# # p = 1
# # cnt2 = 0
# # for q in range(2, 13):
# #   a, b, c = 2*p*q, p**2-q**2, p**2+q**2
# #   if c <= 125 and math.gcd(a, b):
# #     cnt2 += 1
# # cnt1 + cnt2
# # 20

# # ただし、同じ比で長さが整数倍になっているものは 1 つとしてカウントします。
# # (例) 
# # ひもの長さが 20 のとき、(縦 x 横) = (1 x 9), (2 x 8), (5 x 5) 
# # ひもの長さが 40 のとき、(縦 x 横) = (2 x 18), (4 x 16), (10 x 10) 
# # ひもの長さが 60 のとき、(縦 x 横) = (3 x 27), (6 x 24), (15 x 15) 
# # この3つは長方形の辺の比が同じで、長さが整数倍になっているので、まとめて一つとしてカウントします。


# # 3 本の同じ長さの紐があるとき、
# # 1 本を正方形にして、２本を長方形とし、長方形二つの面積 = 正方形の面積 となる組み合わせはいくつある？
# # ただし、一度出た正方形と長方形の長さの比は同一のものとしてカウントします

# # x^2 = (x - n)(x + n) + (x - m)(x + m) の等式が成り立つ m, n の組み合わせなので
# #     = x^2 - n^2 + x^2 - m^2
# #     = 2x^2 - (n^2 + m^2)
# # となるので、x^2 = n^2 + m^2 となる n, m の組み合わせを探す
# # なおかつ、一度出た m : n 比はカウントしない

# # import itertools

# # max_length = 500      # ひもの最長
# # result_patterns = {}  # 比率 -> 組み合わせ でハッシュ

# # for x in range(1, int(max_length / 4) + 1):  # 正方形の一辺
# #     combination = itertools.combinations(range(1, x), 2)
# #     valid_patterns = [n for n in combination if n[0] * n[0] + n[1] * n[1] == x * x]
# #     for pat in valid_patterns:
# #         result_patterns[pat[1] / pat[0]] = pat

# # print(len(result_patterns))

# # # サイコロは 1 から6 までの整数がそれぞれの面に書かれており、
# # # 向かい合う面に書かれた数の和はどれも 7 です。
# # # サイコロを使って次のようなゲームを行います。

# # # まず、サイコロを好きな面が上向きになるように置きます。
# # # その後、得点が x 点を超えるまで以下の操作を繰り返します。
# # # サイコロを手前、奥、左、右のどれかの方向に 90° だけ回転させ、
# # # 上を向いている面に書かれた数を得点として得る。

# # # x が与えられた時、上のゲームで x 点以上獲得するために必要な最小の操作の回数を求めてください。

# # # (例)
# # # x = 7 -> 2 回
# # # x = 149696127901 -> 27217477801 回
# # def func(m, tensu):
# #     s_list = list(range(1, 7))
# #     total = 0
# #     count = 0
# #     while total < tensu:
# #         p = 7 - m
# #         a = m
# #         s_list.remove(m)
# #         s_list.remove(p)
# #         m = max(s_list)
# #         total += m
# #         count += 1
# #         s_list.append(a)
# #         s_list.append(p)
# #         print(count)
# #     return count

# # # 始まりの数, x 点
# # print(func(6, 7))
# # print(func(6, 149696127901))
# # # print(func(6, 149))

# # # a = [False for i in range(100)]
# # # for m in range(2, 101):
# # #     p = m - 1
# # #     while p < 100:
# # #         # print(a, p)
# # #         # 反転
# # #         a[p] = not a[p]
# # #         p += m

# # # for i, x in enumerate(a):
# # #     if x == False:
# # #         print(i+1)
# # # def func(a, b, c, x):
# # #     for p in list(range(0, a+1)):
# # #         for q in list(range(0, b+1)):
# # #             for r in list(range(0, c+1)):
# # #                 print(p, q, r)
# # #                 if 100 * p + 50 * q + 10 * r == x:
# # #                     return True
# # #     return False

# # # print(func(5, 3, 1, 560))
# # # print(func(2, 3, 2, 130))
# # # print(func(3, 4, 4, 540))


# # # def hantei(a, b, c, x):
# # #     mo = {100: a, 50: b, 10: c}
# # #     used = {100:0, 50:0, 10:0}
# # #     for k, v in sorted(mo.items(),key=lambda x: x[0],reverse=True):
# # #         for i in range(1,v+1):
# # #             if x >= k:
# # #                 x -= k
# # #                 used[k] += 1
# # #             else:
# # #                 break
# # #     print("使った数={}".format(used))
# # #     if x==0:
# # #         return True
# # #     else:
# # #         return False

# # # ある正方形があり、一辺の長さが 1cm の正方形のマス目で区切られています。この境界上を通って左上から右下まで最短距離で往復することを考えます。
# # # このとき、往路で通った道は、復路では通ることができないものとします。（ただし、交差点が重なること、クロスすることは ok とします。）
# # # 例えば、正方形の一辺の長さが 2cm の場合、 10 通りの経路があります。

# # # https://dev.sizebook.jp/gitbucket/kitamura/sonogym/blob/master/img/q31_figure.png

# # # 一辺が 6 cm の正方形の場合、最短経路がいくつあるか求めてください。




# # # 同じ場所を通らない掃除ロボットを考えます。このロボットは前後左右の4方向にのみ移動することができます。
# # # 例えば、3回移動する場合、最初に後ろに移動する経路は 9 パターンあります 。

# # # (https://dev.sizebook.jp/gitbucket/kitamura/sonogym/blob/master/img/q8_figure.png)
# # # 最初の移動方向は前後左右があるので、考えられる移動経路は全部で 9 x 4 = 36 通りあります。
# # # このロボットが12回移動するとき、考えられる移動経路のパターンが何通りあるかを求めてください。

# # # N = 12
# # # # 前後左右に移動
# # # ugoku = [[0,1],[0,-1],[1,0],[-1,0]]

# # # def move(x):

# # #     # 最初の位置を含んで、N+1個調べれば終了
# # #     if len(x) == N+1:
# # #         return 1
        
# # #     cnt = 0    
# # #     for d in ugoku:
# # #         # print(d)
# # #         next_pos = [x[-1][0] + d[0], x[-1][1] + d[1]]
# # #         # 探索済みでなければ移動させる
# # #         if not next_pos in x:
# # #             cnt += move(x + [next_pos])
# # #     return cnt

# # # print(move([[0,0]]))


# # # 百人一首のかるたでは、特に「決まり文字」を知っているかが勝負を分けるポイントになります。
# # # 決まり文字とは、「ここまで読まれれば、札がわかる（何の句か判断できる）」という部分のことです。
# # # 決まり字を覚えることで、上の句の最初の数文字で札を取ることが出きます。

# # # 今回は、上の句で決まり字を求めるだけでなく、下の句についても札に記載する文字数を最小限にすることを考えてください。
# # # 例えば、

# # # 村雨の　露もまだひぬ　まきの葉に　霧たちのぼる　秋の夕ぐれ

# # # という句では、上の句は最初の「む」一文字で判別できます。また、下の句も最初の「き」一文字で判別できます。
# # # つまり、この句では、読み札は一文字、取り札も一文字の合計二文字で表現できることになります。

# # # すべての句（100句）を一意に識別するのに必要な最小の文字数を求めてください。

# # # 百人一首のデータは下記の csv ファイルを使用することにします。
# # # https://www.shoeisha.co.jp/book/download/1761/read
# # # （圧縮フォルダ内の q33.csv を開き、「上の句かな」と「下の句かな」の列を使ってください）

# # # import csv
# # # import re

# # # def dup(key, pattern):
# # #     """
# # #     重複チェック
# # #     """
# # #     count = 0

# # #     for i in pattern:
# # #         if re.match(key, i):
# # #             count += 1

# # #             if count > 1:
# # #                 return True

# # #     return False


# # # def countlen(array):
# # #     """
# # #     最小文字数のカウント
# # #     """
# # #     cnt = 0

# # #     for i in array:
# # #         index = 0
# # #         check = i[index]

# # #         while dup(check, array):
# # #             index += 1
# # #             check += i[index]

# # #         print(check, " : ", i)
# # #         cnt += len(check)

# # #     return cnt

# # # def main():
# # # csvfile = open('./q33.csv', 'r', encoding='utf-8')
# # # reader = csv.reader(csvfile)
# # # _ = next(reader)  # ヘッダーを捨てる

# # # kami = []
# # # shimo = []

# # # for row in reader:
# # #     # print(row)
# # #     kami += [row[3]]
# # #     shimo += [row[4]]

# # # def dup(key, pattern):
# # #     """
# # #     重複チェック
# # #     """
# # #     count = 0

# # #     for i in pattern:
# # #         if re.match(key, i):
# # #             count += 1

# # #             if count > 1:
# # #                 return True

# # #     return False
# # # print(dup(kami))

# # # print(countlen(kaminoku) + countlen(simonoku))

# # # サイコロは 1 から6 までの整数がそれぞれの面に書かれており、向かい合う面に書かれた数の和はどれも 7 です。
# # # サイコロを使って次のようなゲームを行います。

# # # まず、サイコロを好きな面が上向きになるように置きます。
# # # その後、得点が x 点を超えるまで以下の操作を繰り返します。
# # # サイコロを手前、奥、左、右のどれかの方向に 90° だけ回転させ、
# # # 上を向いている面に書かれた数を得点として得る。

# # # x が与えられた時、
# # # 上のゲームで x 点以上獲得するために必要な最小の操作の回数を求めてください。

# # # (例)
# # # x = 7 -> 2 回
# # # x = 149696127901 -> 27217477801 回

# # # def func(m, tensu):
# # #     s_list = list(range(1, 7))
# # #     total = 0
# # #     count = 0
# # #     while total < tensu:
# # #         p = 7 - m
# # #         s_list.remove(m)
# # #         s_list.remove(p)
# # #         m = max(s_list)
# # #         total += m
# # #         count += 1
# # #         s_list.append(m)
# # #         s_list.append(p)
# # #     return count

# # # # 始まりの数、最大の点数
# # # print(func(6, 7))
# # # print(func(6, 149))
# # # print(func(6, 149696127901))



# # # 最初に選ぶ好きな面
# # # N = 2

# # # X点以上獲得
# # # X = 7






# # # 同じ場所を通らない掃除ロボットを考えます。
# # # このロボットは前後左右の4方向にのみ移動することができます。
# # # 例えば、3回移動する場合、最初に後ろに移動する経路は 9 パターンあります 。
# # # (https://dev.sizebook.jp/gitbucket/kitamura/sonogym/blob/master/img/q8_figure.png)
# # # 最初の移動方向は前後左右があるので、考えられる移動経路は全部で 9 x 4 = 36 通りあります。
# # # このロボットが12 回移動するとき、考えられる移動経路のパターンが何通りあるかを求めてください。


# # # N = 12
# # # SHIFT = [[0,1],[0,-1],[1,0],[-1,0]]

# # # def move(log):
    
# # #     if len(log) == N+1:
# # #         return 1
        
# # #     cnt = 0
    
# # #     for d in SHIFT:
# # #         next_pos = [log[-1][0]+d[0], log[-1][1]+d[1]]
# # #         if not next_pos in log:
# # #             cnt += move(log + [next_pos])
# # #     return cnt

# # # print(move([[0,0]]))





# # # 1～100までのバングが書かれた100枚のカードが順番に並べられています。
# # # 最初、すべてのカードは裏返しの状態で置かれています。
# # # ある人が2番のカードから、1枚おきにカードを裏返していきます。
# # # すると、2,4,6・・・,100番のカードが表を向くようになります。
# # # 次に、別の人が、3番のカードを2枚おきにカードを裏返していきます。
# # # （裏向きのカードは表を向き、表を向いているカードは裏返されます。）
# # # また、別の人が4番のカードから3枚おきにカードを裏返していきます。
# # # このように、n番目のカードからn-1枚おきにカードを裏返す操作を、
# # # どのカードの向きも変わらなくなるまで続けたとします。
# # # カードの向きが変わらなくなったとき、
# # # 裏向きになっているカードの番号をすべて求めてください。

# # # a = [False for i in range(100)]
# # # for m in range(2, 101):
# # #     p = m - 1
# # #     while p < 100:
# # #         # print(a, p)
# # #         # 反転
# # #         a[p] = not a[p]
# # #         p += m

# # # for i, x in enumerate(a):
# # #     if x == False:
# # #         print(i+1)


# # # 一つのリストxが与えられた時、0の要素ごとにくぎって総和を返す関数を作成せよ
# # # 例1:[1, 0, 2, 3, 0, 4, 8] => [1, 5, 12] # (1, 2 + 3, 4 + 8)
# # # 例2:[0, 9, 10, 0, 3, 0, 4, 8] => [0, 19, 3, 12]

# # # list = [1, 2, 3, 4, 5]
# # # result = list[0]
# # # for x in list[1:]:
# # #     print(x)
# # #     result = result + x
# # # print(result)


# # # def func(x):
# # #     p = []
# # #     m = []
# # #     for i in x:
# # #         if i != 0:
# # #             p.append(i)
# # #         else:
# # #             m.append(sum(p))
# # #             p = []
# # #     m.append(sum(p))
# # #     return m

# # # print(func([1, 0, 2, 3, 0, 4, 8]))
# # # print(func([0, 9, 10, 0, 3, 0, 4, 8]))


# # # def func(x):
# # #     xlist = []
# # #     y = []
# # #     for i in x:
# # #         if i == 0:
# # #             xlist.append(sum(y))
# # #             y = []
# # #             print('a')
# # #         else:
# # #             y.append(i)
# # #             print('b')
# # #     return xlist

# # # print(func([1, 0, 2, 3, 0, 4, 8]))
# # # print(func([0, 9, 10, 0, 3, 0, 4, 8]))

# # # print([1, 0, 2, 3, 0, 4, 8].count(0))

# # # cnt = 0
# # # while cnt < [1, 0, 2, 3, 0, 4, 8].count(0):
# # #     cnt += 1

# # # def convert(num_list):
# # #     result = []
# # #     cont = 0
# # #     for num in num_list:
# # #         print(len(result))
# # #         if len(result) != cont + 1:
# # #             result.append(0)
# # #         result[cont] += num
# # #         if num == 0:
# # #             cont += 1
# # #     return result
# # # print(convert([1, 0, 2, 3, 0, 4, 8]))
# # # print(convert([0, 9, 10, 0, 3, 0, 4, 8]))

# # # d = [0, 9, 10, 0, 3, 0, 4, 8]
# # # print(func(d))



# # # sum = 0
# # # xlist = []
# # # klist = []
# # # for i, p in enumerate(ylist):
# # #     if p == 0:
# # #         pass
# # #     else:
# # #         klist.append(p)
# # #         xlist.append(sum(klist))
# # #     print(xlist)
# # # print('a')





# # # print([i+1 for i, x in enumerate(N) if x == False])

# # # xlist = []
# # # for i in range(100):
# # #     if N[i] == False:
# # #         xlist.append(i+1)
# # # print(xlist)


# # #1, 4, 9, 16, 25, 36, 49, 64, 81, 100

# # # C = 100
# # # N = ['ura'] * 100
# # # for i in range(1, 101):
# # #     print(i)
# # #     j = i - 1
# # #     while j < 100:
# # #         print(N[j])
# # #         N[j] = not N[j]
# # #         print(j)
# # #         j += i

# # # print([k + 1 for k in range(100) if N[k] == False])






# # # print([k + 1 for k in range(100) if xlist == 'ura'])

# # # カードを裏返す
# # # for i in range(1, N):
# #     # for j in range(i, N, i+1):
# #         # print(j)
# # #         # print(C[j])
# # #         C[j] = not C[j]
# # #         # print(C[j])

# # # # 結果表示
# # # for i in range(0, N):
# # #     if not C[i]:
# # #         print(str(i+1))

# # # N = [True]*100
# # # for i in range(1, 101):
# # #     j = i - 1
# # #     while j < 100:
# # #         N[j] = not N[j]
# # #         j += i

# # # print([k + 1 for k in range(100) if N[k] == False])
# # # #1, 4, 9, 16, 25, 36, 49, 64, 81, 100








# # # print(count_line(0, 0, 20, 10))
# # # import itertools

# # # p = ['B']*20 + ['G']*10

# # # count = 0
# # # for i in set(itertools.permutations(p, 30)):
# # #     # 2人+28人 ~28人+2人で区切る
# # #     for n in range (2, 29):
# # #         mae = i[:n]
# # #         ato = i[n:]
# # #         if mae.count('B') != mae.count('G') or ato.count('B') != ato.count('G'):
# # #             count += 1
# # # print(count)

# # # 学生にとっては勉強以上に大事なクラブ活動。
# # # あなたは新しく設置される学校の 校長に就任することが決まりました。
# # # スポーツをしたい150人の学生に、どんなクラ ブ活動を準備するか考えています。
# # # 各クラブに必要なグラウンドの 各クラブに必要な土地と想定部員数 広さを調べてみたところ、[表1]の ようになりました
# # # 各クラブに所属する部員数との関係を考え、土地を確保する必要があります。

# # # [表1]
# # # クラブ | 必要な広さ | 想定部員数
# # # 野球 | 11000m2 | 40人
# # # サッカー | 8000m2 | 30人
# # # バレーボール | 400m2 | 24人
# # # バスケットボール | 800m | 20人
# # # テニス | 900m2 | 14人
# # # 陸上 | 1800m2 | 16人
# # # ハンドボール | 1000m2 | 15人
# # # ラグビー | 7000m | 40人
# # # 卓球 | 100m2 | 10人
# # # バドミントン | 300m2 | 12人

# # # 問題
# # # 150人を超えないようにクラブ活動を選び、必要な土地の面積を最大にします。その 面積の最大値を求めてください。

# # # 男性２０人、女性１０人が到着した場合、
# # # どこで区切っても２つのグループのいずれも男女の数が異なってしまうような到着順が何通りあるかを求めてください。

# # # buin = [40, 30, 24, 20, 14, 16, 15, 40, 10, 12]
# # # menseki = [11000, 8000, 400, 800, 900, 1800, 1000, 7000, 100, 300]
# # # mb = [i for i in zip(menseki, buin)]

# # # import itertools

# # # xlist = []
# # # for i in range(1, len(mb)+1):
# # #     for j in itertools.combinations(mb, i):
# # #         print(list(map(lambda x: x[0], j)))
# # #         menseki = sum(map(lambda x: x[0], j))
# # #         print(menseki)
# # #         ninzu = sum(map(lambda x: x[1], j))

# # #         if ninzu <= 150:
# # #             xlist.append(menseki)
# # # print(max(xlist))

# # # import itertools

# # # p = ['B']*4 + ['G']*2

# # # count = 0
# # # for i in itertools.permutations(p, 6):
# # #     # print(i)
# # # #     # 2人+28人 ~28人+2人で区切る
# # #     for n in range (2, 5):
# # #         mae = i[:n]
# # #         ato = i[n:]
# # #         if mae.count('B') == mae.count('G') or ato.count('B') == ato.count('G'):
# # #             print(mae, ato)
# # #             continue
# # #         else:
# # #             count += 1
# # # print(count)




# # # class Item:
# # #     def __init__(self,w=0,p=0):
# # #         self.weight=w
# # #         self.price=p

# # # items = [ Item(40,11000), Item(30,8000), Item(24,400),
# # #           Item(20,800), Item(14,900), Item(16,1800),
# # #           Item(15,1000), Item(40,7000), Item(10,100), Item(12,300) ]

# # # def knapsack(i, w):
# # #     print(i, w)
# # #     if i>=len(items):
# # #         return 0
# # #     elif  w - items[i].weight < 0.0:
# # #         return knapsack(i+1, w)
# # #     else:
# # #         p1 = knapsack(i+1, w)
# # #         #                      i番目の重量　　　　　i番目の品の価値
# # #         p2 = knapsack(i+1, w - items[i].weight) + items[i].price
# # #         if p1>p2:
# # #             return p1
# # #         else:
# # #             return p2

# # # p = knapsack(0, 150)
# # # print("TOTAL PRICE=",p)


# # # 正の整数のリストの要素と＋、✕をもちいて計算できる最大値を出力して下さい。
# # # (例)
# # # [1, 2, 3, 4] -> (1 + 2) * 3 * 4 = 36
# # # [2, 3, 4] -> 2 * 3 * 4 = 24

# # # あるイベント会場に入場待ちの列が一列にできています。
# # # ある位置で区切って２つのグループに分けたいと考えています。
# # # ２つのグループのいずれかは男女の人数が均等になるように分けたいのですが、
# # # 到着した順番が悪い場合、どこで区切っても２つのグループで男女の数が異なってしまいます。

# # # 例えば、男女３人ずつが到着している場合、「男男女男女女」 の順番で
# # # 到着するとどこで区切っても男女の数が異なってしまいます。
# # # https://dev.sizebook.jp/gitbucket/kitamura/sonogym/blob/master/img/q9_figure.png

# # # 男性２０人、女性１０人が到着した場合、
# # # どこで区切っても２つのグループのいずれも男女の数が異なってしまうような到着順が何通りあるかを求めてください。

# # # 模範解答では、男女の順列の問題を2次元の表を使って考えている。
# # # 男性が来たら右へ、女性が来たら上へ移動する経路を考える。
# # # 男女が同数になる場所をカウントしないように、経路が何通りあるかを算出する。

# # # ホールケーキを切り分けるとき、ケーキに乗っているいちごの数がすべて異なるような切り方を考える。
# # # ここでは、N 個に切り分けるときには 「1 ~ N 個のいちご (合計 N (N + 1) / 2 個)」 がそれぞれに乗っているようにする。
# # # ただし、隣り合う２つのケーキに乗っているいちごの数の和が、いずれも平方数になるように切らなければならないという条件を追加する。
# # # このような条件を満たすような切り方ができる最小の N (> 1) を求めてください。

# # # def path(b, g):
# # #     if b == g:
# # #         return 0
# # #     elif b - g == 9:
# # #         return path(b-1, g)
# # #     elif b == 0 or g == 0:
# # #         return 1
# # #     else:
# # #         return path(b-1, g) + path(b, g-1)

# # # print(path(19,10))

# # # p = ['B']*20 + ['G']*10

# # # count = 0
# # # for i in itertools.permutations(p, 30):
# # #     # 2人+28人 ~28人+2人で区切る
# # #     for n in range (2, 29):
# # #         mae = i[:n]
# # #         ato = i[n:]
# # #         if mae.count('B') != mae.count('G') and ato.count('B') != ato.count('G'):
# # #             count += 1
# # # print(count)

# # # import itertools

# # # def func(N, M):
# # #     for i in itertools.product(range(0, N), repeat=3):
# # #     	print(i)
# #         # if i[0]*2 + i[1]*3 + i[2]*4 == M and i[0] + i[1] + i[2] == N:
# #             # return i
# #     # return (-1, -1, -1)  

# # # import itertools

# # # p = ['B']*2 + ['G']*2

# # # count = 0
# # # for i in itertools.permutations(p, 4):
# # #     print(i)
# #     # 2人+28人 ~28人+2人で区切る
# # #     for n in range (2, 29):
# # #         mae = i[:n]
# # #         ato = i[n:]
# # #         if mae.count('B') != mae.count('G') and ato.count('B') != ato.count('G'):
# # #             count += 1
# # # print(count)
# #     # 2人+28人 ~28人+2人で区切る
# # #     for n in range (2, 29):
# # #         mae = i[:n]
# # #         ato = i[n:]
# # #         if mae.count('B') != mae.count('G') and ato.count('B') != ato.count('G'):
# # #             count += 1
# # # print(count)
# # # (例)
# # # N = 3, M = 9 -> "1, 1, 1"
# # # N = 10, M = 41 -> "-1, -1, -1"
# # # N = 1500, M = 5000 -> "200, 600, 700"

# # # def func(N, M):
# # #     for i in range(0, N):
# # #         for j in range(0, N):
# # #             for k in range(0, N):
# # #                 print(i, j, k)
# # #                 if 2 * i + 3 * j + 4 * k == M and i + j + k == N:
# # #                     print(i, j, k)
# # #     return -1, -1, -1

# # # print(func(3, 9))
# # # print(func(10, 41))
# # # print(func(1500, 5000))


# # # import itertools

# # # p = ['B']*20 + ['G']*10

# # # count = 0
# # # for i in itertools.permutations(p, 30):
# # #     # 2人+28人 ~28人+2人で区切る
# # #     for n in range (2, 29):
# # #         mae = i[:n]
# # #         ato = i[n:]
# # #         if mae.count('B') != mae.count('G') and ato.count('B') != ato.count('G'):
# # #             count += 1
# # # print(count)

# # # p = ['B']*6 + ['G']*4

# # # for i in range(2, 29):
# # # 	print(i)
# # # # print(p[:2])
# # # # print(p[2:])
# # # print(p[8:])
# # # print(p[:8])


# # # for q in set(itertools.permutations(p,r)):
# # #     for n in range (2, 28):
# # #         former = q[:n]
# # #         latter = q[n:]
# # #         if former.count('M') != former.count('F') or latter.count('M') != latter.count('F'):
# # #             cnt += 1
# # # print cnt


# # # def path(b, g):
# # #     if b == g:
# # #         return 0
# # #     elif b - g == 9:
# # #         return path(b-1, g)
# # #     elif b == 0 or g == 0:
# # #         return 1
# # #     else:
# # #         return path(b-1, g) + path(b, g-1)

# # # print path(19,10)




# # # A[0][0] = 1

# # # for i in range(B):
# # #     for j in range(G):
# # #         if (i != j) and (B - i != G - j):
# # #             if i > 0:
# # #                 A[i][j] += A[i-1][j]
# # #             if j > 0:
# # #                 A[i][j] += A[i][j-1]

# # # print(A[B - 1][G - 2] + A[B - 2][G - 1])

# # # import itertools
# # # from itertools import zip_longest

# # # def func(x):
# # #     s = ['+', '*']
# # #     for i in itertools.product(s, repeat=len(x)-1):
# # #         xlist = []
# # #         ylist = []
# # #         for a, b in zip_longest(x, list(i)):
# # #             xlist.append('{}, {}'.format(a, b))
# # #         a = [s.replace('None', '') for s in xlist]
# # #         b = [s.replace(', ', '') for s in a]
# # #         c = ylist.append(eval(''.join(b)))
# # #     print(ylist)    

# # # # func([1, 2, 3, 4])
# # # print(func([2, 3, 4]))




# # # # 国士無双
# # # # a,b,c,d,e,f,g,h,i,j,k,l,m をそれぞれ0文字以上用いた13文字の文字列が与えられた時に、
# # # # その文字列に一文字加えると a ~ m のうちどれか一つの文字を2つ、それ以外の文字を1つずつ含むようにできるかどうかを判別し、
# # # # できる場合にはその文字を全て出力してください

# # # # (例)
# # # # abcdfghijklmm -> e
# # # # abcdefghijklm -> a, b, c, d, e, f, g, h, i, j, k, l, m
# # # # abbccdefghijk -> false

# # # xlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
# # #          'h', 'i', 'j', 'k', 'l', 'm', 'n']

# # # def func(x):
# # # 	print(set(x))


# # # # print(func('abcdfghijklmm'))
# # # # print(func('abcdefghijklm'))
# # # print(func('abbccdefghijk'))

# # # ある街には大人、老人、赤ちゃんが合わせて N 人います。
# # # 大人の足は 2 本、老人の足は 3 本、赤ちゃんの足は 4 本とします。
# # # この街の足の数の合計が M 本のとき、
# # # 人数の組み合わせとしてあり得るものを 1 つ、
# # # "大人の人数、老人の人数、赤ちゃんの人数" の形で出力してください。
# # # ただし、そのような組み合わせが存在しない場合は "-1 -1 -1" と出力してください。

# # # (例)
# # # N = 3, M = 9 -> "1, 1, 1"
# # # N = 10, M = 41 -> "-1, -1, -1"
# # # N = 1500, M = 5000 -> "200, 600, 700"

# # # print(int(700/2))

# # # def func(N, M):
# # #     for i in range(0, N):
# # #         for j in range(0, N):
# # #             for k in range(0, N):
# # #                 if 2 * i + 3 * j + 4 * k == M and i + j + k == N:
# # #                     return i, j, k    
# # #     return -1, -1, -1

# # # print(func(3, 9))
# # # print(func(10, 41))
# # # print(func(1500, 5000))




# # # rslt = []
# # # max_val = 10000
# # # s = 0
# # # for m in range(1, max_val+1):
# # #     n = y(m)
# # #     if m >= n:
# # #         continue
# # #     if y(n) == m:
# # #         rslt.append((n, m))
# # #         s += 1
# # #         if s == 5:
# # #             break
# # # print(rslt)


# # # (例)
# # # (220, 284) 
# # # -> 220 の自分自身を除いた約数は 1, 2, 4, 5, 10, 11, 22, 44, 55, 110 で和は 284、
# # # 284 の自分自身を除いた約数は 1, 2, 4, 71, 142 で和は 220 なので、
# # # (220, 284) は友愛数である。
# # # 友愛数を小さい順に 5 組求めてください。


# # # def yakusu(p):
# # #     div = []
# # #     for i in range(1, p+1):
# # #         if p % i == 0:
# # #             div.append(i)
# # #     return sum(div[:-1])

# # # rslt = []
# # # max_val = 15000
# # # s = 0
# # # for m in range(1, max_val+1):
# # #     n = yakusu(m)
# # #     if n >= m:
# # #         continue
# # #     if yakusu(n) == m:
# # #         print(n, m)
# # #         rslt.append((n, m))
# # #         s += 1
# # #         if s == 5:
# # #             break
# # # print(rslt)

