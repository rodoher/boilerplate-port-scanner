import socket
import common_ports

def get_open_ports(target, port_range, verbose = False):
    if target[0].isdigit():
        try:
            socket.inet_aton(target)

        except socket.error:
            return("Error: Invalid IP address")

    else:
        try:
            socket.gethostbyname(target)
        except:
            return("Error: Invalid hostname")


    open_ports = []
    for i in range(port_range[0], port_range[1]+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        if s.connect_ex((target, i)):
            continue

        else:
            open_ports.append(i)
    try:
        ipnum = socket.gethostbyname(target)
        print("open ports for "+target+" ("+ipnum+")")
    except:
        hostname = socket.gethostbyaddr(target)
        print("open ports for "+hostname[0]+" ("+target+")")

    if verbose==True:
        text = "PORT     SERVICE\n"
        for i in open_ports:
            val = common_ports.ports_and_services[i]
            text += str(i)+"       "+val+"\n"

        return (text)
    return(open_ports)