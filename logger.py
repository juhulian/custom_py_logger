from bcolors import bcolors as b
from time import gmtime, strftime


class Log:
    """
    simple logger
    """

    time_format = "%H:%M:%S"  # %Y-%m-%d %H:%M:%S

    def __init__(self, name=""):
        self.name = name

    def info(self, msg):
        print("{} {}{}{} [{}i{}] {}{}{}".format(strftime(self.time_format, gmtime()),
                                                b.BOLD, self.name, b.ENDC,
                                                b.OKBLUE, b.ENDC, b.OKBLUE, msg, b.ENDC))

    def info2(self, msg):
        print("{} {}{}{} [{}ii{}] {}{}{}".format(strftime(self.time_format, gmtime()),
                                                 b.BOLD, self.name, b.ENDC,
                                                 b.OKGREEN, b.ENDC, b.OKGREEN, msg, b.ENDC))

    def error(self, msg):
        print("{} {}{}{} [{}e{}] {}{}{}".format(strftime(self.time_format, gmtime()),
                                                b.BOLD, self.name, b.ENDC,
                                                b.FAIL, b.ENDC, b.FAIL, msg, b.ENDC))

    def warning(self, msg):
        print("{} {}{}{} [{}w{}] {}{}{}".format(strftime(self.time_format, gmtime()),
                                                b.BOLD, self.name, b.ENDC,
                                                b.WARNING, b.ENDC, b.WARNING, msg, b.ENDC))

    def debug(self, msg):
        print("{} {}{}{} [d] {}".format(strftime(self.time_format, gmtime()),
                                        b.BOLD, self.name, b.ENDC, msg))
