import shlex
from subprocess import run, CalledProcessError, PIPE

cmd_to_run = "netstat -n"
cmd_words = shlex.split(cmd_to_run)

print(f"{cmd_words = }")
proc = run(cmd_words)
print('-' * 60)
print(f"{proc = }")
print('-' * 60)

proc = run(cmd_words, stdout=PIPE)
print(f"{type(proc.stdout) = }")
output = proc.stdout.decode()
print(f"{type(output) = }")
all_lines = output.splitlines()  # split on \n into individual lines

established_connections = [line for line in all_lines if "ESTABLISHED" in line if line.startswith('tcp4')]
for connection in established_connections:
    print(connection)



