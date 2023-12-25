pipeline {
    agent { label 'docker' }

    environment {
        PYENV_VERSION = '3.8.5'  // Set your Python version here
    }
    
    stages {
        stage('cred') {
            steps {
                withCredentials([usernamePassword(credentialsId: '1238281f-93c6-417f-9675-854d7c6c29ca', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh 'echo "The user is => $PASSWORD"'
                    sh 'echo "The password is => $USERNAME"'
                }
            }
        }
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
