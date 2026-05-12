#*** Settings ***
#Resource    ../resources/login_resources.resource
#
#Suite Setup       Open Application
#Suite Teardown    Close Application
#
#*** Test Cases ***
#Valid Login Test
#
#    Login To Application    standard_user    secret_sauce
#
#    Verify Login Success
#
#*** Settings ***
#Resource    ../resources/login_resources.resource
#
#Suite Setup       Open Application
#Suite Teardown    Close Application
#Test Teardown     Capture Failure Screenshot
#
#*** Test Cases ***
#Valid Login Test
#
#    Login To Application    standard_user    secret_sauce
#
#    Verify Login Success

*** Settings ***
Resource    ../resources/login_resources.resource

Suite Setup       Open Application
Suite Teardown    Close Application
Test Teardown     Capture Failure Screenshot

*** Test Cases ***
Valid Login Test
    [Tags]    Smoke    Critical
    [Documentation]    Verify successful login functionality using valid credentials.

    Login To Application    standard_user    secret_sauce

    Verify Login Success