import json

# create the dictionary
servers_dict = {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}

# Part 1: Convert to JSON string

json_string= json.dumps(servers_dict)
print(json_string)
#json.dumps() --> converts dictionary to text

# with open ("servers.json", 'r') as f:
#     json_string

# Part 2: Save to JSON file
with open("servers.json", "w") as f:
    json.dump(servers_dict, f)
# with open() --> opens a file called output.json
# json.dump(saves dictionary --> file )
# file shows in folder

#dumps --> makes a string
#dump = makes a file
