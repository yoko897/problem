# coding: utf-8
# #!/usr/bin/env python


def get_range_tenshoku_min(n):
    min_range = {
        '1000': '1000万以下',
        '1200': '1000~1200万',
        '1400': '1200~1400万',
        '1600': '1400~1600万',
        '1800': '1600~1800万',
        '2000': '1800~2000万',
        '2001': '2000万以上',
    }

    m = sorted(min_range.items(), key=lambda x:x[0])
    # print(m)
    for k, v in m:
        # print(n, k, int(n) <= int(k))
        if int(n) <= int(k):
            return v
        else:
            continue            
    return '2000万以上'

print(get_range_tenshoku_min(10))
print(get_range_tenshoku_min(1001))
print(get_range_tenshoku_min(1501))
# csvfile = open('./2.txt', 'r', encoding='utf-8')
# reader = csv.reader(csvfile)
# # print(reader)
# header = next(reader)  # ヘッダーを捨てる

# kaminoku, simonoku = [], []

# for row in reader:
#     kaminoku += [row[3]]
#     simonoku += [row[4]]
