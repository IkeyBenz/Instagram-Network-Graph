from os import listdir, path

from util import get_data_dir, get_mutual_followship_path, get_user_connections_path, get_authenticated_username

data_dir = get_data_dir()
authenticated_username = get_authenticated_username()
connections_path = get_user_connections_path()

def get_users_connections():
    return set(open(connections_path).read().splitlines())




def correct_mutual_follwers():
    for account in listdir(data_dir):
        mutuals_path = get_mutual_followship_path(account)
        if account is authenticated_username or not path.exists(mutuals_path):
            continue

        mutuals = set(open(mutuals_path).read().splitlines())
        corrected = mutuals.intersection(get_users_connections())

        with open(mutuals_path, 'w') as out:
            out.write("\n".join(corrected))


def check_mutual_correctness():
    for account in listdir(data_dir):
        mutuals_path = get_mutual_followship_path(account)
        if account is authenticated_username or not path.exists(mutuals_path):
            continue

        stored_mutuals = set(open(mutuals_path).read().splitlines())
        extras = stored_mutuals.difference(get_users_connections())
        if len(extras) > 0:
            print(account, "has extra mutuals:", extras)


if __name__ == '__main__':
    correct_mutual_follwers()
    check_mutual_correctness()
