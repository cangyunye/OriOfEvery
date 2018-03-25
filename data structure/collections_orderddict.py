from collections import OrderedDict
"""OrderedDict的Key会按照插入的顺序排列，不是Key本身排序"""


def OrderedDict_dict():
    d = dict([('a', 1), ('b', 2), ('c', 3)])
    od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])  # 按顺序插入
    print(f'{od.values()},{od.keys()},{od.items()}')


def main():
    OrderedDict_dict()


if __name__ == '__main__':
    main()
