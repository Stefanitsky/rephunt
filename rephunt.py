#!/usr/bin/env python3
"""
RepHunt - is a simple console app for those, who want to increase their
reputation on any of the sites, that are included in the Stack Exchange.
"""

import argparse
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


if __name__ == '__main__':
    """
    Run the program from the console
    """
    # Create argument parser
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser._optionals.title = 'Optional arguments'

    # Custom check for count value
    def check_count(count):
        c = int(count)
        if c < 1 or c > 100:
            raise argparse.ArgumentTypeError(
                'count must be greater than 0 and less than 100')
        else:
            return c

    def get_site_choices():
        api_url = 'http://api.stackexchange.com/2.2/sites'
        response = requests.get(api_url)
        return [
            item['api_site_parameter']
            for item in response.json()['items']
            if item['site_type'] == 'main_site'
        ]

    # Create arguments
    parser.add_argument(
        '-s',
        '--site',
        help='select the needed site',
        default='stackoverflow',
        choices=get_site_choices())
    parser.add_argument(
        '-c',
        '--count',
        type=check_count,
        help='select the number of questions to display',
        default=10)
    parser.add_argument(
        '-o',
        '--order',
        help='select order type',
        default='desc',
        choices=['desc', 'asc'])
    parser.add_argument(
        '--sort',
        help='select sort type',
        default='creation',
        choices=[
            'activity', 'votes', 'creation', 'hot', 'week', 'month'
        ])
    parser.add_argument(
        '-t', '--tag', help='select tag for filtering questions')
    # Parse arguments
    args = parser.parse_args()
    # Create request GET arguments
    GET_params = {}
    GET_params['site'] = args.site
    GET_params['pagesize'] = args.count
    GET_params['order'] = args.order
    GET_params['sort'] = args.sort
    if args.tag:
        GET_params['tagged'] = args.tag
    # Get questions
    questions = get_questions(**GET_params)
    # Print questions
    for question in questions[::-1]:
        print(question)