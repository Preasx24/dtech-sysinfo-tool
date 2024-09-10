import re
import time
import sys
import os
from colorama import Fore, Style, init

# Initialize colorama
init()

def print_banner():
    os.system('clear')  # Clear the terminal for a clean look

    # Cool animation effect
    animation = [
        "Loading.",
        "Loading..",
        "Loading..."
    ]
    
    for frame in animation:
        sys.stdout.write('\r' + frame)
        sys.stdout.flush()
        time.sleep(0.5)
    
    # Hacker-style banner
    banner = f'''
{Fore.GREEN}██████████████████████████████████████████████████████████████████████████████████████████████████████████
███  ███   ███   ███████   ███████   ███   ███   ████████████████████████████████████████████████████████████████
███████   ███   ███   ███   ███   ███   ███   ███   ███   ███████   ███   ███   ███   ███   ███   ███████   ███████████████
{Fore.RESET}
{Fore.GREEN}███   ███████   ███   ███   ███   ███   ███   ███   ███   ███   ███   ███   ███   ███████   ███████   ███   ███   ███████████
███   ███   ███   ███████   ███   ███   ███   ███   ███   ███████   ███   ███   ███   ███████   ███   ███   ███   ███   ███
███   ███████   ███   ███████   ███   ███   ███   ███   ███   ███████   ███████   ███   ███   ███████   ███████████████
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
{Fore.RESET}
    '''
    made_by = f'''
{Fore.GREEN}   ██████╗  █████╗ ███╗   ███╗███████╗███████╗██████╗ 
   ██╔══██╗██╔══██╗████╗ ████║██╔════╝██╔════╝██╔══██╗
   ██████╔╝███████║██╔████╔██║█████╗  █████╗  ██████╔╝
   ██╔═══╝ ██╔══██║██║╚██╔╝██║██╔══╝  ██╔══╝  ██╔═══╝ 
   ██║     ██║  ██║██║ ╚═╝ ██║███████╗███████╗██║     
   ╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝╚═╝     
    {Fore.RESET}
    '''
    
    # Print banner
    print(banner)
    time.sleep(1)  # Brief pause after animation

def extract_email_password(text):
    pattern = re.compile(r'(\S+@\S+)\s*:\s*(\S+)')
    matches = pattern.findall(text)
    return matches

def process_accounts():
    # Display the banner
    print_banner()

    # Prompt user to input the file path
    input_file_path = input(f'{Fore.GREEN}Enter the path to the input file: {Fore.RESET}')
    
    try:
        with open(input_file_path, 'r') as infile:
            content = infile.read()
            results = extract_email_password(content)
            if results:
                print(f"{Fore.GREEN}\nExtracting email:password pairs...\n{Fore.RESET}")
                time.sleep(1)  # Brief pause before displaying results
                for email, password in results:
                    print(f"{email}:{password}")
            else:
                print(f"{Fore.RED}No valid email:password pairs found.{Fore.RESET}")
    except FileNotFoundError:
        print(f"{Fore.RED}Error: File '{input_file_path}' not found.{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Fore.RESET}")

    # Display D-TECH
    time.sleep(1)  # Brief pause before showing "D-TECH"
    print(f"{Fore.GREEN}███████████████████████████████████████████████████████████████████████████████████████████████████████████████{Fore.RESET}")
    print(f"{Fore.GREEN}███████████████████████████████████████████████████████████████████████████████████████████████████████████████{Fore.RESET}")
    print(f"{Fore.GREEN}███████████████████████████████████████████████████████████████████████████████████████████████████████████████{Fore.RESET}")
    print(f"{Fore.GREEN}███████████████████████████████████████████████████████████████████████████████████████████████████████████████{Fore.RESET}")
    print(f"{Fore.GREEN}███      ███      ███      ███      ███      ███      ███      ███      ███      ███      ███      ███      ███      ███{Fore.RESET}")
    print(f"{Fore.GREEN}███      ███      ███      ███      ███      ███      ███      ███      ███      ███      ███      ███      ███      ███{Fore.RESET}")
    print(f"{Fore.GREEN}███      ███      ███      ███      ███      ███      ███      ███      ███      ███      ███      ███      ███      ███{Fore.RESET}")
    print(f"{Fore.GREEN}███████████████████████████████████████████████████████████████████████████████████████████████████████████████{Fore.RESET}")
    print(f"{Fore.GREEN}███████████████████████████████████████████████████████████████████████████████████████████████████████████████{Fore.RESET}")
    print(f"{Fore.GREEN}███████████████████████████████████████████████████████████████████████████████████████████████████████████████{Fore.RESET}")
    print(f"{Fore.GREEN}███████████████████████████████████████████████████████████████████████████████████████████████████████████████{Fore.RESET}")
    print(f"{Fore.GREEN}                           ███   D-TECH   ███                            {Fore.RESET}")
    print(f"{Fore.GREEN}                           ███  PREASX24  ███                            {Fore.RESET}")

# Run the processing function
process_accounts()
