from os import read, write
from pathlib import Path
import yaml
import argparse

parser = argparse.ArgumentParser(description='Personal information')
parser.add_argument('-n', dest='namespace', type=str, help='namespace')
parser.add_argument('-f', dest='file_path', type=str, help='file path')
args = parser.parse_args()
namespace = (args.namespace)
imageFile = (args.file_path)

input_file = open(imageFile,"r") 
for line in input_file.readlines():
    Path(line).mkdir(parents=True, exist_ok=True)
    env = open(line+'/.env',"w+")
    read_env = env.write(str('NAMESPACE='+namespace+'\nIMAGE_NAME='+line))
    repository = open('image_repository.yaml',"r+")
    read_repository = yaml.safe_load(repository)
    file = open(line+"/image repository.yaml","w+")
    yaml.dump(read_repository, file)
    file.close()
    policy = open('image_policy.yaml',"r+")
    read_policy = yaml.safe_load(policy)
    file = open(line+"/image policy.yaml","w+")
    yaml.dump(read_policy, file)
    file.close()