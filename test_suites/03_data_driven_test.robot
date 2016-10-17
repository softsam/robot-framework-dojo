*** Variables ***
${number_of_items}      0

*** Keywords ***
Number Of Item Is ${number}
    set suite variable  ${number_of_items}      ${number}
    Log     number_of_items=${number_of_items}

Adding ${number} items
    ${result}=  evaluate   ${number_of_items}+${number}
    set suite variable  ${number_of_items}      ${result}

Multiplying items by ${number}
    ${result}=  evaluate   ${number_of_items}*${number}
    set suite variable  ${number_of_items}      ${result}

Number of items should be equal to ${number}
    should be equal as numbers  ${number_of_items}     ${number}

*** Test Cases ***
Robotframework should be able to add
    Given Number Of Item Is 3
    When Adding 2 items
    Then number of items should be equal to 5

Robotframework should be able to substract
    Given Number Of Item Is 4
    When Multiplying items by 8
    Then number of items should be equal to 32
