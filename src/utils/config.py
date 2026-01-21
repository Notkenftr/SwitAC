import os.path

import yaml
from ..utils import PathManager

class Config:
    def __init__(self):
        self.configData = self._read()


    def _read(self):
        config_path = os.path.join(PathManager.getRoot(),'config.yml')
        with open(config_path, 'r') as stream:
            config = yaml.load(stream, Loader=yaml.SafeLoader)
            return config

    def getToken(self):
        if self.configData:
            return self.configData['Discord']['bot-token']
