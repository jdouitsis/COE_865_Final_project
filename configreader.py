asninfo = {
    "asn": 0,
    "linkcapacity": 0,
    "linkcost": 0
    }

rcinfo = {
    "rcid": 0,
    "asn": 0,
    "ipa": "0.0.0.0"
    }

def read_config(filename):
    
    f = open(filename)
    line = f.readline()
    splitline = line.split()
    rcinfo["rcid"] = int(splitline[0])
    rcinfo["asn"] = int(splitline[1])
    rcinfo["ipa"] = splitline[2]
    RCnuminfo = rcinfo.copy()
    
    adj = int(f.readline())
    adj_rcinfo = []
    
    for i in range(adj):
        line = f.readline()
        splitline = line.split()
        rcinfo["rcid"] = int(splitline[0])
        rcinfo["asn"] = int(splitline[1])
        rcinfo["ipa"] = splitline[2]
        adj_rcinfo.append(rcinfo.copy())
    
    adj = int(f.readline())
    adj_asninfo = []
    
    for i in range(adj):
        line = f.readline()
        splitline = line.split()
        asninfo["asn"] = int(splitline[0])
        asninfo["linkcapacity"] = int(splitline[1])
        asninfo["linkcost"] = int(splitline[2])
        adj_asninfo.append(asninfo.copy())
    
    f.close()
    return  RCnuminfo, adj_rcinfo, adj_asninfo;


RC1info, RC1adj_rcinfo, RC1adj_asninfo = read_config("config\RC1_config.txt")
RC2info, RC2adj_rcinfo, RC2adj_asninfo = read_config("config\RC2_config.txt")
RC3info, RC3adj_rcinfo, RC3adj_asninfo = read_config("config\RC3_config.txt")
RC4info, RC4adj_rcinfo, RC4adj_asninfo = read_config("config\RC4_config.txt")

# print(RC1info,"\n\n",RC1adj_rcinfo,"\n\n",RC1adj_asninfo,"\n")
# print(RC2info,"\n\n",RC2adj_rcinfo,"\n\n",RC2adj_asninfo,"\n")
# print(RC3info,"\n\n",RC3adj_rcinfo,"\n\n",RC3adj_asninfo,"\n")
# print(RC4info,"\n\n",RC4adj_rcinfo,"\n\n",RC4adj_asninfo,"\n")
