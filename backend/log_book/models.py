from django.db import models

# TODO: record duties of driver and co-driver
# TODO: record rest stop
# TODO: add remarks
# Duties: 1. Off duty, 2. Sleeper berth, 3. Driving, 4. On duty, not driving
# Rest stop: 1. Rest area, 2. Truck stop, 3. Home, 4. Other


class DutyStatus(models.Choices):
    OFF_DUTY = "Off Duty"
    SLEEPER_BERTH = "Sleeper Berth"
    DRIVING = "Driving"
    ON_DUTY = "On Duty, Not Driving"


class LogEntry(models.Model):
    trip = models.ForeignKey(
        "trips.Trip", on_delete=models.CASCADE, related_name="log_entries"
    )
    status = models.CharField(
        max_length=100, choices=DutyStatus.choices, default=DutyStatus.OFF_DUTY
    )
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)
    duration = models.DurationField()
    driver = models.ForeignKey(
        "users.Driver", on_delete=models.CASCADE, related_name="driver_log_entries"
    )
    co_driver = models.ForeignKey(
        "users.Driver",
        null=True,
        on_delete=models.SET_NULL,
        related_name="co_driver_log_entries",
    )
    rest_stop = models.CharField(max_length=100)
    remarks = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.driver} - {self.status} - {self.start_time} to {self.end_time}"
