#!encoding=utf-8
import cProfile
import os
import pstats
import tempfile
try:
    from cStringIO import StringIO  # py2
except ImportError:
    from io import StringIO  # py3

from django.conf import settings


class ProfilerMiddleware(object):
    """
    View performance efficiency tools , only for the development phase
    Add parameters after the url to see prof
    eg: http://localhost:8000/index?prof
    """

    def process_view(self, request, view, args, kwargs):
        if settings.DEBUG and 'prof' in request.GET:
            self.profiler = cProfile.Profile()
            args = (request,) + args
            return self.profiler.runcall(view, *args, **kwargs)

    def process_response(self, request, response):
        if settings.DEBUG and 'prof' in request.GET:
            (fd, self.profiler_file) = tempfile.mkstemp()
            self.profiler.dump_stats(self.profiler_file)
            out = StringIO()
            stats = pstats.Stats(self.profiler_file, stream=out)
            stats.strip_dirs()
            stats.print_stats()
            os.unlink(self.profiler_file)
            response.content = out.getvalue()
        return response
