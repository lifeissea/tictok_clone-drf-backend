from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError

from users.models import User, UserFollow
from . import serializers


class Me(APIView):
    def get(self, request):
        user = request.user
        serializer = serializers.UsersSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = serializers.UsersSerializer(
            user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            user = serializer.save()
            serializer = serializers.UsersSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class Users(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = serializers.UsersSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not password:
            raise ParseError
        serializer = serializers.UsersSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer = serializers.UsersSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class PublicUser(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound
        serializer = serializers.UsersSerializer(user)
        return Response(serializer.data)


class Likes(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound
        serializer = serializers.UsersSerializer(user)
        return Response(serializer.data)

    def post(self, request, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound
        user.likes += 1
        user.save()
        serializer = serializers.UsersSerializer(user)
        return Response(serializer.data)


class Follow(APIView):
    def post(self, request, username):
        follower = request.user
        try:
            following = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound
        UserFollow.objects.get_or_create(follower=follower, following=following)
        return Response({"detail": f"You are now following {following.username}"})


class Unfollow(APIView):
    def post(self, request, username):
        follower = request.user
        try:
            following = User.objects.get(username=username)
            user_follow = UserFollow.objects.get(follower=follower, following=following)
        except User.DoesNotExist or UserFollow.DoesNotExist:
            raise NotFound
        user_follow.delete()
        return Response({"detail": f"You have unfollowed {following.username}"})


class Following(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound
        following = user.following_users.all()
        serializer = serializers.UsersSerializer(following, many=True)
        return Response(serializer.data)


class Followers(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound
        followers = user.follower_users.all()
        serializer = serializers.UsersSerializer(followers, many=True)
        return Response(serializer.data)
