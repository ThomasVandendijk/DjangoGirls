# DjangoGirls

## Followed the tutorial from djangogirls: https://tutorial.djangogirls.org/en/ until "Forms" and did some adaptations:

### Extend the Application:
- Because the text of each article can be very long and we don’t want to clutter the homepage too much, we want to have for each post an additional summary field. On the homepage, we want for each article to see the title and the summary. Under the summary there should be a “read more” link or button, which links to another page where you will see for that blogpost the full text.
- The URL of the page containing the full text should be /post/123/full/(where 123 is the id of the post)
- Once this is done, commit all your work into the previously created git repository and push it to GitHub.

### Architecture Change:

- Django created a new way of building views. Instead of a view being a function, it can now be a class. In Django this is called “Class-Based Views”. The Django documentation contains clear examples on this.
- Refactor the view function “post_list” to a class PostListViewwhich inherits from django.views.generic.list.ListView
- Incase you’d need an in-depth view of how Class-Based viewswork, a good reference can be found at https://ccbv.co.uk/
- Once this is done, commit all your work into the previously created git repository and push it to GitHub.

### Extra variation 

- Added an extra variation which is based on real life posts where only part of the text is shown and the read more button redirects to the full article
- This way the writer doesn't have to create a summary which makes posting stories easier and faster

