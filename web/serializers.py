from rest_framework import serializers

from web.models import Chairman


class ChairmanSerializer(serializers.Serializer):
    # pk = serializers.SerializerMethodField()
    id = serializers.SerializerMethodField()
    # id = serializers.HyperlinkedIdentityField(view_name='chairman-detail', format='html')
    title = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    href = serializers.SerializerMethodField()
    img = serializers.SerializerMethodField()
    num = serializers.SerializerMethodField()
    desc = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()
    avatar = serializers.SerializerMethodField()
    class Meta:
        model = Chairman

    def get_id(self, obj):
        return obj.id

    def get_title(self, obj):
        return obj.title

    def get_name(self, obj):
        return obj.name

    def get_href(self, obj):
        return obj.href

    def get_img(self, obj):
        return obj.img

    def get_num(self, obj):
        return obj.num

    def get_desc(self, obj):
        return obj.desc

    def get_type(self, obj):
        return obj.type

    def get_avatar(self, obj):
        return obj.avatar