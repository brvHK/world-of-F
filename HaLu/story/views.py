from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class IndexView(TemplateView):

    template_name = 'story/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['chapter'] = "1st"
        ctx['items'] = 'item'
        return ctx

class First(TemplateView):

    template_name = 'story/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['chapter'] = "1st"
        ctx['items'] = 'item'
        ctx['story'] = u'''
        
            幾千年も昔。
            この世界の片隅、ひとつの街に、"時"を自由自在に操る民族がいたと云う。
            言い伝えによれば、時を進める事も、戻すことも、…またその影響範囲さえも彼らの意図通りだった。

            【在るものを無かった事】に出来る特別な力を持つ民族。
            かつての人は皆、彼らのことを【時の魔術師】と呼んだ。

            だが今となっては昔の話、その血は薄れ、時の魔法を使える人間は居なくなってしまったそうだ。
            ――ただ、今尚彼らの身に着けていた装身具を着用する文化は根強く、
            この街に住む皆が、いづれかの装身具を手にしているという。

            いつか戻る、その力を信じて――…

            Fの世界　第１章　The Fixed　World　－失われた時の世界－
        '''
        return ctx

class Second(TemplateView):

    template_name = 'story/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['chapter'] = "2nd"
        ctx['items'] = 'item'
        return ctx

class MainView(TemplateView):

    template_name = "html/index.html"

    def get_context_data(self,**kwargs):

        return None