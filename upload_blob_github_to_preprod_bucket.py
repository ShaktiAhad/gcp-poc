from gcp_class import starting
import arg, os

def upload_blob_to_preprod_bucket(bucket_name):
    version = arg.version
    blob_file_name = arg.blob_file_name
    storage_client = starting().storage_client 
    output = os.popen(f'find /var/jenkins_home/workspace/gcp-pipeline -type f -name {blob_file_name}.blob').read()
    source_file_name = output.strip()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f"{blob_file_name}_{version}.blob")
    blob.upload_from_filename(source_file_name)

    print(f"---> File {blob_file_name} uploaded to {bucket_name} & renamed as {blob_file_name}_{version}.blob")
