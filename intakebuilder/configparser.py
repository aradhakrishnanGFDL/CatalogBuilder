import yaml

class Config:
   def __init__(self,config):
     self.config = config 
     with open(self.config, 'r') as file:
        configfile = yaml.safe_load(file)
     try:
         self.input_path = configfile['input_path']
         print(self.input_path)
     except:
         raise KeyError("input_path does not exist in config")
     try:
         self.output_path = configfile['output_path']
         print(self.output_path)
     except:
         raise KeyError("output_path does not exist in config")
