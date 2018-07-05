import asyncio, aiohttp, urllib, random

class SMSAuthorizer:

    def __init__(self, author: str, code_length: int):
        self.author = author_number
        self.code_length = self.code_length

    class FormatException(Exception):
        pass

    def authorize(self, check: str, message: str=None):
        code = ""
        for i in range(code_length):
            code += str(random.randint())
        if not message:
            message = f"Your verification code is: {code}"
        else:
            message_l = message.split("[]")
            if len(message_l) != 2:
                raise FormatException("Format your message with '[]' in place of the verification code.")

