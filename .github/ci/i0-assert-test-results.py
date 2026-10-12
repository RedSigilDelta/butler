#!/usr/bin/env python3
"""Fail closed on missing, failed, errored or skipped JUnit report cases (I0)."""
import argparse
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def audit(directory: Path) -> dict:
    if not directory.is_dir():
        raise ValueError(f"No test result directory: {directory}")
    xmls = sorted(directory.glob('TEST-*.xml'))
    if not xmls:
        raise ValueError(f"No TEST-*.xml reports: {directory}")
    totals = {k: 0 for k in ('tests', 'failures', 'errors', 'skipped')}
    for path in xmls:
        try:
            root = ET.parse(path).getroot()
        except ET.ParseError as exc:
            raise ValueError(f"Invalid JUnit XML: {path}") from exc
        suites = [root] if root.tag == 'testsuite' else root.findall('./testsuite')
        if not suites:
            raise ValueError(f"No test suites in {path}")
        for suite in suites:
            for key in totals:
                try:
                    n = int(suite.attrib[key])
                except (ValueError, KeyError) as exc:
                    raise ValueError(f"Invalid '{key}' count in {path}") from exc
                if n < 0:
                    raise ValueError(f"Negative '{key}' count in {path}")
                totals[key] += n
            actual = len(suite.findall('.//testcase'))
            if actual != int(suite.attrib['tests']):
                raise ValueError(f"JUnit declared cases disagree with testcase elements: {path}")
    if totals['tests'] < 1:
        raise ValueError('No tests executed')
    if any(totals[k] for k in ('failures', 'errors', 'skipped')):
        raise ValueError(f"Unaccepted non-PASS test outcomes: {totals}")
    return totals


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--dir', required=True, type=Path)
    args = p.parse_args()
    try:
        result = audit(args.dir)
    except ValueError as exc:
        print(f'I0 fail-closed JUnit audit: FAIL: {exc}', file=sys.stderr)
        return 1
    print(f'I0 fail-closed JUnit audit: PASS: {result}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
