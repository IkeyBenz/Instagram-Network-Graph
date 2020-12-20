from os import path

CREDENTIALS_PATH = 'ig.credentials.txt'
DATA_DIR = 'data/instagram'

def valid_input(prompt, acceptable_responses):
    response = input(prompt)
    if response in acceptable_responses:
        return response

    print("Invalid response. Expected", acceptable_responses)
    return valid_input(prompt, acceptable_responses)

def get_data_dir():
    return DATA_DIR

def get_authenticated_username():
    assert path.exists(CREDENTIALS_PATH), "Credentials haven't been stored"
    return open(CREDENTIALS_PATH).read().split(',')[0]

def get_ig_credentials_path():
    return CREDENTIALS_PATH

def get_user_connections_path():
    username = get_authenticated_username()
    return path.join(DATA_DIR, username, 'connections.txt')

def get_user_following_path():
    username = get_authenticated_username()
    return path.join(DATA_DIR, username, 'following.txt')

def get_user_follower_path():
    username = get_authenticated_username()
    return path.join(DATA_DIR, username, 'followers.txt')

def get_mutual_followship_path(with_username):
    username = get_authenticated_username()
    return path.join(DATA_DIR, with_username, f'mutuals_with_{username}.txt')