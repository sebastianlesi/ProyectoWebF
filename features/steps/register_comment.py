from behave import *
import operator
from functools import reduce
from django.db.models import Q

import os

from eracom.settings import BASE_DIR

use_step_matcher("parse")

@given('Exists comment at publication "{publication_name}" by "{username}"')
def step_impl(context, publication_name, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from era.models import Publicacion
    publicacion = Publicacion.objects.get(name=publication_name)
    from era.models import Comentario
    for row in context.table:
        comment = Comentario(publicacion=publicacion, user=user)
        for heading in row.headings:
            setattr(comment, heading, row[heading])
        comment.save()

@when('I register comment at pubication "{publication_name}"')
def step_impl(context, publication_name):
    from era.models import Publicacion
    publicacion = Publicacion.objects.get(name=publication_name)
    for row in context.table:
        context.browser.visit(context.get_url('era:comment_create', publicacion.pk))
        if context.browser.url == context.get_url('era:comment_create', publicacion.pk):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                if heading == 'image':
                    filePath = os.path.join(BASE_DIR, row[heading])
                    context.browser.fill(heading, filePath)
                else:
                    context.browser.fill(heading, row[heading])
            form.find_by_value('Submit').first.click()

@then('I\'m viewing the details page for comment at publication "{publication_name}" by "{username}"')
def step_impl(context, publication_name, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username=username))))
    from era.models import Publicacion
    q_list.append(Q(('publicacion', Publicacion.objects.get(name=publication_name))))
    from era.models import Comentario
    comment = Comentario.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(comment)
    if comment.image:
        comment.image.delete()

@then('There are {count:n} comments')
def step_impl(context, count):
    from era.models import Comentario
    assert count == Comentario.objects.count()