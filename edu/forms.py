from django.forms import ModelForm, fields
from .models import EduPost, JobPost

class EduPostForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    class Meta:
        '''ModelFormのインナークラス

        Attributes:
            model: モデルのクラス
            fields: フォームで使用するモデルのフィールドを指定
        '''
        model = EduPost
        fields = ['category', 'title', 'organizer', 'summary', 'description', 'jobinfo', 'thumbnail', 'image1', 'image2', 'link']

class JobPostForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    
    class Meta:
        '''ModelFormのインナークラス

        Attributes:
            model: モデルのクラス
            fields: フォームで使用するモデルのフィールドを指定
        '''
        model = JobPost
        fields = ['line', 'title', 'summary', 'description', 'thumbnail', 'image1', 'link', 'relation']