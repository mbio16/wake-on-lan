import logging

def __get_level(level:str)->None:
    if level=="DEBUG":
        return logging.DEBUG
    elif level=="INFO":
        return logging.INFO
    elif level=="WARNING":
        return logging.WARNING
    elif level=="ERROR":
        return logging.ERROR
    else:
        return logging.WARNING
    
def set_logging(level:str="WARNING")->None:
    FORMAT = '%(levelname)s:%(asctime)s:%(message)s'
    logging.basicConfig(
     level=__get_level(level), 
     format= FORMAT,
     datefmt='%Y-%m-%d %H:%M:%S'
 )