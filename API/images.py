import json
from os import mkdir
from os.path import dirname, basename
from os.path import join, isfile, isdir


try:
    from API.apibase import get
    from API.cache import Cache, cache_path
    from API.omdb import omdbData
except:
    from apibase import get
    from cache import Cache, cache_path
    from omdb import omdbData
    pass


dir_path = dirname(__file__).replace('API', '')


class Images():
    def __init__(self):
        self.dir = dir_path
        self.nocov = join(self.dir, 'images/no-cover.jpg')
        self.cache_path = join(self.dir, 'cache')


    def parseData(self, _type, _id):
        try:
            self.omdb = omdbData(_id)
        except Exception as e:
            raise e


        if self.omdb.status_code == 200:
            try:
                self.omdb = json.loads(self.omdb.content)
            except Exception as e:
                raise e

            if _type == 'poster':
                try:
                    return self.omdb['Poster']
                except Exception as e:
                    return None
                pass
            pass
        pass


    def retImg(self, _type, imdbid, traktid):
        traktid = str(traktid)
        try:
            import urllib.request
        except Exception as e:
            raise e

        try:
            url = self.parseData(_type, imdbid)
        except Exception as e:
            return self.nocov

        if not url is None:
            if _type == 'poster':
                file_name = basename(url)
                cont_dir = join(self.cache_path, traktid)
                poster_path = join(self.cache_path, traktid, ''.join(['poster.', file_name.split('.')[-1]]))


                if isfile(poster_path) == False:
                    try:
                        urllib.request.urlretrieve(url, join('/tmp/', file_name))
                        tmpfile = join('/tmp/', file_name)
                    except Exception as e:
                        raise e

                    if isfile(tmpfile) is True:
                        print('here')
                        if isdir(cont_dir) == False:
                            mkdir(cont_dir)
                            pass
                        try:
                            from shutil import move as movefile
                        except Exception as e:
                            raise e

                        try:
                            movefile(tmpfile, poster_path)
                        except Exception as e:
                            raise e

                        if isfile(poster_path) == True:
                            print('sss')
                            return poster_path
                else:
                    return poster_path
                pass
            pass

# im = Images()
# print(im.retImg('poster', 'tt0114168', '999999'))
# omdbData('movie', 'tt0114168')