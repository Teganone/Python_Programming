import yaml
import json

# def yml2json(input_file,output_file):
#     with open(input_file, 'r') as f:
#         data = yaml.safe_load(f)
#     with open(output_file, 'w') as f:
#         json.dump(data, f)

def read_yaml(filename):
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)
    return data

def print_json(data):
    print(json.dumps(data, indent=4))

# def print_run_variable(data):
#     return data['jobs']['build']['steps'][-1]['run']

def find_and_print_run(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == 'run':
                print(f"需要运行:{value}")
            else:
                find_and_print_run(value)
    elif isinstance(data, list):
        for item in data:
            find_and_print_run(item)

if __name__ == "__main__":
    input_filename = './datasets.yml'
    output_filename = './datasets.json'
    # yml2json(input_filename,output_filename)
    data = read_yaml(input_filename)
    print_json(data)
    find_and_print_run(data)

    
