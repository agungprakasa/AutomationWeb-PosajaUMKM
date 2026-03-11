import org.jenkinsci.plugins.pipeline.modeldefinition.Utils 

//GIT CHECKOUT
def git_credentials_id = scm.userRemoteConfigs[0].credentialsId
def git_repo = scm.userRemoteConfigs[0].url
def git_branch = scm.branches[0].name
def gitCommitId
def resultlog
def pomappName = "PosajaUMKM-AutomationTest"
def urlJenkinsJob = 'http://10.24.7.14:8080/job/'
def buildNumber = currentBuild.number

def sendTelegramNotification(String message) {
    def token = "token"
    def chatId = "-4800804566"
    def url = "https://api.telegram.org/bot${token}/sendMessage"

    sh """
    curl -s -X POST ${url} -d chat_id=${chatId} -d text="${message}"
    """
}





node {
    stage('Checkout') {
        cleanWs()
        git url: "${git_repo}", branch: "${git_branch}", credentialsId: "${git_credentials_id}"
        resultlog = sh(returnStdout: true, script: 'git log  -1 --pretty=%B')
        env.M2_HOME = "/opt/maven"
        env.PATH="/opt/oc:${env.M2_HOME}/bin:${env.PATH}"
    }

    
    stage('Sonarqube Check'){ 
        def scannerHome = tool 'SonarScanner';
        withSonarQubeEnv() {
        sh "${scannerHome}/bin/sonar-scanner"
        }    
    }


    stage('Run in Docker') {
        docker.image('python:3.10-slim').inside {
            stage('Install Dependencies') {
                sh '''
                    apt-get update
                    apt-get install -y curl
                    pip install selenium
                '''
            }

            stage('Run Selenium Test') {
                def result

                sh 'mkdir -p output' 
                // sh 'python3 tests/register.py > output/register.log 2>&1'
                // sh 'python3 tests/login.py > output/login.log 2>&1'
                // sh 'python3 tests/lupa_password.py > output/lupa_password.log 2>&1'
                // sh 'python3 tests/toko.py > output/toko.log 2>&1'

                result = sh(script: 'python3 tests/register.py > output/register.log 2>&1', returnStatus: true)
                echo "Register.py exit code: ${result}"

                result = sh(script: 'python3 tests/login.py > output/login.log 2>&1', returnStatus: true)
                echo "Login.py exit code: ${result}"

                result = sh(script: 'python3 tests/lupa_password.py > output/lupa_password.log 2>&1', returnStatus: true)
                echo "Lupa_password.py exit code: ${result}"

                result = sh(script: 'python3 tests/toko.py > output/toko.log 2>&1', returnStatus: true)
                echo "Toko.py exit code: ${result}"
                sendTelegramNotification("${env.JOB_NAME} #${env.BUILD_NUMBER} >> \nAutomation Testing Selesai")

            }
            stage('Archive Artifacts') {
                archiveArtifacts artifacts: 'output/**', fingerprint: true
            }

            stage('Send to Telegram') {
            // Kirim semua log
            sh '''
            for file in output/*.log; do
                if [ -f "$file" ]; then
                    curl -s -X POST https://api.telegram.org/bottoken/sendDocument \
                        -F chat_id=-4800804566 \
                        -F document=@"$file" \
                        -F caption="Log: $(basename $file)"
                fi
            done
            '''

            // Kirim semua gambar jika ada
            sh '''
            for file in output/*.png; do
                [ -e "$file" ] || continue
                curl -s -X POST https://api.telegram.org/bottoken/sendPhoto \
                    -F chat_id=-4800804566 \
                    -F photo=@"$file" \
                    -F caption="Screenshot: $(basename $file)"
            done
            '''
        }
        }
    } 

}
