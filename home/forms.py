from django import forms
from .models import Createportfolio

class TemplateForm(forms.ModelForm):
    class Meta:
        model = Createportfolio
        help_text = {
            'template_url': 'Provide A Url You Want For Your Site , Eg: hellobusiness',
            'heading': 'Website Title for Your Site: Eg:ABC PVT LTD',
            'brand_name': 'Name For Your Business/Personal Site',
            'about_image: Image URLs for About-us Section'
            'about_info': 'A Long Text Para Describing You/Your Company',
            'p1_url':'URL of your project from github/website',
            'p2_url':'URL of your project from github/website',
            'p3_url':'URL of your project from github/website',
            'p1_title':'Title of your project',
            'p2_title':'Title of your project',
            'p3_title':'Title of your project',
            'p3_content': 'content For project Section',
            'p2_content': 'content For project Section',
            'p1_content': 'content For project Section',
            'templates':'select a template',
        }
        widgets = {
            'about_info': forms.Textarea,
            'p1_content': forms.Textarea,
            'p2_content': forms.Textarea,
            'p3_content': forms.Textarea,

        }
        fields = (
            "template_url",
            "title",
            "subtitle",
            "about_image",
            "about_info",
            
            "p1_title",
            "p1_content",
            "p1_url",
            "p2_title",
            "p2_content",
            "p2_url",
            "p3_title",
            "p3_content",
            "p3_url",


            "instagram",
            "github",
            "linkedin",
            "gmail",
            "templates"
        )
        
    def save(self, commit=True):
        return super().save(commit=commit)
