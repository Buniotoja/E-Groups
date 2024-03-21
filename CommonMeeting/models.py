from django.db import models


MEETING_STATUS=(
    ('Before', 'Before the meeting'),
    ('During', 'During the meeting'),
    ('After', 'After the meeting'),
    ('Archival', 'Meeting was archived'),
    ('Removed', 'Meeting was removed')
)

LIKES_OPTIONS=(
    ('Nothing', 'No comments added'),
    ('Like', "Good message"),
    ('Dislike', "Bad message")
)


class Meeting(models.Model):
    id=models.AutoField(primary_key=True)
    unique_code=models.CharField(max_length=20)
    status=models.CharField(max_length=30, choices=MEETING_STATUS, default='Before')
    name=models.CharField(max_length=30)
    date=models.DateTimeField()
    location=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MeetingChatMessage(models.Model):
    id=models.AutoField(primary_key=True)
    meeting_id=models.ForeignKey(Meeting, on_delete=models.CASCADE)
    author=models.CharField(max_length=30)
    text=models.TextField(max_length=255)
    date=models.DateTimeField()
    image=models.ImageField(upload_to='Images/% Y/% m/% d/', blank=True, null=True)
    url_link=models.URLField(blank=True, null=True)
    likes=models.IntegerField(default=0, blank=True, null=True)
    dislikes=models.IntegerField(default=0, blank=True, null=True)

