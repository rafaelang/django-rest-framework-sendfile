# django-rest-framework-sendfile
Generic API View to create a method file/image to post files to a field model

#Usage

- model

```python
def imgage_path(instance, filename):
    return os.path.join(u'profile',str(instance.id), u'image', filename)

class Profile(models.Model):
    real_name = models.CharField(max_length=60, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    imgage = models.ImageField(verbose_name=u'Profile Image', upload_to=imgage_path, null=True, blank=True)

    class Meta:
        ordering = ('-updated',)

    def __str__(self):
        return u'%s' %(self.real_name)
```

- serializer
```python
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'real_name',)
        read_only_fields = ('image',)
```        
- view
```python
from sendfile.views import UpdateUploadMixin

class ProfileViewSet(ModelViewSet, UpdateUploadMixin):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    upload_fields = ('image',)
```    
-Thanks

Inspired at http://www.machinalis.com/blog/image-fields-with-django-rest-framework/

Based on http://www.django-rest-framework.org/
