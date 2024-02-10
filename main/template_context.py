from . import models

def get_logo(request):
    logo = models.AppSetting.objects.first()
    
    if logo is not None:  # Check if logo is not None
        logo_tag = logo.image_tag
    else:
        logo_tag = None  # Or any appropriate handling for the None case
    
    data = {
        'logo': logo_tag
    }
    
    return data
