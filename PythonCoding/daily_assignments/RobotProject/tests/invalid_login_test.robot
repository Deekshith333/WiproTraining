*** Settings ***
Library     SeleniumLibrary
Resource    ../resources/login_resources.resource

Suite Setup       Open Application
Suite Teardown    Close Application
Test Teardown     Capture Failure Screenshot

*** Test Cases ***
Invalid Login Tests
    [Tags]    Regression
    [Documentation]    Verify invalid login scenarios using multiple test data combinations.

    [Template]    Invalid Login Scenario

    invalid_user      wrongpass      Epic sadface: Username and password do not match any user in this service
    locked_out_user   secret_sauce   Epic sadface: Sorry, this user has been locked out.
    problem_user      wrongpass      Epic sadface: Username and password do not match any user in this service

*** Keywords ***
Invalid Login Scenario
    [Arguments]    ${username}    ${password}    ${error}

    Input Text        id:user-name    ${username}
    Input Password    id:password     ${password}
    Click Button      id:login-button

    Element Should Contain
    ...    xpath://h3[@data-test='error']
    ...    ${error}

    Reload Page