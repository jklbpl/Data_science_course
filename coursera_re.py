import re
def logs():
    with open("assets/logdata.txt", "r") as file:
        logdata = file.read()
    
    host = re.findall("[\d.*]+",logdata)
    #filtration numbers and ip (not ip -> garbage)
    lenlist = []
    hostlist = [] 
    for i in range(0, len(host)):
        lenlist.append(len(host[i]))
        if lenlist[i] >= 8:
            hostlist.append(host[i])
            continue
            
    username = re.findall("([A-Za-z]{3,8}[0-9]{3,6})|(\- -)",logdata) 
    # finds either group with letters (from 3 to 8 letters) in addition to numbers (at least 3 and max 6) OR (- -)
    usernamelist = []
    # username filter 
    for element in range(len(username)):
        u = username[element]
        if len(u[0]) > 4:
            usernamelist.append(u[0])
        if len(u[1]) in range(2,4): # if it's (- -)
            usernamelist.append("-")
        else:
            continue
            
    time = re.findall("(\[.*\])",logdata) # finds anything in []
    timelist = []
    for i in range(len(time)):
        r = re.sub(r"[\[\]]",'', time[i])
        timelist.append(r)
    
    request = re.findall("(\".*\")",logdata) # finds anything in ""
    requestlist = []
    for i in range(len(request)):
        r = re.sub(r"[\"]",'', request[i])
        requestlist.append(r)
        
    logs_list  = []
    for item in range(0,len(hostlist)):
        log = {"host": hostlist[item],"user_name": usernamelist[item],"time": timelist[item],"request": requestlist[item] }
        logs_list.append(log)
      
    #print(len(usernamelist), len(hostlist),len(timelist), len(requestlist))
    return logs_list
logs()