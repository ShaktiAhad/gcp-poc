pipeline {
    agent any

    stages {
        stage('prepare') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('upload to bucket') {
            steps {
                script {
                   echo 'uploading'
                   withCredentials([file(credentialsId: 'gcp-cred', variable: 'CredentialFile')]){
                        bat(script:"b.py ${CredentialFile}", returnStdout: true)
                    }    
                }
            }
        }  
    }
}
