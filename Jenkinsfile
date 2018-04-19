pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('Construyendo imagen') {
      steps {
        echo 'Mensaje dentro de contenedor'
      }
    }
    stage('limpiando docker') {
      agent any
      steps {
        sh 'docker images -a'
      }
    }
  }
}