import datetime

from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.mail import send_mail
from django.views import View

from .forms import ContactForm


def hello(request):
    return HttpResponse("Welcome to the page at %s" % request.path)


def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, "dateapp/current_datetime.html", {"current_date": now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # assert False
    context = {"hour_offset": offset,
               "next_time": dt}
    return render(request, "dateapp/hours_ahead.html", context)


def ua_display(request):
    ua = request.META.get("HTTP_USER_AGENT", "unknown")
    return HttpResponse("Your browser is % s" % ua)

"""
or 
def ua_display(request):
    try:
        ua = request.META["HTTP_USER_AGENT"]
    except KeyError:
        ua = "unknown"
    return HttpResponse("Your browser is % s" % ua)
"""


def display_meta(request):
    values = request.META.items()
    values = sorted(values)
    html = []
    for k, v in values:
        html.append("<tr><td>%s</td><td>%s</td></tr>" % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}
        )
    return render(request, 'contact_form.html', {'form': form})


def debug(request):
    pass


class PostListView(View):
    def get(self, request):
        return JsonResponse(self.get_data(), json_dumps_params={'ensure_ascii': True})

    def get_data(self):
        return {
            "message": "안녕 파이썬 장고",
            "items": ["파이썬", "장고", "AWS", "Azure"]
        }


post_list = PostListView.as_view()