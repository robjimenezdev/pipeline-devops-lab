pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
        }
    }

    environment {
        APP_ENV = "${env.BRANCH_NAME == 'main' ? 'production' : env.BRANCH_NAME}"
    }

    stages {
        stage('Test') {
            steps {
                sh 'python3 -m unittest test_app.py -v'
            }
        }

        stage('Deploy') {
            when {
                anyOf {
                    branch 'develop'
                    branch 'staging'
                    branch 'main'
                }
            }
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
