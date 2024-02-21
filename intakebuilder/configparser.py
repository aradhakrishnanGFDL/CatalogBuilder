import yaml
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)
try:
    input_path = config['input_path']
    print(input_path)
except:
    raise KeyError("input_path does not exist in config")
try:
    output_path = config['output_path']
    print(output_path)
except:
    raise KeyError("output_path does not exist in config")
