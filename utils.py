def DatatoString(from_ID,from_IP,from_Port,new_pairs,update:bool):
    # 分隔符就用$吧
    result = ''
    result += str(from_ID)
    result += '$'
    result += str(from_IP)
    result += '$'
    result += str(from_Port)
    result += '$'
    result += str(new_pairs)
    result += '$'
    if update:
        result += 'True'
    else:
        result += 'False'
    return result

def DatadeString(StringData:str):
    resList = StringData.split('$')
    from_ID = resList[0]
    from_IP = resList[1]
    from_Port = int(resList[2])
    new_pairs = eval(resList[3])
    if resList[4] == 'True':
        update = True
    else:
        update = False
    return [from_ID,from_IP,from_Port,new_pairs,update]


# 自定义编解码器测试完成

# if __name__ == '__main__':
#     from_ID = 'u'
#     DV_pairs = {'x': 5, 'w': 3, 'v': 7, 'y': -1, 'z': -1}
#     s = DatatoString(from_ID,'127.0.0.1',5555,DV_pairs,True)
#     print(s)
#     print(DatadeString(s))
#     t = DatadeString(s)[1]
#     print(t.__class__)
#     # # test DV_al
#     # myrouter1 = Router('u','127.0.0.1',5560,'127.0.0.1',5555)
#     # myrouter1.DV_pairs = {'x':5,'w':3,'v':7,'y':-1,'z':-1}
#     # myrouter1.DV_Algorithm('x',{'u':5,'w':4,'v':-1,'y':7,'z':9})