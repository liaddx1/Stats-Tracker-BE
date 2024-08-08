from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify
from shortuuid.django_fields import ShortUUIDField
import shortuuid


class UserData(models.Model):
    GENDER = (
        ("זכר", "זכר"),
        ("נקבה", "נקבה"),
    )
    NUM_OF_MEALS = (
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
    )
    NUM_OF_TRAINING = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30, null=True)
    israeli_id = models.CharField(max_length=9, unique=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    address = models.CharField(max_length=30)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    age = models.DateField(null=True)
    guardian_name = models.CharField(max_length=30, blank=True, default="")
    guardian_phone_number = models.CharField(max_length=10, blank=True, default="")
    gender = models.CharField(max_length=10, choices=GENDER)
    is_having_regular_menstruation = models.BooleanField(default=True, blank=True)
    is_on_cocp = models.BooleanField(default=False, blank=True)
    front_image = models.FileField(
        upload_to=f"images/questionnaire/", null=True, blank=True
    )
    side_image = models.FileField(
        upload_to=f"images/questionnaire/", null=True, blank=True
    )
    back_image = models.FileField(
        upload_to=f"images/questionnaire/", null=True, blank=True
    )
    daily_routine = models.TextField()
    daily_diet = models.TextField()
    unliked_sauce = models.CharField(max_length=50, blank=True, default="")
    alergies = models.CharField(max_length=50, blank=True, default="")
    supplements = models.CharField(max_length=50, blank=True, default="")
    liked_food = models.TextField(blank=True, default="")
    num_of_meals = models.CharField(max_length=10, choices=NUM_OF_MEALS)
    is_drinking_soda = models.BooleanField(default=False)
    which_soda = models.TextField(blank=True, default="")
    liked_sauce = models.CharField(max_length=50, blank=True, default="")
    is_able_to_weight_food = models.BooleanField(default=False)
    is_drinking_alcohol = models.BooleanField(default=False)
    which_alcohol = models.TextField(blank=True, default="")
    was_under_thousand_calories_diet = models.BooleanField(default=False)
    thousand_calorie_diet = models.TextField(blank=True, default="")
    current_training = models.TextField(blank=True, default="")
    current_training_image = models.FileField(
        upload_to=f"images/current_training/", null=True, blank=True
    )
    weekly_aerobic = models.TextField(blank=True, default="")
    unliked_exercises = models.TextField(blank=True, default="")
    commit_training_number = models.CharField(max_length=10, choices=NUM_OF_TRAINING)
    former_injuries = models.TextField(blank=True, default="")
    further_info = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.israeli_id}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    user_data = models.ForeignKey(
        UserData, null=True, blank=True, on_delete=models.CASCADE
    )
    profile_picture = models.FileField(
        upload_to=f"images/profile_picture/",
        default="default/default-user.jpg",
        null=True,
        blank=True,
    )
    has_filled_questionnaire = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


def create_user_related_data(sender, instance, created, **kwargs):
    if created:
        user_data = UserData.objects.create(user=instance)
        UserProfile.objects.create(user=instance, user_data=user_data)


def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


post_save.connect(create_user_related_data, sender=User)
post_save.connect(save_user_profile, sender=User)


class UserUpdateHistory(models.Model):
    ONE_TO_TEN = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
    )

    # halfs_one_to_ten = (
    #     ("0.5", "0.5"),
    #     ("1", "1"),
    #     ("1.5", "1.5"),
    #     ("2", "2"),
    #     ("2.5", "2.5"),
    #     ("3", "3"),
    #     ("3.5", "3.5"),
    #     ("4", "4"),
    #     ("4.5", "4.5"),
    #     ("5", "5"),
    #     ("5.5", "5.5"),
    #     ("6", "6"),
    #     ("6.5", "6.5"),
    #     ("7", "7"),
    #     ("7.5", "7.5"),
    #     ("8", "8"),
    #     ("8.5", "8.5"),
    #     ("9.5", "9.5"),
    #     ("10", "10"),
    # )
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    recorded_at = models.DateTimeField(auto_now_add=True)
    weight = models.CharField(max_length=10, default="")
    is_done_all_aerobic_exer = models.BooleanField(default=False)
    missing_aerobic = models.TextField(blank=True, default="")
    is_done_all_training_exer = models.BooleanField(default=False)
    missing_training = models.TextField(blank=True, default="")
    level_of_diet_fulfillment = models.CharField(
        max_length=10, choices=ONE_TO_TEN, default=""
    )
    protein_intake = models.CharField(max_length=10, choices=ONE_TO_TEN, default="")
    carb_intake = models.CharField(max_length=10, choices=ONE_TO_TEN, default="")
    fat_intake = models.CharField(max_length=10, choices=ONE_TO_TEN, default="")
    water_intake = models.TextField(default="")
    avg_sleep_hours = models.CharField(max_length=10, default="")
    further_info = models.TextField(default="")
    front_image = models.FileField(
        upload_to=f"images/update_history/{recorded_at}/",
        null=True,
        blank=True,
    )
    side_image = models.FileField(
        upload_to=f"images/update_history/{recorded_at}/",
        null=True,
        blank=True,
    )
    back_image = models.FileField(
        upload_to=f"images/update_history/{recorded_at}/",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["-recorded_at"]

    def __str__(self):
        formatted_date = self.recorded_at.strftime("%Y-%m-%d %H:%M")
        return f"{self.user.username}: {self.weight} kg on {formatted_date}"


class Notification(models.Model):
    NOTI_TYPE = (
        ("תפריט", "תפריט"),
        ("אימונים", "אימונים"),
        ("מידע", "מידע"),
    )

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, null=True, on_delete=models.CASCADE)
    type = models.CharField(choices=NOTI_TYPE, max_length=50, default="מידע")
    is_watched = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return (
            f"{self.user.username}: {self.type} - {self.is_watched} | {self.created_at}"
        )

    class Meta:
        ordering = ["-created_at"]
