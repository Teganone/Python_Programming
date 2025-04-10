import pandas as pd

def csv2dict(filename):
    data = pd.read_csv(filename)
    route_dic = {}
    for _, row in data.iterrows():
        transfer_list = row['可换乘站点ID']
        if(pd.isna(transfer_list)):
            transfer_list = []
        else: 
            transfer_list = str(transfer_list).split('/')  
        route_dic[str(row['站点ID'])] = {
            "id": str(row['站点ID']), 
            "line": row['线路名'], 
            "name": row['站名'], 
            'transfer_list':transfer_list
            } 
    return route_dic

def find_station_by_line_name(route_dic, line, name):
    # line, name  = info[0].strip(), info[1].strip()
    for key, value in route_dic.items():
        if value['name'] == name and value['line'] == line:
            return key
    return None


def find_station_by_name_line(route_dic,info):
    line, name  = info[0].strip(), info[1].strip()
    for key, value in route_dic.items():
        if value['name'] == name and value['line'] == line:
            return key
    return None