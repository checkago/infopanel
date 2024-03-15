from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from panel.models import Header, BackGround, Section, Pravila, PushkinCard, Reglament, Qr


class KrujokAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(config_name='awesome_ckeditor'))

    class Meta:
        verbose_name = 'Текст'
        model = Section
        fields = '__all__'


class KrujokAdmin(admin.ModelAdmin):
    form = KrujokAdminForm
    list_display = ('name',)


class PravilaAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(config_name='awesome_ckeditor'))

    class Meta:
        verbose_name = 'Текст'
        model = Pravila
        fields = '__all__'


class PravilaAdmin(admin.ModelAdmin):
    form = PravilaAdminForm
    list_display = ('name',)


class PushkinCardAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(config_name='awesome_ckeditor'))

    class Meta:
        verbose_name = 'Текст'
        model = PushkinCard
        fields = '__all__'


class PushkinCardAdmin(admin.ModelAdmin):
    form = PushkinCardAdminForm
    list_display = ('name',)


class ReglamentAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(config_name='awesome_ckeditor'))

    class Meta:
        verbose_name = 'Текст'
        model = Reglament
        fields = '__all__'


class ReglamentAdmin(admin.ModelAdmin):
    form = ReglamentAdminForm
    list_display = ('name',)


admin.site.register(Header)
admin.site.register(BackGround)
admin.site.register(Qr)
admin.site.register(Pravila, PravilaAdmin)
admin.site.register(PushkinCard, PushkinCardAdmin)
admin.site.register(Reglament, ReglamentAdmin)
admin.site.register(Section, KrujokAdmin)


