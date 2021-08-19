from django.db import models


class Testimonial(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.CharField(max_length=100, blank=True, null=True)
    your_thoughts = models.TextField(max_length=1000, blank=False, null=False)
    # upload_image = models.ImageField(blank=True, null=True, upload_to='testimonial_submitted_images',
    #                                  help_text='Show us an image of your purchased product')

    twitter_link = models.URLField(blank=True, null=True,
                                   max_length=200, default='')
    linkedin_link = models.URLField(blank=True, null=True,
                                    max_length=200, default='')
    facebook_link = models.URLField(blank=True, null=True,
                                    max_length=200, default='')
    instagram_link = models.URLField(blank=True, null=True,
                                     max_length=200, default='')
    other_social_media_link = models.URLField(blank=True, null=True,
                                              max_length=200, default='')

    def __str__(self):
        return self.name
