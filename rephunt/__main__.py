"""
Run the program from the console
"""


import argparse
from . import rephunt


# Create argument parser
parser = argparse.ArgumentParser(
    description=rephunt.__doc__,
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
    response = rephunt.requests.get(api_url)
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
questions = rephunt.get_questions(**GET_params)
# Print questions
for question in questions[::-1]:
    print(question)