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
        sh 'uname -a;ps -a;ls -alh'
      }
    }
  }
}