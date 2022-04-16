import logging

# logger=logging.getLogger('dev')
# logger.setLevel(logging.DEBUG)

# logging.warning('this is a warring')

# mainLogger=logging.getLogger('main')
# # mainLogger.setLevel(logging.INFO)

# devLogger=logging.getLogger('main.dev')

# print(mainLogger.getEffectiveLevel())
# print(devLogger.getEffectiveLevel())

import logging

logger=logging.getLogger('dev')
logger.setLevel(logging.INFO)

fileHandler=logging.FileHandler('test.log')
fileHandler.setLevel(logging.INFO)

consoleHandler=logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)

logger.addHandler(fileHandler)
logger.addHandler(consoleHandler)

logger.info('information message')