pipeline {
    agent any

    stages {
        stage('prepare') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('upload to bucket') {
            steps {
                script {
                   echo 'uploading'
                   withCredentials([file(credentialsId: 'gcp-cred', variable: 'CredentialFile')]){
                        sh 'python3 b.py ${CredentialFile}'
                    }    
                }
            }
        }  
    }
}
