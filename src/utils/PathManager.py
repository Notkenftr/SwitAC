import os
root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..'))
class PathManager:
    @staticmethod
    def getRoot():
        return root
    def getTempPath(self):
        os.makedirs(os.path.join(PathManager.getRoot(), 'temp'),exist_ok=True)
        return os.path.join(PathManager.getRoot(), 'temp')