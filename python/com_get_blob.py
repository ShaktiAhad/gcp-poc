from gcp_class import starting
import python.arg as arg

def get_blob(bucket_name):
    storage_client = starting().storage_client
    version = arg.version
    blobs = storage_client.list_blobs(bucket_name)
    for obj in blobs:
        if vars(obj)["name"].endswith(f"{version}.blob"):
            return vars(obj)["name"]
        elif vars(obj)["name"].endswith(f"_Release_{version}.blob"):
            return vars(obj)["name"]