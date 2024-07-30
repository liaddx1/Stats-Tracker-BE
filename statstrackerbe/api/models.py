from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=30)
    israeli_id = models.CharField(max_length=9, unique=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    address = models.CharField(max_length=30)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    birthdate = models.DateField()
    guardian_phone_number = models.CharField(max_length=10)
    guardian_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    is_having_regular_menstruation = models.BooleanField(default=True)
    is_on_cocp = models.BooleanField(default=False)
    # front_image = models.ImageField(upload_to="user_images/")
    # side_image = models.ImageField(upload_to="user_images/")
    # back_image = models.ImageField(upload_to="user_images/")
    daily_routine = models.TextField()
    daily_diet = models.TextField()
    unliked_sauce = models.CharField(max_length=50)
    alergies = models.CharField(max_length=50)
    supplements = models.CharField(max_length=50)
    liked_food = models.TextField()
    num_of_meals = models.CharField(max_length=10)
    is_drinking_soda = models.BooleanField(default=False)
    which_soda = models.TextField()
    liked_sauce = models.CharField(max_length=50)
    is_able_to_weight_food = models.BooleanField(default=False)
    is_drinking_alcohol = models.BooleanField(default=False)
    which_alcohol = models.TextField()
    was_under_thousand_calories_diet = models.BooleanField(default=False)
    thousand_calorie_diet = models.TextField()
    current_training = models.TextField()
    weekly_aerobic = models.TextField()
    unliked_exercises = models.TextField()
    commit_training_number = models.CharField(max_length=10)
    former_injuries = models.TextField()
    further_info = models.TextField()

    def __str__(self):
        return self.user.username


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    # user_prfile = models.ForeignKey(
    #     UserProfile, on_delete=models.CASCADE, related_name="user_profile"
    # )
    # profile_picture = models.ImageField(
    #     upload_to="profile_pictures/", null=True, blank=True
    # )
    has_filled_questionnaire = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class UserUpdateHistory(models.Model):
    user = models.ForeignKey(
        UserData, on_delete=models.CASCADE, related_name="weight_history"
    )
    weight = models.CharField(max_length=10)
    # front_image = models.ImageField(upload_to="user_images/")
    # side_image = models.ImageField(upload_to="user_images/")
    # back_image = models.ImageField(upload_to="user_images/")
    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-recorded_at"]

    def __str__(self):
        f"{self.user_profile.user.username} - {self.weight} kg on {self.recorded_at}"
