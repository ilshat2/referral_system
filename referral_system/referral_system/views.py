import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from referral_system.models import User, Referral
from referral_system.serializers import UserSerializer


class AuthView(APIView):

    def post(self, request):
        phone = request.data.get("phone")
        if not phone:

            return Response(
                {"error": "Phone number is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        user, created = User.objects.get_or_create(phone=phone)
        time.sleep(2)

        return Response(
            {"message": "Verification code sent"},
            status=status.HTTP_200_OK
        )


class VerifyCodeView(APIView):

    def post(self, request):
        phone = request.data.get("phone")
        if not User.objects.filter(phone=phone).exists():

            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            {"message": "Verified successfully"},
            status=status.HTTP_200_OK
        )


class ProfileView(APIView):

    def get(self, request, phone):
        user = User.objects.filter(phone=phone).first()
        if not user:

            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = UserSerializer(user)

        return Response(serializer.data)

    def post(self, request, phone):
        user = User.objects.filter(phone=phone).first()
        invite_code = request.data.get("invite_code")
        if not user or not invite_code:

            return Response(
                {"error": "Invalid data"},
                status=status.HTTP_400_BAD_REQUEST
            )
        inviter = User.objects.filter(invite_code=invite_code).first()
        if not inviter or user.activated_invite_code:

            return Response(
                {"error": "Invalid or already activated invite code"},
                status=status.HTTP_400_BAD_REQUEST
            )
        Referral.objects.create(inviter=inviter, invited=user)
        user.activated_invite_code = invite_code
        user.save()

        return Response(
            {"message": "Invite code activated successfully"},
            status=status.HTTP_200_OK
        )
