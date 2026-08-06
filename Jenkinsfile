pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
        }
    }

    environment {
        APP_ENV = 'production'
    }

    stages {
        stage('Test') {
            steps {
                sh 'python3 -m unittest test_app.py -v'
            }
        }

        stage('Deploy') {
            steps {
                sh 'python3 app.py'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'deploy.log', allowEmptyArchive: true
        }
    }
}
