pipeline {
    agent any

    parameters {
        string(name: 'USER_NAME', defaultValue: 'John', description: 'Enter the user name')
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', credentialsId: 'gitvik', url: 'https://github.com/vikasstanwar/greetings.git'
            }
        }
        stage('Build Docker Image Atomatically') {
            steps {
                sh 'docker build -t greetings-app .'
            }
        }
        stage('Run Docker Container Automatically') {
            steps {
                sh "docker run --rm greetings-app ${params.USER_NAME}"
            }
        }
    }
}
