from django.db import models
from django.contrib.auth.models import User


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
    created_at = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=30, null=True)
    israeli_id = models.CharField(max_length=9, unique=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    address = models.CharField(max_length=30)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    birthdate = models.DateField()
    guardian_phone_number = models.CharField(max_length=10, blank=True, default="")
    guardian_name = models.CharField(max_length=30, blank=True, default="")
    gender = models.CharField(max_length=10, choices=GENDER)
    is_having_regular_menstruation = models.BooleanField(default=True, blank=True)
    is_on_cocp = models.BooleanField(default=False, blank=True)
    # front_image = models.ImageField(upload_to="user_images/")
    # side_image = models.ImageField(upload_to="user_images/")
    # back_image = models.ImageField(upload_to="user_images/")
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
    # current_training_image = models.ImageField(upload_to="user_images/")
    weekly_aerobic = models.TextField(blank=True, default="")
    unliked_exercises = models.TextField(blank=True, default="")
    commit_training_number = models.CharField(max_length=10, choices=NUM_OF_TRAINING)
    former_injuries = models.TextField(blank=True, default="")
    further_info = models.TextField(blank=True, default="")

    def __str__(self):
        return f"{self.user.username} - {self.israeli_id}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    user_data = models.ForeignKey(
        UserData, on_delete=models.CASCADE, related_name="user_data", null=True
    )
    # profile_picture = models.ImageField(
    #     upload_to="profile_pictures/", null=True, blank=True
    # )
    has_filled_questionnaire = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class UserUpdateHistory(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    weight = models.CharField(max_length=10)
    # front_image = models.ImageField(upload_to="user_images/")
    # side_image = models.ImageField(upload_to="user_images/")
    # back_image = models.ImageField(upload_to="user_images/")
    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-recorded_at"]

    def __str__(self):
        formatted_date = self.recorded_at.strftime("%Y-%m-%d %H:%M")
        return f"{self.user.username}: {self.weight} kg on {formatted_date}"
