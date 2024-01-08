pipeline {
    agent { label 'docker' }
    options {
        timeout(time: 180, unit: 'SECONDS')
    }
    
    parameters {
        string(name: 'API_IP_ADDR', defaultValue: '172.30.2.2', description: 'The URL of the API server')
        choice(name: 'API_USERNAME', choices: ['administrator', 'root', 'user2'], description: 'Username of the API server')
        password(name: 'API_PASSWORD', defaultValue: 'my_password', description: 'Enter a password')
        string(name: 'AUTHORIZATION_HEADER', defaultValue: 'Authorization', description: 'Header of authorization to use in API requests')
    }

    environment {
        PYENV_VERSION = '3.8.5'  // Set your Python version here
    }
    
    stages {
        stage('echo params') {
            steps {
                echo "Hello ${params.API_IP_ADDR}"
            }
        }
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
                sh 'python3 get_token.py "${API_IP_ADDR}" "${API_USERNAME}" "${API_PASSWORD}" "${AUTHORIZATION_HEADER}"'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
