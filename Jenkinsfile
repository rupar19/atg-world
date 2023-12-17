pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository
                checkout scm
            }
        }

        stage('Build and Test') {
            steps {
                script {
                    // Install dependencies
                    sh 'pip3 install -r requirements.txt'

                    // Run the Python unit test
                    sh 'python3 test_atg_world.py'
                }
            }
        }
    }

    post {
        success {
            echo 'Unit test passed! Job successful.'
        }
        failure {
            echo 'Unit test failed! Job failed.'
        }
    }
}
