#*** Settings ***
#Library    SeleniumLibrary
#
#*** Variables ***
#${URL}               https://www.saucedemo.com
#${BROWSER}           edge
#${USERNAME_FIELD}    id:user-name
#${PASSWORD_FIELD}    id:password
#${LOGIN_BUTTON}      id:login-button
#${PRODUCT_TITLE}     xpath://span[text()='Products']
#
#*** Keywords ***
#Open Application
#    Open Browser    ${URL}    ${BROWSER}
#    Maximize Browser Window
#
#Login To Application
#    [Arguments]    ${username}    ${password}
#
#    Input Text        ${USERNAME_FIELD}    ${username}
#    Input Password    ${PASSWORD_FIELD}    ${password}
#    Click Button      ${LOGIN_BUTTON}
#
#Verify Login Success
#    Element Should Be Visible    ${PRODUCT_TITLE}
#
#Close Application
#    Close Browser
#
*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}               https://www.saucedemo.com
${BROWSER}           edge
${USERNAME_FIELD}    id:user-name
${PASSWORD_FIELD}    id:password
${LOGIN_BUTTON}      id:login-button
${PRODUCT_TITLE}     xpath://span[text()='Products']

*** Keywords ***
Open Application
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Login To Application
    [Arguments]    ${username}    ${password}

    Input Text        ${USERNAME_FIELD}    ${username}
    Input Password    ${PASSWORD_FIELD}    ${password}
    Click Button      ${LOGIN_BUTTON}

Verify Login Success
    Element Should Be Visible    ${PRODUCT_TITLE}

Capture Failure Screenshot
    Run Keyword If Test Failed
    ...    Capture Page Screenshot
    ...    failure_${TEST NAME}.png

Close Application
    Close Browser
