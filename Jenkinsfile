pipeline {
    agent any
    environment {
        DH_USERNAME=credentials('DH_USERNAME')
        DH_PASSWD=credentials('DH_PASSWD')
    }
    stages {
        stage('Test'){
            steps {
                sh 'sudo apt install python3 python3-pip python3-venv -y'
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'bash tests.sh'
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
                sh 'scp docker-compose.yaml swarm-manager:/home/jenkins/docker-compose.yaml'
                sh 'scp nginx.conf swarm-manager:/home/jenkins/nginx.conf'
                sh 'ssh ahsarasul@swarm-manager < sudo useradd jenkins'
                sh 'ssh jenkins@swarm-manager < deploy.sh'
            }
        }

    }
}
