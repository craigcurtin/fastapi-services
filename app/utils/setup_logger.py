import sys
import logging
from pytz import timezone
from datetime import datetime

# *force* UTC based time in log messages
tz = timezone('UTC')


# logging formatter, specify UTC as TZ to hardcode
def time_tz(*args):
    return datetime.now(tz).timetuple()


# TODO - CSC working this function to be JSON aware/enabled ...

def setup_logger(app_name, log_level):
    """configure logger with UTC timestamp, bunch of default values"""
    # Setting up logger
    # log_levels: NOTSET=0, DEBUG=10, INFO=20, WARN=30, ERROR=40, and CRITICAL=50
    log_file_name = '{}.log'.format(app_name)
    short_file_format = "%(asctime)s:%(levelname)s:%(message)s"

    # some playing around adding 'extra' keywords in the logging file format
    long_file_format = "%(asctime)s %(HOST)s %(AppId)d %(AppVersion)s %(levelname)s %(name)s %(message)s %(filename)s %(funcName)s %(levelname)s %(lineno)d %(message)s %(module)s %(msecs)d %(name)s %(pathname)s %(process)d %(processName)s %(relativeCreated)d %(thread)d %(threadName)s %(uid)"
    long_file_format = "%(asctime)s %(levelname)s %(name)s %(message)s %(filename)s %(funcName)s %(levelname)s %(lineno)d %(message)s %(module)s %(msecs)d %(name)s %(pathname)s %(process)d %(processName)s %(relativeCreated)d %(thread)d %(threadName)s"
    # long_file_format = "%(asctime)s:%(levelname)s%(name)s %(message)s %(filename)s %(funcName)s %(levelname)s %(lineno)d %(message)s %(module)s %(msecs)d %(name)s %(pathname)s %(process)d %(processName)s %(relativeCreated)d %(thread)d %(threadName)s"
    log_file_format = short_file_format

    # make sure valid log level is passed in, default to DEBUG ...
    valid_log_levels = [logging.DEBUG, logging.INFO, logging.WARN, logging.ERROR, logging.CRITICAL]
    if log_level not in valid_log_levels:
        log_level = logging.DEBUG

    # these are the extra attributes to be added to standard logging
    extra_attributes = {'Host': '10.0.0.1',
                        'AppId': 1024,
                        'AppVersion': '1.0.0',
                        'uid': 12345
                        }
    logger = logging.getLogger()
    logging.LoggerAdapter(logger, extra_attributes)

    # add in our custom UTC timezone converter
    logging.Formatter.converter = time_tz
    logging.basicConfig(level=log_level, filename=log_file_name, filemode="a",
                        format=log_file_format)

    # configure stdout same as file
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(logging.Formatter(log_file_format))
    logging.getLogger().addHandler(sh)

    logging.info('App:{} startup'.format(app_name))
    return

