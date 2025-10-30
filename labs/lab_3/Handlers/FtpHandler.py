from labs.lab_3.LogLevel import LogLevel
from ILogHandler import ILogHandler

class FtpHandler(ILogHandler):
    def __init__(self, server: str, username: str, password: str, message_file: str) -> None:
        self.server = server
        self.username = username
        self.password = password
        self.message_file = message_file

    def handle(self, log_level: LogLevel, text: str) -> None:
        from ftplib import FTP

        with open(self.message_file, "w") as file:
            file.write(text)
        

        with open(self.message_file, 'rb') as file:
            
            ftp = FTP(self.server)

            ftp.login(self.usernamer, self.password)
            ftp.storbinary(f"STOR {self.message_file}", file)

            ftp.quit()