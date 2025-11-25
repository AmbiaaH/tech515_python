import json
import os
import sys
import yaml



# # 1. Convert the JSON to YAML - use yaml library
# # WRITE YOUR CODE HERE
# # Checking there is a file name passed
# #Code which tests
# if len(sys.argv) > 1:
#     # Opening the file
#     if os.path.exists(sys.argv[1]):
#         source_file = open(sys.argv[1], "r")
#         source_content = json.load(source_file)
#         source_file.close()
#         print(yaml.dump(source_content)) # converts json to yaml
#     # Failing if the file isn't found
#     else:
#         print("ERROR: " + sys.argv[1] + " not found")
#         exit(1)
# # No source file specified
# else:
#     print("ERROR: No JSON file was specified")
#     print("Usage: json2yaml.py <source_file.json> <target_file.yaml>")

# 2. Save the YAML into a new file with the name for it received as a argument







# 2.1 Check the target file name was specified as an argument, if not, output the YAML to the screen instead
# WRITE YOUR CODE HERE


# 2.2 Check the target file doesn't already exist
# WRITE YOUR CODE HERE


# 2.3 If previous conditions not met, then save YAML file
# WRITE YOUR CODE HERE


import json
import os
import sys
import yaml

# Checking there is a file name passed
if len(sys.argv) > 1:
    # Opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = json.load(source_file)
        source_file.close()

        # 2.1 Check if target filename was given
        if len(sys.argv) > 2:
            target_filename = sys.argv[2]

            # 2.2 Check if file already exists
            if os.path.exists(target_filename):
                print("ERROR: " + target_filename + " already exists")
                exit(1)

            # 2.3 Save to file
            target_file = open(target_filename, "w")
            yaml.dump(source_content, target_file)
            target_file.close()
            print("YAML saved to " + target_filename)
        else:
            # No target file, just print
            print(yaml.dump(source_content))

    # Failing if the file isn't found
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)
# No source file specified
else:
    print("ERROR: No JSON file was specified")
    print("Usage: json2yaml.py <source_file.json> <target_file.yaml>")