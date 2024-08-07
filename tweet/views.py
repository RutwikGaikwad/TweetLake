from django.shortcuts import render, redirect
from .models import Tweet,User
from .forms import TweetForm, UserRegistrationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def all_tweets(request):
  tweets = Tweet.objects.all().order_by('-created_at')
  return render(request,'all_tweets.html',{'tweets':tweets})

@login_required
def create_tweet(request):
  if request.method == 'POST':
    form = TweetForm(request.POST,request.FILES)
    if form.is_valid():
      tweet = form.save(commit=False)
      tweet.user = request.user
      tweet.save()
      return redirect('all_tweets')
  else:
    form = TweetForm()
  return render(request,'tweet_form.html',{'form':form})

@login_required
def edit_tweet(request,tweet_id):
  tweet = get_object_or_404(Tweet,pk=tweet_id,user=request.user)
  if request.method == 'POST':
     form = TweetForm(request.POST,request.FILES,instance=tweet)
     if form.is_valid():
       tweet = form.save(commit=False)
       tweet.user = request.user
       tweet.save()
       return redirect('all_tweets')
  else:
    form = TweetForm(instance=tweet)
  return render(request,'tweet_form.html',{'form':form})

@login_required
def delete_tweet(request,tweet_id):
  tweet = get_object_or_404(Tweet,pk=tweet_id,user=request.user)
  if request.method == 'POST':
    tweet.delete()
    return redirect('all_tweets')
  return render(request,'confirm_delete_tweet.html',{'tweet':tweet})

def register(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.set_password(form.cleaned_data['password1'])
      user.save()
      login(request,user)
      return redirect('all_tweets')
  else:
    form = UserRegistrationForm()
  return render(request,'registration/register.html',{'form':form})

def search_results(request):
  query = request.GET.get('query')
  tweets = []
  if query:
    tweets = Tweet.objects.filter(text__icontains=query)
  return render(request,'search_results.html',{'tweets':tweets})