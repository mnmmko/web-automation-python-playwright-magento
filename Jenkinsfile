pipeline {
    agent any
      stages {
       stage('Git Main Branch') {
         steps {
           git branch:'main', url:'https://github.com/mnmmko/web-automation-python-playwright-magento'
                      }
			 }

    stage('Build') {

            steps {


                bat 'python -m pip install --upgrade pip && pip install -r requirements.txt'

            }
        }
      stage('Test') {

                steps {


                    bat 'pytest -v'

                }

      }
          }

}