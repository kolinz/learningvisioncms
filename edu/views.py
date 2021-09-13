from django.shortcuts import render
# django.views.genericからTemplateView、ListView、CreateViewをインポート
from django.views.generic import TemplateView, ListView, DetailView, CreateView
# django.urlsからreverse_lazyをインポート
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
# modelsモジュールからモデルEduPostとJobPostをインポート
from .models import EduPost, JobPost, Category
# formsモジュールからPhotoPostForm, JobPostFormをインポート
from .forms import EduPostForm, JobPostForm
# method_decoratorをインポート
from django.utils.decorators import method_decorator
# login_requiredをインポート
from django.contrib.auth.decorators import login_required


# Create your views here.

class IndexView(ListView):
    '''トップページのビュー
    '''
    #　index.htmlをレンダリング
    template_name = 'index.html'

    # モデルEduPostのオブジェクト、並び替え。投稿日順
    queryset = EduPost.objects.order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 6

class CategoryListView(ListView):
    '''学習別カテゴリの一覧ビュー
    '''
    #　cat_list.htmlをレンダリング
    template_name = 'cat_list.html'

    # モデルCategoryのオブジェクト、並び替え。タイトル順
    queryset = Category.objects.order_by('-title')
    # 1ページに表示するレコードの件数
    paginate_by = 6

# デコレーターにより、CreateEduViewへのアクセスはログインユーザーに限定される
# ログイン状態でなければsettings.pyのLOGIN_URLにリダイレクトされる
@method_decorator(login_required, name='dispatch')
class CreateEduView(CreateView):
    '''学習情報の投稿ページのビュー
    
    EduPostFormで定義されているモデルとフィールドと連携して
    投稿データをデータベースに登録する
    
    Attributes:
      form_class: モデルとフィールドが登録されたフォームクラス
      template_name: レンダリングするテンプレート
      success_url: データベスへの登録完了後のリダイレクト先
    '''
    # forms.pyのEduPostFormをフォームクラスとして登録
    form_class = EduPostForm
    # レンダリングするテンプレート
    template_name = "post_edu.html"
    # フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('edu:post_done')
    
    def form_valid(self, form):
        '''CreateViewクラスのform_valid()をオーバーライド
        
        フォームのバリデーションを通過したときに呼ばれる
        フォームデータの登録をここで行う
        
        parameters:
          form(django.forms.Form):
            form_classに格納されているEduPostFormオブジェクト
        Return:
          HttpResponseRedirectオブジェクト:
            スーパークラスのform_valid()の戻り値を返すことで、
            success_urlで設定されているURLにリダイレクトさせる
        '''
        # commit=FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        # 投稿ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        # 投稿データをデータベースに登録
        postdata.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)

# デコレーターにより、CreateJobEduViewへのアクセスはログインユーザーに限定される
# ログイン状態でなければsettings.pyのLOGIN_URLにリダイレクトされる
@method_decorator(login_required, name='dispatch')
class CreateJobEduView(CreateView):
    '''職業別学習情報の投稿ページのビュー
    
    EduPostFormで定義されているモデルとフィールドと連携して
    投稿データをデータベースに登録する
    
    Attributes:
      form_class: モデルとフィールドが登録されたフォームクラス
      template_name: レンダリングするテンプレート
      success_url: データベスへの登録完了後のリダイレクト先
    '''
    # forms.pyのEduPostFormをフォームクラスとして登録
    form_class = JobPostForm
    # レンダリングするテンプレート
    template_name = "post_job.html"
    # フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('edu:post_job_done')
    
    def form_valid(self, form):
        '''CreateViewクラスのform_valid()をオーバーライド
        
        フォームのバリデーションを通過したときに呼ばれる
        フォームデータの登録をここで行う
        
        parameters:
          form(django.forms.Form):
            form_classに格納されているEduPostFormオブジェクト
        Return:
          HttpResponseRedirectオブジェクト:
            スーパークラスのform_valid()の戻り値を返すことで、
            success_urlで設定されているURLにリダイレクトさせる
        '''
        # commit=FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        # 投稿ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        # 投稿データをデータベースに登録
        postdata.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    '''投稿完了ページのビュー

    Attributes:
        template_name: レンダリングするテンプレート
    '''
    #post_success.htmlをレンダリング
    template_name = 'post_success.html'
    
class CategoryView(ListView):
    '''カテゴリページのビュー
    
    Attributes:
      template_name: レンダリングするテンプレート
      paginate_by: 1ページに表示するレコードの件数
    '''
    # index.htmlをレンダリングする
    template_name ='category_top.html'
    # 1ページに表示するレコードの件数
    paginate_by = 6

    def get_queryset(self):
      '''クエリを実行する
      
      self.kwargsの取得が必要なため、クラス変数querysetではなく、get_queryset（）のオーバーライドによりクエリを実行する
      
      Returns:
        クエリによって取得されたレコード
      '''
      # print(self.kwargs)
      # print(type(self))
      # print(self.request.session)
      
      # self.kwargsでキーワードの辞書を取得し、
      # categoryキーの値(Categorysテーブルのid)を取得
      category_id = self.kwargs['category']
      # filter(フィールド名=id)で絞り込む
      categories = EduPost.objects.filter(
        category=category_id).order_by('-posted_at')
      # クエリによって取得されたレコードを返す
      return categories

class DetailView(DetailView):
    '''詳細ページのビュー
    
    投稿記事の詳細を表示するので、DetailViewを継承する
    Attributes:
      template_name: レンダリングするテンプレート
      model: モデルのクラス
    '''
  # detail.htmlをレンダリングする
    template_name ='detail.html'
  # クラス変数modelにモデルEduPostを設定
    model = EduPost


class ModelIndexView(ListView):
    '''職業モデル情報のトップページのビュー
    '''
    #　index.htmlをレンダリング
    template_name = 'model_index.html'

    # モデルJobPostのオブジェクト、並び替え。投稿日順
    queryset = JobPost.objects.order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 6

class ModelDetailView(DetailView):
    '''職業モデル詳細ページのビュー
    
    投稿記事の詳細を表示するので、DetailViewを継承する
    Attributes:
      template_name: レンダリングするテンプレート
      model: モデルのクラス
    '''
  # model_detail.htmlをレンダリングする
    template_name ='model_detail.html'
  # クラス変数modelにモデルEduPostを設定
    model = JobPost

class LineView(ListView):
    '''Line(分野)ページのビュー
    
    Attributes:
      template_name: レンダリングするテンプレート
      paginate_by: 1ページに表示するレコードの件数
    '''
    # index.htmlをレンダリングする
    template_name ='line_top.html'
    # 1ページに表示するレコードの件数
    paginate_by = 6

    def get_queryset(self):
      '''クエリを実行する
      
      self.kwargsの取得が必要なため、クラス変数querysetではなく、get_queryset（）のオーバーライドによりクエリを実行する
      
      Returns:
        クエリによって取得されたレコード
      '''
      # print(self.kwargs)
      # print(type(self))
      # print(self.request.session)
      
      # self.kwargsでキーワードの辞書を取得し、
      # lineキーの値(Categorysテーブルのid)を取得
      line_id = self.kwargs['line']
      # filter(フィールド名=id)で絞り込む
      lines = JobPost.objects.filter(
        line=line_id).order_by('-posted_at')
      # クエリによって取得されたレコードを返す
      return lines

class MypageEduView(ListView):
    '''マイページのビュー
    
    Attributes:
      template_name: レンダリングするテンプレート
      paginate_by: 1ページに表示するレコードの件数
    '''
    # mypage.htmlをレンダリングする
    template_name ='mypage_edupost.html'
    # 1ページに表示するレコードの件数
    paginate_by = 6

    def get_queryset(self):
      '''クエリを実行する
      
      self.kwargsの取得が必要なため、クラス変数querysetではなく、get_queryset（）のオーバーライドによりクエリを実行する
      
      Returns:
        クエリによって取得されたレコード
      '''
      # filter(userフィールド=userオブジェクト)で絞り込む
      queryset = EduPost.objects.filter(
        user=self.request.user).order_by('-posted_at')
      # クエリによって取得されたレコードを返す
      return queryset

class MypageJobView(ListView):
    '''マイページのビュー
    
    Attributes:
      template_name: レンダリングするテンプレート
      paginate_by: 1ページに表示するレコードの件数
    '''
    # mypage.htmlをレンダリングする
    template_name ='mypage_jobpost.html'
    # 1ページに表示するレコードの件数
    paginate_by = 6

    def get_queryset(self):
      '''クエリを実行する
      
      self.kwargsの取得が必要なため、クラス変数querysetではなく、get_queryset（）のオーバーライドによりクエリを実行する
      
      Returns:
        クエリによって取得されたレコード
      '''
      # filter(userフィールド=userオブジェクト)で絞り込む
      queryset = JobPost.objects.filter(
        user=self.request.user).order_by('-posted_at')
      # クエリによって取得されたレコードを返す
      return queryset

class EduPostDeleteView(DeleteView):
  '''レコードの削除を行うビュー
  Attributes:
   model: モデル
   temaplate_name: レンダリングするテンプレート
   paginate_by: 1ページに表示するレコードの件数
   success_url: 削除完了後のリダイレクト先のURL
  '''
  model = EduPost
  template_name = 'post_delete.html'
  success_url = reverse_lazy('edu:mypage_edu')

  def delete(self, request, *args, **kwargs):
      '''レコードの削除を行う
      
      Parameters:
        self: PhotoDeleteViewオブジェクト
        request: WSGIRequest(HttpRequest)オブジェクト
        args: 引数として渡される辞書(dict)
        kwargs: キーワード付きの辞書(dict)
                {'pk': 21}のようにレコードのidが渡される
      
      Returns:
        HttpResponseRedirect(success_url)を返して
        success_urlにリダイレクト
      '''
      # スーパークラスのdelete()を実行
      return super().delete(request, *args, **kwargs)

class JobPostDeleteView(DeleteView):
  '''レコードの削除を行うビュー
  Attributes:
   model: モデル
   temaplate_name: レンダリングするテンプレート
   paginate_by: 1ページに表示するレコードの件数
   success_url: 削除完了後のリダイレクト先のURL
  '''
  model = JobPost
  template_name = 'model_delete.html'
  success_url = reverse_lazy('edu:mypage_job')

  def delete(self, request, *args, **kwargs):
      '''レコードの削除を行う
      
      Parameters:
        self: PhotoDeleteViewオブジェクト
        request: WSGIRequest(HttpRequest)オブジェクト
        args: 引数として渡される辞書(dict)
        kwargs: キーワード付きの辞書(dict)
                {'pk': 21}のようにレコードのidが渡される
      
      Returns:
        HttpResponseRedirect(success_url)を返して
        success_urlにリダイレクト
      '''
      # スーパークラスのdelete()を実行
      return super().delete(request, *args, **kwargs)
