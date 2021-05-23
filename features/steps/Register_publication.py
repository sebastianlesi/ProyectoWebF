from behave import *
import operator
from functools import reduce
from django.db.models import Q

use_step_matcher("parse")

@given(u'Exists publication registered by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from era.models import Publicacion
    for row in context.table:
        publicacion = Publicacion(user=user) #Revisar register de profe por
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

@then(u'I\'m viewing the details page for publication with name "{title}"')
def step_impl(context, title):
    from era.models import Publicacion
    publicacion = Publicacion.objects.get(titulo = title)
    context.browser.visit(context.get_url(publicacion))

@then(u'There are {count:n} publications')
def step_impl(context, count):
    from era.models import Publicacion
    assert count == Publicacion.objects.count()

@when(u'I edit the publication with name "{name}"')
def step_impl(context, name):
    from era.models import Publicacion
    publicacion = Publicacion.objects.get(titulo=name)
    context.browser.visit(context.get_url('era:publicacion_edit', publicacion.pk))
    if context.browser.url == context.get_url('era:publicacion_edit', publicacion.pk)\
            and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        form.find_by_value('Submit').first.click()