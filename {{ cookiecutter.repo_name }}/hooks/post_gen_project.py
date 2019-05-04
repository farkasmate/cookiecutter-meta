import os
import subprocess

def run(command):
  with open(os.devnull, 'w') as dev_null:
    return subprocess.call(command, stdout=dev_null, stderr=subprocess.STDOUT)

code = run(['git', 'init'])

if code == 0:
  code = run(['git', 'add', '--all'])

if code == 0:
  code = run(['git', 'commit', '--message', 'Initial commit'])

if code == 0:
  code = run(['git', 'remote', 'add', 'origin', 'git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git'])
