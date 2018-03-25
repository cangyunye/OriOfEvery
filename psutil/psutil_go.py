# 系统信息获取包
import psutil as ps
ps.cpu_count()  # CPU逻辑数量
ps.cpu_count(logical=False)  # CPU物理核心
ps.cpu_times()  # 统计用户，系统，空闲时间
# 实现类似top命令，每10s刷新一次
for x in range(10):
    ps.cpu_percent(interval=1, percpu=True)
# 获取内存信息，返回的字节为单位的整数
ps.virtual_memory()  # 物理内存信息
ps.swap_memory()  # 交换内存信息
# 获取磁盘信息
ps.disk_partitions()  # 磁盘分区信息
ps.disk_usage('c:')  # 磁盘使用情况 linux下，磁盘用"/"
ps.disk_io_counters()  # 磁盘IO
# 获取网络信息
ps.net_io_counters()  # 获取网络读写字节／包的个数
ps.net_if_addrs()  # 获取网络接口信息
ps.net_if_stats()  # 获取网络接口状态
ps.net_connections()  # 获取当前网络信息
# 获取进程信息
ps.pids()  # 所有进程ID
ps.test()  # 类似linux的ps
p = ps.Process(ps.pids()[0])  # 获取指定ID
p.name()  # 进程名称
p.exe()  # 进程exe路径
p.cwd()  # 进程工作目录
p.cmdline()  # 进程启动的命令行
p.ppid()  # 父进程ID
p.parent()  # 父进程
p.children()  # 子进程列表
p.status()  # 进程状态
p.username()  # 进程用户
p.create_time()  # 进程创建时间
p.terminal()  # 进程终端
p.cpu_times()  # 进程使用CPU时间
p.memory_info()  # 进程占用内存
p.open_files()  # 进程打开的文件
p.connections()  # 进程相关的网络连接
p.num_threads()  # 进程的线程数量
p.threads()  # 进程的所有线程数量
p.environ()  # 进程环境变量
p.terminate()  # 结束进程
