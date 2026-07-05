Feature: Dashboard Verification
  As a logged-in admin
  I want to verify the dashboard loads correctly
  So that I can trust the system entry point

  @smoke @dashboard
  Scenario: Dashboard loads after login
    Given I am logged in as a valid user
    Then the dashboard page should be displayed
    And the sidebar should be visible
