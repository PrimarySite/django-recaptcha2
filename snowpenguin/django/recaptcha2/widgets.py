from django.conf import settings
from django.forms.widgets import Widget
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class ReCaptchaWidget(Widget):
    def __init__(self, theme=None, type=None, size=None, tabindex=None, callback=None,
                 expired_callback=None, attrs={}, *args, **kwargs):
        super(ReCaptchaWidget, self).__init__(*args, **kwargs)
        self.theme = theme
        self.type = type
        self.size = size
        self.tabindex = tabindex
        self.callback = callback
        self.expired_callback = expired_callback
        self.attrs = attrs

    def render(self, name, value, attrs=None):
        template = 'snowpenguin/recaptcha/recaptcha.html'

        return mark_safe(
            render_to_string(template, {
                'container_id': 'id_%s' % name,
                'public_key': settings.RECAPTCHA_PUBLIC_KEY,
                'theme': self.theme,
                'type': self.type,
                'size': self.size,
                'tabindex': self.tabindex,
                'callback': self.callback,
                'expired_callback': self.expired_callback
            })
        )

    def value_from_datadict(self, data, files, name):
        return [data.get('g-recaptcha-response', None)]
