from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import Message
from .models import *
from django.views.generic import DetailView, ListView

voices_dict = {
    1: 'Глас первый',
    2: 'Глас второй',
    3: 'Глас третий',
    4: 'Глас четвертый',
    5: 'Глас пятый',
    6: 'Глас шестой',
    7: 'Глас седьмой',
    8: 'Глас восьмой'
}
vozglasy = {
    1: 'Ћкw твоS держaва, и3 твоE є4сть цrтво, и3 си1ла, и3 слaва, nц7A, и3 сн7а, и3 с™aгw д¦а, нhнэ и3 при1снw,'
       ' и3 во вёки вэкHвъ.',
    2: 'Ћкw бlгъ и3 чlвэколю1бецъ бGъ є3си2, и3 тебЁ слaву возсылaемъ, nц7Y, и3 сн7у, и3 с™0му д¦у, нhнэ '
       'и3 при1снw, и3 во вёки вэкHвъ.',
    3: 'Ћкw бlгослови1сz и4мz твоE, и3 прослaвисz цrтво твоE, nц7A, и3 сн7а, и3 с™aгw д¦а, нhнэ и3 при1снw,'
       ' и3 во вёки вэкHвъ.',
    4: 'Ћкw ты2 є3си2 бGъ нaшъ, и3 тебЁ слaву возсылaемъ, nц7Y, и3 сн7у, и3 с™0му д¦у, нhнэ и3 при1снw, '
       'и3 во вёки вэкHвъ.',
    5: 'Тh бо є3си2 цRь ми1ра, и3 сп7съ: душ наших и3 тебЁ слaву возсылaемъ, nц7Y, и3 сн7у, и3 с™0му д¦у, '
       'нhнэ и3 при1снw, и3 во вёки вэкHвъ.',
    6: 'Ћкw тS хвaлzтъ вс‰ си6лы нбcныz и3 тебЁ слaву возсылaемъ, nц7Y, и3 сн7у, и3 с™0му д¦у, нhнэ и3 при1снw, и3'
       ' во вёки вэкHвъ.'
}


def main(request):
    data = {
        'voices_dict': voices_dict,
    }
    return render(request, 'oktoih/main_page.html', context=data)


class Voices(DetailView):
    model = SundayServicesVespers
    queryset = SundayServicesVespers.objects.select_related('canon', 'matins', 'trvs').all()  # Оптимизация запроса ?
    template_name = 'oktoih/voice.html'  # По умолчанию 'oktoih/oktoih_list.html'
    context_object_name = 'glas'  # По умолчанию 'object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voices_dict'] = voices_dict
        context['vozglasy'] = vozglasy
        context['voice'] = voices_dict[self.object.pk]
        return context


def send_message(request):
    if request.method == 'POST':
        form = Message(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            subject = f'{form.cleaned_data["subject"]}. Это письмо от {form.cleaned_data["sender"]}'
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['d.nikomah@yandex.ru']
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return redirect('home')
    else:
        form = Message()
    return render(request, 'oktoih/send-message.html', {'form': form})


class SundayEvang(ListView):
    model = EvangSunday
    paginate_by = 3
    template_name = 'oktoih/evang_sunday.html'


class SundayExapost(ListView):
    model = EvangSunday
    paginate_by = 3
    template_name = 'oktoih/exapost.html'


class SundayStEv(ListView):
    model = EvangSunday
    paginate_by = 3
    template_name = 'oktoih/st_ev.html'
