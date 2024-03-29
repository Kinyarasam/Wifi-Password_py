#!/usr/bin/python3

import subprocess

def main():
    """
    Extracts the names and passwords for all user profiles stored in the
    wireless network configuration on the local machine.

    Returns:
        A list of tuples, where each tuple contains the name and password
        for a user profile.
    """
    data = subprocess.check_output(
        ['netsh', 'wlan', 'show', 'profiles']
    ).decode('utf-8').split('\n')

    profiles = (
            i.split(":")[1][1:-1] for i in data if "All User Profile" in i)

    for i in profiles:
        #running the 2nd cmd command to check passwords
        results = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profiles', i, 'key=clear']
        ).decode('utf-8').split('\n')

        #storing passwords after converting them to List
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print("{:<30} | {:<}".format(i, results[0]))
            # print("show password")
        except IndexError:
            print("{:<30} | {:<}".format(i, ""))


if __name__ == '__main__':
    main()
