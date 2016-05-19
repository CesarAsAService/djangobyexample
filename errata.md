# Errata
Self explanatory. All that I could find.

## Page 18

The last line of the snippet will raise an error because `post` wasn't created yet. However, the `create()` method already persists data in the database.

The possibilities are:

1) instanciate `Post` model in `post` object and then use `save()` method to persist it:

```
post = Post(title='One more post', slug='one-more-post', body='Post body.', author=user)
post.save()
```

or

2) save directly from the queryset in the database using `create()`


```
Post.objects.create(title='One more post', slug='one-more-post', body='Post body.', author=user)
```
