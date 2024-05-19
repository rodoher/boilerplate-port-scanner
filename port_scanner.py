import socket
import common_ports
import pandas as pd

def get_open_ports(target, port_range, verbose = False):
    open_ports = []

    for i in range(port_range[0], port_range[1]):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        if s.connect_ex((target, i)):
            continue

        else:
            open_ports.append(i)

    if verbose==True:
        dic_ports = {}
        for i in open_ports:
            val = common_ports.ports_and_services[i]
            dic_ports[i] = val
        df = pd.DataFrame.from_dict(dic_ports, orient="index")
        df = df.reset_index()
        df.columns = ['PORT', 'SERVICE']
        return df
    return(open_ports)