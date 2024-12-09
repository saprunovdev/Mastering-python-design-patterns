from typing import Protocol


class MessageSender(Protocol):
    def send(self, message: str):
        ...

class Email(MessageSender):
    def send(self, message:str):
        print(f"Sending email: {message}")


class Notification(MessageSender):
    def __init__(self, sender: MessageSender):
        self.sender: MessageSender = sender

    def send(self, message):
        self.sender.send(message)

if __name__ == "__main__":
    email = Email()
    notification = Notification(sender=email)
    notification.send(message="This is the messsage")