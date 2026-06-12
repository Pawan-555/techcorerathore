from django.shortcuts import render

def home_view(request):
    context = {
        'articles': [
            {'category': 'Cloud', 'comment_count': 5, 'title': 'Future of AWS and Cloud Computing', 'published_date': 'June 11, 2026'},
            {'category': 'AI', 'comment_count': 12, 'title': 'How Generative AI is Changing DevOps', 'published_date': 'June 10, 2026'},
        ],
        'faqs': [
            {'number': 1, 'question': 'What services do you provide?', 'answer': 'We offer cloud infrastructure, custom software, and digital transformation consulting.'},
            {'number': 2, 'question': 'How can I schedule a consultation?', 'answer': 'You can use the consultation form at the bottom of the page.'},
        ]
    }
    # Yahan 'home.html' render hona chahiye kyuki file ka naam home.html hai
    return render(request, 'home.html', context)