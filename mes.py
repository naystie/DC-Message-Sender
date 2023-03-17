import requests
import time
import os
from colorama import init, Fore, Style
from typing import List, Tuple

# ASCII art
ascii_art = '''
  _   _                 _   _      
 | \ | |               | | (_)     
 |  \| | __ _ _   _ ___| |_ _  ___ 
 | . ` |/ _` | | | / __| __| |/ _ \\
 | |\  | (_| | |_| \__ \ |_| |  __/
 |_| \_|\__,_|\__, |___/\__|_|\___|
               __/ |               
              |___/ 

Python Discord Message Sender
'''

init(convert=True)

class Exploit:
    def __init__(self, token: str, channel_id: str, message: str):
        self.token = token
        self.channel_id = channel_id
        self.message = message
        self.headers = {'Authorization': token}

    def send_message(self) -> bool:
        """Send the message and return True if successful, False otherwise."""
        res = requests.post(
            f'https://discordapp.com/api/v6/channels/{self.channel_id}/messages',
            headers=self.headers,
            json={'content': self.message}
        )

        if res.status_code == 200:
            print(f'{Fore.GREEN}Message #{self.message_count} sent successfully: {self.message}{Style.RESET_ALL}')
            self.message_count += 1
            return True
        else:
            print(f'{Fore.RED}Error sending message: {res.content.decode()}{Style.RESET_ALL}')
            return False

    def start_sending_messages(self, interval: int):
        self.message_count = 1
        failed_attempts = 0
        while True:
            success = self.send_message()
            time.sleep(interval)
            if self.message_count % 3 == 0:
                if not success:
                    failed_attempts += 1
                    if failed_attempts >= 3:
                        print(f"{Fore.RED}Couldn't send message after {failed_attempts} attempts. Try again.{Style.RESET_ALL}")
                        self.channel_id = input('Enter channel ID: ')
                        failed_attempts = 0
                        self.message_count = 1
                        break

def main():
    print(f'{Fore.CYAN}{ascii_art}{Style.RESET_ALL}\n')

    token_file = 'token.txt'

    if not os.path.isfile(token_file):
        print(f'{Fore.RED}Error: {token_file} file not found.{Style.RESET_ALL}\n')
        time.sleep(5)
        return

    with open(token_file, 'r') as f:
        token = f.readline().strip()

    while True:
        channel_id = input('Enter channel ID: ')
        message = input('Enter message to send: ')
        interval = int(input('Enter message interval (in seconds): '))

        print(f'\n{Fore.BLUE}Sending message every {interval} seconds...{Style.RESET_ALL}\n')

        exploit = Exploit(token, channel_id, message)
        exploit.start_sending_messages(interval)

if __name__ == '__main__':
    main()
