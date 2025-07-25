#!/usr/bin/env python3
"""
A simple hello world command line tool.
"""
import argparse
import sys


def main():
    """Main function for the hello world CLI tool."""
    parser = argparse.ArgumentParser(description='A simple hello world CLI tool')
    parser.add_argument('--version', action='version', version='1.0.0')
    parser.add_argument('name', nargs='?', default='world', help='Name to greet (default: world)')
    
    args = parser.parse_args()
    
    print(f"Hello {args.name}!")
    return 0


if __name__ == '__main__':
    sys.exit(main())