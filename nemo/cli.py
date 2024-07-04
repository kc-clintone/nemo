import argparse
import sys
import subprocess
from termcolor import colored
import pyfiglet
from nemo.scanners.port_scan import port_scan
from nemo.scanners.ping_sweep import ping_sweep
from nemo.monitors.bandwidth_analysis import bandwidth_analysis
from nemo.monitors.latency_measure import measure_latency
from nemo.utils.report_generator import generate_report
from nemo.alerts.alerting_system import send_alert

def print_banner():
    banner = pyfiglet.figlet_format("Ne - Mo")
    print(colored(banner, 'cyan'))

def main():
    print_banner()
    parser = argparse.ArgumentParser(
        description="Nemo Network Tool",
        usage="nemo <command> [<args>]"
    )
    subparsers = parser.add_subparsers(dest='command', metavar='command')

    # Ping sweep
    ping_parser = subparsers.add_parser('p', help='Perform a ping sweep')
    ping_parser.add_argument('-i', '--ip-range', required=True, help='IP range to scan (e.g. 192.168.1.0/24)')

    # Port scan
    port_parser = subparsers.add_parser('ps', help='Perform a port scan')
    port_parser.add_argument('-i', '--ip', required=True, help='IP address to scan')
    port_parser.add_argument('-r', '--range', required=True, help='Port range to scan (e.g. 20-80)')

    # Advanced scan
    advanced_parser = subparsers.add_parser('a', help='Perform an advanced scan')
    advanced_parser.add_argument('-i', '--ip', required=True, help='IP address to scan')
    advanced_parser.add_argument('-r', '--range', required=True, help='Port range to scan (e.g. 20-80)')
    advanced_parser.add_argument('-sV', action='store_true', help='Enable service version detection')

    # Bandwidth monitoring
    bandwidth_parser = subparsers.add_parser('b', help='Monitor bandwidth usage')
    bandwidth_parser.add_argument('-i', '--interface', required=True, help='Network interface to monitor (e.g. eth0)')

    # Latency measurement
    latency_parser = subparsers.add_parser('l', help='Measure latency to a host')
    latency_parser.add_argument('-t', '--target', required=True, help='Host to measure latency to')

    # Alert system
    alert_parser = subparsers.add_parser('al', help='Send an alert')
    alert_parser.add_argument('-m', '--message', required=True, help='Alert message to send')

    # Report generation
    report_parser = subparsers.add_parser('r', help='Generate a report')
    report_parser.add_argument('-t', '--type', required=True, choices=['ping', 'port', 'bandwidth', 'latency'], help='Type of report to generate')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    if args.command == 'p':
        handle_ping(args)
    elif args.command == 'ps':
        handle_port(args)
    elif args.command == 'a':
        handle_advanced_scan(args)
    elif args.command == 'b':
        handle_bandwidth(args)
    elif args.command == 'l':
        handle_latency(args)
    elif args.command == 'al':
        handle_alert(args)
    elif args.command == 'r':
        handle_report(args)
    else:
        parser.print_help()

def handle_ping(args):
    res = ping_sweep(args.ip_range)
    if res:
        print(colored("Ping sweep results:", 'green'))
        for ip, details in res.items():
            print(colored(f"{ip}: {details}", 'green'))
    else:
        print(colored("No hosts found or an error occurred", 'red'))
    print(colored("Ping sweep completed", 'green'))

def handle_port(args):
    res = port_scan(args.ip, args.range)
    if res:
        print(colored("Port scan results:", 'green'))
        for port in res:
            print(colored(f"Port {port['port']}: {port['state']} ({port['service']} - {port['version']})", 'green'))
    else:
        print(colored("No open ports found or scan failed", 'red'))
    print(colored("Port scan completed", 'green'))

def handle_advanced_scan(args):
    res = port_scan(args.ip, args.range, service_version=args.sV)
    if res:
        print(colored("Advanced scan results:", 'green'))
        for port in res:
            print(colored(f"Port {port['port']}: {port['state']} ({port['service']} - {port['version']})", 'green'))
    else:
        print(colored("No open ports found or scan failed", 'red'))
    print(colored("Advanced scan completed", 'green'))

def handle_bandwidth(args):
    res = bandwidth_analysis(args.interface)
    if res:
        print(colored("Bandwidth usage:", 'green'))
        print(colored(res, 'green'))
    else:
        print(colored("Failed to monitor bandwidth", 'red'))
    print(colored("Bandwidth monitoring completed", 'green'))

def handle_latency(args):
    res = measure_latency(args.target)
    if res:
        print(colored("Latency measurement:", 'green'))
        print(colored(res, 'green'))
    else:
        print(colored("Failed to measure latency", 'red'))
    print(colored("Latency measurement completed", 'green'))

def handle_alert(args):
    res = send_alert(args.message)
    if res:
        print(colored("Alert sent successfully", 'green'))
    else:
        print(colored("Failed to send alert", 'red'))

def handle_report(args):
    res = generate_report(args.type)
    if res:
        print(colored("Report generated:", 'green'))
        print(colored(res, 'green'))
    else:
        print(colored("Failed to generate report", 'red'))
    print(colored("Report generation completed", 'green'))

if __name__ == '__main__':
    main()

