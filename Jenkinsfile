pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
        }
    }

    stages {
        stage('Run App') {
            steps {
                sh 'python3 app.py'
            }
        }
    }
}