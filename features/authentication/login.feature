Feature: User Authentication
  As a school admin
  I want to login to the education portal
  So that I can access the system

  @smoke @login
  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter valid credentials
    Then I should be redirected to the dashboard

  @login @negative
  Scenario: Login fails with invalid credentials
    Given I am on the login page
    When I enter invalid credentials
    Then I should remain on the login page
