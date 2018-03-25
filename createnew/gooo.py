from collections import Counter
"""Counter是一个简单的计数器，例如，统计字符出现的个数"""

def main():
    c = Counter()
    for ch in 'programming':
        c[ch] = c[ch] + 1
    print(c)
if __name__ == '__main__':
    main()
