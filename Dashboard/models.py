from django.db import models
from Accounts.models import SignUpModel

    
class Vault(models.Model):
    user=models.ForeignKey(SignUpModel,on_delete=models.CASCADE,default=None)
    PLATFORM_CHOICES = [
                ("Facebook", "Facebook"),
                ("Instagram", "Instagram"),
                ("Twitter (X)", "Twitter (X)"),
                ("LinkedIn", "LinkedIn"),
                ("Snapchat", "Snapchat"),
                ("Pinterest", "Pinterest"),
                ("Reddit", "Reddit"),
                ("Quora", "Quora"),
                ("YouTube", "YouTube"),
                ("Telegram", "Telegram"),
                ("WhatsApp", "WhatsApp"),
                ("Discord", "Discord"),
                ("GitHub", "GitHub"),
                ("GitLab", "GitLab"),
                ("Bitbucket", "Bitbucket"),
                ("Gmail", "Gmail"),
                ("Yahoo Mail", "Yahoo Mail"),
                ("Outlook", "Outlook"),
                ("ProtonMail", "ProtonMail"),
                ("Zoho Mail", "Zoho Mail"),
                ("Amazon", "Amazon"),
                ("Flipkart", "Flipkart"),
                ("Myntra", "Myntra"),
                ("Snapdeal", "Snapdeal"),
                ("Netflix", "Netflix"),
                ("Hotstar (Disney+)", "Hotstar (Disney+)"),
                ("Spotify", "Spotify"),
                ("Zoom", "Zoom"),
                ("Slack", "Slack"),
                ("Medium", "Medium")
            ]

    platform = models.CharField(max_length=100, choices=PLATFORM_CHOICES)
    username = models.CharField(max_length=100)
    encrypted_password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def str(self):
        return f"{self.platform} | {self.username}"
