from django.db import models


class StudentQuestionnaire(models.Model):
    # Contact Information
    full_name = models.CharField(max_length=200)

    CONTACT_METHOD_CHOICES = [
        ('email', 'Email'),
        ('whatsapp', 'WhatsApp'),
        ('line', 'LINE'),
    ]
    preferred_contact_method = models.CharField(
        max_length=10,
        choices=CONTACT_METHOD_CHOICES
    )

    contact_detail = models.CharField(
        max_length=200,
        help_text="Email, phone number, or LINE ID"
    )

    # Age Range
    AGE_RANGE_CHOICES = [
        ('under_12', 'Under 12'),
        ('13_17', '13–17'),
        ('18_25', '18–25'),
        ('26_40', '26–40'),
        ('40_plus', '40+'),
    ]
    age_range = models.CharField(max_length=10, choices=AGE_RANGE_CHOICES)

    # Learning Interest
    LEARNING_TYPE_CHOICES = [
        ('language', 'Language'),
        ('culture', 'Culture'),
        ('wellness', 'Wellness'),
        ('not_sure', "Not sure yet (I'd like recommendations)"),
    ]
    learning_type = models.CharField(max_length=20, choices=LEARNING_TYPE_CHOICES)

    # Language Selection (multiple choice)
    language_english = models.BooleanField(default=False)
    language_mandarin = models.BooleanField(default=False)
    language_french = models.BooleanField(default=False)
    language_korean = models.BooleanField(default=False)
    language_other = models.CharField(max_length=100, blank=True)

    # Current Level
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('not_sure', 'Not sure'),
    ]
    current_level = models.CharField(
        max_length=15,
        choices=LEVEL_CHOICES,
        blank=True
    )

    # Previous Study
    studied_before = models.BooleanField(
        null=True,
        help_text="Have you studied this subject/language before?"
    )

    # Main Goals (multiple choice)
    goal_conversation = models.BooleanField(default=False, verbose_name="Conversation / real-life use")
    goal_school_prep = models.BooleanField(default=False, verbose_name="School or study abroad preparation")
    goal_work = models.BooleanField(default=False, verbose_name="Work / professional use")
    goal_personal = models.BooleanField(default=False, verbose_name="Personal interest/hobby")
    goal_cultural = models.BooleanField(default=False, verbose_name="Cultural experience")
    goal_confidence = models.BooleanField(default=False, verbose_name="Confidence building")
    goal_other = models.CharField(max_length=200, blank=True)

    # Class Format
    CLASS_FORMAT_CHOICES = [
        ('online', 'Online'),
        ('in_person', 'In-person'),
        ('either', 'Either is fine'),
    ]
    class_format = models.CharField(max_length=10, choices=CLASS_FORMAT_CHOICES)

    # Preferred Location
    LOCATION_CHOICES = [
        ('taipei', 'Taipei'),
        ('new_york', 'New York'),
        ('other', 'Other'),
    ]
    preferred_location = models.CharField(
        max_length=10,
        choices=LOCATION_CHOICES,
        blank=True
    )
    location_other = models.CharField(max_length=100, blank=True)

    # Class Type
    CLASS_TYPE_CHOICES = [
        ('one_on_one', 'One-on-one'),
        ('small_group', 'Small group'),
    ]
    class_type = models.CharField(max_length=15, choices=CLASS_TYPE_CHOICES)

    # Schedule
    SCHEDULE_CHOICES = [
        ('weekday_day', 'Weekdays (daytime)'),
        ('weekday_evening', 'Weekdays (evening)'),
        ('weekends', 'Weekends'),
        ('flexible', 'Flexible'),
    ]
    preferred_schedule = models.CharField(max_length=20, choices=SCHEDULE_CHOICES)

    # Teacher Style
    TEACHER_STYLE_CHOICES = [
        ('patient', 'Patient & encouraging'),
        ('conversational', 'Conversational & relaxed'),
        ('structured', 'Structured & academic'),
        ('creative', 'Creative & activity-based'),
        ('not_sure', 'Not sure'),
        ('other', 'Other'),
    ]
    teacher_style = models.CharField(max_length=20, choices=TEACHER_STYLE_CHOICES)
    teacher_style_other = models.CharField(max_length=200, blank=True)

    # Learning Topics (multiple choice)
    topic_business = models.BooleanField(default=False, verbose_name="Business / Workplace communication")
    topic_technology = models.BooleanField(default=False, verbose_name="Technology / Computer Science")
    topic_music_arts = models.BooleanField(default=False, verbose_name="Music / Arts / Creative fields")
    topic_film_media = models.BooleanField(default=False, verbose_name="Film / Media / Content creation")
    topic_travel = models.BooleanField(default=False, verbose_name="Travel & daily life")
    topic_culture = models.BooleanField(default=False, verbose_name="Culture & social topics")
    topic_academic = models.BooleanField(default=False, verbose_name="Academic subjects")
    topic_exam_prep = models.BooleanField(default=False, verbose_name="Exam preparation")
    topic_casual = models.BooleanField(default=False, verbose_name="Casual conversation")
    topic_other = models.CharField(max_length=200, blank=True)

    # Open-ended Questions
    specific_topic_interest = models.TextField(
        blank=True,
        help_text="Specific topic you'd love to learn or talk about"
    )

    additional_notes = models.TextField(blank=True)

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Student Questionnaire'
        verbose_name_plural = 'Student Questionnaires'

    def __str__(self):
        return f"{self.full_name} - {self.created_at.strftime('%Y-%m-%d')}"

