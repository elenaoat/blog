from modeltranslation.translator import translator, TranslationOptions
from blogengine.models import Post

class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'teaser')

translator.register(Post, PostTranslationOptions)