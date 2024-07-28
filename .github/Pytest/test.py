import argparse
from unittest import mock
import pytest

def parse_arguments():
    parser = argparse.ArgumentParser(description="Telegram Bot Configuration")
    parser.add_argument('--telegram_id', type=str, required=True, help='ID of the Telegram chat')
    parser.add_argument('--telegram_token', type=str, required=True, help='Telegram Bot token')
    parser.add_argument('--telegram_report_url', type=str, help='Link for the test report')
    parser.add_argument('--telegram_custom_text', type=str, help='Custom text added to messages, use "\\n" for newlines')
    parser.add_argument('--telegram_success_sticker_id', type=str, help='File ID of the Telegram sticker for success reports')
    parser.add_argument('--telegram_fail_sticker_id', type=str, help='File ID of the Telegram sticker for failure reports')
    parser.add_argument('--telegram_disable_stickers', action='store_true', help='Disable stickers for the bot')
    parser.add_argument('--telegram_list_failed', action='store_true', help='Send failed test names')
    return parser.parse_args()

def test_required_arguments():
    test_args = ['test_script.py', '--telegram_id=12345', '--telegram_token=abcdef']
    with mock.patch('sys.argv', test_args):
        args = parse_arguments()
        assert args.telegram_id == '12345'
        assert args.telegram_token == 'abcdef'

def test_optional_arguments():
    test_args = [
        'test_script.py',
        '--telegram_id=12345',
        '--telegram_token=abcdef',
        '--telegram_report_url=https://example.com/report',
        '--telegram_custom_text=Custom\\nText',
        '--telegram_success_sticker_id=sticker_success_id',
        '--telegram_fail_sticker_id=sticker_fail_id',
        '--telegram_disable_stickers',
        '--telegram_list_failed'
    ]
    with mock.patch('sys.argv', test_args):
        args = parse_arguments()
        assert args.telegram_report_url == 'https://example.com/report'
        assert args.telegram_custom_text == 'Custom\nText'
        assert args.telegram_success_sticker_id == 'sticker_success_id'
        assert args.telegram_fail_sticker_id == 'sticker_fail_id'
        assert args.telegram_disable_stickers is True
        assert args.telegram_list_failed is True

def test_missing_required_arguments():
    test_args = ['test_script.py']
    with mock.patch('sys.argv', test_args), pytest.raises(SystemExit):
        parse_arguments()
