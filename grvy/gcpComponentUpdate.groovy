#!/usr/bin/env groovy
def call(){
    sh(script: 'gcloud components update -q')
}