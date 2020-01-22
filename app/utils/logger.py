# -*- Coding: UTF-8 -*-
import time
from logging import config
from logging import getLogger


class Logger(object):

    @staticmethod
    def get_logger(name):
        config.dictConfig(
            {
                'version': 1,
                'formatters':
                    {
                        'customFormatter': {
                            'format': '%(asctime)s %(levelname)s %(filename)s:%(lineno)d %(funcName)s %(message)s',
                            'datefmt': '%Y-%m-%d %H:%M:%S'
                        }
                    },
                'loggers': {
                    'console': {
                        'handlers': ['consoleHandler'],
                        'level': 'DEBUG',
                        'qualname': 'console',
                        'propagate': False
                    }},
                'handlers': {
                    'consoleHandler': {
                        'class': 'logging.StreamHandler',
                        'level': 'DEBUG',
                        'formatter': 'customFormatter',
                        'stream': 'ext://sys.stdout'
                    }},
                'root': {
                    'level': 'DEBUG',
                    'handlers': ['consoleHandler']}
            }
        )
        return getLogger(name)

    @staticmethod
    def time_measure(logger, target):
        def __decorator(func):
            def __wrapper(obj, *args, **kwargs):
                start = time.time()
                logger.info('Measure execution time.')
                logger.info('target: {}'.format(target))
                logger.info('func: {}'.format(func.__name__))
                f = func(obj, *args, **kwargs)
                end = time.time() - start
                m, s = divmod(end, 60)
                logger.info('Elapsed time:{0} [sec], {1} [min]'.format(s, m))
                return f

            return __wrapper

        return __decorator
