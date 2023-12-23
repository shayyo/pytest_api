pipeline {
    agent any
    
    environment {
        PYENV_VERSION = '3.8.5'  // Set your Python version here
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout source code from the specified Git repository
                git 'https://github.com/shayyo/pytest_api.git'
            }
        }

        stage('Set up Python') {
            steps {
                script {
                    // Install and set up Python using pyenv
                    sh '''
                        export PATH="/home/jenkins/.pyenv/bin:$PATH"
                        eval "$(pyenv init --path)"
                        eval "$(pyenv virtualenv-init -)"
                        pyenv install $PYENV_VERSION
                        pyenv global $PYENV_VERSION
                    '''
                    // Install required Python packages
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run pytest
                    sh 'pytest'
                }
            }
        }
    }

    post {
        always {
            // Clean up and deactivate virtual environment
            script {
                sh 'pyenv deactivate'
            }
        }
    }
}

