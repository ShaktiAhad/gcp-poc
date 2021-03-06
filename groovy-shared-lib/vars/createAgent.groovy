import groovy.json.JsonSlurper

def call(){
    def payload = """{
        "displayName": "${params.agent_name}",
        "defaultLanguageCode": "en",
        "timeZone": "Asia/Tokyo", 
        "description": "${params.agent_name} agent"
        }"""
    def create_agent = apiPreparation(null)[1]
    create_agent.setRequestMethod("POST")
    create_agent.setDoOutput(true)
    create_agent.getOutputStream().write(payload.getBytes("UTF-8"))
    def agnt_details = new JsonSlurper().parseText(create_agent.inputStream.text)
    def name = agnt_details.name.split('/')
    def agent_id = name[name.length - 1]
    def display_name = agnt_details.displayName
    def agntName_n_id = ["${display_name}": " ${agent_id}"]
    println agntName_n_id
    println agent_id
    return agent_id
}