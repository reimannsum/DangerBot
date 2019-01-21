import logging

logging.basicConfig(
                    format='%(asctime)s.%(msecs)03d %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='dangerbot.log'
                   )

logger = logging.getLogger('dangerbot')
