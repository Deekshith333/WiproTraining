*** Settings ***
Library     ../libraries/ProductPage.py
Resource    ../resources/login_resources.resource

Suite Setup       Open Application
Suite Teardown    Close Application

*** Test Cases ***
Verify Product Total

    Login To Application    standard_user    secret_sauce

    ${price1}=    Get Product Price By Name    Sauce Labs Backpack

    ${price2}=    Get Product Price By Name    Sauce Labs Bike Light

    ${total}=    Evaluate    ${price1}+${price2}

    Should Be Equal As Numbers    ${total}    39.98