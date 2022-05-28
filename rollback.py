import com_restore_agent, rollback_arg

def task_exec(env):
    print(f"\n---> working on {env} env.")
    if env == "preprod":
        project_id = "prerprod-project"
        bucket_name = "dialogflow-bucket-preprod"
        agent_id = "b19e696a-f210-4555-b4d1-abeb3f03f16b"
        com_restore_agent.restore_agent(env, bucket_name, project_id, agent_id)
    elif env == "prod":
        project_id = "prod-project-351108"
        destination_bucket_name = "dialogflow-bucket-prod"
        agent_id = "8b2cbcda-3c04-4197-adf0-ea489426a11c"
        com_restore_agent.restore_agent(env, destination_bucket_name, project_id, agent_id)
    print("---> __task is completed.__")

task_exec(rollback_arg.env)