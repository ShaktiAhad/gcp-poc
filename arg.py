import sys

credFile = sys.argv[1] # prerprod-project-dialogflowcx.json
env = sys.argv[2] # preprod/prod
version = sys.argv[3] # v0.0.0
if env == "preprod":
    blob_file_name = sys.argv[4] # exported_agent