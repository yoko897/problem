# coding: utf-8
# #!/usr/bin/env python


# コラッツの予想
# 自然数nについて
# nが偶数の場合、nを2で割る。
# nが奇数の場合、nに３をかけて１を足す
# という操作を繰り返すとき、初期値がどんな数であっても必ず１に到達する。
# (1⇒4⇒2⇒1のように繰り返す)
#　例えば②で始めた場合は以下のようになります。
# 2⇒7






def if_even(x):
    return n / 2

def if_odd(x):
    return n * 3 + 1

def collatz(x):
    m = if_odd(x)  # 初回
    while(True):
        if m == 1:
            return False
        elif m == n:
            return True
        elif m % 2 == 0:
            m = if_even(m)
        else:
            m = if_odd(m)


def main():
    collatz_nums = []
    for n in range(1, 10001):
        if collatz(n):
            collatz_nums.append(n)
    print(collatz_nums)
    print(len(collatz_nums))


if __name__ == '__main__':
    main()

























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













