*** Settings ***
Library     OperatingSystem
Library     DateTime

*** Test Cases ***
Application file must be present
    Directory Should Exist  ./app-to-test
    File Should Exist       ./app-to-test/login.py
    log     file is present

Test is only valid on developer's day
    ${current_date}=    Get Current Date    result_format=datetime
    should be equal as integers     ${current_date.year}     2016
    log  year is good
    should be equal as integers     ${current_date.month}     10
    log  month is good
    should be equal as integers     ${current_date.day}     19
    log  year is good

