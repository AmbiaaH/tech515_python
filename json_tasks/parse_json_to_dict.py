import json

with open("servers.json", "r") as f:
    servers = json.load(f)

print(servers)

print(type(servers))

print(servers["server1"])

print(servers["server2"])

for key, value in servers.items():
    print(f"Key and value: '{key}' = '{value}'")  # prints server1 and server 2 with dictionary

    for sub_key, sub_value in value.items():
        print(f"  Record key and sub value: '{sub_key}' = '{sub_value}'") #nests through dictionary and prints key: value of the first and second servers