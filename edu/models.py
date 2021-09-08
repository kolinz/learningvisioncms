from django.db import models
# accountsアプリのmodelsモジュールから、CustomUserをインポート
from accounts.models import CustomUser

# Create your models here.

class Category(models.Model):
    '''モデルクラス、リカレント教育・リスキリングのカテゴリ
    '''
    # カテゴリ名のフィールド
    title = models.CharField(
        verbose_name='カテゴリ', # フィールドのタイトル
        max_length=200)         # 最大文字数は200
    # カテゴリ概要のフィールド
    summary = models.TextField(
        verbose_name='概要',    # フィールドのタイトル
        )
    # 関連
    relation = models.ManyToManyField(
        'self',                 # 自身を対象
        verbose_name='関連',    # フィールドのタイトル
        blank=True,             # フィールド値の設定は必須でない
        null=True               # 関連がなかった場合に保存できるようにする
        )

    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        
        Returns(str):カテゴリ名
        '''
        return self.title
      


class Line(models.Model):
    '''モデルクラス、JobPost(モデル化した仕事)のビジネス分野
    '''
    # 分野名のフィールド
    title = models.CharField(
        verbose_name='分野', # フィールドのタイトル
        max_length=200)         # 最大文字数は200
    # 概要のフィールド
    summary = models.TextField(
        verbose_name='概要',    # フィールドのタイトル
        )
    # 関連
    relation = models.ManyToManyField(
        'self',                 # 自身を対象
        verbose_name='関連',    # フィールドのタイトル
        blank=True,             # フィールド値の設定は必須でない
        null=True               # 関連がなかった場合に保存できるようにする
        )

    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        
        Returns(str):分野
        '''
        return self.title


class JobPost(models.Model):
    '''モデルクラス、モデル化した職種情報
    '''
    # CustomUserモデル(のuser_id)とJobPostモデルを、1対多の関係で結び付ける
    # CustomUserが親でJobPostが子の関係となる
    user = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='作成者',
        # ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.CASCADE
        )
    # Lineモデル(のtitle)とJobPostモデルを、1対多の関係で結び付ける
    # Lineが親でJobPostが子の関係となる
    line = models.ForeignKey(
        Line,
        # フィールドのタイトル
        verbose_name='分野',
        # 業界に関連付けられた投稿データが存在する場合は、そのカテゴリを削除できないようにする
        on_delete=models.PROTECT
        )
    # タイトル用のフィールド
    title = models.CharField(
        verbose_name='タイトル', # フィールドのタイトル
        max_length=200        # 最大文字数は200
        )
    # 概要用のフィールド
    summary = models.TextField(
        verbose_name='概要',  # フィールドのタイトル
        )
    # 詳細用のフィールド
    description = models.TextField(
        verbose_name='詳細',  # フィールドのタイトル
        )
    # イメージのサムネイル
    thumbnail = models.ImageField(
        verbose_name='サムネイル', # フィールドのタイトル
        upload_to = 'jobimages'   # MEDIA_ROOT以下のphotosにファイルを保存
        )
    # 学習ロードマップ用イメージのフィールド
    image1 = models.ImageField(
        verbose_name='学習ロードマップ',    # フィールドのタイトル
        upload_to = 'jobimages',            # MEDIA_ROOT以下のjobimagesにファイルを保存  
        )
    # 外部リンク先URLのフィールド
    link = models.URLField(
        verbose_name='リンク先URL', # フィールドのタイトル
        max_length=200,             # 最大文字数は200
        blank=True,                 # フィールド値の設定は必須でない
        null=True                   # データベースにnullが保存されることを許容
        )
    # 関連Categoryモデル(のtitle)とJobPostモデルを、多対多の関係で結び付ける
    relation = models.ManyToManyField(
        Category,
        verbose_name='関連学習カテゴリ',    # フィールドのタイトル
        blank=True,                         # フィールド値の設定は必須でない
        null=True                           # データベースにnullが保存されることを許容
        )
    # キャリアプラン(関連職種)
    relationjob = models.ManyToManyField(
        'self',                         # 自身を対象
        verbose_name='キャリアプラン',  # フィールドのタイトル
        blank=True,                     # フィールド値の設定は必須でない
        null=True                       # 関連がなかった場合に保存できるようにする
        )
    # 投稿日時のフィールド
    posted_at = models.DateTimeField(
        verbose_name='投稿日時', # フィールドのタイトル
        auto_now_add=True       # 日時を自動追加
        )
    
    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        
        Returns(str):仕事情報のタイトル
        '''
        return self.title


class EduPost(models.Model):
    '''モデルクラス、リカレント教育情報およびリスキリング情報
    '''
    # CustomUserモデル(のuser_id)とEduPostモデルを、1対多の関係で結び付ける
    # CustomUserが親でEduPostが子の関係となる
    user = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='作成者',
        # ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.CASCADE
        )
    # Categoryモデル(のtitle)とEduPostモデルを、1対多の関係で結び付ける
    # Categoryが親でEduPostが子の関係となる
    category = models.ForeignKey(
        Category,
        # フィールドのタイトル
        verbose_name='カテゴリ',
        # カテゴリに関連付けられた投稿データが存在する場合は、そのカテゴリを削除できないようにする
        on_delete=models.PROTECT
        )
    # 講義名用のフィールド
    title = models.CharField(
        verbose_name='講義名', # フィールドのタイトル
        max_length=200        # 最大文字数は200
        )
    # 主催団体名用のフィールド
    organizer = models.CharField(
        verbose_name='主催団体', # フィールドのタイトル
        max_length=200        # 最大文字数は200
        )
    # 概要用のフィールド
    summary = models.TextField(
        verbose_name='概要',  # フィールドのタイトル
        )
    # 詳細用のフィールド
    description = models.TextField(
        verbose_name='詳細',  # フィールドのタイトル
        )
    # イメージのサムネイル
    thumbnail = models.ImageField(
        verbose_name='サムネイル', # フィールドのタイトル
        upload_to = 'eduimages'    # MEDIA_ROOT以下のphotosにファイルを保存
        )
    # イメージのフィールド1
    image1 = models.ImageField(
        verbose_name='イメージ1', # フィールドのタイトル
        upload_to = 'eduimages',  # MEDIA_ROOT以下のphotosにファイルを保存  
        blank=True,               # フィールド値の設定は必須でない
        null=True                 # データベースにnullが保存されることを許容
        )
    # イメージのフィールド2
    image2 = models.ImageField(
        verbose_name='イメージ2', # フィールドのタイトル
        upload_to = 'eduimages',  # MEDIA_ROOT以下のphotosにファイルを保存
        blank=True,               # フィールド値の設定は必須でない
        null=True                 # データベースにnullが保存されることを許容
        )
    # 外部リンク先URLのフィールド
    link = models.URLField(
        verbose_name='申込み先URL', # フィールドのタイトル
        max_length=200,             # 最大文字数は200
        blank=True,                 # フィールド値の設定は必須でない
        null=True                   # データベースにnullが保存されることを許容
        )
    # 受講推奨職種用のフィールド
    jobinfo = models.ManyToManyField(
        JobPost,
        verbose_name='受講推奨職種', # フィールドのタイトル
        blank=True,                  # フィールド値の設定は必須でない
        null=True                    # データベースにnullが保存されることを許容
        )
    # 投稿日時のフィールド
    posted_at = models.DateTimeField(
        verbose_name='投稿日時', # フィールドのタイトル
        auto_now_add=True       # 日時を自動追加
        )
    
    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        
        Returns(str):学習情報のタイトル
        '''
        return self.title