def call(agent_id){
    withCredentials([file(credentialsId: 'gcp-cred', variable: 'credentials_file')]){
        sh(script: '''
            export GOOGLE_APPLICATION_CREDENTIALS=${credentials_file}
            gcloud auth application-default print-access-token > token.txt
            ''', returnStdout: true)
        def gcloud_auth = sh (script: 'gcloud auth activate-service-account --key-file ${credentials_file}')
        env.token = new File("${env.WORKSPACE}/token.txt").text.trim()
        def url = "https://asia-northeast1-dialogflow.googleapis.com/v3/projects/${env.PROJECT_NAME}/locations/${env.LOCATION}/agents"
        def restore_agent_url = "${url}/${agent_id}:restore"
        def call_agent_api_url = new URL(url).openConnection()
        def call_restore_agent_api_url = new URL(restore_agent_url).openConnection()
        def api_urls = [call_agent_api_url, call_restore_agent_api_url]
        for (each_url in api_urls){
            each_url.setRequestProperty("Authorization", "Bearer ${token}")
            each_url.setRequestProperty("Content-Type", "application/json")
        }
        return [gcloud_auth, call_agent_api_url, call_restore_agent_api_url]
    }
}
