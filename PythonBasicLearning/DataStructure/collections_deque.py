from collections import deque
"""使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈："""


def deque_list():
    deq_list = deque(['1', '2', '3', '4'])  # 初始化列表
    deq_list.append('0')  # 最后边增加元素
    deq_list.appendleft('5')  # 最左边增加元素
    deq_list.popleft()  # 删除最左边元素
    return deq_list


def main():
    print(
        f'Show the deque_list:{deque_list()}\nThe first in deq_list is: {deque_list()[0]},the last in deq_list is: {deque_list()[-1]}')


if __name__ == '__main__':
    main()
