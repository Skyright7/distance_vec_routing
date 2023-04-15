def DatatoString(from_ID,new_pairs,update:bool):
    # 分隔符就用$吧
    result = ''
    result += str(from_ID)
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
    new_pairs = eval(resList[1])
    if resList[2] == 'True':
        update = True
    else:
        update = False
    return [from_ID,new_pairs,update]