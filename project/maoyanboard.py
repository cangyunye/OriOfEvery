import re,requests,json

def parse_html(url):
    #请求头，必须加，不然无法爬取
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    board_get = requests.get(url,headers=headers)
    #榜单列表，榜单列表区根据当前网页直接设定，也可在board页面找到特征，取href进行拼接
    pattern_board = re.compile('<i class="board-index board-index-\d">(.*?)</i>.*?<img data-src="(.*?)" alt=.*?class="movie-item-info".*?<a href="(.*?)" title=".*?" data-act="boarditem-click" data-val="(.*?)">(.*?)</a>.*?class="star">\s*(.*?)\s*?</p>.*?<p class="releasetime">(.*?)</p>.*?<p class="score"><i class="integer">(.*?)</i><i class="fraction">(.*?)</i>',re.S)
    board_lists = re.findall(pattern_board,board_get.text)
    return board_lists

def return_dict(board_lists):
    #使用生成器以迭代返回生成字典数据
    for board_list in board_lists:
        yield {
            'index' : board_list[0],
            'image' : board_list[1],
            'href' : board_list[2],
            'movieid' : board_list[3],
            'star' : board_list[4].strip() if len(board_list[4])>3 else '',
            'releasetime' : board_list[5] if len(board_list[5])>5 else '',
            'score' : board_list[6] + board_list[7]
            }

        
#写入文件
def write_to_file(board_dict):
    with open('board_dict.txt','wt',encoding='utf-8') as f:
        for line in board_dict:
            #write只能写str，所以使用dumps解析字典成str，如果不使用ensure_ascii=False，则会将中文输出二进制数据，+"\n"完成换行
            f.write(json.dumps(line,ensure_ascii=False)+"\n")

def main():
    #猫眼看板地址
    maoyan_board = 'http://maoyan.com/board/4'
    #图个方便写一起了
    write_to_file(return_dict(parse_html(maoyan_board)))
if __name__ == '__main__':
    main()