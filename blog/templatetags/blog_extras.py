from django.contrib.auth import get_user_model
from django.template import Library
from django.utils.html import format_html

user_model = get_user_model()
register = Library()

@register.filter
def author_details(author, current_user=None):
  if not isinstance(author, user_model):
    # return empty string as safe default
    return ""


  if author == current_user:
    return format_html("<strong>me</strong>")
  elif author.first_name and author.last_name:
    name =  f"{author.first_name} {author.last_name}"
  else:
    name = f"{author.username}"
  
  if author.email:
    prefix = format_html("<a href='mailto:{}'>", author.email)
    suffuix = format_html("</a>")
  else:
    prefix = ""
    suffuix = ""

  return format_html("{} {} {}", prefix, name, suffuix)