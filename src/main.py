import os
import logging
from log import set_logging

def main()->None:
    set_logging(str(os.environ.get("LOG_LEVEL","WARNING")))
    logging.info("Test zprava")
    logging.debug("Test zprava")
    logging.warning("Test zprava")
    logging.error("Test zprava")
if __name__ == '__main__':
    main()