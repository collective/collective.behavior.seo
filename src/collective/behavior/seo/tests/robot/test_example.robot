# Start a single robot test
#
# Install rfbrowser
#
# rfbrowser init
#
# Start the server
#
# WSGI_SERVER_HOST=localhost WSGI_SERVER_PORT=50003 robot-server collective.behavior.seo.testing.COLLECTIVE_BEHAVIOR_SEO_ACCEPTANCE_TESTING
#
# Start the test
#
# WSGI_SERVER_HOST=localhost WSGI_SERVER_PORT=50003 robot src/collective/behavior/seo/tests/robot/test_example.robot
#



*** Settings ***

Resource  keywords.robot

Test Setup    Run keyword    Default Setup
Test Teardown    Run keyword    Default Teardown

# disable headless mode for browser
# set the variable BROWSER to chrome or firefox
# *** Variables ***
# ${BROWSER}    chrome

*** Test Cases ***

Scenario: As a member I want to be able to log into the website
    Given a login form
     When I enter valid credentials
     Then I am logged in
