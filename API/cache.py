import json
from os.path import isdir, isfile, join, dirname

cache_path = join(dirname(__file__).replace('API', ''), 'cache')


class Cache():
    def __init__(self, tmdbid):
        self.id = tmdbid
        self.id_path = join(cache_path, tmdbid)
        self.file_path = join(join(cache_path, tmdbid), 'tmdb.json')


    def makeDir(self):
        try:
            from os import mkdir
        except Exception as e:
            raise e

        if not isdir(cache_path):
            try:
                mkdir(cache_path)
            except Exception as e:
                raise e
            pass

        if isdir(self.id_path):
            return True
        else:
            try:
                mkdir(self.id_path)
                return True
            except Exception as e:
                return False
            pass
        pass


    def doCache(self, jsondata):
        if self.makeDir() is True:
            try:
                with open(self.file_path, 'w') as tmdbfile:
                    tmdbfile.write(json.dumps(jsondata, sort_keys=True, indent=4))
                    tmdbfile.close()
            except Exception as e:
                raise e

            try:
                return jsondata
            except Exception as e:
                raise e


    def returnCache(self):
        return json.loads(open(self.file_path, 'r').read())


    def isOnCache(self):
        if isfile(self.file_path) is True:
            try:
                file = open(self.file_path, 'r').read()
                if self.id in file:
                    return True
                else:
                    return False
                    pass
                file.close()
            except Exception as e:
                return False
        else:
            return False
            pass
        pass