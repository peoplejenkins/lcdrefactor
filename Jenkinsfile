pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('Construyendo imagen') {
      agent {
        dockerfile {
          filename 'Dockerfile'
        }

      }
      steps {
        echo 'Mensaje dentro de contenedor'
        sh 'uname -a;ps -a'
      }
    }
  }
}