pipeline {
  agent any
  stages {
    stage('Construyendo imagen') {
      agent {
        dockerfile {
          filename 'Dockerfile'
        }

      }
      steps {
        echo 'Mensaje dentro de contenedor'
        readFile 'Data.py'
        sh 'uname -a'
      }
    }
    stage('Como quedo docker host') {
      steps {
        sh 'docker ps -a;docker images -a'
      }
    }
  }
}