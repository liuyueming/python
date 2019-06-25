db = {}
path = []
 
while True:
    #定义临时字典temp
    temp = db
    #path默认是空列表根据进入的节点深度有对应的内容
    for item in path:
        temp = temp[item]
    #列出节点下面对应的可选key值
    print('当前可选节点',list(temp.keys()),'\n')
 
    choice = input('1:添加节点；2：查看并进入节点(Q退出/返回上一级B) \n>>>')
    if choice == '1':
        k = input('请输入要添加的子节点名称：')
        if k in temp:
            print('节点已经存在')
        else:
            temp[k] = {}
    elif choice == '2':
        k = input('请输入要查看的子节点：')
        if k in temp:
            path.append(k)
        else:
            print('子节点名称错误')
    elif choice.lower() == 'b':
        if path:
            path.pop()
    elif choice.lower() == 'q':
        break
    else:
        print('输入不合法')
 
    print('字典和path值为：',db,path)
