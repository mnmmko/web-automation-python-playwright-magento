pipeline {
    agent any
      stages {
       stage('Git Main Branch') {
         steps {
           git branch:'main', url:'https://github.com/mnmmko/Automation-selenium-python-web-Magento'
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