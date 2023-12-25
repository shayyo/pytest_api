pipeline {
    agent { label 'docker' }

    environment {
        PYENV_VERSION = '3.8.5'  // Set your Python version here
        MY_CREDENTIALS = credentials('1238281f-93c6-417f-9675-854d7c6c29ca')
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
                sh 'python3 get_token.py "${API_IP_ADDR}" "${API_USERNAME}" "${API_PASSWORD}"'
                //sh '~/.local/bin/pytest'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
