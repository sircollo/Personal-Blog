import unittest
from app.models import Blog
from app import db


class BlogModelTest(unittest.TestCase):
  
    def setUp(self):
      self.new_blog = Blog(title = 'This is a title',author='Me',blog_post='anything goes here')
      
      
    def tearDown(self):
      Blog.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog, Blog))

    def test_check_instance_variables(self):
      self.assertEquals(self.new_blog.title,'This is a title')
      self.assertEquals(self.new_blog.author,'Me')
      self.assertEquals(self.new_blog.blog_post,"anything goes here")

      
    def test_save_blog(self):
      self.new_blog.save_blog()
      self.assertTrue(len(Blog.query.all())>0)
        
   
    def test_get_blog_by_category(self):
      self.new_blog.save_blog()
      found_blogs = Blog.get_blog("Me")
      self.assertTrue(len(found_blogs) > 0)
