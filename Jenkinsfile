pipeline {
    agent any
    environment {
        DH_USERNAME=credentials('DH_USERNAME')
        DH_PASSWD=credentials('DH_PASSWD')
    }
    stages {
        stage('Test'){
            steps {
                sh './tests.sh'
            }
        }
        stage('Building docker images and push to dockerhub'){
            steps {
                sh '''docker-compose build
                docker login --username ${DH_USERNAME} --password ${DH_PASSWD}
                docker-compose push'''
            }
        }
        stage('Deploy to dockerswarm'){
            steps {
                sh 'scp docker-compose.yaml docker-manager:/home/jenkins/docker-compose.yaml'
                sh 'scp nginx.conf docker-manager:/home/jenkins/nginx.conf'
                sh 'ssh ahsarasul@docker-manager < sudo useradd jenkins'
                sh 'ssh jenkins@docker-manager < deploy.sh'
            }
        }

    }
}
