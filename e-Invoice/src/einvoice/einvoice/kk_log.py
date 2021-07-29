import logging

def create_logger(name):
    """This function creates a logger template for the einvoice package.

    This funtion creates a consistant format and location for
    all application log files to write to.
    """
    print("Create logger with name %s" % name)
    clog = logging.getLogger("clog_" + name)
    flog = logging.getLogger("flog_" + name)

    # It's okay to run INFO in Dev.  Turn it down to DEBUG for QA
    # and WARN for Prod unless troubleshooting an issue.
    flog.setLevel(logging.DEBUG)
    clog.setLevel(logging.DEBUG)

    # create file handler which writes to a file.
    flogger = logging.FileHandler("jupyter_output.log")
    flogger.setLevel(logging.DEBUG)

    # create console handler with a higher log level
    clogger = logging.StreamHandler()
    clogger.setLevel(logging.DEBUG)

    # Create a custom formatter and add it to the handlers
    _format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    datefmt = "%m/%d/%Y %I:%M:%S %p"
    formatter = logging.Formatter(_format, datefmt)

    flogger.setFormatter(formatter)
    clogger.setFormatter(formatter)

    # Associate the the handlers to the loggers
    flog.addHandler(flogger)
    clog.addHandler(clogger)

    return clog
