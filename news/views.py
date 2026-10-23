from django.shortcuts import render

# Create your views here.
def news_feed(request):
    context = {
        'reporter_name' : 'Farzeen Ali',
        'is_editor' : True,
        'news_list' : [
            {
                'title': 'AI Revolution in 2026',
                'category': 'Technology',
                'views' : 12500,
                'breaking': True
            },
            {
                'title': 'Accounting',
                'category': 'Finance',
                'views' : 600,
                'breaking': False
            },
            {
                'title': 'Cricket Match',
                'category': 'Sports',
                'views' : 300,
                'breaking': False
            },
        ]
    }
    return render(request, 'news/feed.html', context)