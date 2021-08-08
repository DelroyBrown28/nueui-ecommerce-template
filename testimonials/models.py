from django.db import models



class Testimonial(models.Model):
    full_name = models.CharField(max_length=100, blank=False, null=False)
    your_thoughts = models.CharField(max_length=450, blank=False, null=False)

    twitter_link = models.URLField(blank=True, null=True,
                                   max_length=200, default='https://twitter.com/')
    linkedin_link = models.URLField(blank=True, null=True,
                                    max_length=200, default='https://linkedin.com/')
    facebook_link = models.URLField(blank=True, null=True,
                                    max_length=200, default='https://facebook.com/')
    instagram_link = models.URLField(blank=True, null=True,
                                     max_length=200, default='https://instagram.com/')

    def __str__(self):
        return self.full_name
