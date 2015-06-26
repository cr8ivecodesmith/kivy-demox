from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import sys
import traceback
import linecache

if sys.version_info.major < 3:
    from __builtin__ import xrange as range

from kivy.config import Config
from kivy.logger import Logger


def get_exception(full_tb=False):
    exc_type, exc_obj, tb = sys.exc_info()
    if full_tb:
        exc_obj = traceback.format_exc()

    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)

    return 'Exception in ({}, line {} "{}"):\n{}'.format(
        filename,
        lineno,
        line.strip(),
        exc_obj
    )


def main():
    from font_render.app import FontRenderApp

    Config.set('kivy', 'log_level', 'debug')
    Config.write()

    try:
        FontRenderApp().run()
    except:
        exc = get_exception(full_tb=True)
        Logger.exception(str(exc))


if __name__ == '__main__':
    main()
