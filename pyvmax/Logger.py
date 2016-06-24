import logging

def logger_setup():
    """
    setup the style and defults of the python logger

    Args:
    Returns:
    Raises:

    """
    # set up logging everything to file with timestamp formatting
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename='pyvmax.log',
                        filemode='w')

    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.WARNING)

    # set a format which is simpler for console use
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    # calm down the chatty requests module
    logging.getLogger("requests").setLevel(logging.WARNING)

def get_logger(log_name):
    """
    creates a new logger object with a customized label

    Args:
        log_name: string of the name of the logger
    Returns:
        logging object
    Raises:

    """
    return logging.getLogger(log_name)


