import argparse
import os
import sys

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
GRAY = "\033[90m"
RESET = "\033[0;0m"


def main():
    arg_parser = argparse.ArgumentParser(description='Hex Editor')
    arg_parser.add_argument('filename', help='Name of file to edit')

    args = arg_parser.parse_args()
    filename = args.filename

    if not os.path.exists(filename):
        print(f'{RED}File {filename} does not exist{RESET}')
        sys.exit(1)

    if not os.access(filename, os.R_OK):
        print(f'{RED}File {filename} access denied{RESET}')
        sys.exit(1)

    with open(filename, 'rb') as f:
        data = f.read()

    print(f'{GREEN}To see a list of commands, type {YELLOW}help{RESET}')
    while True:
        try:
            command = input(f"> {GRAY}").strip().lower()
            print(RESET, end='')
            parsed_cmd = command.split(' ')
            if command == 'exit' or command == 'quit' or command == 'q':
                print('See you next time! :)')
                break
            elif command == 'help' or command == '?' or command == 'h':
                print(f'''{GREEN}Commands{RESET}:
    {YELLOW}help{RESET}                       - Show this help message   | {GREEN}alias{RESET}: {YELLOW}h{RESET}, {YELLOW}?{RESET}
    {YELLOW}exit{RESET}                       - Exit the program         | {GREEN}alias{RESET}: {YELLOW}q{RESET}, {YELLOW}quit{RESET}
    
    {YELLOW}insert{RESET} {BLUE}<offset> <bytes>{RESET}    - Insert data at offset    | {GREEN}alias{RESET}: {YELLOW}i{RESET}, {YELLOW}put{RESET}
    {YELLOW}delete{RESET} {BLUE}<offset> [length]{RESET}   - Delete data at offset    | {GREEN}alias{RESET}: {YELLOW}d{RESET}, {YELLOW}remove{RESET}
    {YELLOW}replace{RESET} {BLUE}<offset> <bytes>{RESET}   - Replace data at offset   | {GREEN}alias{RESET}: {YELLOW}e{RESET}, {YELLOW}sub{RESET}
    {YELLOW}save{RESET}                       - Save changes to file     | {GREEN}alias{RESET}: {YELLOW}s{RESET}
    
    {YELLOW}read{RESET} {BLUE}[offset] [length]{RESET}     - Read data at offset

{GREEN}Data Formats{RESET}:
    {YELLOW}offset{RESET}   - Hexadecimal offset, e.g. {BLUE}0x10{RESET} etc. (defaults to {BLUE}0{RESET})
    {YELLOW}length{RESET}   - Integer length, starting at {BLUE}1{RESET} (in delete command defaults to {BLUE}1{RESET})
    {YELLOW}bytes{RESET}    - Hexadecimal bytes, e.g. {BLUE}00 6F D4{RESET} etc.
    
{BLUE}Parameters in square brackets are optional{RESET}   - {YELLOW}[]{RESET}
{BLUE}Parameters in angle brackets are required{RESET}    - {YELLOW}<>{RESET}
''')
            elif parsed_cmd[0] == 'read' or parsed_cmd[0] == 'r':
                if len(parsed_cmd) == 1:
                    offset = 0
                    length = len(data)
                elif len(parsed_cmd) == 2:
                    offset = int(parsed_cmd[1], 16)
                    length = len(data)
                elif len(parsed_cmd) == 3:
                    offset = int(parsed_cmd[1], 16)
                    length = int(parsed_cmd[2])
                else:
                    print(f'{RED}Invalid arguments{RESET}')
                    continue

                if offset < 0 or offset >= len(data):
                    print(f'{RED}Invalid offset{RESET}')
                    continue
                if length < 1:
                    print(f'{RED}Invalid length{RESET}')
                    continue
                if offset + length > len(data):
                    length = len(data) - offset

                hex_bytes = data[offset:offset + length]
                line = 1
                for i, byte in enumerate(hex_bytes):
                    if i % 16 == 0:
                        print(f'{YELLOW}{line:04X}{RESET} | ', end='')
                        line += 1
                    print(f'{byte:02X} ', end='')
                    if i % 8 == 7:
                        print(' ', end='')
                    if i % 16 == 15:
                        print()
                print()
            elif parsed_cmd[0] == 'insert' or parsed_cmd[0] == 'i' or parsed_cmd[0] == 'put':
                if len(parsed_cmd) < 3:
                    print(f'{RED}Invalid arguments{RESET}')
                    continue

                offset = int(parsed_cmd[1], 16)
                hex_data = parsed_cmd[2:]
                data = data[:offset] + bytes([int(b, 16) for b in hex_data]) + data[offset:]
                print(f'{YELLOW}{len(hex_data)}{RESET} bytes inserted successfully')
            elif parsed_cmd[0] == 'delete' or parsed_cmd[0] == 'd' or parsed_cmd[0] == 'remove':
                if len(parsed_cmd) < 2:
                    print(f'{RED}Invalid arguments{RESET}')
                    continue

                offset = int(parsed_cmd[1], 16)
                if len(parsed_cmd) == 2:
                    length = 1
                else:
                    length = int(parsed_cmd[2])
                data = data[:offset] + data[offset + length:]
                print(f'{YELLOW}{length}{RESET} bytes deleted successfully')
            elif parsed_cmd[0] == 'replace' or parsed_cmd[0] == 'e' or parsed_cmd[0] == 'sub':
                if len(parsed_cmd) < 3:
                    print(f'{RED}Invalid arguments{RESET}')
                    continue

                offset = int(parsed_cmd[1], 16)
                hex_data = parsed_cmd[2:]
                data = data[:offset] + bytes([int(b, 16) for b in hex_data]) + data[offset + len(hex_data):]
                print(f'{YELLOW}{len(hex_data)}{RESET} bytes replaced successfully')
            elif parsed_cmd[0] == 'save' or parsed_cmd[0] == 's':
                with open(filename, 'wb') as f:
                    f.write(data)
                print(f'File {YELLOW}{filename}{RESET} saved successfully')
            else:
                print(f'{RED}Unknown command: {parsed_cmd[0]}{RESET}')
        except Exception as e:
            print(f'{RED}Error: {e}{RESET}')


if __name__ == "__main__":
    main()
