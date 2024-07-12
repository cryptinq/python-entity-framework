import logging
import os
from datetime import date, datetime

from core.helpers.console.color import c


class Console:

    LOG_LEVEL = logging.INFO

    @classmethod
    def set_log_level(cls, log_level: int): cls.LOG_LEVEL = log_level

    def __init__(self):
        self.styles = {
            "default": self.default,
            "info": self.info,
            "success": self.success,
            "error": self.error
        }

    @classmethod
    def stdout(cls, message, style="default"): cls().styles[style](message)

    # @classmethod
    # def log(cls, message, style="info"):
    #     if channel == "core":
    #         if cls.logLevel >= 10: cls().styles[style](message)
    #     if channel == "app":
    #         cls().styles[style](message)

    @classmethod
    def default(cls, message): print(c(message))

    @classmethod
    def info(cls, message):
        if cls.LOG_LEVEL == logging.INFO:
            print(c("∑9.∑f INFO ") + "    | " + c(message))

    @classmethod
    def warning(cls, message):
        if cls.LOG_LEVEL == logging.WARNING:
            print(c("∑e.∑f WARNING ") + " | " + c(message))

    @classmethod
    # def error(cls, message): print(c("∑c.∑f ERROR ") + " | " + c(message))
    def error(cls, message, fatal: bool = False, format_traceback: bool = True):

        if fatal:

            # if Configuration.get("appEnvironment") == "development":

            # if not os.path.exists(Logger.logDir): os.mkdir(Logger.logDir)

            if format_traceback:
                traceback_lines = message.splitlines()
                # formatted_traceback_lines = [traceback_lines[0]] + [c(f"∑c.∑f ERROR ") + "  " + c(f"∑4{line}") for line in traceback_lines[1:]]
                formatted_traceback_lines = [traceback_lines[0]] + [c(f"∑c.∑f ERROR ") + "  " + line for line in
                                                                    traceback_lines[1:]]
                # formatted_traceback_lines[-1] = c(f"∑c.∑f ERROR ") + "\n" + formatted_traceback_lines[-1][:40] + c("∑4 Message : ") + formatted_traceback_lines[-1][40:]
                formatted_traceback_lines[-1] = c(f"∑c.∑f ERROR ") + "\n" + formatted_traceback_lines[-1][:40] + " " + \
                                                formatted_traceback_lines[-1][40:]
                message = "\n".join(formatted_traceback_lines)

            if cls.LOG_LEVEL == logging.FATAL:
                print("")
                # print(c(f"∑c.∑f ERROR ") + "  ")
                print(c(f"∑c.∑f ERROR ") + "  ",
                      c("∑4============================= A FATAL ERROR OCCURED ============================="))
                print(c(f"∑c.∑f ERROR ") + "  ")
                # print(f"[{Logger.appName}]", f"File: {caller_file}, Line: {caller_line}, Function: {caller_function}()")
                print(c(f"∑c.∑f ERROR ") + "  ", message)
                print(c(f"∑c.∑f ERROR ") + "   ")
                # print(c(f"∑c.∑f ERROR ") + "  ", c(f"Logs : {os.path.abspath(Logger.logFile)}"))
                print(c(f"∑c.∑f ERROR ") + "  ",
                      c(f"Timestamp : {datetime.now().strftime('%d-%m %H:%M:%S')} {datetime.now().microsecond // 1000:03d}ms"))
                print(c(f"∑c.∑f ERROR ") + "  ")
                print(c(f"∑c.∑f ERROR ") + "  ",
                      c("∑4=================================================================================="))

                return

        else:
            if cls.LOG_LEVEL == logging.DEBUG:
                print(c("∑c.∑f ERROR ") + "    | " + c(message))



    @classmethod
    def success(cls, message):
        if cls.LOG_LEVEL == logging.INFO:
            print(c("∑a. SUCCESS ") + " | " + c(message))

    @classmethod
    def system(cls, message):
        if cls.LOG_LEVEL == logging.DEBUG:
            print(c("∑5. SYSTEM ") + "  | " + c(message))

    @classmethod
    def debug(cls, value):
        if cls.LOG_LEVEL == logging.DEBUG:
            print(c("∑6.∑f DEBUG ") + "   | " + c(value))
