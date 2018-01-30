node {
  stage('SCM') {
    git([url: 'ssh://git@github.com:poju0424/parseBotRate.git', branch: 'master', credentialsId: '399e0e6d67d69627316150de230a2c125788919f'])
  }
  stage('Build + SonarQube analysis') {
    def sqScannerMsBuildHome = tool 'sonarBuild'
    withSonarQubeEnv('My SonarQube Server') {
      // Due to SONARMSBRU-307 value of sonar.host.url and credentials should be passed on command line
      bat "${sqScannerMsBuildHome}\\SonarQube.Scanner.MSBuild.exe begin /k:myKey /n:myName /v:1.0 /d:sonar.host.url=%SONAR_HOST_URL% /d:sonar.login=%SONAR_AUTH_TOKEN%"
      bat 'MSBuild.exe /t:Rebuild'
      bat "${sqScannerMsBuildHome}\\SonarQube.Scanner.MSBuild.exe end"
    }
  }
}
