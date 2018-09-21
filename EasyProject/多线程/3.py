'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间
'''

import time
import _thread as thread


def loop1(in1):
    # ctime得到当前时间
    print("Start loop 1 at :", time.ctime())
    # 把参数打印出来
    print("我是参数 ", in1)
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print("End loop 1 at :", time.ctime())


def loop2(in1, in2):
    # ctime得到当前时间
    print("Start loop 2 at :", time.ctime())
    # 把参数打印出来
    print("我是参数 ", in1, "和参数 ", in2)
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print("End loop 2 at :", time.ctime())


def main() -> object:
    print("Starting at :", time.ctime())
    # loop1()
    # loop2()
    thread.start_new_thread(loop1, ("王老大", ))

    thread.start_new_thread(loop2, ("王雪贤", "常耀理"))

    print("All done at :", time.ctime())


if __name__=='__main__':
    main()
    while True:
        time.sleep(5)
