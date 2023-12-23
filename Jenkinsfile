pipeline {
    agent { label 'docker' }

    environment {
        PYENV_VERSION = '3.8.5'  // Set your Python version here
    }

    stages {
        stage('set up python') {
            steps {
                sh 'python3 -m venv venv'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
