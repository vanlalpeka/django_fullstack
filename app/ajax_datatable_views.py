from ajax_datatable.views import AjaxDatatableView
from .models import Note


class NoteAjaxDatatableView(AjaxDatatableView):

    model = Note
    title = 'Note'
    # initial_order = [["id", "asc"], ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
    search_values_separator = '+'

    column_defs = [
        # AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id', 'visible': False, },
        {'name': 'title', 'visible': True, },
        {'name': 'content', 'visible': True, },
    ]

    # def get_initial_queryset(self, request=None):
    #     queryset = self.model.objects.all()
    #     return queryset
