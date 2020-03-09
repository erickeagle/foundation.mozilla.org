# Generated by Django 2.2.12 on 2020-05-12 13:26

from django.db import migrations, models
import django.db.models.deletion
import networkapi.wagtailpages.pagemodels.blog.blog_category
import wagtail.core.blocks
import wagtail.core.blocks.static_block
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('wagtailpages', '0095_auto_20200406_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='author_fy_NL',
            field=models.CharField(max_length=70, null=True, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='body_fy_NL',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'h2', 'h3', 'h4', 'h5', 'ol', 'ul', 'link', 'hr'])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('captionURL', wagtail.core.blocks.CharBlock(help_text='Optional URL that this caption should link out to.', required=False))])), ('image_text', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'link'])), ('url', wagtail.core.blocks.CharBlock(help_text='Optional URL that this image should link out to.', required=False)), ('top_divider', wagtail.core.blocks.BooleanBlock(help_text='Optional divider above content block.', required=False)), ('bottom_divider', wagtail.core.blocks.BooleanBlock(help_text='Optional divider below content block.', required=False))])), ('image_text_mini', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link']))])), ('video', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.CharBlock(help_text='To make sure a video will embed properly, go to your YouTube video and click “Share,” then “Embed,” and then copy and paste the provided URL only. For example: https://www.youtube.com/embed/3FIVXBawyQw')), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('captionURL', wagtail.core.blocks.CharBlock(help_text='Optional URL for caption to link to.', required=False))])), ('linkbutton', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock()), ('URL', wagtail.core.blocks.CharBlock()), ('styling', wagtail.core.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary button'), ('btn-secondary', 'Secondary button')]))])), ('spacer', wagtail.core.blocks.StructBlock([('size', wagtail.core.blocks.ChoiceBlock(choices=[('1', 'quarter spacing'), ('2', 'half spacing'), ('3', 'single spacing'), ('4', 'one and a half spacing'), ('5', 'triple spacing')]))])), ('quote', wagtail.core.blocks.StructBlock([('quotes', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.CharBlock()), ('attribution', wagtail.core.blocks.CharBlock())])))]))], null=True),
        ),
        migrations.AddField(
            model_name='cta',
            name='description_fy_NL',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Body (richtext) of component', null=True),
        ),
        migrations.AddField(
            model_name='cta',
            name='header_fy_NL',
            field=models.CharField(blank=True, help_text='Heading that will display on page for this component', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='cta',
            name='name_fy_NL',
            field=models.CharField(default='', help_text='Identify this component for other editors', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='donationmodal',
            name='body_fy_NL',
            field=models.TextField(default='Mozilla is a nonprofit organization fighting for a healthy internet, where privacy is included by design and you have more control over your personal information. We depend on contributions from people like you to carry out this work. Can you donate today?', help_text='Donation text', null=True),
        ),
        migrations.AddField(
            model_name='donationmodal',
            name='dismiss_text_fy_NL',
            field=models.CharField(default="No, I'll share instead", help_text='Dismiss button label', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='donationmodal',
            name='donate_text_fy_NL',
            field=models.CharField(default="Yes, I'll chip in", help_text='Donate button label', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='donationmodal',
            name='header_fy_NL',
            field=models.CharField(default="Thanks for signing! While you're here, we need your help.", help_text='Donation header', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='donationmodal',
            name='name_fy_NL',
            field=models.CharField(default='', help_text='Identify this component for other editors', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_button_text_fy_NL',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_button_url_fy_NL',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_headline_fy_NL',
            field=models.CharField(blank=True, help_text='Hero story headline', max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_image_fy_NL',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hero_image', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_story_description_fy_NL',
            field=wagtail.core.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='header_fy_NL',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='intro_fy_NL',
            field=models.CharField(blank=True, help_text='Intro paragraph to show in hero cutout box', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='modularpage',
            name='body_fy_NL',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'large', 'h2', 'h3', 'h4', 'h5', 'ol', 'ul', 'link', 'hr'])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('captionURL', wagtail.core.blocks.CharBlock(help_text='Optional URL that this caption should link out to.', required=False))])), ('image_text', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'link'])), ('url', wagtail.core.blocks.CharBlock(help_text='Optional URL that this image should link out to.', required=False)), ('top_divider', wagtail.core.blocks.BooleanBlock(help_text='Optional divider above content block.', required=False)), ('bottom_divider', wagtail.core.blocks.BooleanBlock(help_text='Optional divider below content block.', required=False))])), ('image_text_mini', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link']))])), ('image_grid', wagtail.core.blocks.StructBlock([('grid_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.CharBlock(help_text='Please remember to properly attribute any images we use.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Optional URL that this figure should link out to.', required=False)), ('square_image', wagtail.core.blocks.BooleanBlock(default=True, help_text='If left checked, the image will be cropped to be square.', required=False))])))])), ('video', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.CharBlock(help_text='To make sure a video will embed properly, go to your YouTube video and click “Share,” then “Embed,” and then copy and paste the provided URL only. For example: https://www.youtube.com/embed/3FIVXBawyQw')), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('captionURL', wagtail.core.blocks.CharBlock(help_text='Optional URL for caption to link to.', required=False))])), ('iframe', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.CharBlock(help_text='Please note that only URLs from white-listed domains will work.')), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('captionURL', wagtail.core.blocks.CharBlock(help_text='Optional URL that this caption should link out to.', required=False))])), ('linkbutton', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock()), ('URL', wagtail.core.blocks.CharBlock()), ('styling', wagtail.core.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary button'), ('btn-secondary', 'Secondary button')]))])), ('spacer', wagtail.core.blocks.StructBlock([('size', wagtail.core.blocks.ChoiceBlock(choices=[('1', 'quarter spacing'), ('2', 'half spacing'), ('3', 'single spacing'), ('4', 'one and a half spacing'), ('5', 'triple spacing')]))])), ('quote', wagtail.core.blocks.StructBlock([('quotes', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.CharBlock()), ('attribution', wagtail.core.blocks.CharBlock())])))])), ('pulse_listing', wagtail.core.blocks.StructBlock([('search_terms', wagtail.core.blocks.CharBlock(help_text='Test your search at mozillapulse.org/search', label='Search', required=False)), ('max_number_of_results', wagtail.core.blocks.IntegerBlock(default=6, help_text='Choose 1-12. If you want visitors to see more, link to a search or tag on Pulse.', max_value=12, min_value=0, required=True)), ('only_featured_entries', wagtail.core.blocks.BooleanBlock(default=False, help_text='Featured items are selected by Pulse moderators.', label='Display only featured entries', required=False)), ('newest_first', wagtail.core.blocks.ChoiceBlock(choices=[('True', 'Show newer entries first'), ('False', 'Show older entries first')], label='Sort')), ('advanced_filter_header', wagtail.core.blocks.static_block.StaticBlock(admin_text='-------- ADVANCED FILTERS: OPTIONS TO DISPLAY FEWER, MORE TARGETED RESULTS. --------', label=' ')), ('issues', wagtail.core.blocks.ChoiceBlock(choices=[('all', 'All'), ('Decentralization', 'Decentralization'), ('Digital Inclusion', 'Digital Inclusion'), ('Online Privacy & Security', 'Online Privacy & Security'), ('Open Innovation', 'Open Innovation'), ('Web Literacy', 'Web Literacy')])), ('help', wagtail.core.blocks.ChoiceBlock(choices=[('all', 'All'), ('Attend', 'Attend'), ('Create content', 'Create content'), ('Code', 'Code'), ('Design', 'Design'), ('Fundraise', 'Fundraise'), ('Join community', 'Join community'), ('Localize & translate', 'Localize & translate'), ('Mentor', 'Mentor'), ('Plan & organize', 'Plan & organize'), ('Promote', 'Promote'), ('Take action', 'Take action'), ('Test & feedback', 'Test & feedback'), ('Write documentation', 'Write documentation')], label='Type of help needed')), ('direct_link', wagtail.core.blocks.BooleanBlock(default=False, help_text='Checked: user goes to project link. Unchecked: user goes to pulse entry', label='Direct link', required=False))])), ('profile_listing', wagtail.core.blocks.StructBlock([('max_number_of_results', wagtail.core.blocks.IntegerBlock(default=12, help_text='Pick up to 48 profiles.', max_value=48, min_value=1, required=True)), ('advanced_filter_header', wagtail.core.blocks.static_block.StaticBlock(admin_text='-------- ADVANCED FILTERS: OPTIONS TO DISPLAY FEWER, MORE TARGETED RESULTS. --------', label=' ')), ('profile_type', wagtail.core.blocks.CharBlock(default='', help_text='Example: Fellow.', required=False)), ('program_type', wagtail.core.blocks.CharBlock(default='', help_text='Example: Tech Policy.', required=False)), ('year', wagtail.core.blocks.CharBlock(default='', required=False))])), ('profile_by_id', wagtail.core.blocks.StructBlock([('ids', wagtail.core.blocks.CharBlock(help_text='Show profiles for pulse users with specific profile ids (mozillapulse.org/profile/[##]). For multiple profiles, specify a comma separated list (e.g. 85,105,332).', label='Profile by ID'))])), ('profile_directory', wagtail.core.blocks.StructBlock([('max_number_of_results', wagtail.core.blocks.IntegerBlock(default=12, help_text='Pick up to 48 profiles.', max_value=48, min_value=1, required=True)), ('advanced_filter_header', wagtail.core.blocks.static_block.StaticBlock(admin_text='-------- ADVANCED FILTERS: OPTIONS TO DISPLAY FEWER, MORE TARGETED RESULTS. --------', label=' ')), ('profile_type', wagtail.core.blocks.CharBlock(default='', help_text='Example: Fellow.', required=False)), ('program_type', wagtail.core.blocks.CharBlock(default='', help_text='Example: Tech Policy.', required=False)), ('year', wagtail.core.blocks.CharBlock(default='', required=False)), ('filter_values', wagtail.core.blocks.CharBlock(default='2019,2018,2017,2016,2015,2014,2013', help_text='Example: 2019,2018,2017,2016,2015,2014,2013', required=True))])), ('recent_blog_entries', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('tag_filter', wagtail.core.blocks.CharBlock(help_text='Test this filter at foundation.mozilla.org/blog/tags/', label='Filter by Tag', required=False)), ('category_filter', wagtail.core.blocks.ChoiceBlock(choices=networkapi.wagtailpages.pagemodels.blog.blog_category.BlogPageCategory.get_categories, help_text='Test this filter at foundation.mozilla.org/blog/category/', label='Filter by Category', required=False)), ('top_divider', wagtail.core.blocks.BooleanBlock(help_text='Optional divider above content block.', required=False)), ('bottom_divider', wagtail.core.blocks.BooleanBlock(help_text='Optional divider below content block.', required=False))])), ('airtable', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(help_text="Copied from the Airtable embed code. The word 'embed' will be in the url")), ('height', wagtail.core.blocks.IntegerBlock(default=533, help_text='The height of the view on a desktop, usually copied from the Airtable embed code'))]))], null=True),
        ),
        migrations.AddField(
            model_name='modularpage',
            name='header_fy_NL',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='petition',
            name='share_email_fy_NL',
            field=models.CharField(blank=True, help_text='Share Progress id for email button', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='petition',
            name='share_facebook_fy_NL',
            field=models.CharField(blank=True, help_text='Share Progress id for facebook button', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='petition',
            name='share_link_fy_NL',
            field=models.URLField(blank=True, editable=False, help_text='Link that will be put in share button', max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='petition',
            name='share_link_text_fy_NL',
            field=models.CharField(blank=True, default='Share this', editable=False, help_text='Text content of the share button', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='petition',
            name='share_twitter_fy_NL',
            field=models.CharField(blank=True, help_text='Share Progress id for twitter button', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='petition',
            name='thank_you_fy_NL',
            field=models.CharField(default='Thank you for signing too!', help_text='Message to show after thanking people for signing', max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='primarypage',
            name='body_fy_NL',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'large', 'h2', 'h3', 'h4', 'h5', 'ol', 'ul', 'link', 'hr'])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('captionURL', wagtail.core.blocks.CharBlock(help_text='Optional URL that this caption should link out to.', required=False))])), ('image_text', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'link'])), ('url', wagtail.core.blocks.CharBlock(help_text='Optional URL that this image should link out to.', required=False)), ('top_divider', wagtail.core.blocks.BooleanBlock(help_text='Optional divider above content block.', required=False)), ('bottom_divider', wagtail.core.blocks.BooleanBlock(help_text='Optional divider below content block.', required=False))])), ('image_text_mini', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link']))])), ('image_grid', wagtail.core.blocks.StructBlock([('grid_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.CharBlock(help_text='Please remember to properly attribute any images we use.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Optional URL that this figure should link out to.', required=False)), ('square_image', wagtail.core.blocks.BooleanBlock(default=True, help_text='If left checked, the image will be cropped to be square.', required=False))])))])), ('video', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.CharBlock(help_text='To make sure a video will embed properly, go to your YouTube video and click “Share,” then “Embed,” and then copy and paste the provided URL only. For example: https://www.youtube.com/embed/3FIVXBawyQw')), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('captionURL', wagtail.core.blocks.CharBlock(help_text='Optional URL for caption to link to.', required=False))])), ('iframe', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.CharBlock(help_text='Please note that only URLs from white-listed domains will work.')), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('captionURL', wagtail.core.blocks.CharBlock(help_text='Optional URL that this caption should link out to.', required=False))])), ('linkbutton', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock()), ('URL', wagtail.core.blocks.CharBlock()), ('styling', wagtail.core.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary button'), ('btn-secondary', 'Secondary button')]))])), ('spacer', wagtail.core.blocks.StructBlock([('size', wagtail.core.blocks.ChoiceBlock(choices=[('1', 'quarter spacing'), ('2', 'half spacing'), ('3', 'single spacing'), ('4', 'one and a half spacing'), ('5', 'triple spacing')]))])), ('quote', wagtail.core.blocks.StructBlock([('quotes', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.CharBlock()), ('attribution', wagtail.core.blocks.CharBlock())])))])), ('pulse_listing', wagtail.core.blocks.StructBlock([('search_terms', wagtail.core.blocks.CharBlock(help_text='Test your search at mozillapulse.org/search', label='Search', required=False)), ('max_number_of_results', wagtail.core.blocks.IntegerBlock(default=6, help_text='Choose 1-12. If you want visitors to see more, link to a search or tag on Pulse.', max_value=12, min_value=0, required=True)), ('only_featured_entries', wagtail.core.blocks.BooleanBlock(default=False, help_text='Featured items are selected by Pulse moderators.', label='Display only featured entries', required=False)), ('newest_first', wagtail.core.blocks.ChoiceBlock(choices=[('True', 'Show newer entries first'), ('False', 'Show older entries first')], label='Sort')), ('advanced_filter_header', wagtail.core.blocks.static_block.StaticBlock(admin_text='-------- ADVANCED FILTERS: OPTIONS TO DISPLAY FEWER, MORE TARGETED RESULTS. --------', label=' ')), ('issues', wagtail.core.blocks.ChoiceBlock(choices=[('all', 'All'), ('Decentralization', 'Decentralization'), ('Digital Inclusion', 'Digital Inclusion'), ('Online Privacy & Security', 'Online Privacy & Security'), ('Open Innovation', 'Open Innovation'), ('Web Literacy', 'Web Literacy')])), ('help', wagtail.core.blocks.ChoiceBlock(choices=[('all', 'All'), ('Attend', 'Attend'), ('Create content', 'Create content'), ('Code', 'Code'), ('Design', 'Design'), ('Fundraise', 'Fundraise'), ('Join community', 'Join community'), ('Localize & translate', 'Localize & translate'), ('Mentor', 'Mentor'), ('Plan & organize', 'Plan & organize'), ('Promote', 'Promote'), ('Take action', 'Take action'), ('Test & feedback', 'Test & feedback'), ('Write documentation', 'Write documentation')], label='Type of help needed')), ('direct_link', wagtail.core.blocks.BooleanBlock(default=False, help_text='Checked: user goes to project link. Unchecked: user goes to pulse entry', label='Direct link', required=False))])), ('profile_listing', wagtail.core.blocks.StructBlock([('max_number_of_results', wagtail.core.blocks.IntegerBlock(default=12, help_text='Pick up to 48 profiles.', max_value=48, min_value=1, required=True)), ('advanced_filter_header', wagtail.core.blocks.static_block.StaticBlock(admin_text='-------- ADVANCED FILTERS: OPTIONS TO DISPLAY FEWER, MORE TARGETED RESULTS. --------', label=' ')), ('profile_type', wagtail.core.blocks.CharBlock(default='', help_text='Example: Fellow.', required=False)), ('program_type', wagtail.core.blocks.CharBlock(default='', help_text='Example: Tech Policy.', required=False)), ('year', wagtail.core.blocks.CharBlock(default='', required=False))])), ('profile_by_id', wagtail.core.blocks.StructBlock([('ids', wagtail.core.blocks.CharBlock(help_text='Show profiles for pulse users with specific profile ids (mozillapulse.org/profile/[##]). For multiple profiles, specify a comma separated list (e.g. 85,105,332).', label='Profile by ID'))])), ('profile_directory', wagtail.core.blocks.StructBlock([('max_number_of_results', wagtail.core.blocks.IntegerBlock(default=12, help_text='Pick up to 48 profiles.', max_value=48, min_value=1, required=True)), ('advanced_filter_header', wagtail.core.blocks.static_block.StaticBlock(admin_text='-------- ADVANCED FILTERS: OPTIONS TO DISPLAY FEWER, MORE TARGETED RESULTS. --------', label=' ')), ('profile_type', wagtail.core.blocks.CharBlock(default='', help_text='Example: Fellow.', required=False)), ('program_type', wagtail.core.blocks.CharBlock(default='', help_text='Example: Tech Policy.', required=False)), ('year', wagtail.core.blocks.CharBlock(default='', required=False)), ('filter_values', wagtail.core.blocks.CharBlock(default='2019,2018,2017,2016,2015,2014,2013', help_text='Example: 2019,2018,2017,2016,2015,2014,2013', required=True))])), ('recent_blog_entries', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('tag_filter', wagtail.core.blocks.CharBlock(help_text='Test this filter at foundation.mozilla.org/blog/tags/', label='Filter by Tag', required=False)), ('category_filter', wagtail.core.blocks.ChoiceBlock(choices=networkapi.wagtailpages.pagemodels.blog.blog_category.BlogPageCategory.get_categories, help_text='Test this filter at foundation.mozilla.org/blog/category/', label='Filter by Category', required=False)), ('top_divider', wagtail.core.blocks.BooleanBlock(help_text='Optional divider above content block.', required=False)), ('bottom_divider', wagtail.core.blocks.BooleanBlock(help_text='Optional divider below content block.', required=False))])), ('airtable', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(help_text="Copied from the Airtable embed code. The word 'embed' will be in the url")), ('height', wagtail.core.blocks.IntegerBlock(default=533, help_text='The height of the view on a desktop, usually copied from the Airtable embed code'))]))], null=True),
        ),
        migrations.AddField(
            model_name='primarypage',
            name='header_fy_NL',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='primarypage',
            name='intro_fy_NL',
            field=models.CharField(blank=True, help_text='Intro paragraph to show in hero cutout box', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='redirectingpage',
            name='URL_fy_NL',
            field=models.URLField(help_text='The fully qualified URL that this page should map to.', null=True),
        ),
        migrations.AddField(
            model_name='youtuberegretspage',
            name='faq_fy_NL',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'h2', 'h3', 'h4', 'h5', 'ol', 'ul', 'link', 'hr']))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='youtuberegretspage',
            name='headline_fy_NL',
            field=models.CharField(blank=True, help_text='Page headline', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='youtuberegretspage',
            name='intro_images_fy_NL',
            field=wagtail.core.fields.StreamField([('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True))]))], null=True),
        ),
        migrations.AddField(
            model_name='youtuberegretspage',
            name='intro_text_fy_NL',
            field=wagtail.core.fields.StreamField([('text', wagtail.core.blocks.CharBlock())], null=True),
        ),
        migrations.AddField(
            model_name='youtuberegretspage',
            name='regret_stories_fy_NL',
            field=wagtail.core.fields.StreamField([('regret_story', wagtail.core.blocks.StructBlock([('headline', wagtail.core.blocks.CharBlock(help_text='Headline of this YouTube Regret')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('imageAltText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=False)), ('story', wagtail.core.blocks.TextBlock(help_text='Story of this YouTube Regret', verbose_name='youtube_regret_story'))]))], null=True),
        ),
    ]
