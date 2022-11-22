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