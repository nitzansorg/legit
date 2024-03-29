from notifiers.notifier import INotifier


class ConsoleNotifier(INotifier):
    def notify(self, alert: str):
        print(alert)
