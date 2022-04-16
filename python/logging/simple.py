# logger=logging.getLogger('dev')
# logger.setLevel(logging.DEBUG)

# logging.warning('this is a warring')

# mainLogger=logging.getLogger('main')
# # mainLogger.setLevel(logging.INFO)

# devLogger=logging.getLogger('main.dev')

# print(mainLogger.getEffectiveLevel())
# print(devLogger.getEffectiveLevel())

# logger=logging.getLogger('dev')
# logger.setLevel(logging.INFO)

# fileHandler=logging.FileHandler('test.log')
# fileHandler.setLevel(logging.INFO)

# consoleHandler=logging.StreamHandler()
# consoleHandler.setLevel(logging.INFO)

# logger.addHandler(fileHandler)
# logger.addHandler(consoleHandler)

# logger.info('information message')

# logger=logging.getLogger('dev')
# logger.setLevel(logging.INFO)

# consoleHandler=logging.StreamHandler()
# consoleHandler.setLevel(logging.INFO)

# logger.addHandler(consoleHandler)

# formatter=logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
# consoleHandler.setFormatter(formatter)

# logger.info('information message')

# logging.basicConfig(filename='Deep-Q-Learning-learn/python/test.log', format='%(filename)s: %(message)s',
#                     level=logging.DEBUG)

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

# logger=logging.getLogger('dev')
# logger.setLevel(logging.INFO)

# consoleHandler=logging.StreamHandler()
# consoleHandler.setLevel(logging.INFO)

# logger.addHandler(consoleHandler)

# formatter=logging.Formatter('%(asctime)s %(name)s %(levelname)s:%(message)s')
# consoleHandler.setFormatter(formatter)

# logger.info('This is a info message')

# logging.basicConfig(filename='test.log', format='%(asctime)s %(filename)s : %(message)s', level=logging.INFO)

# logging.info('this is a info message')
# logging.debug('this is a debug message')
# logging.debug('this is a debug msg')
# logging.warning('this is a warning message')
# logging.error('this ia a error')

# import logging
# import logging.config

# logging.config.fileConfig(fname='log.conf')

# logger=logging.getLogger('dev')
# logger.info('This is a info message')

import logging
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

log_format='%(asctime)s %(filename)s : %(message)s'
datefmts='%Y-%m-%d %H:%M:%S'

logging.basicConfig(filename='./test.log', format=log_format, datefmt=datefmts)

logging.error('sssss')