from jinja2 import Environment, PackageLoader

def render_template(user_input):
    # Loading the template with autoescape set to False
    env = Environment(loader=PackageLoader("example"), autoescape=False)
    template = env.from_string('<p>{{ user_input }}</p>')

    # Rendering the template with unescaped user input
    output = template.render(user_input=user_input)

    return output

def get_user_input():
    # Simulating user input that contains a script tag
    return '<script>alert("XSS attack");</script>'

# Separating source (get_user_input) and sink (render_template)
user_input = get_user_input()
result = render_template(user_input)

print(result)
