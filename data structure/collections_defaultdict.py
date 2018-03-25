from collections import defaultdict
"""使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict"""


def defaultdict_dict():
    dd = defaultdict(lambda: 'N/A')
    dd['key1'] = 'abc'
    print(dd['key1'])  # key1存在
    print(dd['key2'])  # key2不存在，返回默认值


def main():
    defaultdict_dict()


if __name__ == '__main__':
    main()
