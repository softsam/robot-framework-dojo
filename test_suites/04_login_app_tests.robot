*** Settings ***
Library           OperatingSystem
Library           ../lib/LoginLibrary.py
Suite Setup       Clear Login Database
Test Teardown     Clear Login Database

*** Variables ***
${DATABASE FILE}          ${TEMPDIR}${/}robotframework-quickstart-db.txt
${PWD INVALID LENGTH}     Creating user failed: Password must be 7-12 characters long
${PWD INVALID CONTENT}    Creating user failed: Password must be a combination of lowercase and uppercase letters and numbers


*** Keywords ***
Clear login database



*** Test Cases ***
Creating user with password too long should fail
    FAIL  implement me

Creating user with invalid password should fail
    FAIL  implement me

User can create a valid account and log in
    FAIL  implement me

User cannot log in with bad password
    FAIL  implement me


