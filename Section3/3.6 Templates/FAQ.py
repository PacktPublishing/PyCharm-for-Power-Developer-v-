import jinja2

faq = [
    'How is my cost calculated?',
    'Where do profits go?',
    'Where are meats collected from?'
]

template = jinja2.Template("""
<html>
<title>FAQs</title>
<h1>Frequently Asked Questions</h1>

<ul>
  {% for question in faqs %}
  <li>{{question}}</li>
  {% endfor %}
</ul>

</html>""")

print template.render({'faqs': faq})
template.stream({'faqs': faq}).dump('FAQ.html')