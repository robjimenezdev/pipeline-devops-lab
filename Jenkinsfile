pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
        }
    }

    environment {
        APP_ENV = 'develop'
    }

    stages {
        stage('Run App') {
            steps {
                sh 'python3 app.py'
            }
        }
    }
}