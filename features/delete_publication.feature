Feature: Delete Publication
In order to delete old or useless publication,
As a user,
I want to delete a publication register I created.

Background: There are registered users and a publication by one of them
    Given Exists a user "user" with password "password"
    And Exists publication registered by "user"
      | titulo        | descripcion    | vistas    |
      | The Tavern    | ingenieria     | 0         |

  Scenario: Delete owned publication registry
    Given I login as user "user" with password "password"
    When I delete the restaurant with name "The Tavern"
      | name            | city            | country         |
      |                 |                 |                 |
    Then I'm viewing the details page for publication by "user"
      | name            | city            | country         |
      |                 |                 |                 |
    And There are 0 publications