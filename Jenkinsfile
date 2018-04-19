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
        sh 'python main.py <<0,0EOF'
      }
    }
    stage('Como quedo docker host') {
      steps {
        sh 'docker ps -a;docker images -a'
      }
    }
  }
}