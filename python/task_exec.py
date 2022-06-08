import upload_blob_github_to_preprod_bucket, com_restore_agent, copy_blob_preprod_to_prod_bucket, python.arg as arg

def task_exec(env):
    print(f"\n---> working on {env} env.")
    if env == "preprod":
        project_id = "prerprod-project"
        bucket_name = "dialogflow-bucket-preprod"
        agent_id = "b19e696a-f210-4555-b4d1-abeb3f03f16b"
        if not arg.task_type == "rollback":upload_blob_github_to_preprod_bucket.upload_blob_to_preprod_bucket(bucket_name)
        com_restore_agent.restore_agent(env, bucket_name, project_id, agent_id)
    elif env == "prod":
        project_id = "prod-project-351108"
        source_bucket_name = "dialogflow-bucket-preprod"
        destination_bucket_name = "dialogflow-bucket-prod"
        agent_id = "8b2cbcda-3c04-4197-adf0-ea489426a11c"
        if not arg.task_type == "rollback":copy_blob_preprod_to_prod_bucket.copy_blob_preprod_to_prod_bucket(source_bucket_name, destination_bucket_name)
        com_restore_agent.restore_agent(env, destination_bucket_name, project_id, agent_id)
    if not arg.task_type == "rollback": print("---> __release is completed.__")
    else: print("---> __rollback is completed.__")

task_exec(arg.env) 
