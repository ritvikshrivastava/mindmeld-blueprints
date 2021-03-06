import os
import luigi
API_KEY = os.environ['TMDB_API_KEY']


class GetTMDB(luigi.Task):
    api_key = API_KEY
    tmdb_endpoint = luigi.Parameter()
    output_dir = luigi.Parameter()

    def __init__(self, *args, **kwargs):
        self._complete = False
        luigi.Task.__init__(self, *args, **kwargs)

    def output(self):
        return self.input()
