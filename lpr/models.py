from django.db import models

class lpr(models.Model):
    ogml = models.BooleanField(blank=True, default=False)
    md = models.BooleanField(blank=True, default=False)
    revisions = models.BooleanField()
    client = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    prospect = models.CharField(max_length=255)
    lessor = models.CharField(max_length=255)
    lessor_address1 = models.CharField(max_length=255)
    lessor_address2 = models.CharField(max_length=255)
    lessor_city = models.CharField(max_length=255)
    lessor_state = models.CharField(max_length=255)
    lessor_zip = models.CharField(max_length=255)
    lessor_phone = models.CharField(max_length=255)
    lessor_email = models.CharField(max_length=255)
    lessor_ssntin = models.CharField(max_length=255)
    lessor_interest = models.CharField(max_length=255)
    royalty = models.DecimalField(max_digits=4, blank=True, decimal_places=4)
    gross_acres = models.DecimalField(max_digits=10, decimal_places=3)
    net_acres = models.DecimalField(max_digits=10, decimal_places=3)
    bonus_per_Acre = models.DecimalField(max_digits=10, decimal_places=2)
    total_bonus = models.DecimalField(max_digits=15, decimal_places=2)
    check_number = models.CharField(max_length=255)
    legal = models.TextField()
    drilling_platform = models.CharField(max_length=255)
    effective_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)
    primary_term_in_years = models.IntegerField(blank=True)
    extension_term_in_years = models.IntegerField(blank=True)
    ogml_only = models.BooleanField(blank=True, default=False)
    horziontal_pugh = models.BooleanField(blank=True, default=False)
    vertical_pugh = models.BooleanField(blank=True, default=False)
    depth_limitation = models.BooleanField(blank=True, default=False)
    cont_dev = models.BooleanField(blank=True, default=False)
    cont_dev_period_days = models.IntegerField(blank=True)
    damages = models.BooleanField(blank=True, default=False)
    swd = models.BooleanField(blank=True, default=False)
    orri_wi = models.BooleanField(blank=True, default=False)
    no_surface = models.BooleanField(blank=True, default=False)
    specific_surface = models.BooleanField(blank=True, default=False)
    free_royalty = models.BooleanField(blank=True, default=False)
    pooling_limit = models.BooleanField(blank=True, default=False)
    max_pooling_acreage = models.CharField(blank=True, max_length=255, default=1280)
    min_pooling_acreage = models.CharField(blank=True, max_length=255)
    consent_assign = models.BooleanField(blank=True, default=False)
    shut_in = models.BooleanField(blank=True, default=False)
    water_well = models.BooleanField(blank=True, default=False)
    lease_image = models.FileField(upload_to='uploads/lprs/leases/')
    memo_image = models.FileField(upload_to='uploads/lprs/memos/')
    payment_image = models.FileField(upload_to='uploads/lprs/checks/')
    plat_image = models.FileField(upload_to='uploads/lprs/plats/')
    source_deed_image = models.FileField(upload_to='uploads/lprs/source_deeds/')
    mor_image = models.FileField(upload_to='uploads/lprs/mors/')
    runsheet_image = models.FileField(upload_to='uploads/lprs/runseets/')
    w9_image = models.FileField(upload_to='uploads/lprs/w9s/')
    curative_image = models.FileField(upload_to='uploads/lprs/curative/')
    timestamp = models.DateTimeField()

    def fields_required(self, fields):
        for field in fields:
            if not self.cleaned_data.get(field, ''):
                msg = forms.ValidationError("This field is required.")
                self.add_error(field, msg)

    def clean(self):
        ogml = self.cleaned_data.get('ogml')
        if ogml:
            self.fields_required(['royalty',
            'primary_term_in_years',
            'extension_term_in_years',
            'expiration_date'
            ])
        else:
            self.cleaned_data['royalty',
            'primary_term_in_years',
            'extension_term_in_years',
            'expiration_date'
            ] = ''
        revisions = self.cleaned_data.get('revisions')
        if revisions:
            self.fields_required(['ogml_only',
                                'horziontal_pugh',
                                'vertical_pugh',
                                'depth_limitation',
                                'cont_dev',
                                'damages',
                                'swd',
                                'orri_wi',
                                'no_surface',
                                'specific_surface',
                                'free_royalty',
                                'pooling_limit',
                                'max_pooling_acreage',
                                'min_pooling_acreage',
                                'consent_assign',
                                'shut_in',
                                'water_well',
            ])
        else:
            self.cleaned_data['ogml_only',
                                'horziontal_pugh',
                                'vertical_pugh',
                                'depth_limitation',
                                'cont_dev',
                                'damages',
                                'swd',
                                'orri_wi',
                                'no_surface',
                                'specific_surface',
                                'free_royalty',
                                'pooling_limit',
                                'max_pooling_acreage',
                                'min_pooling_acreage',
                                'consent_assign',
                                'shut_in',
                                'water_well',

            ] = ''
            
