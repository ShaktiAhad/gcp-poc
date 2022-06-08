def call(){
    apiPreparation(null)[0]
    def blob_file_name = blobFileRename()
    def find_blob_file = sh(script: "find ${env.WORKSPACE} -type f -name ${blob_file_name}.blob", returnStdout: true).trim()
    if (find_blob_file != 0){println "couldn't find the file: ${blob_file_name}"}
    sh(script: "gsutil cp ${find_blob_file} gs://${env.PREPROD_BUCKET}/${params.version}/${params.agent_name}/")
}