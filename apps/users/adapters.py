import re
from urllib.parse import quote

from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from django.utils.http import is_safe_url

from adhocracy4.emails.mixins import SyncEmailMixin
from apps.users import USERNAME_INVALID_MESSAGE
from apps.users import USERNAME_REGEX
from apps.users.emails import EmailAplus as Email


class UserAccountEmail(SyncEmailMixin, Email):
    def get_receivers(self):
        return [self.object]

    @property
    def template_name(self):
        return self.kwargs['template_name']

    def get_context(self):
        context = super().get_context()
        context['contact_email'] = settings.CONTACT_EMAIL
        return context


class AccountAdapter(DefaultAccountAdapter):
    username_regex = re.compile(USERNAME_REGEX)
    error_messages = dict(
        DefaultAccountAdapter.error_messages,
        invalid_username=USERNAME_INVALID_MESSAGE
    )

    def get_email_confirmation_url(self, request, emailconfirmation):
        url = super().get_email_confirmation_url(request, emailconfirmation)
        if 'next' in request.POST and is_safe_url(request.POST['next'],
                                                  allowed_hosts=None):
            return '{}?next={}'.format(url, quote(request.POST['next']))
        else:
            return url

    def send_mail(self, template_prefix, email, context):
        return UserAccountEmail.send(
            email,
            template_name=template_prefix,
            **context
        )

    def get_email_confirmation_redirect_url(self, request):
        if 'next' in request.GET and is_safe_url(request.GET['next'],
                                                 allowed_hosts=None):
            return request.GET['next']
        else:
            return super().get_email_confirmation_redirect_url(request)
