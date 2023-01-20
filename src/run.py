import urllib.request

import myapp
import updater
import getrequirements as gr

def main():

    current_version , online_reqs = None , None

    with open ('src/vers.txt') as f:
        local_reqs = gr.GetRequirements(f.readlines()).get_config_dict()

    target_url = 'https://raw.githubusercontent.com/5neakyz/auto_updater/main/vers.txt'
    data = urllib.request.urlopen(target_url)
    data = data.readlines()
    temp = []
    for line in data:
        temp.append(line.decode()) 

    online_reqs = gr.GetRequirements(temp).get_config_dict()

    print(f"Current : {local_reqs['vers']}")
    print(f"Latest Version : {online_reqs['vers']}")


    # updater.start()
    # myapp.start()


main()
