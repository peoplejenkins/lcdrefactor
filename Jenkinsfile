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
        sh '''python main.py;expect "    LCD_Printer
    @author: Amaury Ortega <amauryocortega@gmail.com>
    
    Program to print numbers in LCD style.
    
    Input should have this format: SIZE,####
    Where:
        SIZE: Digit from 1 to 10
        ####: Any sequence of digits
    ------------------------------------------
    |Special Input: 0,0 will stop the program|
    ------------------------------------------
    
Input: ";send "0,0"'''
      }
    }
    stage('Como quedo docker host') {
      steps {
        sh 'docker ps -a;docker images -a'
      }
    }
  }
}