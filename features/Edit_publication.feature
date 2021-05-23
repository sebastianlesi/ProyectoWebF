Feature: Edit Publication
In order to keep updated my previous registers about publications
As a user,
I want to edit a publication register I created.

Background: There are registered users and a publication by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists publication registered by "user1"
      | titulo                 | descripcion    | vistas    |
      | Movilidad en España    | ingenieria     | 0         |

    Scenario: Edit owned publication registry descripcion
    Given I login as user "user1" with password "password"
    When I edit the publication with name "Movilidad en España"
      | descripcion          |
      | licenciatura         |
    Then I'm viewing the details page for publication with name "Movilidad en España"
      | titulo                 | descripcion      | vistas    |
      | Movilidad en España    | licenciatura     | 0         |
    And There are 1 publications