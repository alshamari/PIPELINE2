pipeline {
    agent any
    stages{
        stage('clone')
        steps{
            checkout scm 
        }
    }
    stage('bulid'){
        steps{
          echo 'wow!'  
        }
    }
    stage('Deploy'){
        steps{
            echo 'The End!'
        }
    }
}
