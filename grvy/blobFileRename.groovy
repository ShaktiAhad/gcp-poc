#!/usr/bin/env groovy
def call(){
    def blob_file_name = "${params.blob_file_name}"
    if (blob_file_name.endsWith("blob")){
        def name = blob_file_name.split('\\.')
        def modified_blob_file_name = name[0]
        return modified_blob_file_name
        }
    else {return blob_file_name}
}
return this