from behave import *
import operator
from functools import reduce
from django.db.models import Q

import os

from eracom.settings import BASE_DIR

use_step_matcher("parse")

@given('Exists comment at publication "{publication_name}"')
def step_impl(context, publication_name):
    from era.models import Publicacion
    publicacion = Publicacion.objects.get(titulo=publication_name)
    from era.models import Comentario
    for row in context.table:
        comment = Comentario(publicacion=publicacion)
        for heading in row.headings:
            setattr(comment, heading, row[heading])
        comment.save()

@when('I register comment at publication "{publication_name}"')
def step_impl(context, publication_name):
    from era.models import Publicacion
    publicacion = Publicacion.objects.get(titulo=publication_name)
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

#@then('I\'m viewing the details page for comment at publication "{publication_name}" with comment "{com}"')
#def step_impl(context, publication_name, com):
#   from era.models import Comentario, Publicacion
#    publicacion = Publicacion.objects.get(titulo=publication_name)
#   comentario = Comentario.objects.get(Comentario=com)
#    context.browser.visit(context.get_url(comentario))

@then('I\'m viewing the details page for comment at publication "{publication_name}"')
def step_impl(publication_name,context):
    from era.models import Comentario, Publicacion
    publicacion2 = Publicacion.objects.get(titulo=publication_name)
    comentario = Comentario.objects.all().filter(publicacion=publicacion2)
    for c in comentario:
     assert not context.browser.find_by_name(f'{publication_name}_{comentario.comentario}').is_empty()
    #context.browser.find_by_name(f'{publication_name}_{comentario.comentario}')

@then('There are {count:n} comments')
def step_impl(context, count):
    from era.models import Comentario
    assert count == Comentario.objects.count()

@when('I edit the comment at publication with the id_comentario "{name}"')
def step_impl(context, name):
    from era.models import Comentario
    comentario = Comentario.objects.get(id_comentario=name)
    context.browser.visit(context.get_url('era:comment_edit', comentario.pk, name))
    if context.browser.url == context.get_url('era:comment_edit', comentario.pk, name)\
            and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        form.find_by_value('Submit').first.click()

@when(u'I try deleting the comment with comment "{com}"')
def step_impl(context, com):
    kwargs1={Comentario:com}
    from era.models import Comentario
    pr = Comentario.objects.filter(kwargs1).first()
    print(f'{Comentario.__name__.lower()}/delete/{pr.pk}')
    context.browser.visit(context.get_url(f'/{Comentario.__name__.lower()}/delete/{pr.pk}'))