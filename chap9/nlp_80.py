# -*- coding: utf-8 -*-
with open('enwiki-20150112-400-r100-10576.txt','r') as f:
    for line in f:
        token_list = []
        for word in line.split(' '):
            token = word.strip().strip('.,!?;:()[]\'"')
            if len(token) == 0:
                break
            token_list.append(token)
        print(' '.join(token_list))
