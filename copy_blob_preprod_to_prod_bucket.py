from gcp_class import starting
import com_get_blob, arg

def copy_blob_preprod_to_prod_bucket(source_bucket_name, destination_bucket_name):
    storage_client = starting().storage_client
    version = arg.version
    source_blob_name = com_get_blob.get_blob(source_bucket_name)
    blob_file_name = source_blob_name.split('_{arg.version}.blob').pop(-2)
    dest_blob_name = f"{blob_file_name}_Release_{version}.blob"

    source_bucket = storage_client.bucket(source_bucket_name, user_project="prerprod-project")
    source_blob = source_bucket.blob(source_blob_name)
    destination_bucket = storage_client.bucket(destination_bucket_name, user_project="prod-project-351108")

    blob_copy = source_bucket.copy_blob(source_blob, destination_bucket, dest_blob_name)

    print(f"Blob {source_blob.name} in bucket {source_bucket.name} copied to blob {blob_copy.name} in bucket {destination_bucket.name}.")
