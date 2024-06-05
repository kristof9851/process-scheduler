import os
import sys
import platform
from subprocess import Popen, PIPE, STDOUT
import shlex

def getTmpDirPath():
    utilDir = os.path.dirname(__file__)
    e2eDir = os.path.dirname(utilDir)
    tmpDir = os.path.join(e2eDir, "tmp")
    return tmpDir

def getFixturesDirPath():
    utilDir = os.path.dirname(__file__)
    e2eDir = os.path.dirname(utilDir)
    fixturesDir = os.path.join(e2eDir, "fixtures")
    return fixturesDir

def getFixturePath(fileName):
    return os.path.join(getFixturesDirPath(), fileName)

def getPythonVenvLoader():
    utilDir = os.path.dirname(__file__)
    if platform.system().lower() == 'windows':
        pythonLoader = os.path.join(utilDir, "python-venv-loader.bat")
    else:
        pythonLoader = os.path.join(utilDir, "python-venv-loader.sh")
    return pythonLoader

def getProcessBossExecutable(configParam=""):
    cmdString = f"{getPythonVenvLoader()} -m process-boss {configParam}"
    cmdList = shlex.split(cmdString)
    return cmdList

def popenProcessBoss(configParam="", cwdParam=None):
    with Popen(getProcessBossExecutable(configParam), stdout=PIPE, stderr=STDOUT, cwd=cwdParam) as p:
        output = ""
        for line in iter(p.stdout.readline, b""):
            output = output + line.decode(sys.stdout.encoding)

        p.wait(2)
        return (p, output)
