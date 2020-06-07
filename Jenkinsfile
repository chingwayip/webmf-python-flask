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
    stage('build2') {
      script {
        dockerImage = docker.build("${env.DOCKER_IMAGE_TAG}",  '-f ./Dockerfile .')
        pipelineContext.dockerImage = dockerImage
      }
    }
    stage('test') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
          sh 'python test.py'
        }
      }
    post {
      always {
          junit 'test-reports/*.xml'
        }
      }              
    }
  }
}
