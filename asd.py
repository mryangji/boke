def zhuangshiqi(hanshu):
    print('____--------------------')
    try:
        hanshu(*args)
    except:
        print('meizhixing')
    print('qqqqqqqqqqqqqqqqqqqqqqqqqqq')

@zhuangshiqi
def hanshu(s = 'qwe'):
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    s=s+1



re = r'//'
# hanshu()

# def use_logging(func):

#     print("asd is running")
#     func()

# @use_logging
# def foo():
#     print("i am foo")

# foo()