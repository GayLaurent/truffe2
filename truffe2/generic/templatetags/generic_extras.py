from django import template
from django.utils.safestring import mark_safe

from bootstrap3.renderers import FieldRenderer
from bootstrap3.text import text_value
import re
import bleach

register = template.Library()

pos = [(0, 0), (1, 0), (0, 1), (2, 3), (1, 2), (2, 1), (2, 2)]
re_spaceless = re.compile("(\n|\r)+")


@register.filter
def node_x(value):
    x, _ = pos[value]
    return x


@register.filter
def node_y(value):
    _, y = pos[value]
    return y


@register.filter
def get_attr(value, arg):
    v = getattr(value, arg, None)
    if hasattr(v, '__call__'):
        v = v()
    elif isinstance(value, dict):
        v = value.get(arg)
    if v is None:
        return ''
    return v


@register.filter
def call(obj, methodName):
    method = getattr(obj, methodName)
    if "__callArg" in obj.__dict__:
        ret = method(*obj.__callArg)
        del obj.__callArg
        return ret
    return method()


@register.filter
def args(obj, arg):
    if "__callArg" not in obj.__dict__:
        obj.__callArg = []

    obj.__callArg += [arg]
    return obj


@register.filter
def get_class(value):
    return value.__class__.__name__


@register.filter
def is_new_for(obj, user):
    return obj.is_new(user)


@register.simple_tag(takes_context=True)
def switchable(context, obj, user, id):
    return 'true' if obj.may_switch_to(user, id) else 'false'


@register.simple_tag(takes_context=True)
def get_list_quick_switch(context, obj):
    if hasattr(obj.MetaState, 'list_quick_switch'):
        return filter(lambda status_values: obj.may_switch_to(context['user'], status_values[0]), obj.MetaState.list_quick_switch.get(obj.status, []))


@register.simple_tag(takes_context=True)
def get_states_quick_switch(context, obj):
    if hasattr(obj.MetaState, 'states_quick_switch'):
        return filter(lambda status_values: obj.may_switch_to(context['user'], status_values[0]), obj.MetaState.states_quick_switch.get(obj.status, []))


@register.tag
def nocrlf(parser, token):
    nodelist = parser.parse(('endnocrlf',))
    parser.delete_first_token()
    return CrlfNode(nodelist)


class CrlfNode(template.Node):

    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        rendered = self.nodelist.render(context).strip()
        return re_spaceless.sub("", rendered)


@register.filter
def html_check_and_safe(value):
    tags = bleach.ALLOWED_TAGS + ['div', 'br', 'font', 'p', 'table', 'tr', 'td', 'th', 'img', 'u', 'span', 'tbody', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr']
    attrs = {
        '*': ['class', 'style', 'color', 'align', 'title', 'data-toggle', 'data-placement'],
        'a': ['href', 'rel'],
        'img': ['src', 'alt'],
    }
    style = ['line-height', 'background-color', 'font-size', 'margin-top']
    return mark_safe(bleach.clean(value, tags=tags, attributes=attrs, styles=style))


class SimpleFieldRenderer(FieldRenderer):

    def render(self):
        # See if we're not excluded
        if self.field.name in self.exclude.replace(' ', '').split(','):
            return ''
        # Hidden input requires no special treatment
        if self.field.is_hidden:
            return text_value(self.field)
        # Render the widget
        self.add_widget_attrs()
        html = self.field.as_widget(attrs=self.widget.attrs)
        self.restore_widget_attrs()
        # Start post render
        html = self.post_widget_render(html)
        html = self.wrap_widget(html)
        html = self.make_input_group(html)
        html = self.append_to_field(html)
        html = self.wrap_field(html)

        return html


@register.simple_tag()
def simple_bootstrap_field(field):

    return SimpleFieldRenderer(field).render()
