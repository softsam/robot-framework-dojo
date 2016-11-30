*** Settings ***
Library  Selenium2Library
Library           OperatingSystem
Suite Setup  Start My Browser
Suite Teardown  Run Keywords    close all browsers
Test Teardown  Clear login database


*** Variables ***
${DATABASE_FILE}          ${TEMPDIR}${/}robotframework-quickstart-db.json

*** Keywords ***
Start My Browser
    Create WebDriver  PhantomJS
    # Either run
    # Create WebDriver  PhantomJS
    # or
    # Create WebDriver  Firefox
    # or
    # Open browser  about:  chrome

Clear login database
    Remove File         ${DATABASE_FILE}

Logout if logged
    Go To       http://localhost:5000
    ${is_not_logged}=       run keyword and return status  Page Should Contain     SignIn
    Run Keyword Unless      ${is_not_logged}    Click Element   id=logout


*** Test Cases ***
Not logged Should Redirect To Login
    Go To       http://localhost:5000
    Page Should Contain     SignIn
    Page Should Contain     Unauthorized

Signup should work
    Go To       http://localhost:5000/signup
    Input Text  name=username       toto
    Input Text  name=password       Toto1234
    Submit Form     id=signupForm
    Page Should Contain     Home

Signin existing account should work
    [Setup]  Create User     toto    Toto1234
    # Aller sur l ihm, Se connecter, on devrait etre sur la page d accueuil
    Fail    Implement me

Signup on existing account should fail
    [Setup]  Create User     toto    Toto1234
    # Aller sur l ihm, S'inscrire, on devrait etre sur la page de signup avec une erreur
    Fail    Implement me

Signout should work
    [Setup]  Create User     toto    Toto1234
    Go To       http://localhost:5000
    # signin , signout, on devrait etre sur la page de signout

