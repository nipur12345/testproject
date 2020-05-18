from rest_framework import serializers
from .models import Members,Activity_periods
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Members
        fields=('member_id','realname','activity_periods' )
        read_only_fields=('activity_periods',)
        depth=1
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Activity_periods
        fields=('start_time','end_time')