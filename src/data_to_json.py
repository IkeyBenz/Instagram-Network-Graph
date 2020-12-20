"""
Goes through the folders in data/instagram and writes a json object, containing
the nodes and all of their links, to data.json. Once data.json exists, you'll be
able to open index.html and see a D3.js visualization of your social network.

"""
import json
from os import listdir, path
from clean_data import correct_mutual_follwers, get_users_connections
from util import get_data_dir, get_mutual_followship_path, get_user_connections_path

data_dir = "data/instagram"
username = open('ig.credentials.txt').read().split(',')[0]
connections_path = get_user_connections_path()


def get_links():
    links = []
    for followed in listdir(data_dir):
        mutuals_path = get_mutual_followship_path(followed)
        if followed == username or not path.exists(mutuals_path):
            continue

        for follower in open(mutuals_path).read().splitlines():
            links.append({"source": follower, "target": followed})
    print("Links", len(links))
    return links

def save_follow_data_to_json():
    users_connections = get_users_connections()
    data = {
        "nodes": [
            {"id": acc, "group": 1}
            for acc in users_connections
        ] + [{"id": username, "group": 1}],
        "links": get_links()
    }

    with open('data.json', 'w') as out:
        json.dump(data, out)

if __name__ == '__main__':
    correct_mutual_follwers()
    save_follow_data_to_json()
