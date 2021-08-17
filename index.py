from os import read, write, chdir
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
Path("home_dir").mkdir(parents=True, exist_ok=True)
chdir("./home_dir")
for lines in input_file.read().split():
    line = lines[lines.find("/")+1:] 
    Path(line).mkdir(parents=True, exist_ok=True)

    data ="""
    apiVersion: image.toolkit.fluxcd.io/v1beta1
    kind: ImageRepository
    metadata:
        name: {}
        namespace: {}
    spec:
        secretRef:
            name: regecd
    image: rabazhub.azurecr.io/test
    interval: 1m0s
""".format(line, namespace)

    file = open(line+"/image repository.yaml","w+")
    docs = yaml.load(data,  Loader=yaml.FullLoader)
    yaml.dump(docs, file)
    file.close()

    data="""
    #Image policy
    apiVersion: image.toolkit.fluxcd.io/v1beta1
    kind: ImagePolicy
    metadata:
        name: {}-policy
        namespace: {}
    spec:
        imageRepositoryRef:
            name: {}-repo
        policy:
            numerical:
                 order: asc
    """.format(line, namespace, line)
    file = open(line+"/image policy.yaml","w+")
    docs = yaml.load(data,  Loader=yaml.FullLoader)
    yaml.dump(docs, file)
    file.close()
