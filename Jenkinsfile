node {
  stage('SCM') {
    git 'https://github.com/poju0424/parseBotRate.git'
    git branch: 'master',
    credentialsId: 'poju0424+t04241128',
    url: 'https://github.com/poju0424/parseBotRate.git'
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
