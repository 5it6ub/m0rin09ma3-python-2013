#!/usr/bin/env python

import subprocess
import shlex

def Uptime():
    """
    extract 3 uptime avgs - 1, 5, 15 minutes
    """
#print subprocess.check_call("uptime")
#print subprocess.check_output("while [ 1 ]; do uptime; sleep 3; done")
#try:
#    subprocess.check_output("exit 1", shell=True)
#    sp_output = subprocess.check_output("while [ 1 ]; do uptime; sleep 3; done",
#                            stderr=subprocess.STDOUT,
#                            shell=True)
#    print sp_output

#    command_line = "while [ 1 ]; do uptime; sleep 3; done"
#    args = shlex.split(command_line)
#    print args
    pipe = subprocess.Popen(['./check_uptime.sh', '3', '5'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=False)
    stdoutdata,stderrdata = pipe.communicate()
#    print stdoutdata, stderrdata
#    if not stdoutdata and stderrdata: # not display if it's (None, None)
        #print pipe.communicate()
    return stdoutdata
#except subprocess.CalledProcessError:
#except ValueError:
#    print 'exception raised'

if __name__ == '__main__':
    print Uptime()

