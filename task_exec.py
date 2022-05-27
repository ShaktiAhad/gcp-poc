import upload_blob_github_to_preprod_bucket, com_restore_agent, copy_blob_preprod_to_prod_bucket, arg

def task_exec(env):
    if env == "preprod":
        project_id = "prerprod-project"
        bucket_name = "dialogflow-bucket-preprod"
        upload_blob_github_to_preprod_bucket.upload_blob_to_preprod_bucket(bucket_name)
        com_restore_agent.restore_agent(env, bucket_name, project_id)
    elif env == "prod":
        project_id = "prod-project-351108"
        source_bucket_name = "dialogflow-bucket-preprod"
        destination_bucket_name = "dialogflow-bucket-prod"
        copy_blob_preprod_to_prod_bucket.copy_blob_preprod_to_prod_bucket(source_bucket_name, destination_bucket_name)
        com_restore_agent.restore_agent(env, destination_bucket_name, project_id)
    print("task is completed.")

task_exec(arg.env) 