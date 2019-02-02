import logging

logging.basicConfig(
                    format='%(asctime)s.%(msecs)03d %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                   )


logger = logging.getLogger('dangerbot:log')
outputFileHandler = logging.TimedRotatingFileHandler('dangerbot.log', when='midnight')
logger.addHandler(outputFileHandler)

reporter = logging.getLogger('dangerbot:report')
outputFileHandler = logging.TimedRotatingFileHandler('dangerbot.report', when='midnight')
reporter.addHandler(outputFileHandler)
