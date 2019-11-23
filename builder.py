from git import Repo
from argparse import ArgumentParser
import os
import subprocess
import docker

docker_client = docker.from_env()
parser = ArgumentParser()
parser.add_argument("-u", dest="url", help="Git repository url", metavar="<url>", required=True)
parser.add_argument("-t", dest="tag", help="Docker image tag", metavar="<tag>", required=True)
args = parser.parse_args()

directory = os.getcwd() + "/tmp"
print("Cloning repository " + args.url)
Repo.clone_from(args.url, directory)

subprocess.run(["docker", "build", "-t", f"{args.tag}", f"{directory}"])

docker_client.login(username=os.environ["DOCKER_USERNAME"], password=os.environ["DOCKER_PASSWORD"])
for line in docker_client.images.push(args.tag, stream=True, decode=True):
    print(line)
