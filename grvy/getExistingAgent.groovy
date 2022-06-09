#!/usr/bin/env groovy
import groovy.json.JsonSlurper

def call(){
    load "${env.WORKSPACE}/grvy/apiPreparation.groovy"
    def get_agent_detail = apiPreparation(null)[1]
    def agent_details = new JsonSlurper().parseText(get_agent_detail.inputStream.text)
    def agentName_n_id = [:]
    for (each_agent in agent_details.agents){
        def name = each_agent.name.split('/')
        def agent_id = name[name.length - 1]
        def display_name = each_agent.displayName
        agentName_n_id.put(display_name, agent_id)
        }

    def agent_name = "${params.agent_name}".toString()
    return [agentName_n_id, agentName_n_id.get(agent_name)]
}
return this