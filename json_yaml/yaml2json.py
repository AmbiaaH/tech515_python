import json
import os
import sys
import yaml

# Checking there is a file name passed
if len(sys.argv) > 1:
    # Opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = yaml.safe_load(source_file)
        source_file.close()

        # Check if target filename was given
        if len(sys.argv) > 2:
            target_filename = sys.argv[2]

            # Check if file already exists
            if os.path.exists(target_filename):
                print("ERROR: " + target_filename + " already exists")
                exit(1)

            # Save to file
            target_file = open(target_filename, "w")
            json.dump(source_content, target_file, indent=2)
            target_file.close()
            print("JSON saved to " + target_filename)
        else:
            # No target file, just print
            print(json.dumps(source_content, indent=2))

    # Failing if the file isn't found
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)
# No source file specified
else:
    print("ERROR: No YAML file was specified")
    print("Usage: yaml2json.py <source_file.yaml> <target_file.json>")