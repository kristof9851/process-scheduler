import json
import logging
from pathlib import Path

class Config:
    def __init__(self, config):
        logging.debug(f"config={config}")

        self.scheduler = self.initScheduler(config)
        self.logs = self.initLogs(config)
        self.processes = self.initProcesses(config)

    def initScheduler(self, config):
        configScheduler = None
        if type(config) is dict and 'scheduler' in config:
            configScheduler = config['scheduler']

        return ConfigScheduler(configScheduler)
        
    def initLogs(self, config):
        configLogs = None
        if type(config) is dict and 'logs' in config:
            configLogs = config['logs']

        return ConfigLogs(configLogs)
        
    def initProcesses(self, config):
        configProcesses = None
        if type(config) is dict and 'processes' in config:
            configProcesses = config['processes']

        return ConfigProcesses(configProcesses)
    
    def __str__(self):
        return json.dumps( self.toDict() )

    def toDict(self):
        return {
            'Config': {
                'scheduler': self.scheduler.toDict(), 
                'logs': self.logs.toDict(),
                'processes': self.processes.toDict()
            }
        }


class ConfigScheduler:
    def __init__(self, configScheduler):
        logging.debug(f"configScheduler={configScheduler}")

        self.maxWorkers = self.initMaxWorkers(configScheduler)
        self.loop = self.initLoop(configScheduler)

    def initMaxWorkers(self, configScheduler):
        maxWorkers = 10

        if type(configScheduler) is not dict or 'maxWorkers' not in configScheduler:
            return maxWorkers
        
        maxWorkers = configScheduler['maxWorkers']

        if type(maxWorkers) is not int or maxWorkers <= 0:
            errorMessage = f"Invalid configuration for \"scheduler.maxWorkers\": Positive integer required: \"{maxWorkers}\""
            logging.error(errorMessage)
            raise Exception(errorMessage)

        return maxWorkers

    def initLoop(self, configScheduler):
        configSchedulerLoop = None
        if type(configScheduler) is dict and 'loop' in configScheduler:
            configSchedulerLoop = configScheduler['loop']

        return ConfigSchedulerLoop(configSchedulerLoop)

    def __str__(self):
        return json.dumps( self.toDict() )

    def toDict(self):
        return {
            'ConfigScheduler': {
                'maxWorkers': self.maxWorkers, 
                'loop': self.loop.toDict()
            }
        }


class ConfigSchedulerLoop:
    def __init__(self, configSchedulerLoop):
        logging.debug(f"configSchedulerLoop={configSchedulerLoop}")
        
        self.restartSeconds = self.initRestartSeconds(configSchedulerLoop)
        self.runOnce = self.initRunOnce(configSchedulerLoop)

    def initRestartSeconds(self, configSchedulerLoop):
        restartSeconds = 15

        if type(configSchedulerLoop) is not dict or 'restartSeconds' not in configSchedulerLoop:
            return restartSeconds
        
        restartSeconds = configSchedulerLoop['restartSeconds']

        if type(restartSeconds) is not int or restartSeconds < 0:
            errorMessage = f"Invalid configuration for \"scheduler.loop.restartSeconds\": Non-negative integer required: \"{restartSeconds}\""
            logging.error(errorMessage)
            raise Exception(errorMessage)

        return restartSeconds

    def initRunOnce(self, configSchedulerLoop):
        runOnce = False

        if type(configSchedulerLoop) is not dict or 'runOnce' not in configSchedulerLoop:
            return runOnce
        
        runOnce = configSchedulerLoop['runOnce']

        if type(runOnce) is not bool:
            errorMessage = f"Invalid configuration for \"scheduler.loop.runOnce\": Boolean value required: \"{runOnce}\""
            logging.error(errorMessage)
            raise Exception(errorMessage)

        return runOnce

    def __str__(self):
        return json.dumps( self.toDict() )

    def toDict(self):
        return {
            'ConfigSchedulerLoop': {
                'restartSeconds': self.restartSeconds, 
                'runOnce': self.runOnce
            }
        }


class ConfigLogs:
    def __init__(self, configLogs):
        logging.debug(f"configLogs={configLogs}")

        self.enabled = self.initEnabled(configLogs)
        self.schedulerLogDir = self.initSchedulerLogDir(configLogs)
        self.processLogDir = self.initProcessLogDir(configLogs)

    def initEnabled(self, configLogs):
        enabled = False

        if type(configLogs) is not dict or 'enabled' not in configLogs:
            return enabled
        
        enabled = configLogs['enabled']

        if type(enabled) is not bool:
            errorMessage = f"Invalid configuration for \"logs.enabled\": Boolean value required: \"{enabled}\""
            logging.error(errorMessage)
            raise Exception(errorMessage)

        return enabled

    def initSchedulerLogDir(self, configLogs):
        schedulerLogDir = ""

        if type(configLogs) is not dict or 'schedulerLogDir' not in configLogs:
            return schedulerLogDir
        
        schedulerLogDir = configLogs['schedulerLogDir']

        if type(schedulerLogDir) is not str or not Path(schedulerLogDir).is_dir():
            errorMessage = f"Invalid configuration for \"logs.schedulerLogDir\": Valid directory path required: \"{schedulerLogDir}\""
            logging.error(errorMessage)
            raise Exception(errorMessage)

        return schedulerLogDir

    def initProcessLogDir(self, configLogs):
        processLogDir = ""

        if type(configLogs) is not dict or 'processLogDir' not in configLogs:
            return processLogDir
        
        processLogDir = configLogs['processLogDir']

        if type(processLogDir) is not str or not Path(processLogDir).is_dir():
            errorMessage = f"Invalid configuration for \"logs.processLogDir\": Valid directory path required: \"{processLogDir}\""
            logging.error(errorMessage)
            raise Exception(errorMessage)

        return processLogDir

    def __str__(self):
        return json.dumps( self.toDict() )

    def toDict(self):
        return {
            'ConfigLogs': {
                'enabled': self.enabled, 
                'schedulerLogDir': self.schedulerLogDir, 
                'processLogDir': self.processLogDir
            }
        }


class ConfigProcesses:
    def __init__(self, configProcesses):
        logging.debug(f"configProcesses={configProcesses}")

        self.processes = self.initProcesses(configProcesses)

    def initProcesses(self, configProcesses):
        processes = []

        if type(configProcesses) is not list or len(configProcesses) == 0:
            errorMessage = f"Invalid configuration for \"processes.*\": You have to define at least one process!"
            logging.error(errorMessage)
            raise Exception(errorMessage)
        
        for c in configProcesses:
            processes.append( ConfigProcess(c) )

        return processes

    def __iter__(self):
        self.i = -1
        return self
    
    def __next__(self):
        self.i += 1
        if self.i < len(self.processes):
            return self.processes[ self.i ]
        else:
            raise StopIteration

    def __str__(self):
        return json.dumps( self.toDict() )

    def toDict(self):
        return {
            'ConfigProcesses': [ p.toDict() for p in self.processes ]
        }


class ConfigProcess:
    def __init__(self, configProcess):
        logging.debug(f"configProcess={configProcess}")
        
        self.id = self.initId(configProcess)
        self.cron = self.initCron(configProcess)
        self.command = self.initCommand(configProcess)
        self.runAtStartup = self.initRunAtStartup(configProcess)

    def initId(self, configProcess):
        if (type(configProcess) is not dict or 
            'id' not in configProcess or 
            type(configProcess['id']) is not str or 
            len(configProcess['id']) == 0
        ):
            errorMessage = f"Invalid configuration for \"processes.*.id\": Non-empty string required: \"{configProcess['id']}\""
            logging.error(errorMessage)
            raise Exception(errorMessage)
        
        return configProcess['id']
    
    def initCron(self, configProcess):
        if (type(configProcess) is not dict or 
            'cron' not in configProcess or 
            type(configProcess['cron']) is not str or 
            len(configProcess['cron']) == 0
        ):
            errorMessage = f"Invalid configuration for \"processes.*.cron\": Non-empty string required: \"{configProcess['cron']}\""
            logging.error(errorMessage)
            raise Exception(errorMessage)
        
        return configProcess['cron']

    def initCommand(self, configProcess):
        if (type(configProcess) is not dict or
            'command' not in configProcess or 
            type(configProcess['command']) is not str or 
            len(configProcess['command']) == 0
        ):
            errorMessage = f"Invalid configuration for \"processes.*.command\": Non-empty string required: \"{configProcess['command']}\""
            logging.error(errorMessage)
            raise Exception(errorMessage)
        
        return configProcess['command']
    
    def initRunAtStartup(self, configProcess):
        runAtStartup = False

        if type(configProcess) is not dict or 'runAtStartup' not in configProcess:
            return runAtStartup

        runAtStartup = configProcess['runAtStartup']

        if type(runAtStartup) is not bool:
            errorMessage = f"Invalid configuration for \"processes.*.runAtStartup\": Boolean value required: \"{configProcess['runAtStartup']}\""
            logging.error(errorMessage)
            raise Exception(errorMessage)
        
        return runAtStartup

    def __str__(self):
        return json.dumps( self.toDict() )

    def toDict(self):
        return {
            'ConfigProcess': {
                'id': self.id,
                'cron': self.cron,
                'command': self.command,
                'runAtStartup': self.runAtStartup
            }
        }
