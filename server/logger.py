import logging

def setup_logger(name="Medical_Assistant"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG) # Get logs above the level of DEBUG

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG) # handler helps in bringing log to your console

    formatter=logging.Formatter("[%(asctime)s] [%(levelname)s] --- [%(message)s]") # format in which you want your log
    handler.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(handler)

    return logger

logger = setup_logger()

## TYPES OF LOGS ##
# logger.info("RAG-test")
# logger.debug("debugging")
# logger.error("Error")
# logger.critical("Critical")

    