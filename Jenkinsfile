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
                sh 'echo "${PWD}"'
                sh '. venv/bin/activate'
                sh 'PATH=$PATH:~/.local/bin'
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh '~/.local/bin/pytest'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
