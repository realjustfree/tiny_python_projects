#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import csv
import io
import random
import re
from pprint import pprint
from tabulate import tabulate

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create Workout Of (the) Day (WOD)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='CSV input file of exercises',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default='inputs/exercises.csv')

    parser.add_argument('-s',
                        '--seed',
                        metavar="seed",
                        help='Random seed',
                        type=int,
                        default=None)

    parser.add_argument('-n',
                        '--num',
                        metavar="exercises",
                        help='Number of exercises',
                        type=int,
                        default=4)

    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps',
                        type=bool,
                        default=False)


    return parser.parse_args()


def read_csv(fh):
    """read the csv input"""
    reader = csv.DictReader(fh, delimiter=',')
    exercise = []

    for rec in reader:
        name, reps = rec['exercise'], rec['reps']
        reps_match = re.match('(\d+)-(\d+)', reps)
        low, high = int(reps_match.group(1)), int(reps_match.group(2))
        exercise.append((name, low, high))

    return exercise


def test_read_csv():
    """test read_csv"""

    text = io.StringIO('exercise,reps\nBurpees,20-50\nSitups,40-100')
    assert read_csv(text) == [('Burpees', 20, 50), ('Situps', 40, 100)]


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    random.seed(args.seed)

    exercises = read_csv(args.file)
    choose_exercises = random.sample(exercises, k=args.num)

    list_exercises = []
    for i in choose_exercises:
        num_reps = random.randint(i[1], i[2])
        if args.easy:
            num_reps = int(num_reps)
        list_exercises.append((i[0], num_reps))

    print(tabulate(list_exercises, headers=('Exersices', 'Reps')))








# --------------------------------------------------
if __name__ == '__main__':
    main()
