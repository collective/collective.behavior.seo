*** Settings ***

Resource    plone/app/robotframework/browser.robot

Library    OperatingSystem
Library    Remote    ${PLONE_URL}/RobotRemote

*** Keywords ***

Default Setup
    Run Keyword    Plone Test Setup

Default Teardown
    Run Keyword If Test Failed    Capture Page Screenshot
    Run Keyword If Test Failed    Log Variables
    Run Keyword    Plone Test Teardown

# --- Given ------------------------------------------------------------------

a login form
    Go To    ${PLONE_URL}/login_form
    Get Text    //body    contains    Login Name
    Get Text    //body    contains    Password


# --- WHEN -------------------------------------------------------------------

I enter valid credentials
    Type Text    //input[@name="__ac_name"]    admin
    Type Text    //input[@name="__ac_password"]    secret
    Click    //button[@name="buttons.login"]


# --- THEN -------------------------------------------------------------------

I am logged in
    Get Text    //body    contains    You are now logged in