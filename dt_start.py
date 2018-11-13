#!/usr/bin/env python3

import dt_bot


class startBot(decision_bot.DTBot):
    def __init__(self):
        super().__init__("dt.svc")


if __name__ == '__main__':
    bot = startBot()
    bot.run()
