"""为了防止黑客通过彩虹表根据哈希值反推原始口令，在计算哈希的时候，不能仅针对原始输入计算，需要增加一个salt来使得相同的输入也能得到不同的哈希
我们首先需要准备待计算的原始消息message，随机key，哈希算法，这里采用MD5，使用hmac的代码如下"""
# -*- coding: utf-8 -*-
import hmac
message = b'Go,with me,to the future.'  # 要求bytes类型
key = b'secretlove'  # 要求bytes类型
h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())
