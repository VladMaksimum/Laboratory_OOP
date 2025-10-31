from Logger import Logger
from Filters.SimpleLogFilter import SimpleLogFilter
from Filters.ReLogFilter import ReLogFilter
from Filters.LevelLogFilter import LevelLogFilter
from Formatters.SimpleFormatter import SimpleFormatter
from Handlers.ConsoleHandler import ConsoleHandler
from Handlers.FtpHandler import FtpHandler
from Handlers.SocketHandler import SocketHandler
from Handlers.FileHandler import FileHandler
from Handlers.SyslogHandler import SyslogHandler
from LogLevel import LogLevel


logger1 = Logger([SimpleLogFilter("test"), LevelLogFilter(LogLevel.INFO)], [SimpleFormatter()], \
                [ConsoleHandler(), SyslogHandler("labs/lab_3/test1.log"), FileHandler("labs/lab_3/log1.txt")])
logger2 = Logger([ReLogFilter("[#]\d{3}\s\w{1,}\s\w{1,}")], [SimpleFormatter()], [ConsoleHandler(),\
                     SyslogHandler("labs/lab_3/test2.log"), FileHandler("labs/lab_3/log2.txt")])

logger1.log(LogLevel.INFO, "It's test")
logger2.log_warn("#456 Session soon")
logger2.log_error("#123 Not found")