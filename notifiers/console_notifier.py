from notifiers.notifier import INotifier, Notification


class ConsoleNotifier(INotifier):
    """
    notifies to the console, in a readable human formatting
    """
    def notify(self, notification: Notification):
        print(f"suspicious behavior was found!\n"
              f"suspicious event type: {notification.event_type}\n"
              f"suspect reason: {notification.suspect_reason}")
