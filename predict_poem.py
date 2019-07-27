# -*- coding:utf-8 -*-
'''
预测诗句
'''
import argparse

from config import Config
from poem_model import PoetryModel

if __name__ == '__main__':
    model = PoetryModel(Config)
    if model.loaded_model:
        print("model loaded from %s" % Config.weight_file)
        parser = argparse.ArgumentParser("诗词生成器")
        group = parser.add_mutually_exclusive_group()
        # action = store_true 表示可以不指定参数值
        group.add_argument("-pr","--predict_random",action="store_true"
                           ,help = "随机从诗库中抽取一个诗的开头一句，生成一首诗")
        group.add_argument("-pf","--predict_first",help="给定一个字，生成一首五言绝句")
        group.add_argument("-ps","--predict_sentence",help="给定首句(五个字),生成一首五言绝句")
        group.add_argument("-ph","--predict_hide",help="给定四个字，生成一首藏头诗")
        args = parser.parse_args()
        if args.predict_random:
            output = model.predict_random()
        elif args.predict_first:
            first_char = args.predict_first[0]
            output = model.predict_first(first_char)
        elif args.predict_sentence:
            if len(args.predict_sentence) < 5:
                print("输入的首句应该是五个字!")
                output = ""
            else:
                sentence = args.predict_sentence[:5]
                output = model.predict_sen(sentence)
        elif args.predict_hide:
            if len(args.predict_hide) != 4:
                print("藏头诗的输入应该为四个字!")
                output = ""
            else:
                output = model.predict_hide(args.predict_hide)
        else:
            # 默认输出 predict_random
            output = model.predict_random()
        print(output)
    else:
        print("Can't load pretrained model!Do you want to train the model now?[y/n]\n")
        i = input()
        if i in ["y","Y","yes","YES"]:
            model.train()
        else:
            print("Exit,bye!")
