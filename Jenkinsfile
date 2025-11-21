pipeline {
  agent any

  options {
    // prevent concurrent builds
    disableConcurrentBuilds()
    // do not resume if controller restarts
    disableResume()
    // keep a small number of builds
    buildDiscarder(logRotator(numToKeepStr: '10'))
  }

  stages {
    stage('Checkout') {
      steps {
        // Checkout using the specified credentials (set credentials in job)
        git branch: 'main',
            url:  'https://github.com/masauso-lungu/ai4devops.git',
            credentialsId: 'ai4d_github_token'

        echo "Checked out repo successfully"
      }
    }

    stage('Build/Test') {
      steps {
        // Run commands from the jenkins/ dir but run pytest relative to repo root
        dir('jenkins') {
          sh '''#!/bin/bash -l
set -euo pipefail

# run tests from the repo root (venv placed at repo root)
if [ -d "../tests" ]; then
  # create venv at repo root (idempotent if already exists)
  python3 -m venv ../venv || true
  . ../venv/bin/activate

  pip install --upgrade pip
  # install requirements if file exist
  if [ -f "../requirements.txt" ]; then
    pip install -r ../requirements.txt
  fi

  # ensure tests can import local packages
  export PYTHONPATH="$(pwd)/..:$PYTHONPATH"

  # results
  mkdir -p ../jenkins/reports

  # run pytest from the repo root path
  pytest ../tests/ --maxfail=1 --disable-warnings -q --junitxml=../jenkins/reports/results.xml
else
  echo "No tests found"
fi
'''
        }
      }
    }

    stage('Update JIRA') {
      steps {
        // Demo/mock step — replace with real REST call if desired
        echo "Would update JIRA ticket AI4D-5 here (mock)"
      }
    }
  }

  post {
    always {
      echo 'Archiving test reports and cleaning workspace'
      archiveArtifacts artifacts: 'jenkins/reports/**', allowEmptyArchive: true
      cleanWs()
    }
    failure {
      echo 'Build failed — check Console Output for details'
    }
  }
}
