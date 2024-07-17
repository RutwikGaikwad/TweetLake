from django.shortcuts import render, redirect
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404

# Create your views here.

def all_tweets(request):
  tweets = Tweet.objects.all().order_by('-created_at')
  return render(request,'all_tweets.html',{'tweets':tweets})

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

def delete_tweet(request,tweet_id):
  tweet = get_object_or_404(Tweet,pk=tweet_id,user=request.user)
  if request.method == 'POST':
    tweet.delete()
    return redirect('all_tweets')
  return render(request,'confirm_delete_tweet.html',{'tweet':tweet})