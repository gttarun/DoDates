import subprocess
import os

# A toolbox class that helps me to write small scripts faster
class terminal:

    #if provided with no working directory it will
    #use the current directory as the working directory
    def __init__(self,workingDirectory=""):
        #setup current working directory
        if workingDirectory == "":
            self.workingDir = subprocess.Popen("pwd", stdout=subprocess.PIPE, shell=True).stdout.read().strip()
        else:
            self.workingDir = workingDirectory

        self.doEcho = True #set this to false to disable this module from printing to stdout

    #execute a command, return the resulting string
    #blocks until complete
    #does not support multiple commands separated by ';' (expect bugs if you try)
    def execute(self,command):

        command = command.strip()

        if self.doEcho:
            print "pyscr:" + self.workingDir + "$ " + command

        result = ""

        #special case
        if command[0:3] == "cd ":
            self.cd(command[3:].strip())
        else:
            result = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, cwd=self.workingDir).stdout.read()

        if self.doEcho and result != "":
            print result.strip()

        return result.strip()

    #for internal use
    #all calls to execute that use cd will eventually use this function
    def cd(self, path):
        
        if path[-1] == '/':
            path = path[:-1]

        newWD = ""

        if path[0] == '/':
            newWD = path
        else:
            newWD = self.workingDir + "/" + path

        if not self.isDir(newWD):
            if self.doEcho:
                print "ERROR: " + newWD + " does not exist!"
            return "ERROR: " + newWD + " does not exist!"

        self.workingDir = subprocess.Popen("pwd", stdout=subprocess.PIPE, shell=True, cwd=newWD).stdout.read().strip()


    ####################################################
    #                Useful actions                    #
    ####################################################

    #returns true if the file or directory exists
    def exists(self,path):
        path = path.strip()
        #path is relative to root
        if path[0] == '/': 
            return os.path.exists(path)
        #path is relative to cwd
        else:
            return os.path.exists(self.workingDir + "/" + path)

    #returns true if the object exists and is a file
    def isFile(self,path):
        path = path.strip()
        #path is relative to root
        if path[0] == '/': 
            return os.path.isfile(path)
        #path is relative to cwd
        else:
            return os.path.isfile(self.workingDir + "/" + path)

    #returns true if the object exists and is a directory
    def isDir(self,path):
        path = path.strip()
        #path is relative to root
        if path[0] == '/': 
            return os.path.isdir(path)
        #path is relative to cwd
        else:
            return os.path.isdir(self.workingDir + "/" + path)
