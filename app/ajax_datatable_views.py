from ajax_datatable.views import AjaxDatatableView
from .models import Note
from django.utils.text import Truncator


class NoteAjaxDatatableView(AjaxDatatableView):

    model = Note
    title = 'Note'
    # initial_order = [["id", "asc"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
    # search_values_separator = '+'
    show_date_filters = True
    # show_column_filters = True

    column_defs = [
        # AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'file_number', 'visible': True, 'lookup_field': '__icontains',},
        {'name': 'concerned_department', 'foreign_field': 'concerned_department__name', 'visible': True, 'choices': True, 'autofilter': True,},
        {'name': 'date', 'visible': True,'lookup_field': '__icontains', },
        {'name': 'subject', 'visible': True, 'lookup_field': '__icontains', },
    ]


    def customize_row(self, row, obj):
        # 'row' is a dictionary representing the current row, and 'obj' is the current object.
        row['file_number'] = f'<a href="/notes/{int(obj.pk)}">{obj.file_number}</a>'
        # row['concerned_department'] =Truncator(obj.concerned_department).chars(20)
        # row['comment'] =Truncator(obj.comment).chars(30)
        row['date'] = obj.date.strftime("%d.%m.%Y")
        return

    # def get_initial_queryset(self, request=None):
    #     queryset = self.model.objects.all()
    #     return queryset
