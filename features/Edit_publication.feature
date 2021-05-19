Feature: Edit Publication
In order to keep track of the changes I do,
As a user,
I want to edit a publication register I created.

Background: There are registered users and a publication by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists publication registered by "user1"
      | titulo        | descripcion    | vistas    |
      | The Tavern    | ingenieria     | 0         |

  Scenario: Edit owned publication registry vistas
    Given I login as user "user1" with password "password"
    When I edit the publication with name "The Tavern"
      | vistas    |
      | 1         |
    Then I'm viewing the details page for publication by "user1"
      | titulo        | descripcion    | vistas    |
      | The Tavern    | ingenieria     | 1         |
    And There are 1 publications