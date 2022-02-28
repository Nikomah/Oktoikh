from django import forms
from captcha.fields import CaptchaField


class Message(forms.Form):
    subject = forms.CharField(max_length=100, label='Тема')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')
    sender = forms.EmailField(label='Ваш адрес электронной почты')
    cc_myself = forms.BooleanField(required=False, label='Отправить себе копию')
    captcha = CaptchaField()
