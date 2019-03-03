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
         echo "Hello World"  
        }
    }
    stage ('Deploy'){
        steps{
            sh "mvn package"
        }
    }
}
}
