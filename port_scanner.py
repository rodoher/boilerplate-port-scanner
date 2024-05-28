import socket
import common_ports

def get_open_ports(target, port_range, verbose = False):
    name = False
    if target[0].isdigit():

        try:
            socket.inet_aton(target)

        except socket.error:
            return("Error: Invalid IP address")

    else:
        name = True
        try:
            socket.gethostbyname(target)
        except socket.error:
            return("Error: Invalid hostname")


    open_ports = []
    for i in range(port_range[0], port_range[1]+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((target, i)):
            s.close()
            continue

        else:
            open_ports.append(i)
            s.close()
    text=""
    if name is True:
        try:
            ipnum = socket.gethostbyname(target)
            text+="Open ports for "+target+" ("+ipnum+")"
        except:
            return("Error: Invalid hostname")

    else:
        try:
            hostname = socket.gethostbyaddr(target)
            text+="Open ports for "+hostname[0]+" ("+target+")"
        except:
            text+="Open ports for "+target

    if verbose==True:
        text += "\nPORT     SERVICE"
        for i in open_ports:
            val = common_ports.ports_and_services[i]
            if i<100:
                text += "\n"+str(i)+"       "+val
            elif i<1000:
                text += "\n"+str(i)+"      "+val
            else:
                text += "\n"+str(i)+"     "+val

        return (text)
    return(open_ports)