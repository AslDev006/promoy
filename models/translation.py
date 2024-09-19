from    modeltranslation.translator import register, TranslationOptions
from .models import ServiceModel, PartnerModel


@register(ServiceModel)
class ServiceOption(TranslationOptions):
    fields = ('title', 'description')

@register(PartnerModel)
class ServiceOption(TranslationOptions):
    fields = ('position', 'opinion')