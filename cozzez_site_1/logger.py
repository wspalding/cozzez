import logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters':
    {
        'verbose':
        {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple':
        {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers':
    {
        'null':
        {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console':
        {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
            }
        },
    'loggers':
    {
        '':
        {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'django':
        {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'testlogger':
        {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}
