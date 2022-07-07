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
        stage('Remove existing images'){
            steps {
                sh 'docker system prune --all --volumes --force'
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
                sh 'scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml ahsanrasul@swarm-manager:/home/ahsanrasul/docker-compose.yaml'
                sh 'scp -i ~/.ssh/ansible_id_rsa nginx.conf ahsanrasul@swarm-manager:/home/ahsanrasul/nginx.conf'
                sh 'scp -i ~/.ssh/ansible_id_rsa deploy.sh ahsanrasul@swarm-manager:/home/ahsanrasul/deploy.sh'
                sh 'ssh ahsanrasul@swarm-manager bash deploy.sh'
            }
        }

    }
}
