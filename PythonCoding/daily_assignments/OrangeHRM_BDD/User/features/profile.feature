Feature: Profile Update

  Scenario: Upload Profile Picture

    Given user opens My Info page

    When user uploads profile image

    Then profile should update successfully