pipeline {
    agent any
    environment {
        DH_USERNAME=credentials('DH_USERNAME')
        DH_PASSWD=credentials('DH_PASSWD')
    }
    stages {
        stage('Test'){
            steps {
                sh 'sudo apt update'
                sh 'sudo apt install python3 python3-pip python3-venv -y'
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
        stage('Setup dockerswarm'){
            steps {
                sh 'ansible-playbook -i ansible/inventory.yaml ansible/playbook.yaml'
            }
        }
        stage('Deploy to dockerswarm'){
            steps {
                sh 'scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml swarm-manager:/home/ahsanrasul/docker-compose.yaml'
                sh 'scp nginx.conf swarm-manager:/home/ahsanrasul/nginx.conf'
                // sh 'ssh ahsarasul@swarm-manager < sudo useradd jenkins'
                // sh 'ssh ahsanrasul@swarm-manager < sudo usermod -aG docker ahsanrasul'
                sh 'ssh ahsanrasul@swarm-manager < deploy.sh'
            }
        }

    }
}
