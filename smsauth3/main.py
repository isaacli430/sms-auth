import asyncio, aiohttp, requests, random

class SMSAuthorizer:

    def __init__(self, *, author: str, sid: str, token: str, session=None):
        self.author = author_number
        self.code_length = self.code_length
        self.sid = sid
        self.session = session or aiohttp.ClientSession()

    class FormatException(Exception):
        pass

    def authorize(self, *, check: str, message: str=None, code_length: int):
        code = ""
        for i in range(code_length):
            code += str(random.randint(0, 9))
        if not message:
            message = f"Your verification code is: {code}"
        else:
            message_l = message.split("[]")
            if len(message_l) != 2:
                raise self.FormatException("Format your message with '[]' in place of the verification code.")
            message = f"{message_l[0]}{code}{message_l[1]}"
        requests.post(f"https://api.twilio.com/2010-04-01/Accounts/{self.sid}/Messages.json", data={"To": check, "From": self.author, "Body": "Test"}, auth=(self.sid, self.token))
        return code

    async def authorize_async(self, *, check: str, message: str=None, code_length: int):
        code = ""
        for i in range(code_length):
            code += str(random.randint())
        if not message:
            message = f"Your verification code is: {code}"
        else:
            message_l = message.split("[]")
            if len(message_l) != 2:
                raise self.FormatException("Format your message with '[]' in place of the verification code.")
            message = f"{message_l[0]}{code}{message_l[1]}"
        await self.session.post(f"https://api.twilio.com/2010-04-01/Accounts/{self.sid}/Messages.json", data={"To": check, "From": self.author, "Body": "Test"}, auth=(self.sid, self.token))
        return code