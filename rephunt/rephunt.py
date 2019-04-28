#!/usr/bin/env python3
"""
RepHunt - is a reputation enhancer for Stack Exchange.
"""

import requests
from html import unescape
from datetime import datetime

# Stack Exchange API URL
api_url = 'http://api.stackexchange.com/2.2/questions'


class Question:
    """
    Question class that contains information about the question.
    """

    def __init__(self, data):
        """
        Initialisation method.
        """
        self.__data = data
        self.title = unescape(data['title'])
        self.creation_date = datetime.fromtimestamp(
            data['creation_date'])
        self.votes = data['score']
        self.answers = data['answer_count']
        self.views = data['view_count']
        self.answered = data['is_answered']
        self.link = data['link']
        self.tags = data['tags']

    def formatted_is_answered(self):
        """
        Returns the answered bool in a human readable form.
        """
        return 'yes' if self.answered else 'no'

    def __str__(self):
        """
        Returns the question in a human readable form.
        """
        output_format = """
        Title: {}
        Asked: {}
        Stats: {} votes | {} answers | {} views | answered: {}
        Tags: {}
        Link: {}
        """
        return output_format.format(
            self.title, self.get_formatted_time(),
            self.votes, self.answers, self.views,
            self.formatted_is_answered(), ', '.join(
                self.tags), self.link)

    def get_formatted_time(self):
        """
        Returns the elapsed time of the created question
        in a readable form.
        """
        time_delta = datetime.now() - self.creation_date
        days = time_delta.days
        if days < 1:
            hours = time_delta.seconds // 3600
            if hours < 1:
                minutes = (time_delta.seconds // 60) % 60
                return '{} minutes ago'.format(minutes)
            else:
                return '{} hours ago'.format(hours)
        else:
            return '{} days ago'.format(days)


def get_questions(**kwargs):
    """
    Get response with passed args and return questions list
    """
    response = requests.get(api_url, params=kwargs)
    if response.status_code != 200:
        raise requests.HTTPError(response.text)
    else:
        return [
            Question(question_data)
            for question_data in response.json()['items']
        ]