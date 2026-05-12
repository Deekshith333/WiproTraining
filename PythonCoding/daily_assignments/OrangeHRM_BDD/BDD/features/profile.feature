@Smoke
@Regression
@Profile

Feature: Profile Update

  Scenario: Update nickname and upload profile photo

    Given User launches OrangeHRM application

    And User logs in with valid credentials

    When User navigates to My Info section

    And User changes nickname to "Rechal"

    And User uploads profile picture

    And User clicks profile save button

    Then Profile should be updated successfully