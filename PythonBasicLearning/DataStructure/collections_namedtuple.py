from collections import namedtuple
"""namedtuple是一个函数，它用来创建一个自定义的tuple对象，
并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。"""
#自定义tuple，如，二维坐标，三维坐标

def Point_def():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 3)
    print(f'Point={p},x={p.x},y={p.y}')


def ThreeD_Point_def():
    Point = namedtuple('ThreeD_Point_def', ['x', 'y', 'z'])
    p = Point(1, 3, 5)
    print(f'ThreeD_Point_def={p},x={p.x},y={p.y}, z={p.z}')


def main():
    ThreeD_Point_def()


if __name__ == '__main__':
    main()
