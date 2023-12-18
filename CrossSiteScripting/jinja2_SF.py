from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader("example"),
                  autoescape=False)

template = env.from_string('<p>{{ user_input }}</p>')

# Simulating user input that contains a script tag
user_input = '<script>alert("XSS attack");</script>'

# Rendering the template with unescaped user input
output = template.render(user_input=user_input)

print(output)
