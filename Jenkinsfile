pipeline {
    agent any

    stages {
        stage('python3 installation') {
            steps {
                sh 'apt install python3 -y'
            }
        }
        stage('prepare') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('upload to bucket') {
            steps {
                script {
                   echo 'uploading'
                   withCredentials([file(credentialsId: 'gcp-cred', variable: 'CredentialFile')]){
                        sh 'python b.py ${CredentialFile}'
                    }    
                }
            }
        }  
    }
}
