import groovy.json.JsonSlurperClassic

def jsonParse(def json) {
    new groovy.json.JsonSlurperClassic().parseText(json)
}
pipeline {

    agent any 
    environment {
        appName = "variable" 
    }
    stages {

        stage("paso 1"){
            
              steps {
                  script {			
                  sh "echo 'hola mundo desde GIT'"
                  sh "pwd"
                  sh "ls -ltr"
                  sh 'dotnet build --source ../HolaMundoDotNet/'
                  sh 'ls -ltr'
                  SH 'sleep 30'
                  //def file_in_workspace = inputGetFile('Jenkinsfile');

                }
              }
        }
    }
    post {

          always {          
              deleteDir()
              sh "echo 'ESTA FASE SIEMPRE SE EJECUTA SIN IMPORTAR SI FUE FALLIDO O NO'"
          }
          success {
                sh "echo 'ESTA FASE SE EJECUTA SOLAMENTE SI FUE EXITOSO'"
            }

          failure {
                sh "echo 'ESTA FASE SE EJECUTA SI FUE FALLIDO'"
          }
        
    }
}  

def inputGetFile(String savedfile = null) {
    def filedata = null
    def filename = null
    // Get file using input step, will put it in build directory
    // the filename will not be included in the upload data, so optionally allow it to be specified

    if (savedfile == null) {
        def inputFile = input message: 'Upload file', parameters: [file(name: 'library_data_upload'), string(name: 'filename', defaultValue: 'demo-backend-1.0-SNAPSHOT.jar')]
        filedata = inputFile['library_data_upload']
        filename = inputFile['filename']
    } else {
        def inputFile = input message: 'Upload file', parameters: [file(name: 'library_data_upload')]
        filedata = inputFile
        filename = savedfile
    }

    // Read contents and write to workspace
    writeFile(file: filename, encoding: 'Base64', text: filedata.read().getBytes().encodeBase64().toString())
    // Remove the file from the master to avoid stuff like secret leakage
    filedata.delete()
    return filename
}
