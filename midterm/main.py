from router import csv2dict, find_station_by_line_name
from parser import parse_input, parse_path
from shortest_path import bfs, make_graph

ROUTE_FILE = './线路.csv'


def main(input_str):
    try :
        parsed_e2e = parse_input(input_str)
        route_dic = csv2dict(ROUTE_FILE)
        graph = make_graph(route_dic)
        start_line, start_name  = parsed_e2e[0][0].strip(), parsed_e2e[0][1].strip()
        end_line, end_name = parsed_e2e[1][0].strip(), parsed_e2e[1][1].strip()
        start_id = find_station_by_line_name(route_dic=route_dic, line=start_line, name=start_name)
        end_id = find_station_by_line_name(route_dic=route_dic, line=end_line, name=end_name)
        if start_id is None:
            print(f"起始站 '{parsed_e2e[0][1]}' 在 '{parsed_e2e[0][0]}' 线路上未找到。")
            return
        if end_id is None:
            print(f"终点站 '{parsed_e2e[1][1]}' 在 '{parsed_e2e[1][0]}' 线路上未找到。")
            return
        path = bfs(graph=graph, start=start_id, end=end_id)
        if path is None:
            print("没有找到路径")
            return
        parse_path(path=path, route_dic=route_dic)
    except ValueError as e:
        print(f"输入错误: {str(e)}")
    except FileNotFoundError:
        print(f"找不到文件: {ROUTE_FILE}")
    except pd.errors.EmptyDataError:
        print(f"CSV文件 {ROUTE_FILE} 是空的")
    except Exception as e:
        print(f"发生未知错误: {str(e)}")




if __name__ == "__main__":
    # input_str = input("用户输入:")
    # main(input_str)
    while True:
        input_str = input("请输入起始站和终点站 (格式: 线路名，站名-线路名，站名), 或输入 'quit' 退出: ")
        if input_str.lower() == 'quit':
            break
        main(input_str)