from gcp_class import starting
import com_get_blob

def restore_agent(env, bucket_name, project_id):
    client = starting().client
    dialogflowcx_v3beta1 = starting().dialogflowcx
    if env == "preprod":
        agent_id = "b19e696a-f210-4555-b4d1-abeb3f03f16b"
        blob_file_name = com_get_blob.get_blob(bucket_name)
    elif env == "prod":
        agent_id = "8b2cbcda-3c04-4197-adf0-ea489426a11c"
        blob_file_name = com_get_blob.get_blob(bucket_name)
        print(blob_file_name)
    client.restore_agent(
        request=dialogflowcx_v3beta1.RestoreAgentRequest(
                agent_uri=f"gs://{bucket_name}/{blob_file_name}",
                name=f"projects/{project_id}/locations/asia-northeast1/agents/{agent_id}",
        ))
    print(f"---> restored agent:{blob_file_name} from {bucket_name} to {project_id}.")
