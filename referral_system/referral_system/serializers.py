from rest_framework import serializers
from .models import User, Referral


class UserSerializer(serializers.ModelSerializer):
    referred_by = serializers.SerializerMethodField()
    referrals = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'phone',
            'invite_code',
            'activated_invite_code',
            'referred_by',
            'referrals'
        ]

    def get_referred_by(self, obj):
        return obj.activated_invite_code

    def get_referrals(self, obj):
        return [ref.invited.phone for ref in obj.invited_users.all()]
