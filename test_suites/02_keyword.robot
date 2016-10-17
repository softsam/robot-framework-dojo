*** Keywords ***
Ask user the user ${question}
    log to console  \n${question}
    ${result}=  evaluate    sys.stdin.readline().rstrip('\\r\\n').lower()     sys
    [Return]  ${result}

*** Test Cases ***
Evaluate user identity
    ${username}=    Ask user the user What is your name
    should not be empty     ${username}

User must be happy
    ${user_answer}=     Ask user the user Are you happy to be here
    should be equal     ${user_answer}      yes

User must be adult
    [Tags]	csa
    ${user_age}=    Ask user the user How old are you
    ${user_adult}=  evaluate    int($user_age) >= 18
    should be true  ${user_adult}

User must work for orange
    [Tags]    addon_non_mandatory
    ${user_compagny}=   Ask user the user Who are you working for?
    should be equal     ${user_compagny}    orange
