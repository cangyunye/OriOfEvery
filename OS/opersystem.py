"""
    os模块
    os.remove()删除文件
    os.makedirs()创建多层目录
    os.mkdir(path[, mode])
    os.rmdir(path)删除path指定的空目录，如果目录非空，则抛出一个OSError异常。
    os.removedirs(path)递归删除目录。
    os.rename()重命名文件
    os.renames(old, new)递归地对目录进行更名，也可以对文件进行更名。
    os.path.isfile()判断是否为文件
    os.path.isdir()判断是否为目录
    os.path.join()链接目录，如path1链接path2为path1/如path1链接path2为path1
    os.path.splitext()将文件分割成文件名与扩展名，如分割tmp.txt为tmp和.txt
    os.getcwd()返回当前工作目录
    os.utime(path, times)返回指定的path文件的访问和修改的时间。
    os.tmpfile()返回一个打开的模式为(w+b)的文件对象 .这文件对象没有文件夹入口，没有文件描述符，将会自动删除。
    os.link(src, dst)创建硬链接，名为参数 dst，指向参数 src
    os.listdir(path)返回path指定的文件夹包含的文件或文件夹的名字的列表。
"""
