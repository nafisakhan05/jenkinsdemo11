Pipeline {
    agent any 
    stages {
        stage('Checkout code'){
            step{
               Checkout scm
            }
        }
        stage('Extract Data'){
            step{
               bat "C:\\Users\\nextgen\\AppData\\Local\\Programs\\Python\\Python312\\python.exe extract.py"
            }
        }
    }
}