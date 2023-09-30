#!/usr/bin/env python3
"""tests for picnic.py"""

import os
from subprocess import getoutput

prg = './picnic.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput(f'python3 {prg} {flag}')
        print(f'out:{out}, prg:{prg}, flag:{flag}')
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_one():
    """one item"""

    out = getoutput(f'python3 {prg} chips')
    assert out.strip() == 'You are bringing chips'


# --------------------------------------------------
def test_two():
    """two items"""

    out = getoutput(f'python3 {prg} soda "french fries"')
    assert out.strip() == 'You are bringing soda and french fries.'


# --------------------------------------------------
def test_more_than_two():
    """more than two items"""

    arg = '"potato sweet" coleslaw cupcakes "French silk pie"'
    out = getoutput(f'python3 {prg} {arg}')
    expected = ('You are bringing potato sweet, coleslaw, cupcakes, and French silk pie.')
    assert out.strip() == expected


# --------------------------------------------------
def test_two_sorted():
    """two items sorted output"""

    out = getoutput(f'python3 {prg} -s soda candy')
    assert out.strip() == 'You are bringing candy and soda.'


# --------------------------------------------------
def test_more_than_two_sorted():
    """more than two items sorted output"""

    arg = 'bananas apples dates cherries'
    out = getoutput(f'python3 {prg} {arg} --sorted')
    expected = ('You are bringing apples, bananas, cherries, and dates.')
    assert out.strip() == expected


def test_option_for_comma():
    """further 과제. oxford comma 출력하지 않게"""

    arg = 'bananas apples cherries'
    out = getoutput(f'python3 {prg} {arg} --oxfordcomma')
    expected = ('You are bringing bananas, apples and cherries.')
    assert out.strip() == expected

def test_option_mark():
    """further 과제. 기호 받아서 , 대신 mark 사용"""

    arg = 'bananas apples cherries'
    out = getoutput(f'python3 {prg} {arg} --markadded +')
    expected = ('You are bringing bananas+ apples+ and cherries.')
    assert out.strip() == expected