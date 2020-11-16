import subprocess

subprocess.call("ansible-playbook setup.yml -b",shell=True)
subprocess.call("ansible-playbook download.yml -b",shell=True)
subprocess.call("ansible-playbook build.yml -b",shell=True)
subprocess.call("ansible-playbook fetch_artifact.yml -b",shell=True)
subprocess.call("ansible-playbook deploy.yml -b",shell=True)
subprocess.call("ansible-playbook testing.yml -b",shell=True)
subprocess.call("ansible-playbook delivery.yml -b",shell=True)
