from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from .models import StudentQuestionnaire


class StudentQuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'preferred_contact_method', 'age_range',
                    'learning_type', 'class_format', 'created_at')
    list_filter = (
        ('created_at', DateRangeFilter),
        'learning_type',
        'age_range',
        'class_format',
        'preferred_location',
    )
    search_fields = [
        'full_name', 'contact_detail', 'additional_notes'
    ]
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Contact Information', {
            'fields': ('full_name', 'preferred_contact_method', 'contact_detail')
        }),
        ('Basic Information', {
            'fields': ('age_range', 'learning_type')
        }),
        ('Language Details', {
            'fields': ('language_english', 'language_mandarin', 'language_french',
                       'language_korean', 'language_other', 'current_level', 'studied_before')
        }),
        ('Learning Goals', {
            'fields': ('goal_conversation', 'goal_school_prep', 'goal_work',
                       'goal_personal', 'goal_cultural', 'goal_confidence', 'goal_other')
        }),
        ('Class Preferences', {
            'fields': ('class_format', 'preferred_location', 'location_other',
                       'class_type', 'preferred_schedule', 'teacher_style', 'teacher_style_other')
        }),
        ('Topics of Interest', {
            'fields': ('topic_business', 'topic_technology', 'topic_music_arts',
                       'topic_film_media', 'topic_travel', 'topic_culture',
                       'topic_academic', 'topic_exam_prep', 'topic_casual', 'topic_other')
        }),
        ('Additional Information', {
            'fields': ('specific_topic_interest', 'additional_notes')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


admin.site.register(StudentQuestionnaire, StudentQuestionnaireAdmin)

