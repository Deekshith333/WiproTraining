Feature: Leave Application Workflow

  Scenario: Apply medical leave successfully

    Given User launches OrangeHRM application

    And User logs in with valid credentials

    When User navigates to Leave module

    And User applies for "Medical Leave"

    And User submits leave request

    Then Leave request should be submitted successfully

    And Leave status should be "Pending Approval"

    And Leave balance should be reduced