*** Keywords ***
Prompt User
    [Arguments]  ${prompt}
    log to console  ${EMPTY}
    log to console  ${prompt}
    ${result}=  evaluate    sys.stdin.readline().rstrip('\\r\\n').lower()     sys
    [Return]  ${result}

*** Test Cases ***
Evaluate user identity
    ${username}=    Prompt User     What is your name
    should not be empty     ${username}

User must be happy
    ${user_answer}=     Prompt User     Are you happy to be here
    should be equal     ${user_answer}      yes

User must be adult
    ${user_age}=    Prompt User     How old are you
    ${user_adult}=  evaluate    int($user_age) >= 18
    should be true  ${user_adult}

User must work for orange
    ${user_compagny}=   Prompt User     Who are you working for?
    should be equal     ${user_compagny}    orange
