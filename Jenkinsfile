pipeline {
    agent any

    stages {
        stage('operation details') {
            steps {
                echo "${params.task_type} ${params.env}, ${params.version}, ${params.blob_file_name}"
            }
        }
        stage('installing necessary module') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('restore agent') {
            steps {
                script {
                   withCredentials([file(credentialsId: 'gcp-cred', variable: 'CredentialFile')])
                    {
                        sh "python3 task_exec.py ${CredentialFile} ${params.task_type} ${params.env} ${params.version} ${params.blob_file_name}" 
                    } 
                }
            }
        }  
    }
}
