
def parse_input(input_str):
    try:
        start, end = input_str.split("-")
    except ValueError:
        raise ValueError("Input must contain exactly one '-' to separate start and end stations.")
    start = start.strip().split('，')
    end = end.strip().split('，')
    if len(start) < 2 or len(end) < 2:
        raise ValueError("Input format incorrect. Please provide at least station line and name respectively for both start and end, and separate them with '，'. Example: 18号线，上海财经大学-8号线，东方体育中心")
    return [start[:2], end[:2]]



def parse_path(path,route_dic):
    prev_line = None
    for station in path:
        current_line = route_dic[station]['line']
        station_name = route_dic[station]['name']
        if prev_line is None: 
            print(f"{current_line}, {station_name}")
        elif current_line != prev_line:
            print(f"换乘\n{current_line}, {station_name}")
        else:
            print(f"{current_line}, {station_name}")
        prev_line = current_line