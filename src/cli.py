from os import path, makedirs

from instagram_bot_scraper import InstagramScrapper
from util import valid_input
from clean_data import correct_mutual_follwers
from data_to_json import save_follow_data_to_json
from server import serve_html_and_data

def start():
    print("> Opening Chrome Webdriver...")

    credentials_path = "ig.credentials.txt"

    # Check if credentials are saved
    if not path.exists(credentials_path):
        print("> Instagram requires login credentials to proceed.")
        username = input("Enter your Instagram username: ")
        password = input("Enter your Instagram password: ")

        # Ask user if they want to store their login info
        print("Would you like to save these credentials to bypass this step next time?")
        save_creds = valid_input("Enter y/n: ", ["Y", "y", "N", "n"]) in "yY"

        if save_creds:
            out = open(credentials_path, "w")
            out.write(f"{username},{password}")
            out.close()

    else:  # Use stored credentials
        username, password = open(credentials_path).read().split(',')

    print("> Logging you into instagram.com in Chrome browser...")
    scraper = InstagramScrapper(username, password)

    show_interface(scraper)


def show_interface(scraper):
    print('''
    > What would you like to do?
        1) Log usernames that follow me
        2) Log usernames I follow
        3) Log usernames who I follow and follow me back
        4) Get mutual friend links between my connections
        5) Graph my social network using data stored in data/instagram (running option 4 is a prerequisite)''')
    choice = valid_input("Enter 1/2/3/4/5: ", ['1', '2', '3', '4', '5'])

    user_data_path = f"data/instagram/{scraper.user['username']}/"
    if not path.exists(user_data_path):
        makedirs(user_data_path)

    if choice == '1':
        log_path = user_data_path + "followers.txt"
        print(f"> Saving followers to {log_path}")
        scraper.log_followers(log_path)

    elif choice == '2':
        log_path = user_data_path + "following.txt"
        print(f"> Saving following to {log_path}")
        scraper.log_following(log_path)

    elif choice == '3':
        log_path = user_data_path + "connections.txt"
        print(f"> Saving connections to {log_path}")
        scraper.log_connections(log_path)

    elif choice == '4':
        print("> Getting your connections and their relationships")
        connections_path = f"data/instagram/{scraper.user['username']}/connections.txt"
        connections = (open(connections_path).read().splitlines()
                       if path.exists(connections_path) else
                       scraper.log_connections(connections_path))
        og_user = scraper.user['username']
        for account in connections:
            scraper.user['username'] = account
            scraper.log_mutuals_with(og_user)
    elif choice == '5':
        print('> Cleaning the data...')
        correct_mutual_follwers()

        print('> Generating JSON...')
        save_follow_data_to_json()

        print('> Serving html page...')
        serve_html_and_data()


    print("> Would you like to run another task?")
    choice = valid_input("Enter y/n: ", ['Y', 'y', 'N', 'n'])
    if choice in 'Yy':
        return show_interface(scraper)

    print("> Stopping processes...")
    print("> Done. Bye Bye.")


if __name__ == '__main__':
    start()
