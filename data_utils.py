# *-* coding:utf-8 *-*
'''
@author: ioiogoo
@date: 2018/1/31 19:30
'''

def preprocess_file(Config):
    # 语料文本内容
    files_content = ''
    with open(Config.poetry_file, 'r',encoding='UTF-8') as f:
        for line in f:
            x = line.strip() + "]" # "]" 是作为诗和诗之间的分隔符
            x = x.split(":")[1]
            if len(x) <= 5 :
                continue
            if x[5] == '，':
                files_content += x # 将全部的诗拼接成一个大的字符串
            

    words = sorted(list(files_content))
    # 统计每个字符的出现次数
    counted_words = {}
    for word in words:
        if word in counted_words:
            counted_words[word] += 1
        else:
            counted_words[word] = 1

    # 去掉低频的字
    erase = []
    for key in counted_words:
        if counted_words[key] <= 2:
            erase.append(key)
    for key in erase:
        del counted_words[key]
    # 按照word 出现的次数降序排列
    wordPairs = sorted(counted_words.items(), key=lambda x: -x[1])

    words, _ = zip(*wordPairs)
    words += (" ",)
    # word到id的映射
    word2num = dict((c, i) for i, c in enumerate(words))
    # id 到word 的映射
    num2word = dict((i, c) for i, c in enumerate(words))
    # 构造一个匿名函数,通过word 获取id
    word2numF = lambda x: word2num.get(x, len(words) - 1)
    return word2numF, num2word, words, files_content