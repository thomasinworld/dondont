from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.db import models
from datetime import datetime, timedelta
from .models import DoDont, DailyEntry
import json


def dashboard(request):
    """Display the main dashboard with calendar view of all journal days."""
    # Get date range for the last year
    today = timezone.now().date()
    start_date = today - timedelta(days=364)  # 365 days including today
    
    # Get all dates with entries
    dates_with_entries = DailyEntry.objects.filter(
        date__gte=start_date,
        date__lte=today
    ).values('date').distinct()
    
    # Calculate percentage for each date
    calendar_data = []
    current_date = start_date
    while current_date <= today:
        entries = DailyEntry.objects.filter(date=current_date)
        total = entries.count()
        completed = entries.filter(completed=True).count()
        percentage = (completed / total * 100) if total > 0 else 0
        
        calendar_data.append({
            'date': current_date,
            'percentage': percentage,
            'total': total,
            'completed': completed,
        })
        current_date += timedelta(days=1)
    
    # Convert calendar_data to JSON-serializable format
    import json
    calendar_data_json = json.dumps([
        {
            'date': str(item['date']),
            'percentage': float(item['percentage']),
            'total': item['total'],
            'completed': item['completed'],
        }
        for item in calendar_data
    ])
    
    context = {
        'calendar_data': calendar_data_json,
        'today': today,
    }
    return render(request, 'journal/dashboard.html', context)


def daily_journal(request, date_str=None):
    """Display the daily journal for a specific date."""
    if date_str:
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            date = timezone.now().date()
    else:
        date = timezone.now().date()
    
    # Get all active dodonts
    dodonts = DoDont.objects.filter(is_active=True)
    
    # Get or create entries for this date
    entries_data = []
    for dodont in dodonts:
        entry, created = DailyEntry.objects.get_or_create(
            dodont=dodont,
            date=date,
            defaults={'completed': False}
        )
        entries_data.append({
            'entry': entry,
            'dodont': dodont,
            'streak': dodont.get_current_streak(),
        })
    
    # Calculate percentage
    total = len(entries_data)
    completed = sum(1 for item in entries_data if item['entry'].completed)
    percentage = (completed / total * 100) if total > 0 else 0
    
    # Get previous and next dates
    prev_date = date - timedelta(days=1)
    next_date = date + timedelta(days=1)
    is_today = date == timezone.now().date()
    
    context = {
        'date': date,
        'entries_data': entries_data,
        'percentage': round(percentage, 1),
        'completed': completed,
        'total': total,
        'prev_date': prev_date,
        'next_date': next_date,
        'is_today': is_today,
    }
    return render(request, 'journal/daily_journal.html', context)


def manage_dodonts(request):
    """View to manage (add/edit/delete) dos and don'ts."""
    dodonts_do = DoDont.objects.filter(item_type='do', is_active=True)
    dodonts_dont = DoDont.objects.filter(item_type='dont', is_active=True)
    
    context = {
        'dodonts_do': dodonts_do,
        'dodonts_dont': dodonts_dont,
    }
    return render(request, 'journal/manage_dodonts.html', context)


@require_POST
def toggle_entry(request):
    """Toggle the completion status of a daily entry."""
    data = json.loads(request.body)
    entry_id = data.get('entry_id')
    
    try:
        entry = DailyEntry.objects.get(id=entry_id)
        entry.completed = not entry.completed
        entry.save()
        
        # Recalculate percentage for the day
        date_entries = DailyEntry.objects.filter(date=entry.date)
        total = date_entries.count()
        completed = date_entries.filter(completed=True).count()
        percentage = (completed / total * 100) if total > 0 else 0
        
        return JsonResponse({
            'success': True,
            'completed': entry.completed,
            'percentage': round(percentage, 1),
            'streak': entry.dodont.get_current_streak(),
        })
    except DailyEntry.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Entry not found'}, status=404)


@require_POST
def add_dodont(request):
    """Add a new do or don't item."""
    data = json.loads(request.body)
    text = data.get('text', '').strip()
    item_type = data.get('item_type', 'do')
    
    if not text:
        return JsonResponse({'success': False, 'error': 'Text is required'}, status=400)
    
    if item_type not in ['do', 'dont']:
        return JsonResponse({'success': False, 'error': 'Invalid item type'}, status=400)
    
    # Get the highest order number and add 1
    max_order = DoDont.objects.filter(item_type=item_type).aggregate(
        models.Max('order')
    )['order__max'] or 0
    
    dodont = DoDont.objects.create(
        text=text,
        item_type=item_type,
        order=max_order + 1
    )
    
    return JsonResponse({
        'success': True,
        'id': dodont.id,
        'text': dodont.text,
        'item_type': dodont.item_type,
    })


@require_POST
def delete_dodont(request, dodont_id):
    """Delete (deactivate) a do or don't item."""
    try:
        dodont = DoDont.objects.get(id=dodont_id)
        dodont.is_active = False
        dodont.save()
        return JsonResponse({'success': True})
    except DoDont.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Item not found'}, status=404)


@require_POST
def update_dodont(request, dodont_id):
    """Update a do or don't item."""
    try:
        dodont = DoDont.objects.get(id=dodont_id)
        data = json.loads(request.body)
        
        text = data.get('text', '').strip()
        if text:
            dodont.text = text
            dodont.save()
            return JsonResponse({'success': True, 'text': dodont.text})
        else:
            return JsonResponse({'success': False, 'error': 'Text is required'}, status=400)
    except DoDont.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Item not found'}, status=404)

