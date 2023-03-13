import requests
import time
import os
from colorama import init, Fore, Style

init(convert=True)


class Exploit:
    def __init__(self, token, channel_id, message):
        self.token = token
        self.channel_id = channel_id
        self.message = message
        self.headers = {'Authorization': token}

    def send_message(self):
        """Send the message."""
        res = requests.post(
            f'https://discordapp.com/api/v6/channels/{self.channel_id}/messages',
            headers=self.headers,
            json={'content': self.message}
        )

        if res.status_code == 200:
            print(f'{Fore.GREEN}Message sent successfully: {self.message}{Style.RESET_ALL}')
        else:
            print(f'{Fore.RED}Error sending message: {res.content.decode()}{Style.RESET_ALL}')


def main():
    print(f'{Fore.CYAN}Welcome to the Discord Message Sender!{Style.RESET_ALL}\n')

    token_file = 'token.txt'

    if not os.path.isfile(token_file):
        print(f'{Fore.RED}Error: {token_file} file not found.{Style.RESET_ALL}\n')
        time.sleep(5)
        return

    with open(token_file, 'r') as f:
        token = f.readline().strip()

    channel_id = input('Enter channel ID: ')
    message = input('Enter message to send: ')
    interval = int(input('Enter message interval (in seconds): '))

    print(f'\n{Fore.BLUE}Sending message every {interval} seconds...{Style.RESET_ALL}\n')

    exploit = Exploit(token, channel_id, message)

    # Send the initial message
    exploit.send_message()

    # Loop and send the message every interval seconds
    while True:
        time.sleep(interval)
        exploit.send_message()


if __name__ == '__main__':
    main()
