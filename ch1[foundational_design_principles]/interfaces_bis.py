from typing import Protocol


class Logger(Protocol):
    def log(self, message: str):
        ...

class ConsoleLogger:
    def log(self, message: str):
        print(f"Console: {message}")

class FileLogger:
    def log(self, message: str):
        with open("log.txt", "a") as f:
            f.write(f"File: {message}")


def log_message(logger: Logger, message: str):
    logger.log(message)

if __name__ == "__main__":
    log_message(ConsoleLogger(), "Console message")
    log_message(FileLogger(), "Message to log in file")