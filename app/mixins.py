# mixins.py
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import Group

class SuperUserOrGroupRequiredMixin(UserPassesTestMixin):
    group_name = None  # Set the group name in your view

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        if self.group_name and self.request.user.is_authenticated:
            try:
                group = Group.objects.get(name=self.group_name)
                return group in self.request.user.groups.all()
            except Group.DoesNotExist:
                return False
        return False