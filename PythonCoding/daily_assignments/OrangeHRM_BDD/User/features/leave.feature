Feature: Leave Application

  Scenario: Apply Leave

    Given user is logged into OrangeHRM Leave page

    When user applies leave

    Then leave balance should reduce by one