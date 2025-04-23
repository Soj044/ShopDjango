from tastypie.resources import ModelResource
from .authenticate import CustomAuthentication
from tastypie.authorization import Authorization
from shop.models import *


class CategoryResources(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']


class CourseResources(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        allowed_methods = ['get', 'post', 'delete']
        authentication = CustomAuthentication()
        authorization = Authorization()
        excludes = ['reviews_qty']

    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data['category_id']
        return bundle

    def dehydrate(self, bundle):
        bundle.data['category_id'] = bundle.obj.category_id
        bundle.data['category_name'] = bundle.obj.category
        return bundle

    def dehydrate_title(self, bundle):
        return bundle.data['title'].upper()
