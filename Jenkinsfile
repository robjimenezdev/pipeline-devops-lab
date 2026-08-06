pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
        }
    }

    environment {
        APP_ENV = 'Producción'
    }

    stages {
        stage('Test') {
            steps {
                sh 'python3 -m unittest test_app.py -v'
            }
        }

        stage('Run App') {
            steps {
                sh 'python3 app.py'
            }
        }
    }
}
