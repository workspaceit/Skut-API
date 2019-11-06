"""
This script contains SCUT seed data which is dependant to the project.
User Group and Group Permission being set in this file.
This script only need to execute when the project database is new.
"""

from django.contrib.auth.models import Group, Permission
from django.db import transaction


@transaction.atomic
def add_group_permissions():
    user_group = Group(name='user')
    user_group.save()
    manager_group = Group(name='manager')
    manager_group.save()
    admin_group = Group(name='admin')
    admin_group.save()

    # User Model
    add_user = Permission.objects.get(codename='add_userprofile')
    change_user = Permission.objects.get(codename='change_userprofile')
    view_user = Permission.objects.get(codename='view_userprofile')
    delete_user = Permission.objects.get(codename='delete_userprofile')

    # Area Model
    add_area = Permission.objects.get(codename='add_area')
    change_area = Permission.objects.get(codename='change_area')
    view_area = Permission.objects.get(codename='view_area')
    delete_area = Permission.objects.get(codename='delete_area')

    # Lock Model
    add_lock = Permission.objects.get(codename='add_lock')
    change_lock = Permission.objects.get(codename='change_lock')
    view_lock = Permission.objects.get(codename='view_lock')
    delete_lock = Permission.objects.get(codename='delete_lock')

    # Notice Model
    add_notice = Permission.objects.get(codename='add_notice')
    change_notice = Permission.objects.get(codename='change_notice')
    view_notice = Permission.objects.get(codename='view_notice')
    delete_notice = Permission.objects.get(codename='delete_notice')

    # Notification Model
    add_notification = Permission.objects.get(codename='add_notification')
    change_notification = Permission.objects.get(codename='change_notification')
    view_notification = Permission.objects.get(codename='view_notification')
    delete_notification = Permission.objects.get(codename='delete_notification')

    # Ride Model
    add_ride = Permission.objects.get(codename='add_ride')
    change_ride = Permission.objects.get(codename='change_ride')
    view_ride = Permission.objects.get(codename='view_ride')
    delete_ride = Permission.objects.get(codename='delete_ride')

    # ScooterCategory Model
    add_scootercategory = Permission.objects.get(codename='add_scootercategory')
    change_scootercategory = Permission.objects.get(codename='change_scootercategory')
    view_scootercategory = Permission.objects.get(codename='view_scootercategory')
    delete_scootercategory = Permission.objects.get(codename='delete_scootercategory')

    # ScooterModel Model
    add_scootermodel = Permission.objects.get(codename='add_scootermodel')
    change_scootermodel = Permission.objects.get(codename='change_scootermodel')
    view_scootermodel = Permission.objects.get(codename='view_scootermodel')
    delete_scootermodel = Permission.objects.get(codename='delete_scootermodel')

    # Scooter Model
    add_scooter = Permission.objects.get(codename='add_scooter')
    change_scooter = Permission.objects.get(codename='change_scooter')
    view_scooter = Permission.objects.get(codename='view_scooter')
    delete_scooter = Permission.objects.get(codename='delete_scooter')

    # Setting Model
    add_setting = Permission.objects.get(codename='add_setting')
    change_setting = Permission.objects.get(codename='change_setting')
    view_setting = Permission.objects.get(codename='view_setting')
    delete_setting = Permission.objects.get(codename='delete_setting')

    # Stand Model
    add_stand = Permission.objects.get(codename='add_stand')
    change_stand = Permission.objects.get(codename='change_stand')
    view_stand = Permission.objects.get(codename='view_stand')
    delete_stand = Permission.objects.get(codename='delete_stand')

    # Transaction Model
    add_transaction = Permission.objects.get(codename='add_transaction')
    change_transaction = Permission.objects.get(codename='change_transaction')
    view_transaction = Permission.objects.get(codename='view_transaction')
    delete_transaction = Permission.objects.get(codename='delete_transaction')

    user_group.permissions.add(
        add_user, change_user, view_user, view_area, view_notice, view_notification,
        add_ride, change_ride, view_ride, view_scooter, view_stand, view_transaction
    )

    manager_group.permissions.add(
        add_user, change_user, view_user, delete_user,
        add_area, change_area, view_area, delete_area,
        add_lock, change_lock, view_lock, delete_lock,
        add_notice, change_notice, view_notice, delete_notice,
        add_notification, change_notification, view_notification, delete_notification,
        add_ride, change_ride, view_ride, delete_ride,
        add_scootercategory, change_scootercategory, view_scootercategory, delete_scootercategory,
        add_scootermodel, change_scootermodel, view_scootermodel, delete_scootermodel,
        add_scooter, change_scooter, view_scooter, delete_scooter,
        add_setting, change_setting, view_setting, delete_setting,
        add_stand, change_stand, view_stand, delete_stand,
        add_transaction, change_transaction, view_transaction, delete_transaction
    )

    admin_group.permissions.add(
        add_user, change_user, view_user, delete_user,
        add_area, change_area, view_area, delete_area,
        add_lock, change_lock, view_lock, delete_lock,
        add_notice, change_notice, view_notice, delete_notice,
        add_notification, change_notification, view_notification, delete_notification,
        add_ride, change_ride, view_ride, delete_ride,
        add_scootercategory, change_scootercategory, view_scootercategory, delete_scootercategory,
        add_scootermodel, change_scootermodel, view_scootermodel, delete_scootermodel,
        add_scooter, change_scooter, view_scooter, delete_scooter,
        add_setting, change_setting, view_setting, delete_setting,
        add_stand, change_stand, view_stand, delete_stand,
        add_transaction, change_transaction, view_transaction, delete_transaction
    )
    return


def seed_data():
    try:
        if not Group.objects.filter(name='admin').exists():
            print("Hello world")
            add_group_permissions()
    except Exception as ex:
        print(ex)

