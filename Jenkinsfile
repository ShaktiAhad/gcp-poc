pipeline {
    agent none

    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:latest' 
                }
            }
        stage('prepare') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('upload to bucket') {
            steps {
                script {
                   echo 'uploading'   
                }
            }
        }  
    }
}
