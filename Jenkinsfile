pipeline {
    agent any
    stages{
        stage ('clone'){
        steps{
            checkout scm 
        }
    }
    stage ('bulid'){
        steps{
          sh "mvn clean"  
        }
    }
    stage ('Deploy'){
        steps{
            sh "mvn package"
        }
    }
}
}
