from behave import *
import operator
from functools import reduce
from django.db.models import Q

use_step_matcher("parse")

@given('Exists publication registered by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from era.models import Publicacion
    for row in context.table:
        publicacion = Publicacion(user=user)
        for heading in row.headings:
            setattr(publicacion, heading, row[heading])
        publicacion.save()

@when(u'I register publication')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('era:publicacion_create'))
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('Submit').first.click()

@then(u'I\'m viewing the details page for publication by "{user}"')
def step_impl(context, user):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(user=user))))
    from era.models import Publicacion
    publicacion = Publicacion.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(publicacion)

@then(u'There are {count:n} publications')
def step_impl(context, count):
    from era.models import Publicacion
    assert count == Publicacion.objects.count()