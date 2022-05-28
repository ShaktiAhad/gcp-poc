import sys

credFile = sys.argv[1] # prerprod-project-dialogflowcx.json
task_type = sys.argv[2] # release/rollback
env = sys.argv[3] # preprod/prod
version = sys.argv[4] # v0.0.0
if env == "preprod" and task_type == "release":
    blob_file_name = sys.argv[5] # exported_agent
    if blob_file_name.endswith(".blob"):
        blob_file_name = blob_file_name.split(".blob").pop(-2)
    else: blob_file_name=blob_file_name
