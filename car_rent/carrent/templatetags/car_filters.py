from django.template import Library, Node
from django.template.defaultfilters import stringfilter



register = Library()



@register.filter(name="cut")
@stringfilter
def cut(text, num):
    if len(text) <= num:
        return text
    return f'{text[:num]}...'

def list_cars():
    return {'cars': models.Car.all()}

##@register.simple_tag(name='count')
##def cars_in_garage(garage_id=None, order_by='id'):
    ##return len(objs)

@register.inclusion_tag('car_rent/list_cars.html')
def list_cars():
    return {'cars': models.Car.objects.all()}

@register.tag (name='superif')
def myif(parser, token):
    nodes = parser.parse(('endsuperif',))
    parser.delete_first_token()
    print("NODES", nodes)
    print("TOKEN", token)
    return MyIfNode(token, nodes)

class MyIfNode(Node):
    def __init__(self, token):
        self.nodes = nodes
        self.token = token
    def render(self, context):
        return ''