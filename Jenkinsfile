pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // https://github.com/rupar19/atg-world.git
                checkout scm
            }
        }

        stage('Build and Test') {
            steps {
                script {
                    // Set up a virtual environment and install dependencies
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate'
                    sh 'pip install -r requirements.txt'

                    // Run the Python unit test
                    sh 'python test_atg_world.py'
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
