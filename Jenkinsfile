pipeline {
    agent { label 'docker' }
    options {
        timeout(time: 3, unit: 'SECONDS')
    }
    
    parameters {
        string(name: 'HOST_URL', defaultValue: '172.30.2.2', description: 'The URL of the API server')
        choice(name: 'USERNAME', choices: ['administrator', 'root', 'user2'], description: 'Username of the API server')
        password(name: 'PASSWORD', defaultValue: 'my_password', description: 'Enter a password')
    }

    environment {
        PYENV_VERSION = '3.8.5'  // Set your Python version here
    }
    
    stages {
        stage('set up python') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
                sh 'PATH=$PATH:~/.local/bin'
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('get token from API server') {
            steps {
                sh 'python3 get_token.py "${API_IP_ADDR}" "${API_USERNAME}" "${API_PASSWORD}"'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
