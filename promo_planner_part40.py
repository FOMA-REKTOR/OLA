# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: PromoPlanner
import argparse

def main():
    parser = argparse.ArgumentParser(description="PromoPlanner CLI")
    sub = parser.add_subparsers(dest="command")

    # create_channels
    ch = sub.add_parser("create_channels")
    ch.add_argument("--name", required=True)
    ch.add_argument("--budget", type=float, required=True)

    # create_tasks
    tk = sub.add_parser("create_tasks")
    tk.add_argument("--channel", required=True)
    tk.add_argument("--name", required=True)

    # get_results
    res = sub.add_parser("get_results")
    res.add_argument("--channel", required=True)

    args = parser.parse_args()
    if args.command == "create_channels":
        channels.add(args.name, args.budget)
    elif args.command == "create_tasks":
        tasks.add(args.channel, args.name)
    elif args.command == "get_results":
        print(results.get(args.channel))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
