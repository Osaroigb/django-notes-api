from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes_api', '0001_initial')
    ]

    operations = [
        migrations.RunSQL(
            "ALTER TABLE notes_api_note RENAME TO notes;",
            "ALTER TABLE notes RENAME TO notes_api_note;",
        )
    ]