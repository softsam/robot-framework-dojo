*** Settings ***
Library     OperatingSystem
Library     DateTime
Documentation    Test to check that every thing
...              is perfectly set for this
...              robotframework tutorial.

*** Test Cases ***
Application file must be present
    Directory Should Exist  ./app-to-test
    File Should Exist       ./app-to-test/login.py
    File Should Exist       ./app-to-test/webapp.py

Test is only valid on robot training
    ${current_date}=    Get Current Date    result_format=datetime
    should be equal as integers     ${current_date.year}     2016
    should be equal as integers     ${current_date.month}     12
    should be equal as integers     ${current_date.day}     2

