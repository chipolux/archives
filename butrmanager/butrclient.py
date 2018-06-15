#!/usr/bin/env python
import argparse
import json
import socket
import sys


def parse_args():
    parser = argparse.ArgumentParser(description='Client for ButrManager.')
    parser.add_argument(
        '-s', '--server',
        action='store',
        default='localhost:31337',
        help='hostname:port to connect to, defaults to localhost:31337',
    )
    parser.add_argument(
        '-t', '--command-type',
        action='store',
        choices=['list', 'online', 'start', 'stop', 'command', 'exit'],
        required=True,
        help='The type of command to execute',
    )
    parser.add_argument(
        '-p', '--password',
        action='store',
        help='Password to use when connecting to the server',
    )
    parser.add_argument(
        '-i', '--instance',
        action='store',
        help='Name of a minecraft instance on the server to manage',
    )
    parser.add_argument(
        '-c', '--command',
        action='store',
        help='If command-type is command, what to run on the instance',
    )

    args = parser.parse_args()

    instance_required = args.command_type in ['start', 'stop', 'command']
    if instance_required and args.instance is None:
        print('Must provide -i or --instance with that command-type!')
        sys.exit(1)

    if args.command_type == 'command' and args.command is None:
        print('Must provide -c or --command with that command-type!')
        sys.exit(1)

    try:
        host, port = args.server.split(':', 1)
    except ValueError:
        host = args.server
        port = 31337
    args.server = (host, int(port))

    return args


def send_message(host, port, msg, timeout=None):
    """Tries to send a message to server, returns reply"""
    s = socket.socket()
    if timeout:
        s.settimeout(timeout)

    msg = json.dumps(msg)
    try:
        s.connect((host, port))
        s.send(msg.encode('utf-8'))
        try:
            resp = json.loads(s.recv(2048).decode('utf-8'))
        except EOFError:
            resp = ['print', 'No response recieved']
        finally:
            s.close()
    except socket.error:
        resp = ['print', 'Connection to server errored out']

    return resp


def build_message(args):
    msg = [args.command_type]

    if args.command_type in ['start', 'stop', 'command']:
        msg.append(args.instance)

    if args.command_type == 'command':
        msg.append(args.command)

    if args.password:
        msg.append(args.password)

    return msg


def handle_response(resp):
    if resp[0] == 'print':
        print(resp[1])
    else:
        print('Unknown response type: {}'.format(resp))


if __name__ == '__main__':
    args = parse_args()
    msg = build_message(args)
    resp = send_message(*args.server, msg=msg)
    handle_response(resp)
