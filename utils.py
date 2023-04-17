def DatatoString(from_ID,from_IP,from_Port,new_pairs,update:bool):
    # split using the '$' mark
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

