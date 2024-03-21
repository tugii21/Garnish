from . import views

# Define a URL pattern for the homepage
urlpatterns = [Path('',views.index, name='homepage'),]# Empty string matches the root URL
# 'views.index' refers to the index function in the views module
# 'name' parameter is set to 'homepage' for reverse URL resolution