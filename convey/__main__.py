#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


__doc__ = """Convey – CSV swiss knife brought by CSIRT.cz"""
__author__ = "Edvard Rejthar, CSIRT.CZ"
__date__ = "$Feb 26, 2015 8:13:25 PM$"

import logging

fileHandler = logging.FileHandler("convey.log")
fileHandler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
fileHandler.setLevel(logging.WARNING)
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
consoleHandler.setLevel(logging.WARNING)
handlers = [fileHandler, consoleHandler]
logging.basicConfig(level=logging.INFO, handlers=handlers)
logger = logging.getLogger("convey")

# logging.getLogger("lepl").setLevel(logging.ERROR)  # suppress a superfluous info when using lepl e-mail validator

if sys.version_info[0:2] < (3, 6):
    print("We need at least Python 3.6, your version is " + sys.version + ". Try an older Convey release or rather upgrade Python.")
    quit()


def main():
    #print(__doc__)
    try:
        from .controller import Controller
        Controller()
    except KeyboardInterrupt:
        print("Interrupted")
    except SystemExit as e:
        pass
    except:
        import traceback

        try:
            import pudb as mod
        except ImportError:
            try:
                import ipdb as mod
            except ImportError:
                import pdb as mod
        type_, value, tb = sys.exc_info()
        traceback.print_exc()
        mod.post_mortem(tb)


class WebServer:
    source_parser = None


def application(env, start_response):
    """ WSGI launcher. You may expose installed convey as a web service.
        Launch: uwsgi --http :9090 --wsgi-file wsgi.py
        Access: http://localhost:9090/?q=1.2.3.4
    """
    if not WebServer.source_parser:
        from convey.config import Config
        from convey.sourceParser import SourceParser
        Config.init()
        WebServer.source_parser = SourceParser(prepare=False)

    headers = [('Access-Control-Allow-Origin', '*')]
    t = env["QUERY_STRING"].split("q=")  # XX sanitize?
    if len(t) == 2:
        response = WebServer.source_parser.set_stdin([t[1]]).check_single_cell()
        headers.append(('Content-Type', 'application/json'))
        status = '200 OK'
    else:
        status = '400 Bad Request'
        response = '{"error": "invalid input"}'
    start_response(status, headers)

    # start_response('200 OK', [('Content-Type', 'text/html')])
    # return [b"Hello World" + bytes(repr(aa), "UTF-8")]
    return [bytes(response, "UTF-8")]


if __name__ == "__main__":
    print("*************")
    main()
