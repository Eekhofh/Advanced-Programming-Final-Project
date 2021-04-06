# Program runs the Bash script 'final_project.sh'
from subprocess import call

def run_process():
    call('bash final_project.sh', shell=True)
