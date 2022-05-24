from google.cloud import dialogflowcx_v3beta1
from google.oauth2 import service_account
from google.cloud import storage
import os, sys

credFile = sys.argv[1]
credentials = service_account.Credentials.from_service_account_file(f'{credFile}')
storage_client = storage.Client(credentials=credentials)

output = os.popen('find /var/jenkins_home/workspace/gcp-pipeline/ -type f -name exported_agent_test.blob').read()
d = output.strip()
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)

    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

upload_blob("dialogflow-bucket", d, "agent.blob")
