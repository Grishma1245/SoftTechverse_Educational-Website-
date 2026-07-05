Feature: Navigation
  As a logged-in admin
  I want sidebar navigation to work correctly
  So that I can access all modules

  @smoke @navigation
  Scenario: Unauthenticated user is redirected to login
    Given I am not logged in
    When I try to access the dashboard directly
    Then I should be redirected to the login page
