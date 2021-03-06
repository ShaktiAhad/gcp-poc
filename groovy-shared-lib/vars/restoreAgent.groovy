import groovy.json.JsonSlurper

def call(agent_id){
    def restore_agent = apiPreparation(agent_id)[2]
    def payload = """{
        "agentUri": "gs://${env.PREPROD_BUCKET}/${params.version}/${params.agent_name}/${blobFileRename()}.blob"
        }"""
    println restore_agent
    println payload
    restore_agent.setRequestMethod("POST")
    restore_agent.setDoOutput(true)
    restore_agent.getOutputStream().write(payload.getBytes("UTF-8"))
    def restore_agent_detail = new JsonSlurper().parseText(restore_agent.inputStream.text)
    println restore_agent_detail
}