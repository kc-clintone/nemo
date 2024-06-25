import argparse
import sys
from termcolor import colored
import pyfiglet
from netmon.scanners.ping_sweep import ping_sweep
from netmon.scanners.port_scan import port_scan
from netmon.scanners.advanced_scan import advanced_scan
from netmon.monitors.bandwidth_analysis import bandwidth_analysis
from netmon.monitors.latency_measure import measure_latency
from netmon.alerts.alerting_system import send_alert
from netmon.utils.report_generator import generate_report

def print_banner():
    banner = pyfiglet.figlet_format("NetMon")
    print(colored(banner, 'cyan'))

def main():
    print_banner()

    parser = argparse.ArgumentParser(
        description="Network Monitoring CLI Tool",
        usage="""netmon <command> [<args>]

Available commands:
   ping       Perform a ping sweep
   port       Perform a port scan
   advanced   Perform an advanced scan
   bandwidth  Monitor bandwidth usage
   latency    Measure latency to a host
   alert      Send an alert
   report     Generate a report
"""
    )
    parser.add_argument('command', help='Subcommand to run')

    args = parser.parse_args(sys.argv[1:2])

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == 'ping':
        handle_ping(sys.argv[2:])
    elif args.command == 'port':
        handle_port(sys.argv[2:])
    elif args.command == 'advanced':
        handle_advanced(sys.argv[2:])
    elif args.command == 'bandwidth':
        handle_bandwidth(sys.argv[2:])
    elif args.command == 'latency':
        handle_latency(sys.argv[2:])
    elif args.command == 'alert':
        handle_alert(sys.argv[2:])
    elif args.command == 'report':
        handle_report(sys.argv[2:])
    else:
        print(colored(f"Unknown command: {args.command}", 'red'))
        parser.print_help()
        sys.exit(1)

def handle_ping(args):
    parser = argparse.ArgumentParser(description='Perform a ping sweep')
    parser.add_argument('ip_range', help='IP range to scan (e.g. 192.168.1.0/24)')
    ping_args = parser.parse_args(args)
    res = ping_sweep(ping_args)
    if res:
        print(colored(res, 'red'))
        for k in res:
            print(colored(k, 'red'))
    else:
        print(colored("An error occured", red))
    print(colored("Ping sweep completed", 'green'))


def handle_port(args):
    parser = argparse.ArgumentParser(description='Perform a port scan')
    parser.add_argument('ip', help='IP address to scan')
    parser.add_argument('port_range', help='Port range to scan (e.g. 20-80)')
    port_args = parser.parse_args(args)
    port_range = list(map(int, port_args.port_range.split('-')))
    open_ports = port_scan(port_args.ip, port_range)
    if open_ports:
        print(colored(f"Open ports on {port_args.ip}:", 'green'))
        for port in open_ports:
            print(colored(f"Port {port['port']}: {port['state']} ({port['service']} - {port['version']})", 'green'))
    else:
        print(colored("No open ports found or scan failed.", 'red'))


def handle_advanced(args):
    parser = argparse.ArgumentParser(description='Perform an advanced scan')
    parser.add_argument('ip', help='IP address to scan')
    advanced_args = parser.parse_args(args)
    scan_results = advanced_scan(advanced_args.ip)
    if scan_results:
        print(colored(f"Advanced scan results for {advanced_args.ip}:", 'green'))
        for result in scan_results:
            print(colored(f"{result['type']}: {result['info']}", 'green'))
    else:
        print(colored("Advanced scan failed or no data found.", 'red'))

def handle_bandwidth(args):
    parser = argparse.ArgumentParser(description='Monitor bandwidth usage')
    parser.add_argument('interface', help='Network interface to monitor (e.g., eth0)')
    bandwidth_args = parser.parse_args(args)
    usage_stats = bandwidth_analysis(bandwidth_args.interface)
    if usage_stats:
        print(colored(f"Bandwidth usage on {bandwidth_args.interface}:", 'green'))
        for stat in usage_stats:
            print(colored(f"{stat['time']}: {stat['usage']} bytes", 'green'))
    else:
        print(colored("Bandwidth monitoring failed or no data found.", 'red'))

def handle_latency(args):
    parser = argparse.ArgumentParser(description='Measure latency to a host')
    parser.add_argument('host', help='Host to measure latency to')
    latency_args = parser.parse_args(args)
    latency = measure_latency(latency_args.host)
    if latency is not None:
        print(colored(f"Latency to {latency_args.host}: {latency} ms", 'green'))
    else:
        print(colored(f"Latency measurement failed for {latency_args.host}.", 'red'))

def handle_alert(args):
    parser = argparse.ArgumentParser(description='Send an alert')
    parser.add_argument('email', help='Email address to send alert to')
    parser.add_argument('subject', help='Subject of the alert')
    parser.add_argument('message', help='Message body of the alert')
    alert_args = parser.parse_args(args)
    success = send_alert(alert_args.email, alert_args.subject, alert_args.message)
    if success:
        print(colored(f"Alert sent to {alert_args.email}", 'green'))
    else:
        print(colored(f"Failed to send alert to {alert_args.email}", 'red'))

def handle_report(args):
    parser = argparse.ArgumentParser(description='Generate a report')
    parser.add_argument('report_type', help='Type of report to generate (e.g., full, summary)')
    report_args = parser.parse_args(args)
    report = generate_report(report_args.report_type)
    if report:
        print(colored(f"Report generated successfully:", 'green'))
        print(report)
    else:
        print(colored("Report generation failed.", 'red'))

if __name__ == '__main__':
    main()
