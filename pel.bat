@echo off
SETLOCAL

set _DEF=%1

IF "%_DEF%"=="serve" (
  GOTO :serve
)

IF "%_DEF%"=="site" (
  GOTO :site
)

IF "%_DEF%"=="dev" (
  GOTO :dev
)

IF "%_DEF%"=="pub" (
  GOTO :pub
)

IF "%_DEF%"=="git" (
  GOTO :git
)

IF "%_DEF%"=="help" (
  GOTO :help
)

echo No or incorrect argument given, please review your input or type
echo 'pel help' for help.
GOTO :end

:help
echo Batch file for a pelican Web site
echo.
echo Usage:
echo pel COMMAND
echo.
echo Commands:
echo    serve                   run the server.
echo    run                     generate the dev
echo    pub                     generate the published site
echo    site                    publish the source to github source branch
echo    git                     publish to git
echo.
GOTO :end

:site
echo Publishing the source
git add -A
git commit -m "Deploying changes"
git push origin source
GOTO :end

:serve
echo Running the server
pushd output
python -m pelican.server
popd
GOTO :end

:dev
echo generate the dev
pelican content --debug --autoreload  --output output --settings pelicanconf.py
GOTO :end

:pub
echo generate with publication settings
rd /s /q pub
pelican content --output pub --settings publishconf.py
GOTO :end

:git
echo publish to git
pushd pub
git init
git add .
git commit -m Initial
git remote add origin https://github.com/blackhorus/blackhorus.github.io.git
git push origin master --force
popd
GOTO :end

:end
ENDLOCAL