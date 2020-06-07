pipeline {
  agent { docker { image 'python:3.7.6' } }
  stages {
    stage('build') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
	  sh 'pip install --user -r requirements.txt'
        }
      }
    }
    stage('test') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
          sh 'python test.py'
        }
      }
    stage('Build docker image') {
      sh "docker build . -t webmf-python-flask-app"
    }
    post {
      always {
          junit 'test-reports/*.xml'
        }
      }              
    }
  }
}
