pipeline {
    agent { label 'docker' }

    environment {
        PYENV_VERSION = '3.8.5'  // Set your Python version here
    }

    stages {
        stage('set up python') {
            steps {
                sh 'python3 -m venv venv'
                sh 'ls -l'
                sh 'sleep 5'
                sh 'echo "${PWD}"'
                sh 'source venv/bin/activate'
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
