from rest_framework import serializers
from .models import Vote, PollSubject, Poll

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('id', 'poll', 'subject', 'user')

class PollSubjectSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True)

    class Meta:
        model = PollSubject
        fields = ('id', 'name', 'votes', 'total_votes')

    def get_total_votes(self, subject):
        return subject.votes.count()



