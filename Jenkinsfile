pipeline {
  agent { docker { image 'python:3.7.6' } }
  stages {
    stage('build') {
      steps {
	sh 'pip install -H -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python test.py'
      }
    }
  }
}
