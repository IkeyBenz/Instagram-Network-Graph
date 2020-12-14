from os import listdir, path

data_dir = path.join('data', 'instagram_followers')
authenticated_username = open('ig.credentials.txt').read().split(',')[0]


ikeys_connections = set(open(
    path.join(data_dir, authenticated_username, 'connections.txt')).read().splitlines())


def get_mutuals_path(with_account):
    return path.join(data_dir, with_account, f'mutuals_with_{authenticated_username}.txt')


def correct_mutual_follwers():
    for account in listdir(data_dir):
        mutuals_path = get_mutuals_path(account)
        if account is authenticated_username or not path.exists(mutuals_path):
            continue

        mutuals = set(open(mutuals_path).read().splitlines())
        corrected = mutuals.intersection(ikeys_connections)

        with open(mutuals_path, 'w') as out:
            out.write("\n".join(corrected))


def check_mutual_correctness():
    for account in listdir(data_dir):
        mutuals_path = get_mutuals_path(account)
        if account is authenticated_username or not path.exists(mutuals_path):
            continue

        stored_mutuals = set(open(mutuals_path).read().splitlines())
        extras = stored_mutuals.difference(ikeys_connections)
        if len(extras) > 0:
            print(account, "has extra mutuals:", extras)


if __name__ == '__main__':
    correct_mutual_follwers()
    check_mutual_correctness()
