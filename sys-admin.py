import os

os.system("ls")


#Using subprocess.run
#Though os.system() is simple to use because it takes a string argument, it is recommended that you use the more powerful subprocess.run() function. You can use the subprocess module to spawn new processes, connect to input/output/error pipes, and obtain error codes. The subprocess.run() function can take many new arguments, but those additional arguments are optional.

#The full list of arguments for subprocess.run() looks like the following list:

#subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)

import subprocess

subprocess.run(["ls"]) 

#Confirm that your output lists the file in the directory, similar to the following example. (The contents of your directory might be different.)
#sys-admin.py  sys-admin_2.py  README.md
#Note that the output looks the same as the output of os.system() , but you are using the subprocess module instead of the os module.

subprocess.run(["ls","-l"]) #subprocess.run with two arguments
subprocess.run(["ls","-l","sys-admin.py"]) #subprocess.run with two arguments

#Retrieving system information
#The subprocess.run() function is powerful because you can use it to run any Bash command

command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
#Confirm that the expected output is similar to the following example.
#	Gathering system information with command: uname -a                          
#	Linux ip-172-31-29-181 4.4.0-139-generic #165-Ubuntu SMP Wed Oct 24 10:58:50 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux 

#Retrieving information about disk space
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

#Confirm that the expected output is similar to the following example.
#	Gathering active process information with command: ps -x                       
#	  PID TTY      STAT   TIME COMMAND                                           
#	18976 pts/459  S+     0:00 python3.6 lab_15_2.py                               
#	18977 pts/459  R+     0:00 ps -x                                             
#	21139 pts/459  S      0:00 /bin/bash -c export OLD_HOME=/home/ccc_4dfa91ec5a_
#	21164 pts/459  S      0:00 bash --rcfile /home/ccc_4dfa91ec5a_45122/.termrc -
