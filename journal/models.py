from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta


class DoDont(models.Model):
    """Model for a Do or Don't item that appears in daily journals."""
    ITEM_TYPE_CHOICES = [
        ('do', 'Do'),
        ('dont', "Don't"),
    ]
    
    text = models.CharField(max_length=200)
    item_type = models.CharField(max_length=5, choices=ITEM_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'created_at']
    
    def __str__(self):
        return f"[{self.get_item_type_display()}] {self.text}"
    
    def get_current_streak(self):
        """Calculate the current streak for this item."""
        today = timezone.now().date()
        streak = 0
        current_date = today
        
        # Check backwards from today
        while True:
            try:
                entry = DailyEntry.objects.get(
                    dodont=self,
                    date=current_date
                )
                if entry.completed:
                    streak += 1
                    current_date -= timedelta(days=1)
                else:
                    break
            except DailyEntry.DoesNotExist:
                break
        
        return streak


class DailyEntry(models.Model):
    """Model for tracking whether a DoDont was completed on a specific date."""
    dodont = models.ForeignKey(DoDont, on_delete=models.CASCADE, related_name='entries')
    date = models.DateField()
    completed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-date', 'dodont__order']
        unique_together = ['dodont', 'date']
        verbose_name_plural = 'Daily entries'
    
    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{self.date} - {self.dodont.text} ({status})"

