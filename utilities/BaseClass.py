import inspect
import logging

import pytest



@pytest.mark.usefixtures("setup")
class BaseClass: # We can add a method to wait for a link text or object to appear and it can be called wherever needed

    def test_loggerf(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)  # Prints the file name in logs

        # where to print?
        filehandler = logging.FileHandler('mylog.log')

        # Format the log file
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        # Pass formatter info to file handler
        filehandler.setFormatter(formatter)

        # pass filehandler object to logger
        logger.addHandler(filehandler)

        # Set log level (The log file has logs from that level above in below order)
        logger.setLevel(logging.DEBUG)

        return logger
