from django.forms import ModelForm
from django import forms
from django.conf import settings

from dinette.models import Ftopics ,Reply

#create a form from this Ftopics and use this when posting the a Topic
class FtopicForm(ModelForm):
    subject = forms.CharField(widget = forms.TextInput(attrs={"size": 90}))
    message = forms.CharField(widget = forms.Textarea(attrs={"cols": 90, "rows": 10}))

    class Meta:
        model = Ftopics
        fields = ('subject', 'message', 'message_markup_type', 'file' )
        
    def __init__(self, *args, **kwargs):
        super(FtopicForm, self).__init__(*args, **kwargs)
        self.fields['message_markup_type'].initial = getattr(settings, 'DEFAULT_MARKUP_TYPE', 'plain')
            

#create a form from Reply
class ReplyForm(ModelForm):
    message = forms.CharField(widget = forms.Textarea(attrs={"cols": 90, "rows": 10}))

    class Meta:
        model = Reply
        fields = ('message', 'message_markup_type', 'file')
        
    def __init__(self, *args, **kwargs):
        super(ReplyForm, self).__init__(*args, **kwargs)
        self.fields['message_markup_type'].initial = getattr(settings, 'DEFAULT_MARKUP_TYPE', 'plain')
